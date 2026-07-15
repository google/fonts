"""
Catalog-wide audit script for scanning full Google Fonts repository.
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
    fonts_repo_path: str = ".", max_families: int = 2000, max_workers: int = 10, db_path: str = "gf_catalog_full_audit.db"
) -> Dict[str, Any]:
    pattern = os.path.join(fonts_repo_path, "*", "*", "METADATA.pb")
    pb_files = glob.glob(pattern)

    print(f"Discovered {len(pb_files)} font families in '{fonts_repo_path}'.")
    pipeline = AutoUpdatePipeline(state_db_path=db_path)

    valid_families = []
    for f in pb_files:
        try:
            meta = load_metadata_pb(f)
            if meta.source and meta.source.repository_url:
                valid_families.append((f, meta))
        except Exception:
            pass

    print(f"Found {len(valid_families)} families with valid upstream repository URLs.")
    target_families = valid_families[:max_families]

    work_items = [(f, meta, pipeline) for f, meta in target_families]
    results = []

    print(f"Launching multi-threaded GFAU audit across {len(target_families)} families...")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_single_family, item): item for item in work_items}
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            results.append(res)
            completed += 1
            if completed % 50 == 0 or completed == len(target_families):
                print(f"  Progress: {completed}/{len(target_families)} families processed ({time.time() - start_time:.1f}s)...")

    # Metrics aggregation
    updated_count = 0
    no_update_count = 0
    auto_approve_count = 0
    needs_review_count = 0
    blocked_count = 0
    error_count = 0

    updated_families = []

    for res in results:
        if res.get("status") == "ERROR":
            error_count += 1
            continue

        if res.get("has_update"):
            updated_count += 1
            tier = res.get("safety_tier")
            updated_families.append({
                "family": res.get("family_name"),
                "score": res.get("safety_score"),
                "tier": tier,
            })
            if tier == "AUTO_APPROVE":
                auto_approve_count += 1
            elif tier == "NEEDS_REVIEW":
                needs_review_count += 1
            elif tier == "BLOCKED":
                blocked_count += 1
        else:
            no_update_count += 1

    not_safe_count = needs_review_count + blocked_count
    elapsed = round(time.time() - start_time, 2)

    report = {
        "catalog_summary": {
            "total_families_in_repo": len(pb_files),
            "families_with_source_repo": len(valid_families),
            "families_audited": len(target_families),
            "elapsed_time_seconds": elapsed,
        },
        "update_breakdown": {
            "total_updated": updated_count,
            "no_update": no_update_count,
            "safe_to_update_automatically": auto_approve_count,
            "not_safe_to_update_automatically": not_safe_count,
            "needs_review_count": needs_review_count,
            "blocked_count": blocked_count,
            "api_rate_limited_or_error": error_count,
        },
        "percentages": {
            "update_rate": round((updated_count / (len(target_families) - error_count)) * 100, 2) if (len(target_families) - error_count) > 0 else 0,
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

    report = run_full_catalog_audit(fonts_repo, max_families=max_families, max_workers=max_workers)
    print("\n=================== FULL CATALOG AUDIT REPORT ===================")
    print(json.dumps(report, indent=2))
