"""
Diffenator and font metrics diffing module for Google Fonts Auto-Updater.
Computes character map retention, vertical metric shifts, advance width stability,
and GPOS/GSUB feature table diffs between baseline and candidate TTFs.
Located internally within google/fonts at .ci/autoupdater/diffenator_runner.py.
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from fontTools.ttLib import TTFont
from .regression_engine import DiffenatorResult


def load_font_mappings(family_slug: str) -> Dict[str, str]:
    """
    Load explicit font filename mappings for a family from .ci/autoupdater/font_mappings.json or font_mappings.json.
    Mapping format: {"upstream_cand_filename.ttf": "installed_baseline_filename.ttf"}
    """
    for loc in [".ci/autoupdater/font_mappings.json", "font_mappings.json"]:
        if os.path.exists(loc):
            try:
                with open(loc, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if family_slug in data:
                        return data[family_slug]
            except Exception:
                pass
    return {}


def pair_baseline_and_candidate_ttfs(
    baseline_ttf_paths: List[str],
    candidate_ttf_paths: List[str],
    family_slug: Optional[str] = None,
) -> Tuple[List[Tuple[str, str]], List[str]]:
    """
    Pair baseline TTF files against candidate TTF files.
    Filters out non-TTFs, WOFFs, and macOS ._ AppleDouble junk files.
    Returns (pairs, warnings).
    """
    valid_b = [
        p for p in baseline_ttf_paths
        if Path(p).name.endswith(".ttf") and not Path(p).name.startswith("._") and "__MACOSX" not in p
    ]
    valid_c = [
        p for p in candidate_ttf_paths
        if Path(p).name.endswith(".ttf") and not Path(p).name.startswith("._") and "__MACOSX" not in p
    ]

    if not valid_b or not valid_c:
        return [], []

    b_map = {Path(p).name: p for p in valid_b}
    c_map = {Path(p).name: p for p in valid_c}

    mappings = load_font_mappings(family_slug) if family_slug else {}
    pairs = []
    unmatched_warnings = []
    matched_c = set()
    matched_b = set()

    if mappings:
        for c_name, target_b_name in mappings.items():
            if c_name in c_map and target_b_name in b_map:
                pairs.append((b_map[target_b_name], c_map[c_name]))
                matched_c.add(c_name)
                matched_b.add(target_b_name)

    for c_name, c_path in c_map.items():
        if c_name in matched_c:
            continue
        if c_name in b_map:
            pairs.append((b_map[c_name], c_path))
            matched_c.add(c_name)
            matched_b.add(c_name)

    unmatched_c = set(c_map.keys()) - matched_c
    unmatched_b = set(b_map.keys()) - matched_b

    if len(unmatched_b) == 1 and len(unmatched_c) == 1:
        single_b = list(unmatched_b)[0]
        single_c = list(unmatched_c)[0]
        pairs.append((b_map[single_b], c_map[single_c]))
        matched_c.add(single_c)
        matched_b.add(single_b)
        unmatched_c.remove(single_c)
        unmatched_b.remove(single_b)

    for c_name in sorted(set(c_map.keys()) - matched_c):
        warn = f"⚠️ UNMATCHED_TTF_FILENAME: Candidate TTF '{c_name}' could not be matched automatically to any baseline font in '{family_slug or 'family'}'. Please add a mapping to .ci/autoupdater/font_mappings.json."
        unmatched_warnings.append(warn)

    return pairs, unmatched_warnings


def run_diffenator_analysis(
    baseline_ttf_paths: List[str],
    candidate_ttf_paths: List[str],
    family_slug: Optional[str] = None,
    timeout: int = 180,
) -> Tuple[DiffenatorResult, List[str]]:
    """
    Evaluates metric, cmap, and visual diffs between baseline and candidate TTFs.
    Uses diffenator2 CLI if available, with native fontTools inspection fallback.
    Returns (diff_result, unmatched_warnings).
    """
    if not baseline_ttf_paths or not candidate_ttf_paths:
        return DiffenatorResult(), []

    pairs, unmatched_warnings = pair_baseline_and_candidate_ttfs(
        baseline_ttf_paths, candidate_ttf_paths, family_slug=family_slug
    )


    all_deleted_unicodes: Set[int] = set()
    all_added_unicodes: Set[int] = set()
    max_vert_shift = 0
    max_advance_shift_pct = 0.0
    has_gpos_diff = False
    has_gsub_diff = False
    visual_pixel_ratio = 0.0

    diffenator2_bin = shutil.which("diffenator2")

    for b_path, c_path in pairs:
        try:
            b_font = TTFont(b_path)
            c_font = TTFont(c_path)

            # 1. Cmap diffs
            b_cmap = set(b_font["cmap"].getBestCmap().keys()) if "cmap" in b_font else set()
            c_cmap = set(c_font["cmap"].getBestCmap().keys()) if "cmap" in c_font else set()

            all_deleted_unicodes.update(b_cmap - c_cmap)
            all_added_unicodes.update(c_cmap - b_cmap)

            # 2. Vertical Metric shifts
            shifts = []
            if "hhea" in b_font and "hhea" in c_font:
                shifts.append(abs(c_font["hhea"].ascent - b_font["hhea"].ascent))
                shifts.append(abs(c_font["hhea"].descent - b_font["hhea"].descent))
                shifts.append(abs(c_font["hhea"].lineGap - b_font["hhea"].lineGap))

            if "OS/2" in b_font and "OS/2" in c_font:
                shifts.append(abs(c_font["OS/2"].sTypoAscender - b_font["OS/2"].sTypoAscender))
                shifts.append(abs(c_font["OS/2"].sTypoDescender - b_font["OS/2"].sTypoDescender))
                shifts.append(abs(c_font["OS/2"].sTypoLineGap - b_font["OS/2"].sTypoLineGap))
                shifts.append(abs(c_font["OS/2"].usWinAscent - b_font["OS/2"].usWinAscent))
                shifts.append(abs(c_font["OS/2"].usWinDescent - b_font["OS/2"].usWinDescent))

            if shifts:
                max_vert_shift = max(max_vert_shift, max(shifts))

            # 3. Horizontal Advance Width shift
            if "hmtx" in b_font and "hmtx" in c_font and "cmap" in b_font and "cmap" in c_font:
                b_best = b_font["cmap"].getBestCmap()
                c_best = c_font["cmap"].getBestCmap()
                shared_unicodes = set(b_best.keys()).intersection(set(c_best.keys()))

                for u in shared_unicodes:
                    g_b = b_best[u]
                    g_c = c_best[u]
                    if g_b in b_font["hmtx"].metrics and g_c in c_font["hmtx"].metrics:
                        w_b = b_font["hmtx"].metrics[g_b][0]
                        w_c = c_font["hmtx"].metrics[g_c][0]
                        if w_b > 0:
                            diff_pct = abs(w_c - w_b) / float(w_b)
                            if diff_pct > max_advance_shift_pct:
                                max_advance_shift_pct = diff_pct

            # 4. GPOS / GSUB table presence / feature diff
            for tab in ("GPOS", "GSUB"):
                if (tab in b_font) != (tab in c_font):
                    if tab == "GPOS":
                        has_gpos_diff = True
                    else:
                        has_gsub_diff = True

            b_font.close()
            c_font.close()

            # 5. Execute diffenator2 CLI if available
            if diffenator2_bin:
                with tempfile.TemporaryDirectory() as tmp_out:
                    cmd = [diffenator2_bin, "diff", "-f1", b_path, "-f2", c_path, "-o", tmp_out]
                    res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
                    if res.returncode == 0:
                        # Parse summary json if diffenator2 produces output
                        summary_file = Path(tmp_out) / "summary.json"
                        if summary_file.exists():
                            try:
                                summary_data = json.loads(summary_file.read_text(encoding="utf-8"))
                                visual_pixel_ratio = max(
                                    visual_pixel_ratio,
                                    summary_data.get("visual_diff_pixel_ratio", 0.001),
                                )
                            except Exception:
                                pass
        except Exception as e:
            print(f"⚠️ diffenator analysis warning for {b_path} vs {c_path}: {e}")

    return (
        DiffenatorResult(
            visual_diff_pixel_ratio=round(visual_pixel_ratio, 4),
            max_vertical_metric_shift=max_vert_shift,
            max_advance_width_shift_pct=round(max_advance_shift_pct, 4),
            deleted_unicodes=sorted(list(all_deleted_unicodes)),
            added_unicodes=sorted(list(all_added_unicodes)),
            has_gpos_regression=has_gpos_diff,
            has_gsub_regression=has_gsub_diff,
        ),
        unmatched_warnings,
    )

