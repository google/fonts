"""
Report and PR description generation module for automated upstream updates.
Located internally within google/fonts at .ci/autoupdater/report_generator.py.
"""

import os
import re
import json
import zipfile
import unicodedata
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
from datetime import datetime, timezone
from .models import FamilyMetadata, UpdateCheckResult, SafetyTier
from .regression_engine import SafetyScoreBreakdown, DiffenatorResult, QACheckResult


def format_unicode_codepoint(cp: int) -> str:
    """Format integer Unicode codepoint into 'U+XXXX ('char' - NAME)' string."""
    try:
        char = chr(cp)
        name = unicodedata.name(char, "UNKNOWN")
        return f"U+{cp:04X} (`{char}` - {name})"
    except Exception:
        return f"U+{cp:04X}"


def generate_pr_body(
    family_meta: FamilyMetadata,
    update_result: UpdateCheckResult,
    score_info: SafetyScoreBreakdown,
    diff_result: DiffenatorResult,
    qa_result: QACheckResult,
) -> str:
    """
    Generate structured GitHub Pull Request Markdown body with granular test suite data points.
    """
    tier_emoji = {
        SafetyTier.AUTO_APPROVE: "🟢 **AUTO_APPROVE** (High Confidence)",
        SafetyTier.NEEDS_REVIEW: "🟡 **NEEDS_REVIEW** (Maintainer Attention Required)",
        SafetyTier.BLOCKED: "🔴 **BLOCKED** (Regression Detected)",
    }[score_info.safety_tier]

    lines = []
    lines.append(f"## 🤖 Automated Upstream Font Update: `{family_meta.name}`")
    lines.append("")
    lines.append(f"### 📊 Safe to Update (STU) Score: `{score_info.composite_score} / 100`")
    lines.append(f"**Decision Tier:** {tier_emoji}")
    lines.append("")

    lines.append("### 💡 Test Suite Data Points & Scoring Rationale")
    lines.append("")
    lines.append("#### 🎨 1. `diffenator2` Rendering & Visual Specimen Data Points")
    lines.append(f"- **Visual Pixel Shift Ratio ($S_{{visual}}$):** `{diff_result.visual_diff_pixel_ratio * 100:.2f}%` rendered specimen difference (Sub-Score: `{score_info.s_visual} / 100`)")
    lines.append(f"- **Visual Stability Status:** {'🟢 Pass (< 5% shift)' if diff_result.visual_diff_pixel_ratio <= 0.05 else '⚠️ High rendering shift detected'}")
    lines.append("")

    lines.append("#### 📐 2. `diffenator2` Metrics & Layout Data Points")
    lines.append(f"- **Max Vertical Metric Shift:** `{diff_result.max_vertical_metric_shift}` font units {'(⚠️ EXCEEDS 10 unit threshold)' if diff_result.max_vertical_metric_shift > 10 else '(✅ Stable <= 10 units)'}")
    lines.append(f"- **Advance Width Max Shift:** `{diff_result.max_advance_width_shift_pct * 100:.2f}%` {'(⚠️ EXCEEDS 5% threshold)' if diff_result.max_advance_width_shift_pct > 0.05 else '(✅ Stable <= 5%)'}")
    lines.append(f"- **Layout Table Status:** GPOS: `{'⚠️ Shift' if diff_result.has_gpos_regression else '✅ Stable'}` | GSUB: `{'⚠️ Shift' if diff_result.has_gsub_regression else '✅ Stable'}`")
    lines.append("")

    lines.append("#### 🔤 3. `fontTools` Glyph Set & Unicode Retention Data Points")
    if diff_result.deleted_unicodes:
        lines.append(f"- **Deleted Unicodes (`{len(diff_result.deleted_unicodes)}` Total - ❌ CRITICAL BREAKING CHANGE):**")
        for u in diff_result.deleted_unicodes[:10]:
            lines.append(f"  - {format_unicode_codepoint(u)}")
        if len(diff_result.deleted_unicodes) > 10:
            lines.append(f"  - *...and {len(diff_result.deleted_unicodes) - 10} more deleted Unicodes*")
    else:
        lines.append("- **Unicode Retention Status:** 🟢 `100% Intact` (Zero deleted Unicodes)")

    if diff_result.added_unicodes:
        lines.append(f"- **Added Unicodes (`{len(diff_result.added_unicodes)}` Total):**")
        for u in diff_result.added_unicodes[:5]:
            lines.append(f"  - {format_unicode_codepoint(u)}")
        if len(diff_result.added_unicodes) > 5:
            lines.append(f"  - *...and {len(diff_result.added_unicodes) - 5} more added Unicodes*")
    lines.append("")

    lines.append("#### 📋 4. `Fontspector` QA Check Suite Data Points")
    lines.append(f"- **Candidate Totals:** PASS: `{qa_result.pass_count}` | WARN: `{qa_result.warn_count}` | ERROR: `{qa_result.error_count}` | FATAL: `{qa_result.fatal_count}`")
    lines.append(f"- **New Check Regressions Introduced:** 🔴 `{qa_result.new_fatal_count}` Fatal | 🔴 `{qa_result.new_error_count}` Error | 🟡 `{qa_result.new_warn_count}` Warn")
    lines.append(f"- **Pre-existing Known Failures:** 🟡 `{qa_result.known_failure_count}` (Present in baseline installed font)")
    if qa_result.fixed_failure_count > 0:
        lines.append(f"- **Resolved / Fixed Failures:** 🟢 `{qa_result.fixed_failure_count}` (Failed in baseline, now passing!)")
    lines.append("")

    if qa_result.new_failures:
        lines.append("##### 🔴 New QA Check Regressions:")
        for item in qa_result.new_failures[:10]:
            chk_id = item.get("check_id", "unknown")
            st = item.get("status", "FAIL")
            base_st = item.get("baseline_status", "PASS")
            msg = item.get("message", "Check regression detected")
            lines.append(f"- **`{chk_id}`** ({st}): Baseline was `{base_st}`")
            lines.append(f"  > *{msg}*")
        lines.append("")

    if score_info.blocking_reasons:
        lines.append("#### ⚠️ Blocking Rationale & Warning Items:")
        for reason in score_info.blocking_reasons:
            lines.append(f"- {reason}")
        lines.append("")

    lines.append("### 🕒 Version & Timestamp Comparison")
    lines.append("| Property | Local Installed (GF) | Upstream Candidate | Status |")
    lines.append("| :--- | :--- | :--- | :--- |")
    lines.append(f"| **Font Version String** | `{family_meta.installed_version or 'N/A'}` | `{update_result.upstream_version or 'N/A'}` | {'🆕 Update Available' if update_result.has_update else '✅ Up to Date'} |")
    lines.append(f"| **Numerical Version** | `{family_meta.installed_version_num or 'N/A'}` | `{update_result.upstream_version or 'N/A'}` | `{update_result.comparison_status.value}` |")
    lines.append(f"| **Commit / Mod Date** | `{family_meta.installed_git_commit_date or family_meta.installed_modified_date or 'N/A'}` | `{update_result.upstream_published_at or 'N/A'}` | {'📅 Upstream Newer' if update_result.has_update else '✅ Current'} |")
    lines.append("")

    lines.append("### 📈 Score Breakdown")
    lines.append("| Component | Weight | Tool | Sub-Score | Status |")
    lines.append("| :--- | :--- | :--- | :--- | :--- |")
    lines.append(f"| **Visual Diff ($S_{{visual}}$)** | 35% | `diffenator2` | `{score_info.s_visual} / 100` | {'✅ Pass' if score_info.s_visual >= 90 else '⚠️ Diff Warning'} |")
    lines.append(f"| **Metrics & Layout ($S_{{metric}}$)** | 25% | `diffenator2` | `{score_info.s_metric} / 100` | {'✅ Stable' if score_info.s_metric >= 90 else '⚠️ Metric Shift'} |")
    lines.append(f"| **Glyph Set Retention ($S_{{cmap}}$)** | 25% | `diffenator2` / `fontTools` | `{score_info.s_cmap} / 100` | {'✅ Intact' if score_info.s_cmap == 100 else '❌ Deleted Glyphs'} |")
    lines.append(f"| **QA Checks ($S_{{qa}}$)** | 15% | `Fontspector` | `{score_info.s_qa} / 100` | {'✅ Clean' if score_info.s_qa >= 90 else '⚠️ QA Issues'} |")
    lines.append("")

    lines.append("### 🔗 Upstream Source Metadata")
    lines.append(f"- **Upstream Repository:** {update_result.repository_url or 'N/A'}")
    if update_result.upstream_version:
        lines.append(f"- **Upstream Version Tag:** `{update_result.upstream_version}`")
    if update_result.upstream_commit:
        lines.append(f"- **Upstream Commit Hash:** `{update_result.upstream_commit}`")
    lines.append("")
    lines.append("---")
    lines.append("*Generated automatically by Google Fonts Automated Upstream Update System (GFAU)*")

    return "\n".join(lines)


