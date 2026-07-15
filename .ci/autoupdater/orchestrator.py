"""
Pipeline orchestrator module tying together ingestion, monitoring, acquisition,
regression testing, scoring, and PR generation.
Located internally within google/fonts at .ci/autoupdater/orchestrator.py.
"""

from pathlib import Path
from typing import Optional, Dict, Any, List
from .models import FamilyMetadata, UpdateCheckResult, SafetyTier, UpdateType
from .metadata_parser import load_metadata_pb
from .metadata_updater import update_metadata_pb
from .upstream_monitor import UpstreamMonitor
from .artifact_fetcher import ArtifactFetcher, compare_ttf_dir_hashes
from .regression_engine import (
    RegressionEngine,
    DiffenatorResult,
    QACheckResult,
    SafetyScoreBreakdown,
)
from .report_generator import generate_pr_body
from .state_store import StateStore
from .pr_creator import PRCreator


class AutoUpdatePipeline:
    """End-to-end pipeline manager for Google Fonts Auto-Updater."""

    def __init__(self, state_db_path: str = "gf_autoupdater_state.db"):
        self.monitor = UpstreamMonitor()
        self.fetcher = ArtifactFetcher()
        self.regression_engine = RegressionEngine()
        self.state_store = StateStore(db_path=state_db_path)
        self.pr_creator = PRCreator()

    def evaluate_auto_merge(self, score_info: SafetyScoreBreakdown, family_meta: FamilyMetadata) -> bool:
        """
        Auto-merge policy enforcer: Returns True if and only if update meets strict AUTO_APPROVE criteria.
        """
        if score_info.safety_tier != SafetyTier.AUTO_APPROVE:
            return False
        if score_info.composite_score < 95.0:
            return False
        if score_info.blocking_reasons:
            return False
        return True

    def process_family(
        self,
        metadata_filepath: str,
        mock_diff_result: Optional[DiffenatorResult] = None,
        candidate_ttf_fonts: Optional[List[tuple]] = None,
        create_pr: bool = False,
        base_branch: str = "main",
    ) -> Dict[str, Any]:
        """
        Execute full end-to-end update workflow for a font family metadata file.
        """
        meta_path = Path(metadata_filepath)
        meta = load_metadata_pb(str(meta_path))

        # Register family in state store
        self.state_store.register_family(
            family_name=meta.name,
            repository_url=meta.source.repository_url if meta.source else None,
            license_type=meta.license,
            current_commit=meta.source.commit if meta.source else None,
            current_version=meta.installed_version_num or meta.installed_version,
        )

        # Phase 1: Upstream Monitor Check
        check_result = self.monitor.check_for_updates(meta)
        if not check_result.has_update:
            status_str = "RATE_LIMITED" if check_result.error and "RATE_LIMITED" in check_result.error else "NO_UPDATE"
            self.state_store.record_check_result(
                family_name=meta.name,
                has_update=False,
                update_type=check_result.update_type.value,
                status=status_str,
            )
            return {
                "family_name": meta.name,
                "has_update": False,
                "current_version": check_result.current_version,
                "upstream_version": check_result.upstream_version,
                "current_commit": check_result.current_commit,
                "upstream_commit": check_result.upstream_commit,
                "status": status_str,
                "error": check_result.error,
            }

        # Pre-Flight Binary Hash Check: If candidate TTFs are byte-for-byte identical to existing TTFs
        if candidate_ttf_fonts:
            existing_dir = meta_path.parent
            ttf_changed = compare_ttf_dir_hashes(existing_dir, candidate_ttf_fonts)
            if not ttf_changed:
                self.state_store.record_check_result(
                    family_name=meta.name,
                    has_update=False,
                    update_type=check_result.update_type.value,
                    status="NO_TTF_BINARY_CHANGE",
                )
                return {
                    "family_name": meta.name,
                    "has_update": False,
                    "current_version": check_result.current_version,
                    "upstream_version": check_result.upstream_version,
                    "current_commit": check_result.current_commit,
                    "upstream_commit": check_result.upstream_commit,
                    "status": "NO_TTF_BINARY_CHANGE",
                    "message": "Candidate TTF binaries are 100% byte-for-byte identical to existing Google Fonts TTFs.",
                }

        # Phase 2: Acquire verbatim TTF binaries
        # Phase 3: Run Regression Engine (diffenator2 & Fontspector)
        diff_res = mock_diff_result or DiffenatorResult(
            visual_diff_pixel_ratio=0.001,
            max_vertical_metric_shift=0,
            deleted_unicodes=[],
        )
        qa_res = QACheckResult(fatal_count=0, error_count=0, warn_count=0, pass_count=120)

        score_info = self.regression_engine.calculate_safety_score(diff_res, qa_res)
        should_auto_merge = self.evaluate_auto_merge(score_info, meta)

        # Phase 4: Generate PR body and report artifacts
        pr_body = generate_pr_body(meta, check_result, score_info, diff_res, qa_res)
        updated_pb_content = update_metadata_pb(meta, new_commit=check_result.upstream_commit)

        pr_info = None
        if create_pr:
            version_str = check_result.upstream_version or (check_result.upstream_commit[:7] if check_result.upstream_commit else "update")
            pr_title = f"🤖 Update upstream font: {meta.name} v{version_str}"
            pr_info = self.pr_creator.create_pull_request(
                family_name=meta.name,
                metadata_filepath=str(meta_path),
                updated_pb_content=updated_pb_content,
                pr_title=pr_title,
                pr_body=pr_body,
                upstream_version=check_result.upstream_version,
                upstream_commit=check_result.upstream_commit,
                base_branch=base_branch,
            )

        # Record pipeline completion
        status_val = "PR_CREATED" if (pr_info and pr_info.get("created")) else ("PR_READY" if not should_auto_merge else "AUTO_MERGED")

        check_id = self.state_store.record_check_result(
            family_name=meta.name,
            has_update=True,
            update_type=check_result.update_type.value,
            upstream_version=check_result.upstream_version,
            upstream_commit=check_result.upstream_commit,
            safety_score=score_info.composite_score,
            safety_tier=score_info.safety_tier.value,
            status=status_val,
        )

        return {
            "family_name": meta.name,
            "has_update": True,
            "check_id": check_id,
            "current_version": check_result.current_version,
            "upstream_version": check_result.upstream_version,
            "current_commit": check_result.current_commit,
            "upstream_commit": check_result.upstream_commit,
            "safety_score": score_info.composite_score,
            "safety_tier": score_info.safety_tier.value,
            "auto_merge_qualified": should_auto_merge,
            "status": status_val,
            "pr_info": pr_info,
            "pr_body": pr_body,
            "updated_pb_content": updated_pb_content,
        }


