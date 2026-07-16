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

    def test_gftools_packager_import(self):
        from autoupdater.artifact_fetcher import _import_gftools_packager
        packager = _import_gftools_packager()
        if packager:
            self.assertTrue(hasattr(packager, "PR_CHECKLIST"))
            self.assertTrue(hasattr(packager, "ADD_TO_TRAFFIC_JAM"))

    def test_pr_creator_checklist_integration(self):
        from autoupdater.pr_creator import PRCreator, _import_gftools_packager
        creator = PRCreator()
        packager = _import_gftools_packager()
        result = creator.create_pull_request(
            family_name="Roboto",
            metadata_filepath="ofl/roboto/METADATA.pb",
            updated_pb_content='name: "Roboto"\n',
            pr_title="Update Roboto",
            pr_body="Initial PR body text.",
            dry_run=True,
        )
        self.assertFalse(result["created"])
        self.assertTrue(result["dry_run"])

    def test_font_matching_analysis(self):
        from autoupdater.orchestrator import analyze_font_file_matching
        local_dir = Path("ofl/roboto")
        matching = analyze_font_file_matching(local_dir, None, "roboto")
        self.assertIn("status", matching)
        self.assertIn("match_rate_pct", matching)

    def test_family_verification_report_generation(self):
        from autoupdater.report_generator import generate_family_verification_report
        sample_res = {
            "family_name": "Inter",
            "has_update": True,
            "current_version": "3.000",
            "upstream_version": "3.012",
            "safety_score": 98.5,
            "safety_tier": "AUTO_APPROVE",
            "status": "PR_READY (DRY RUN)",
            "font_matching_analysis": {
                "status": "EXACT_MATCH",
                "local_ttf_count": 2,
                "candidate_ttf_count": 2,
                "match_rate_pct": 100.0,
                "has_binary_changes": True,
                "matched_pairs": [
                    {
                        "local_filename": "Inter[wght].ttf",
                        "candidate_filename": "Inter[wght].ttf",
                        "match_type": "EXACT_NAME",
                        "binary_hash_changed": True,
                    }
                ],
            },
        }
        report_text = generate_family_verification_report(sample_res)
        self.assertIn("Live Repository Verification Report", report_text)
        self.assertIn("PR Submission Mode", report_text)
        self.assertIn("EXACT_MATCH", report_text)


if __name__ == "__main__":
    unittest.main()


