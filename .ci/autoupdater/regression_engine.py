"""
Regression testing engine and 'Safe to Update' (STU) scoring model module.
Located internally within google/fonts at .ci/autoupdater/regression_engine.py.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from pathlib import Path
from .models import SafetyTier


@dataclass
class DiffenatorResult:
    visual_diff_pixel_ratio: float = 0.0
    max_vertical_metric_shift: int = 0
    max_advance_width_shift_pct: float = 0.0
    deleted_unicodes: List[int] = field(default_factory=list)
    added_unicodes: List[int] = field(default_factory=list)
    has_gpos_regression: bool = False
    has_gsub_regression: bool = False


@dataclass
class QACheckResult:
    fatal_count: int = 0
    error_count: int = 0
    warn_count: int = 0
    pass_count: int = 0
    new_fatal_count: int = 0
    new_error_count: int = 0
    new_warn_count: int = 0
    known_failure_count: int = 0
    fixed_failure_count: int = 0
    new_failures: List[Dict[str, Any]] = field(default_factory=list)
    known_failures: List[Dict[str, Any]] = field(default_factory=list)
    fixed_failures: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class SafetyScoreBreakdown:
    s_visual: float
    s_metric: float
    s_cmap: float
    s_qa: float
    composite_score: float
    safety_tier: SafetyTier
    blocking_reasons: List[str] = field(default_factory=list)


class RegressionEngine:
    """
    Evaluates font candidate updates against baseline production fonts using diffenator2
    visual/metric diffs and Fontspector QA evaluations to calculate Safe to Update (STU) Score.
    """

    def __init__(
        self,
        weight_visual: float = 0.35,
        weight_metric: float = 0.25,
        weight_cmap: float = 0.25,
        weight_qa: float = 0.15,
    ):
        self.w_visual = weight_visual
        self.w_metric = weight_metric
        self.w_cmap = weight_cmap
        self.w_qa = weight_qa

    def compute_s_visual(self, diff_res: DiffenatorResult) -> float:
        """S_visual = 100 * (1 - visual_diff_pixel_ratio)."""
        ratio = max(0.0, min(1.0, diff_res.visual_diff_pixel_ratio))
        return max(0.0, 100.0 * (1.0 - ratio))

    def compute_s_metric(self, diff_res: DiffenatorResult, blocking_reasons: List[str]) -> float:
        """
        S_metric evaluates vertical metrics & horizontal advance width stability.
        Vertical metric change > 10 units is a severe web reflow penalty.
        """
        score = 100.0
        if diff_res.max_vertical_metric_shift > 0:
            if diff_res.max_vertical_metric_shift > 10:
                score -= 50.0
                blocking_reasons.append(
                    f"Vertical metric shift of {diff_res.max_vertical_metric_shift} units exceeds threshold (10 units)"
                )
            else:
                score -= 20.0

        if diff_res.max_advance_width_shift_pct > 0.05:
            score -= 20.0
            blocking_reasons.append(
                f"Advance width shift of {diff_res.max_advance_width_shift_pct*100:.1f}% exceeds 5% threshold"
            )

        return max(0.0, score)

    def compute_s_cmap(self, diff_res: DiffenatorResult, blocking_reasons: List[str]) -> float:
        """
        S_cmap evaluates character map retention.
        Deleting any existing Unicode character is a critical breaking change!
        """
        if diff_res.deleted_unicodes:
            blocking_reasons.append(
                f"CRITICAL BREAKING CHANGE: Deleted {len(diff_res.deleted_unicodes)} existing Unicode character(s)"
            )
            return 0.0
        return 100.0

    def compute_s_qa(self, qa_res: QACheckResult, blocking_reasons: List[str]) -> float:
        """
        S_qa evaluates Fontspector / FontBakery checks delta.
        Strictly penalizes NEW regressions, ignoring pre-existing findings.
        """
        score = 100.0
        # Penalize ONLY NEW regressions
        if qa_res.new_fatal_count > 0:
            score -= 50.0 * qa_res.new_fatal_count
            blocking_reasons.append(f"Fontspector QA identified {qa_res.new_fatal_count} NEW FATAL check regression(s)")

        if qa_res.new_error_count > 0:
            score -= 20.0 * qa_res.new_error_count
            blocking_reasons.append(f"Fontspector QA identified {qa_res.new_error_count} NEW ERROR check regression(s)")

        if qa_res.new_warn_count > 0:
            score -= 3.0 * qa_res.new_warn_count

        return max(0.0, score)



    def calculate_safety_score(
        self, diff_res: DiffenatorResult, qa_res: QACheckResult
    ) -> SafetyScoreBreakdown:
        """
        Calculate composite Safe to Update (STU) Score and determine SafetyTier.
        Formula: S = 0.35 * S_visual + 0.25 * S_metric + 0.25 * S_cmap + 0.15 * S_qa
        """
        blocking_reasons: List[str] = []

        s_visual = self.compute_s_visual(diff_res)
        s_metric = self.compute_s_metric(diff_res, blocking_reasons)
        s_cmap = self.compute_s_cmap(diff_res, blocking_reasons)
        s_qa = self.compute_s_qa(qa_res, blocking_reasons)

        composite = (
            self.w_visual * s_visual
            + self.w_metric * s_metric
            + self.w_cmap * s_cmap
            + self.w_qa * s_qa
        )

        if composite >= 95.0 and not blocking_reasons:
            tier = SafetyTier.AUTO_APPROVE
        elif composite >= 75.0 and not any("CRITICAL" in r or "FATAL" in r for r in blocking_reasons):
            tier = SafetyTier.NEEDS_REVIEW
        else:
            tier = SafetyTier.BLOCKED

        return SafetyScoreBreakdown(
            s_visual=round(s_visual, 2),
            s_metric=round(s_metric, 2),
            s_cmap=round(s_cmap, 2),
            s_qa=round(s_qa, 2),
            composite_score=round(composite, 2),
            safety_tier=tier,
            blocking_reasons=blocking_reasons,
        )
