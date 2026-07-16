"""
Report and PR description generation module for automated upstream updates.
Located internally within google/fonts at .ci/autoupdater/report_generator.py.
"""

from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone
from .models import FamilyMetadata, UpdateCheckResult, SafetyTier
from .regression_engine import SafetyScoreBreakdown, DiffenatorResult, QACheckResult


def generate_pr_body(
    family_meta: FamilyMetadata,
    update_result: UpdateCheckResult,
    score_info: SafetyScoreBreakdown,
    diff_result: DiffenatorResult,
    qa_result: QACheckResult,
) -> str:
    """
    Generate structured GitHub Pull Request Markdown body.
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

    lines.append("### 💡 Concise Scoring Rationale")
    lines.append(f"- **Decision Tier:** {tier_emoji} (Score `{score_info.composite_score} / 100`)")
    lines.append(f"- **Max Vertical Metric Shift:** `{diff_result.max_vertical_metric_shift}` font units {'(⚠️ exceeds 10 unit threshold)' if diff_result.max_vertical_metric_shift > 10 else '(✅ Stable)'}")
    lines.append(f"- **Advance Width Max Shift:** `{diff_result.max_advance_width_shift_pct * 100:.2f}%` {'(⚠️ exceeds 5% threshold)' if diff_result.max_advance_width_shift_pct > 0.05 else '(✅ Stable)'}")
    lines.append(f"- **Deleted Unicodes:** `{len(diff_result.deleted_unicodes)}` {'(❌ CRITICAL BREAKING CHANGE)' if diff_result.deleted_unicodes else '(✅ Intact)'}")
    lines.append(f"- **New QA Regressions:** 🔴 `{qa_result.new_fatal_count}` Fatal | 🔴 `{qa_result.new_error_count}` Error | 🟡 `{qa_result.new_warn_count}` Warn")
    lines.append("")

    if score_info.blocking_reasons:
        lines.append("#### ⚠️ Detailed Rationale & Warning Items:")
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

    lines.append("### 🔍 `diffenator2` Primary Regression Summary")
    lines.append(f"- **Visual Specimen Shift:** `{diff_result.visual_diff_pixel_ratio * 100:.2f}%` pixel difference")
    lines.append(f"- **Max Vertical Metric Shift:** `{diff_result.max_vertical_metric_shift}` font units")
    lines.append(f"- **Advance Width Max Shift:** `{diff_result.max_advance_width_shift_pct * 100:.2f}%`")
    lines.append(f"- **Deleted Unicodes:** `{len(diff_result.deleted_unicodes)}` | **Added Unicodes:** `{len(diff_result.added_unicodes)}`")
    lines.append("")

    lines.append("### 📋 `Fontspector` QA Check Delta")
    lines.append(f"- **Candidate Totals:** FATAL: `{qa_result.fatal_count}` | ERROR: `{qa_result.error_count}` | WARN: `{qa_result.warn_count}` | PASS: `{qa_result.pass_count}`")
    lines.append(f"- **New Regressions:** 🔴 `{qa_result.new_fatal_count}` Fatal | 🔴 `{qa_result.new_error_count}` Error | 🟡 `{qa_result.new_warn_count}` Warn")
    lines.append(f"- **Pre-existing Known Failures:** 🟡 `{qa_result.known_failure_count}` (Present in baseline installed font)")
    if qa_result.fixed_failure_count > 0:
        lines.append(f"- **Resolved / Fixed Failures:** 🟢 `{qa_result.fixed_failure_count}` (Failed in baseline, now passing!)")
    lines.append("")

    if qa_result.new_failures:
        lines.append("#### 🔴 New QA Regressions Introduced:")
        for item in qa_result.new_failures[:10]:
            lines.append(f"- `{item['check_id']}` ({item['status']}): *Baseline was {item['baseline_status']}*")
        lines.append("")

    if qa_result.known_failures:
        lines.append("#### 🟡 Pre-existing Known Failures (Inherited from Baseline):")
        for item in qa_result.known_failures[:10]:
            lines.append(f"- `{item['check_id']}` ({item['status']})")
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
    Includes font file matching identification, binary diff status, and system operational mode.
    """
    family_name = result.get("family_name", "Unknown")
    has_update = result.get("has_update", False)
    matching = result.get("font_matching_analysis", {})

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
    lines.append("")

    matched_pairs = matching.get("matched_pairs", [])
    if matched_pairs:
        lines.append("### 📑 Detailed Font File Mapping & Hash Table")
        lines.append("")
        lines.append("| Local Font Filename | Candidate Upstream Filename | Match Strategy | Binary Hash Status |")
        lines.append("| :--- | :--- | :--- | :--- |")
        for p in matched_pairs:
            loc_f = p.get("local_filename", "")
            cand_f = p.get("candidate_filename", "")
            m_type = p.get("match_type", "UNMATCHED")
            hash_chg = "🔴 Changed / Updated" if p.get("binary_hash_changed") else "🟢 Identical (No Change)"
            lines.append(f"| `{loc_f}` | `{cand_f}` | `{m_type}` | {hash_chg} |")
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
    lines.append("")

    if "pr_body" in result:
        lines.append("---")
        lines.append("## 📝 Simulated PR Description & Checklist Preview")
        lines.append("")
        lines.append(result["pr_body"])

    content = "\n".join(lines)
    if output_filepath:
        Path(output_filepath).write_text(content, encoding="utf-8")
    return content


def generate_live_repository_audit_report(
    summary: Dict[str, Any],
    results: List[Dict[str, Any]],
    output_filepath: str = "live_repo_verification_report.md",
) -> str:
    """
    Generate comprehensive multi-family live repository verification report.
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

    lines.append("## 🚀 Family Verification Results Detail")
    lines.append("")
    lines.append("| Family Name | Upstream Update | Installed Ver | Upstream Ver | Font File Matching | STU Score | Decision Tier | Status |")
    lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    for r in results:
        fam = r.get("family_name", "Unknown")
        upd = "YES 🆕" if r.get("has_update") else "NO ✅"
        cur_v = r.get("current_version", "N/A") or "N/A"
        up_v = r.get("upstream_version", "N/A") or "N/A"
        matching_status = r.get("font_matching_analysis", {}).get("status", "N/A")
        match_rate = r.get("font_matching_analysis", {}).get("match_rate_pct", 0.0)
        score = r.get("safety_score", "N/A")
        tier = r.get("safety_tier", "N/A")
        status = r.get("status", "CHECKED")

        match_str = f"`{matching_status}` ({match_rate:.0f}%)"

        lines.append(f"| **{fam}** | {upd} | `{cur_v}` | `{up_v}` | {match_str} | `{score}` | `{tier}` | `{status}` |")

    lines.append("")
    lines.append("---")
    lines.append("*Report generated automatically by Google Fonts Auto-Updater Live Repository Auditor*")

    content = "\n".join(lines)
    Path(output_filepath).write_text(content, encoding="utf-8")
    return content

