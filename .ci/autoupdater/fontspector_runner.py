"""
Fontspector QA integration module for running automated quality checks
and comparing check results between baseline (installed) and candidate (upstream) TTFs.
Located internally within google/fonts at .ci/autoupdater/fontspector_runner.py.
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


SEVERITY_ORDER = ["PASS", "SKIP", "INFO", "WARN", "FAIL", "ERROR", "FATAL"]


@dataclass
class QADiffResult:
    fatal_count: int = 0
    error_count: int = 0
    warn_count: int = 0
    pass_count: int = 0
    skip_count: int = 0
    info_count: int = 0

    # New vs Known / Pre-existing distinction
    new_fatal_count: int = 0
    new_error_count: int = 0
    new_warn_count: int = 0
    known_failure_count: int = 0
    fixed_failure_count: int = 0

    new_failures: List[Dict[str, Any]] = field(default_factory=list)
    known_failures: List[Dict[str, Any]] = field(default_factory=list)
    fixed_failures: List[Dict[str, Any]] = field(default_factory=list)
    all_candidate_checks: Dict[str, str] = field(default_factory=dict)
    all_baseline_checks: Dict[str, str] = field(default_factory=dict)


def parse_fontspector_json(json_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Parse Fontspector JSON output report into a map of check_id -> check_info dict.
    check_info contains: check_id, check_name, worst_status, subresults.
    """
    if not os.path.exists(json_path):
        return {}

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}

    checks: Dict[str, Dict[str, Any]] = {}
    results = data.get("results", {})

    for file_key, sections in results.items():
        if isinstance(sections, dict):
            for sec_name, check_list in sections.items():
                if isinstance(check_list, list):
                    for chk in check_list:
                        cid = chk.get("check_id")
                        status = chk.get("worst_status")
                        if cid and status:
                            if (
                                cid not in checks
                                or SEVERITY_ORDER.index(status)
                                > SEVERITY_ORDER.index(checks[cid]["worst_status"])
                            ):
                                checks[cid] = {
                                    "check_id": cid,
                                    "check_name": chk.get("check_name", cid),
                                    "worst_status": status,
                                    "subresults": chk.get("subresults", []),
                                }

    return checks


def run_fontspector(
    ttf_files: List[str],
    profile: str = "googlefonts",
    output_json: Optional[str] = None,
    timeout: int = 120,
) -> Dict[str, Dict[str, Any]]:
    """
    Run fontspector CLI on a list of TTF font files and return parsed check results map.
    """
    if not ttf_files:
        return {}

    fontspector_bin = shutil.which("fontspector")
    if not fontspector_bin:
        return {}

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        json_out = output_json or tmp.name

    try:
        cmd = [
            fontspector_bin,
            "--profile",
            profile,
            "--skip-network",
            "--json",
            json_out,
        ] + ttf_files
        subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return parse_fontspector_json(json_out)
    except Exception as e:
        print(f"⚠️ fontspector execution warning: {e}")
        return {}
    finally:
        if not output_json and os.path.exists(json_out):
            try:
                os.remove(json_out)
            except Exception:
                pass


def compare_qa_results(
    baseline_checks: Dict[str, Dict[str, Any]],
    candidate_checks: Dict[str, Dict[str, Any]],
) -> QADiffResult:
    """
    Compare baseline (installed) vs candidate (upstream) Fontspector QA check results.
    Categorizes failures into:
    - New Failures (Regressions): Baseline PASSED/SKIPPED/INFO, but Candidate FAILED/WARNED/ERROR/FATAL.
    - Known Failures (Pre-existing): Baseline ALREADY FAILED/WARNED, and Candidate also FAILED/WARNED.
    - Fixed Failures: Baseline FAILED/WARNED, but Candidate PASSED!
    """
    res = QADiffResult()
    res.all_baseline_checks = {
        cid: info["worst_status"] for cid, info in baseline_checks.items()
    }
    res.all_candidate_checks = {
        cid: info["worst_status"] for cid, info in candidate_checks.items()
    }

    # Tally candidate severity counts
    for cid, info in candidate_checks.items():
        st = info["worst_status"]
        if st == "FATAL":
            res.fatal_count += 1
        elif st in ("FAIL", "ERROR"):
            res.error_count += 1
        elif st == "WARN":
            res.warn_count += 1
        elif st == "PASS":
            res.pass_count += 1
        elif st == "SKIP":
            res.skip_count += 1
        elif st == "INFO":
            res.info_count += 1

    # Diff checks against baseline
    all_check_ids = set(baseline_checks.keys()).union(set(candidate_checks.keys()))

    failing_severities = ("FATAL", "ERROR", "FAIL", "WARN")

    for cid in sorted(all_check_ids):
        b_info = baseline_checks.get(cid)
        c_info = candidate_checks.get(cid)

        b_status = b_info["worst_status"] if b_info else "PASS"
        c_status = c_info["worst_status"] if c_info else "PASS"

        b_is_failing = b_status in failing_severities
        c_is_failing = c_status in failing_severities

        if c_is_failing and not b_is_failing:
            # NEW Failure / Regression!
            item = {
                "check_id": cid,
                "check_name": c_info.get("check_name", cid) if c_info else cid,
                "status": c_status,
                "baseline_status": b_status,
            }
            res.new_failures.append(item)
            if c_status == "FATAL":
                res.new_fatal_count += 1
            elif c_status in ("FAIL", "ERROR"):
                res.new_error_count += 1
            elif c_status == "WARN":
                res.new_warn_count += 1

        elif c_is_failing and b_is_failing:
            # KNOWN / Pre-existing Failure!
            item = {
                "check_id": cid,
                "check_name": c_info.get("check_name", cid) if c_info else cid,
                "status": c_status,
                "baseline_status": b_status,
            }
            res.known_failures.append(item)
            res.known_failure_count += 1

        elif b_is_failing and not c_is_failing:
            # FIXED Failure!
            item = {
                "check_id": cid,
                "check_name": b_info.get("check_name", cid) if b_info else cid,
                "status": c_status,
                "baseline_status": b_status,
            }
            res.fixed_failures.append(item)
            res.fixed_failure_count += 1

    return res