def generate_family_verification_report(result: Dict[str, Any], output_filepath: Optional[str] = None) -> str:
    """
    Generate detailed single-family verification report for testing against live repository.
    Follows exact requested format for out-of-date font family verification, including
    Fontspector QA test results and manual directives.
    """
    family_name = result.get("family_name", "Unknown")
    has_update = result.get("has_update", False)
    matching = result.get("font_matching_analysis", {})
    qa_res: Optional[QACheckResult] = result.get("qa_res")
    is_variable_update = result.get("is_variable_update_approved") or matching.get("is_variable_update_approved", False)
    is_human_approved = result.get("is_human_approved", False)

    lines = []
    lines.append(f"# 🔍 Live Repository Verification Report: `{family_name}`")
    lines.append("")
    lines.append(f"**Generated:** `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`")
    lines.append(f"**PR Submission Mode:** `DISABLED (Report / Verification Mode)` 🛑")
    lines.append("")

    lines.append("## 📁 Font File Matching Identification")
    lines.append("")
    lines.append(f"- **Overall Matching Status:** `{matching.get('status', 'N/A')}`")
    lines.append(f"- **Local TTF Count (in google/fonts):** `{matching.get('local_ttf_count', 0)}`")
    lines.append(f"- **Upstream Candidate TTF Count:** `{matching.get('candidate_ttf_count', 0)}`")
    lines.append(f"- **Filename Match Rate:** `{matching.get('match_rate_pct', 0.0)}%`")
    lines.append(f"- **Binary Hash Differences Detected:** `{'YES (Updated Binary Content)' if matching.get('has_binary_changes') else 'NO (Byte-Identical Binaries)'}`")
    if is_variable_update:
        lines.append("- **Manual Directive (Variable Update):** 🟢 `Approved Static-to-Variable Upgrade` (Existing static fonts should be removed and replaced with the new variable version)")
    lines.append("")

    matched_pairs = matching.get("matched_pairs", [])
    if matched_pairs:
        lines.append("### 📑 Detailed Font File Mapping, Version & Hash Table")
        lines.append("")
        lines.append("| Local Font Filename | Candidate Upstream Filename | Catalog Version | Upstream Version | Version Comparison | Binary Hash Status |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")
        for p in matched_pairs:
            loc_f = p.get("local_filename", "")
            cand_f = p.get("candidate_filename", "")
            cat_v = p.get("catalog_ttf_version", "N/A") or "N/A"
            cand_v = p.get("candidate_ttf_version", "N/A") or "N/A"
            v_cmp = p.get("version_comparison", "N/A")
            v_badge = {
                "UPDATE_CONFIRMED": "🟢 Update Confirmed",
                "UP_TO_DATE": "🟡 Up to Date",
                "LOCAL_IS_NEWER": "🔴 Local Newer",
            }.get(v_cmp, f"`{v_cmp}`")
            hash_chg = "🔴 Changed / Updated" if p.get("binary_hash_changed") else "🟢 Identical (No Change)"
            lines.append(f"| `{loc_f}` | `{cand_f}` | `{cat_v}` | `{cand_v}` | {v_badge} | {hash_chg} |")
        lines.append("")


    unmatched_local = matching.get("unmatched_local_filenames", [])
    if unmatched_local:
        lines.append("### ⚠️ Unmatched Local Font Files (Present in GF, Missing in Upstream Candidate)")
        for f in unmatched_local:
            lines.append(f"- `{f}`")
        lines.append("")

    unmatched_cand = matching.get("unmatched_candidate_filenames", [])
    if unmatched_cand:
        lines.append("### 🆕 Unmatched Upstream Candidate Files (New Files Not Yet in GF)")
        for f in unmatched_cand:
            lines.append(f"- `{f}`")
        lines.append("")

    lines.append("## 📊 System Assessment & Scoring Summary")
    lines.append("")
    lines.append(f"- **Update Available:** `{'YES' if has_update else 'NO'}`")
    lines.append(f"- **Current Installed Version:** `{result.get('current_version', 'N/A')}`")
    lines.append(f"- **Upstream Candidate Version:** `{result.get('upstream_version', 'N/A')}`")
    lines.append(f"- **Safe to Update (STU) Score:** `{result.get('safety_score', 'N/A')} / 100`")
    lines.append(f"- **Decision Tier:** `{result.get('safety_tier', 'N/A')}`")
    lines.append(f"- **Pipeline Status:** `{result.get('status', 'N/A')}`")
    if is_human_approved:
        lines.append("- **Manual Directive (Human Approval):** 🟢 `Human Reviewed & Evaluated as Safe to Update`")
    lines.append("")

    if qa_res:
        lines.append("## 📋 Fontspector QA Test Results & Delta")
        lines.append("")
        lines.append(f"- **Candidate Check Totals:** PASS: `{qa_res.pass_count}` | WARN: `{qa_res.warn_count}` | ERROR: `{qa_res.error_count}` | FATAL: `{qa_res.fatal_count}`")
        lines.append(f"- **New Check Regressions Introduced:** 🔴 `{qa_res.new_fatal_count}` Fatal | 🔴 `{qa_res.new_error_count}` Error | 🟡 `{qa_res.new_warn_count}` Warn")
        lines.append(f"- **Pre-existing Known Failures:** 🟡 `{qa_res.known_failure_count}` (Inherited from baseline installed font)")
        if qa_res.fixed_failure_count > 0:
            lines.append(f"- **Resolved / Fixed Failures:** 🟢 `{qa_res.fixed_failure_count}` (Failed in baseline, now passing!)")
        lines.append("")

        if qa_res.new_failures:
            lines.append("### 🔴 New QA Check Regressions Introduced")
            for item in qa_res.new_failures[:10]:
                chk_id = item.get("check_id", "unknown")
                st = item.get("status", "FAIL")
                base_st = item.get("baseline_status", "PASS")
                msg = item.get("message", "Check regression detected")
                lines.append(f"- **`{chk_id}`** ({st}): Baseline was `{base_st}`")
                lines.append(f"  > *{msg}*")
            lines.append("")

        if qa_res.known_failures:
            lines.append("### 🟡 Pre-existing Known Failures (Inherited from Baseline)")
            for item in qa_res.known_failures[:10]:
                chk_id = item.get("check_id", "unknown")
                st = item.get("status", "FAIL")
                lines.append(f"- **`{chk_id}`** ({st})")
            lines.append("")

    content = "\n".join(lines) + "\n"
    if output_filepath:
        Path(output_filepath).write_text(content, encoding="utf-8")
    return content



