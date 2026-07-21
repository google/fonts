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
from .artifact_fetcher import ArtifactFetcher, compare_ttf_dir_hashes, compute_sha256
from .regression_engine import (
    RegressionEngine,
    DiffenatorResult,
    QACheckResult,
    SafetyScoreBreakdown,
)
from .report_generator import generate_pr_body
from .state_store import StateStore
from .pr_creator import PRCreator
from .fontspector_runner import run_fontspector, compare_qa_results
from .diffenator_runner import run_diffenator_analysis, load_font_mappings
from .manual_instructions import ManualInstructions



def analyze_font_file_matching(
    local_dir: Path,
    candidate_fonts: Optional[List[Any]],
    family_slug: str,
) -> Dict[str, Any]:
    """
    Analyze font file matching between existing local TTF files in Google Fonts repo
    and acquired upstream candidate TTF files. Identifies filename identity, mapped files,
    unmatched files, and flags required mapping entries in font_mappings.json.
    """
    local_ttf_paths = sorted(list(local_dir.glob("*.ttf")))
    local_filenames = [p.name for p in local_ttf_paths]

    if not candidate_fonts:
        return {
            "status": "NO_CANDIDATE_FONTS",
            "naming_identity_status": "NO_CANDIDATE_FONTS",
            "are_filenames_identical": False,
            "mapping_action_required": False,
            "local_ttf_count": len(local_filenames),
            "candidate_ttf_count": 0,
            "local_filenames": local_filenames,
            "candidate_filenames": [],
            "matched_pairs": [],
            "unmatched_local_filenames": local_filenames,
            "unmatched_candidate_filenames": [],
            "suggested_mapping_snippet": {},
            "match_rate_pct": 0.0,
            "has_binary_changes": False,
        }

    mappings = load_font_mappings(family_slug)

    cand_tuples = []
    for item in candidate_fonts:
        if isinstance(item, (list, tuple)):
            cand_path = Path(item[0])
            cand_hash = str(item[1]) if len(item) > 1 else ""
        else:
            cand_path = Path(item)
            cand_hash = ""
        cand_tuples.append((cand_path, cand_hash))

    cand_filenames = [c[0].name for c in cand_tuples]
    cand_by_name = {c[0].name: c for c in cand_tuples}

    matched_pairs = []
    unmatched_local = []
    unmatched_cand = set(cand_filenames)
    has_binary_changes = False

    for loc_path in local_ttf_paths:
        loc_name = loc_path.name
        loc_hash = ""
        try:
            loc_hash = compute_sha256(str(loc_path))
        except Exception:
            pass

        cand_match_name = None
        match_type = "UNMATCHED"

        if loc_name in cand_by_name:
            cand_match_name = loc_name
            match_type = "EXACT_NAME"
        else:
            # Check if any candidate maps to loc_name via font_mappings
            for cand_name, target_name in mappings.items():
                if target_name == loc_name and cand_name in cand_by_name:
                    cand_match_name = cand_name
                    match_type = "MAPPED_NAME"
                    break

        if cand_match_name:
            cand_path, cand_hash = cand_by_name[cand_match_name]
            if cand_match_name in unmatched_cand:
                unmatched_cand.remove(cand_match_name)
            hash_changed = (loc_hash != cand_hash) if (loc_hash and cand_hash) else True
            if hash_changed:
                has_binary_changes = True

            matched_pairs.append({
                "local_filename": loc_name,
                "candidate_filename": cand_match_name,
                "match_type": match_type,
                "local_sha256": loc_hash,
                "candidate_sha256": cand_hash,
                "binary_hash_changed": hash_changed,
            })
        else:
            unmatched_local.append(loc_name)

    unmatched_candidate_list = sorted(list(unmatched_cand))

    # Determine filename identity and mapping action requirements
    are_filenames_identical = (sorted(local_filenames) == sorted(cand_filenames))
    mapping_action_required = False
    suggested_mapping_snippet = {}

    if are_filenames_identical:
        naming_identity_status = "IDENTICAL_NAMES"
    elif all(p["match_type"] in ("EXACT_NAME", "MAPPED_NAME") for p in matched_pairs) and not unmatched_candidate_list:
        naming_identity_status = "MAPPED_NAMES"
    else:
        naming_identity_status = "UNMATCHED_NAMES"
        if unmatched_candidate_list:
            mapping_action_required = True
            for un_cand in unmatched_candidate_list:
                # Suggest ground truth target fallback
                suggested_mapping_snippet[un_cand] = local_filenames[0] if local_filenames else "TargetFont.ttf"

    if len(matched_pairs) == len(local_filenames) and not unmatched_candidate_list:
        status = "EXACT_MATCH"
    elif len(matched_pairs) > 0 and all(p["match_type"] in ("EXACT_NAME", "MAPPED_NAME") for p in matched_pairs):
        status = "MAPPED_MATCH"
    elif len(matched_pairs) > 0:
        status = "FLAGGED_FOR_REVIEW"
    else:
        status = "NO_MATCH_FOUND"
        naming_identity_status = "NO_MATCH_FOUND"

    match_rate = (len(matched_pairs) / len(local_filenames) * 100.0) if local_filenames else 0.0

    return {
        "status": status,
        "naming_identity_status": naming_identity_status,
        "are_filenames_identical": are_filenames_identical,
        "mapping_action_required": mapping_action_required,
        "suggested_mapping_snippet": suggested_mapping_snippet,
        "local_ttf_count": len(local_filenames),
        "candidate_ttf_count": len(cand_filenames),
        "local_filenames": local_filenames,
        "candidate_filenames": cand_filenames,
        "matched_pairs": matched_pairs,
        "unmatched_local_filenames": unmatched_local,
        "unmatched_candidate_filenames": unmatched_candidate_list,
        "match_rate_pct": round(match_rate, 2),
        "has_binary_changes": has_binary_changes,
    }



