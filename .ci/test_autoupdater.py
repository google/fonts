"""
Unit and integration tests for internal Google Fonts Auto-Updater (.ci/autoupdater).
"""

import sys
import unittest
from pathlib import Path

ci_dir = str(Path(__file__).parent)
if ci_dir not in sys.path:
    sys.path.insert(0, ci_dir)

from autoupdater.models import FamilyMetadata, UpstreamRelease, UpstreamSource, VersionComparisonStatus
from autoupdater.metadata_parser import parse_metadata_pb
from autoupdater.version_comparator import (
    parse_clean_version,
    compare_version_numbers,
    compare_local_vs_upstream,
)
from autoupdater.regression_engine import (
    RegressionEngine,
    DiffenatorResult,
    QACheckResult,
    SafetyTier,
)
from autoupdater.catalog_audit import format_eta, make_progress_bar


class TestInternalAutoUpdater(unittest.TestCase):

    def test_version_string_parsing(self):
        self.assertEqual(parse_clean_version("Version 3.012;FEA", None), "3.012")
        self.assertEqual(parse_clean_version(None, 4.001), "4.001")
        self.assertEqual(parse_clean_version("Version 2.5", 2.5), "2.5")

    def test_version_number_comparison(self):
        self.assertEqual(compare_version_numbers("3.012", "3.000"), 1)
        self.assertEqual(compare_version_numbers("2.000", "2.000"), 0)
        self.assertEqual(compare_version_numbers("1.900", "2.000"), -1)

    def test_local_vs_upstream_comparison(self):
        meta = FamilyMetadata(
            name="Inter",
            installed_version_num="3.000",
            installed_git_commit_date="2026-01-01T00:00:00+00:00",
            source=UpstreamSource(repository_url="https://github.com/rsms/inter", commit="abc1234"),
        )
        release_newer = UpstreamRelease(
            tag_name="v3.012",
            version="3.012",
            published_at="2026-06-01T00:00:00Z",
        )
        status, info = compare_local_vs_upstream(meta, upstream_release=release_newer)
        self.assertEqual(status, VersionComparisonStatus.UPDATE_AVAILABLE)

    def test_regression_safety_scoring(self):
        engine = RegressionEngine()
        diff_res = DiffenatorResult(
            visual_diff_pixel_ratio=0.001,
            max_vertical_metric_shift=0,
            deleted_unicodes=[],
        )
        qa_res = QACheckResult(fatal_count=0, error_count=0, warn_count=0, pass_count=100)
        score = engine.calculate_safety_score(diff_res, qa_res)
        self.assertEqual(score.safety_tier, SafetyTier.AUTO_APPROVE)
        self.assertGreaterEqual(score.composite_score, 95.0)

    def test_progress_helpers(self):
        self.assertEqual(format_eta(3665), "01:01:05")
        self.assertEqual(format_eta(0), "--:--:--")
        bar_half = make_progress_bar(50.0, width=10)
        self.assertEqual(bar_half, "█████░░░░░")


if __name__ == "__main__":
    unittest.main()