def package_out_of_date_reports(
    results: List[Dict[str, Any]],
    output_dir: str = "out_of_date_reports",
    zip_filepath: str = "autoupdate_verification_reports.zip",
) -> Tuple[str, List[str]]:
    """
    Generate individual verification report files for each out-of-date font family
    and package them into a single ZIP archive for GitHub Actions artifact upload.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    generated_files: List[str] = []

    for r in results:
        if r.get("has_update"):
            fam_name = r.get("family_name", "Unknown")
            fam_slug = re.sub(r'[^a-zA-Z0-9_-]', '', fam_name.lower().replace(" ", "_"))
            report_filename = f"{fam_slug}_verification_report.md"
            filepath = out_path / report_filename

            generate_family_verification_report(r, output_filepath=str(filepath))
            generated_files.append(str(filepath))

    zip_path = Path(zip_filepath)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in generated_files:
            p = Path(f)
            zf.write(p, arcname=p.name)

    return str(zip_path), generated_files


def generate_live_repository_audit_report(
    summary: Dict[str, Any],
    results: List[Dict[str, Any]],
    output_filepath: str = "live_repo_verification_report.md",
) -> str:
    """
    Generate comprehensive multi-family live repository verification report.
    Includes full detailed Live Repository Verification Reports for EACH family that needs an update.
    """
    lines = []
    lines.append("# 🌐 Live Repository Verification Report: Google Fonts Catalog")
    lines.append("")
    lines.append(f"**Audit Date:** `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`")
    lines.append(f"**PR Submission Status:** `DISABLED (Report / Verification Mode)` 🛑")
    lines.append(f"**Total Families Audited:** `{len(results)}`")
    lines.append("")

    lines.append("## 📊 Overview & Font File Matching Statistics")
    lines.append("")
    
    exact_matches = sum(1 for r in results if r.get("font_matching_analysis", {}).get("status") == "EXACT_MATCH")
    partial_matches = sum(1 for r in results if r.get("font_matching_analysis", {}).get("status") == "PARTIAL_MATCH")
    no_matches = sum(1 for r in results if r.get("font_matching_analysis", {}).get("status") == "NO_MATCH")
    updates_found = sum(1 for r in results if r.get("has_update"))

    lines.append("| Metric | Count | Percentage |")
    lines.append("| :--- | :--- | :--- |")
    lines.append(f"| **Upstream Updates Detected** | **{updates_found}** | **{(updates_found / len(results) * 100.0) if results else 0:.1f}%** |")
    lines.append(f"| 🟢 **Exact Font File Matches (100% Filename Alignment)** | **{exact_matches}** | **{(exact_matches / len(results) * 100.0) if results else 0:.1f}%** |")
    lines.append(f"| 🟡 **Partial Font File Matches** | {partial_matches} | - |")
    lines.append(f"| 🔴 **Mismatched / Unmatched Font Files** | {no_matches} | - |")
    lines.append("")

    lines.append("## 🚀 Summary Table of Audited Families")
    lines.append("")
    lines.append("| Family Name | Upstream Update | Installed Ver | Upstream Ver (TTF) | Font Naming Identity | STU Score | Decision Tier | Status |")
    lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    for r in results:
        fam = r.get("family_name", "Unknown")
        upd = "YES 🆕" if r.get("has_update") else "NO ✅"
        cur_v = r.get("current_version", "N/A") or "N/A"
        up_v = r.get("upstream_version") or (f"commit {r['upstream_commit'][:7]}" if r.get("upstream_commit") else "N/A")
        naming_status = r.get("font_matching_analysis", {}).get("naming_identity_status", "N/A")

        score = r.get("safety_score", "N/A")
        tier = r.get("safety_tier", "N/A")
        status = r.get("status", "CHECKED")

        lines.append(f"| **{fam}** | {upd} | `{cur_v}` | `{up_v}` | `{naming_status}` | `{score}` | `{tier}` | `{status}` |")

    lines.append("")
    lines.append("---")
    lines.append("# 🔬 Live Repository Verification Reports for Updated Families")
    lines.append("")

    updated_results = [r for r in results if r.get("has_update")]
    if updated_results:
        for idx, res in enumerate(updated_families := updated_results, 1):
            lines.append(f"## Family {idx} of {len(updated_families)}: `{res.get('family_name')}`")
            lines.append("")
            family_report = generate_family_verification_report(res)
            lines.append(family_report)
            lines.append("")
            lines.append("---")
    else:
        lines.append("✅ **All audited font families are up to date! No updates detected.**")
        lines.append("")

    lines.append("*Report generated automatically by Google Fonts Auto-Updater Live Repository Auditor*")

    content = "\n".join(lines)
    Path(output_filepath).write_text(content, encoding="utf-8")
    return content