class AutoUpdatePipeline:
    """End-to-end pipeline manager for Google Fonts Auto-Updater."""

    def __init__(self, state_db_path: str = "gf_autoupdater_state.db"):
        self.monitor = UpstreamMonitor()
        self.fetcher = ArtifactFetcher()
        self.regression_engine = RegressionEngine()
        self.state_store = StateStore(db_path=state_db_path)
        self.pr_creator = PRCreator()
        self.manual_instructions = ManualInstructions()


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

        # Ensure local installed version is extracted before upstream check
        from .metadata_parser import ensure_local_version_extracted
        ensure_local_version_extracted(meta)

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

        family_slug = meta.name.lower().replace(" ", "")

        # Lazily extract local installed version details for update candidate
        from .metadata_parser import ensure_local_version_extracted
        ensure_local_version_extracted(meta)
        check_result.current_version = meta.installed_version_num or meta.installed_version


        # Phase 2: Acquire verbatim TTF binaries from upstream
        if not candidate_ttf_fonts:
            cache_dir = Path("download_cache") / family_slug
            candidate_ttf_fonts = self.fetcher.acquire_upstream_binaries(
                release=check_result.release_info,
                family_meta=meta,
                output_dir=cache_dir,
                upstream_commit=check_result.upstream_commit,
            )

        directives = self.manual_instructions.get_family_directives(meta.name)

        # If catalog family is variable or variable update is approved, filter candidate binaries to variable fonts only
        is_catalog_variable = any("[" in f.filename for f in meta.catalog_font_files)
        if candidate_ttf_fonts and (is_catalog_variable or directives["is_variable_update"]):
            var_candidates = [
                c for c in candidate_ttf_fonts
                if "[" in (Path(c[0]).name if isinstance(c, (list, tuple)) else Path(c).name)
                or "variable" in (Path(c[0]).name if isinstance(c, (list, tuple)) else Path(c).name).lower()
                or "vf" in (Path(c[0]).name if isinstance(c, (list, tuple)) else Path(c).name).lower()
            ]
            if var_candidates:
                candidate_ttf_fonts = var_candidates

        # Validate actual font version string from candidate TTF binary rather than relying solely on tag name
        if candidate_ttf_fonts:
            from .version_comparator import extract_ttf_font_version
            for cand_item in candidate_ttf_fonts:
                cand_path = Path(cand_item[0]) if isinstance(cand_item, (list, tuple)) else Path(cand_item)
                name_ver, ver_num, rev = extract_ttf_font_version(cand_path)
                if ver_num:
                    check_result.upstream_version = ver_num
                    break


        # Step 3: Font File Matching Analysis & Mapping Flagging
        font_matching_analysis = analyze_font_file_matching(
            local_dir=meta_path.parent,
            candidate_fonts=candidate_ttf_fonts,
            family_slug=family_slug,
        )
        font_matching_analysis["is_variable_update_approved"] = directives["is_variable_update"]

        # 4th Category: NO_MATCH_FOUND exit in Step 3
        if font_matching_analysis.get("status") == "NO_MATCH_FOUND" and not directives["is_variable_update"]:
            self.state_store.record_check_result(
                family_name=meta.name,
                has_update=False,
                update_type=check_result.update_type.value,
                status="NO_MATCH_FOUND",
            )
            return {
                "family_name": meta.name,
                "has_update": False,
                "current_version": check_result.current_version,
                "upstream_version": check_result.upstream_version,
                "current_commit": check_result.current_commit,
                "upstream_commit": check_result.upstream_commit,
                "status": "NO_MATCH_FOUND",
                "font_matching_analysis": font_matching_analysis,
                "is_human_approved": directives["is_human_approved"],
                "is_variable_update_approved": directives["is_variable_update"],
                "message": "Step 3 Exit: No matching font files found between candidate upstream binaries and local catalog fonts. Create mapping entry in font_mappings.json or manual_instructions.json.",
            }

        # If unmatched candidate filenames exist and not approved for variable upgrade, flag for review
        if font_matching_analysis.get("mapping_action_required") and not directives["is_variable_update"]:
            font_matching_analysis["status"] = "FLAGGED_FOR_REVIEW"

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
                    "font_matching_analysis": font_matching_analysis,
                    "is_human_approved": directives["is_human_approved"],
                    "is_variable_update_approved": directives["is_variable_update"],
                    "message": "Candidate TTF binaries are 100% byte-for-byte identical to existing Google Fonts TTFs.",
                }

        # Step 4: Embedded Binary Version Validation (Upstream TTF vs Catalog TTF)
        from .version_comparator import extract_ttf_font_version, compare_version_numbers

        has_newer_binary = False
        latest_upstream_ttf_ver = None
        latest_catalog_ttf_ver = None

        matched_pairs = font_matching_analysis.get("matched_pairs", [])
        for pair in matched_pairs:
            loc_path = meta_path.parent / pair["local_filename"]
            # Find candidate path
            cand_path = None
            if candidate_ttf_fonts:
                for c in candidate_ttf_fonts:
                    cp = Path(c[0]) if isinstance(c, (list, tuple)) else Path(c)
                    if cp.name == pair["candidate_filename"]:
                        cand_path = cp
                        break

            if loc_path.exists() and cand_path and cand_path.exists():
                _, loc_ver, _ = extract_ttf_font_version(loc_path)
                _, cand_ver, _ = extract_ttf_font_version(cand_path)

                pair["catalog_ttf_version"] = loc_ver
                pair["candidate_ttf_version"] = cand_ver

                if cand_ver:
                    latest_upstream_ttf_ver = cand_ver
                if loc_ver:
                    latest_catalog_ttf_ver = loc_ver

                if cand_ver and loc_ver:
                    cmp_res = compare_version_numbers(cand_ver, loc_ver)
                    if cmp_res > 0:
                        pair["version_comparison"] = "UPDATE_CONFIRMED"
                        has_newer_binary = True
                    elif cmp_res == 0:
                        pair["version_comparison"] = "UP_TO_DATE"
                    else:
                        pair["version_comparison"] = "LOCAL_IS_NEWER"
                elif cand_ver:
                    has_newer_binary = True

        if latest_upstream_ttf_ver:
            check_result.upstream_version = latest_upstream_ttf_ver

        # If candidate TTF version is NOT newer than catalog font version (or 0 candidate TTFs acquired), stop
        if not has_newer_binary and not directives["is_human_approved"]:
            self.state_store.record_check_result(
                family_name=meta.name,
                has_update=False,
                update_type=check_result.update_type.value,
                status="VERSION_NOT_NEWER" if candidate_ttf_fonts else "NO_MATCH_FOUND",
            )
            return {
                "family_name": meta.name,
                "has_update": False,
                "current_version": latest_catalog_ttf_ver or check_result.current_version,
                "upstream_version": latest_upstream_ttf_ver or check_result.upstream_version,
                "current_commit": check_result.current_commit,
                "upstream_commit": check_result.upstream_commit,
                "status": "VERSION_NOT_NEWER" if candidate_ttf_fonts else "NO_MATCH_FOUND",
                "font_matching_analysis": font_matching_analysis,
                "is_human_approved": directives["is_human_approved"],
                "is_variable_update_approved": directives["is_variable_update"],
                "message": f"Upstream candidate font binary version ({latest_upstream_ttf_ver}) is not newer than installed catalog font version ({latest_catalog_ttf_ver})." if candidate_ttf_fonts else "No candidate .ttf font binaries found in upstream repository or release assets.",
            }



        # Phase 3: Run Regression Engine (diffenator2 & Fontspector QA)
        baseline_ttf_paths = [str(p) for p in meta_path.parent.glob("*.ttf")]
        cand_ttf_paths = [str(t[0]) for t in candidate_ttf_fonts] if candidate_ttf_fonts else baseline_ttf_paths

        if mock_diff_result:
            diff_res = mock_diff_result
            unmatched_warnings = []
        else:
            diff_res, unmatched_warnings = run_diffenator_analysis(
                baseline_ttf_paths, cand_ttf_paths, family_slug=family_slug
            )

        baseline_qa_checks = run_fontspector(baseline_ttf_paths)
        candidate_qa_checks = run_fontspector(cand_ttf_paths) if cand_ttf_paths != baseline_ttf_paths else baseline_qa_checks

        qa_diff = compare_qa_results(baseline_qa_checks, candidate_qa_checks)

        qa_res = QACheckResult(
            fatal_count=qa_diff.fatal_count,
            error_count=qa_diff.error_count,
            warn_count=qa_diff.warn_count,
            pass_count=qa_diff.pass_count,
            new_fatal_count=qa_diff.new_fatal_count,
            new_error_count=qa_diff.new_error_count,
            new_warn_count=qa_diff.new_warn_count,
            known_failure_count=qa_diff.known_failure_count,
            fixed_failure_count=qa_diff.fixed_failure_count,
            new_failures=qa_diff.new_failures,
            known_failures=qa_diff.known_failures,
            fixed_failures=qa_diff.fixed_failures,
        )

        score_info = self.regression_engine.calculate_safety_score(diff_res, qa_res)
        if unmatched_warnings:
            score_info.blocking_reasons.extend(unmatched_warnings)

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
                candidate_ttf_fonts=candidate_ttf_fonts,
                upstream_version=check_result.upstream_version,
                upstream_commit=check_result.upstream_commit,
                base_branch=base_branch,
            )

        # Record pipeline completion
        status_val = "PR_CREATED" if (pr_info and pr_info.get("created")) else ("PR_READY (DRY RUN)" if not create_pr else "PR_READY")

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
            "blocking_reasons": score_info.blocking_reasons,
            "auto_merge_qualified": should_auto_merge,
            "status": status_val,

            "pr_submission_enabled": create_pr,
            "pr_info": pr_info,
            "font_matching_analysis": font_matching_analysis,
            "is_human_approved": directives["is_human_approved"],
            "is_variable_update_approved": directives["is_variable_update"],
            "qa_res": qa_res,
            "diff_res": diff_res,
            "pr_body": pr_body,
            "updated_pb_content": updated_pb_content,
            "candidate_ttf_fonts": candidate_ttf_fonts,
        }




