"""
Report and PR description generation module for automated upstream updates.
Located internally within google/fonts at .ci/autoupdater/report_generator.py.
"""

from typing import Optional
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
