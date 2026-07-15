"""
Catalog-wide audit script for scanning full Google Fonts repository.
Features real-time progress tracking, ETA calculation, and live state updates.
Located internally within google/fonts at .ci/autoupdater/catalog_audit.py.
"""

import sys
import os
import glob
import json
import time
import concurrent.futures
from pathlib import Path
from typing import Dict, Any, List

# Ensure .ci is in sys.path
ci_dir = str(Path(__file__).parent.parent)
if ci_dir not in sys.path:
    sys.path.insert(0, ci_dir)

from autoupdater.orchestrator import AutoUpdatePipeline
from autoupdater.metadata_parser import load_metadata_pb


def format_eta(seconds: float) -> str:
    """Format seconds into HH:MM:SS string."""
    if seconds <= 0 or seconds > 86400:
        return "--:--:--"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def make_progress_bar(pct: float, width: int = 20) -> str:
    """Generate ASCII progress bar string."""
    filled = int(round(width * pct / 100))
    bar = "█" * filled + "░" * (width - filled)
    return bar


def process_single_family(item):
    filepath, meta, pipeline = item
    try:
        res = pipeline.process_family(filepath)
        return res
    except Exception as e:
        return {
            "family_name": meta.name if meta else Path(filepath).parent.name,
            "has_update": False,
            "error": str(e),
            "status": "ERROR",
        }


def run_full_catalog_audit(
    fonts_repo_path: str = ".",
    max_families: int = 2000,
    max_workers: int = 10,
    db_path: str = "gf_catalog_full_audit.db",
    progress_file: str = "gf_audit_progress.json",
    log_interval: int = 10,
) -> Dict[str, Any]:
    pattern = os.path.join(fonts_repo_path, "*", "*", "METADATA.pb")
    pb_files = glob.glob(pattern)

    print(f"🔍 Discovered {len(pb_files)} total font families in '{fonts_repo_path}'.")
    pipeline = AutoUpdatePipeline(state_db_path=db_path)

    valid_families = []
    for f in pb_files:
        try:
            meta = load_metadata_pb(f)
            if meta.source and meta.source.repository_url:
                valid_families.append((f, meta))
        except Exception:
            pass

    print(f"🌐 Found {len(valid_families)} families with valid upstream repository URLs.")
    target_families = valid_families[:max_families]
    total_count = len(target_families)

    if total_count == 0:
        print("⚠️ No valid font families to process.")
        return {"catalog_summary": {"total_audited": 0}}

    work_items = [(f, meta, pipeline) for f, meta in target_families]
    results = []

    print(f"\n🚀 Launching multi-threaded GFAU audit sweep ({total_count} families, {max_workers} worker threads)...")
    print("=" * 95)

    start_time = time.time()
    completed = 0
    updated_count = 0
    auto_approve_count = 0
    needs_review_count = 0
    blocked_count = 0
    error_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_single_family, item): item for item in work_items}

        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            results.append(res)
            completed += 1

            # Update live metrics
            status = res.get("status")
            has_up = res.get("has_update", False)
            tier = res.get("safety_tier")

            if status == "ERROR":
                error_count += 1
            elif has_up:
                updated_count += 1
                if tier == "AUTO_APPROVE":
                    auto_approve_count += 1
                elif tier == "NEEDS_REVIEW":
                    needs_review_count += 1
                elif tier == "BLOCKED":
                    blocked_count += 1

            # Progress calculation
            elapsed = time.time() - start_time
            pct = (completed / total_count) * 100
            rate = completed / elapsed if elapsed > 0 else 0
            remaining_sec = (total_count - completed) / rate if rate > 0 else 0
            eta_str = format_eta(remaining_sec)
            bar = make_progress_bar(pct, width=15)

            family_name = res.get("family_name", "Unknown")

            # Write real-time progress JSON snapshot
            progress_snap = {
                "completed": completed,
                "total": total_count,
                "pct_complete": round(pct, 2),
                "rate_per_sec": round(rate, 2),
                "elapsed_sec": round(elapsed, 1),
                "eta_formatted": eta_str,
                "updated_count": updated_count,
                "auto_approve_count": auto_approve_count,
                "needs_review_count": needs_review_count,
                "blocked_count": blocked_count,
                "error_count": error_count,
                "last_processed": family_name,
                "last_status": "UPDATED" if has_up else status,
            }
            try:
                Path(progress_file).write_text(json.dumps(progress_snap, indent=2))
            except Exception:
                pass

            # Print progress log line
            if completed % log_interval == 0 or completed == total_count or has_up:
                print(
                    f"[{completed:4d}/{total_count:4d} | {pct:5.1f}%] {bar} | "
                    f"🟢 Auto:{auto_approve_count:2d} | 🟡 Review:{needs_review_count:2d} | 🔴 Block:{blocked_count:2d} | "
                    f"⚡ {rate:4.1f}/s | ⌛ ETA:{eta_str} | Last: {family_name}"
                )
                sys.stdout.flush()

    print("=" * 95)
    print("✅ Catalog audit sweep completed!")

    # Metrics aggregation
    not_safe_count = needs_review_count + blocked_count
    total_elapsed = round(time.time() - start_time, 2)

    updated_families = [
        {"family": r.get("family_name"), "score": r.get("safety_score"), "tier": r.get("safety_tier")}
        for r in results if r.get("has_update")
    ]

    report = {
        "catalog_summary": {
            "total_families_in_repo": len(pb_files),
            "families_with_source_repo": len(valid_families),
            "families_audited": total_count,
            "elapsed_time_seconds": total_elapsed,
            "average_rate_per_sec": round(total_count / total_elapsed, 2) if total_elapsed > 0 else 0,
        },
        "update_breakdown": {
            "total_updated": updated_count,
            "no_update": completed - updated_count - error_count,
            "safe_to_update_automatically": auto_approve_count,
            "not_safe_to_update_automatically": not_safe_count,
            "needs_review_count": needs_review_count,
            "blocked_count": blocked_count,
            "api_rate_limited_or_error": error_count,
        },
        "percentages": {
            "update_rate": round((updated_count / (total_count - error_count)) * 100, 2) if (total_count - error_count) > 0 else 0,
            "safe_auto_update_pct": round((auto_approve_count / updated_count) * 100, 2) if updated_count else 0,
            "not_safe_auto_update_pct": round((not_safe_count / updated_count) * 100, 2) if updated_count else 0,
        },
        "updated_families_list": updated_families[:25],
    }

    return report


if __name__ == "__main__":
    fonts_repo = "."
    if len(sys.argv) > 1:
        fonts_repo = sys.argv[1]

    max_families = 2000
    if len(sys.argv) > 2:
        max_families = int(sys.argv[2])

    max_workers = 10
    if len(sys.argv) > 3:
        max_workers = int(sys.argv[3])

    report = run_full_catalog_audit(fonts_repo, max_families=max_families, max_workers=max_workers, log_interval=5)
    print("\n=================== FULL CATALOG AUDIT REPORT ===================")
    print(json.dumps(report, indent=2))
