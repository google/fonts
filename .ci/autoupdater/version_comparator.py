"""
Version and Date Comparison Engine for Google Fonts Auto-Updater.
Extracts font version strings, font revisions, local git/file modification dates,
and compares them against upstream releases and update timestamps.
"""

import re
import os
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, Dict, Any
from .models import FamilyMetadata, UpstreamRelease, VersionComparisonStatus

try:
    from fontTools.ttLib import TTFont
    HAS_FONTTOOLS = True
except ImportError:
    HAS_FONTTOOLS = False


def clean_version_string(tag: str) -> str:
    """Clean release tag into normalized version string (e.g. 'v4.0' -> '4.0')."""
    if not tag:
        return ""
    tag = tag.strip()
    if tag.startswith("v") or tag.startswith("V"):
        tag = tag[1:]
    return tag


def parse_clean_version(name_version: Optional[str], font_revision: Optional[float]) -> Optional[str]:
    """
    Extract numerical version string from nameID 5 (e.g. 'Version 3.012;FEA' -> '3.012')
    or fontRevision (e.g. 3.012).
    """
    if name_version:
        m = re.search(r'(\d+\.\d+(?:\.\d+)?)', name_version)
        if m:
            return m.group(1)
    if font_revision is not None:
        return f"{font_revision:.3f}".rstrip("0").rstrip(".")
    return None


def extract_local_font_version(family_dir: Path) -> Tuple[Optional[str], Optional[str], Optional[float]]:
    """
    Scan .ttf files in family_dir and extract:
    (name_version_string, clean_numerical_version, font_revision_float)
    """
    if not HAS_FONTTOOLS or not family_dir.exists():
        return None, None, None

    ttf_files = list(family_dir.glob("*.ttf"))
    if not ttf_files:
        return None, None, None

    for ttf_path in ttf_files:
        try:
            ttf = TTFont(str(ttf_path))
            rev = ttf["head"].fontRevision if "head" in ttf else None
            name_ver = None
            if "name" in ttf:
                for record in ttf["name"].names:
                    if record.nameID == 5:
                        name_ver = record.toUnicode()
                        break
            if name_ver or rev:
                ver_num = parse_clean_version(name_ver, rev)
                return name_ver, ver_num, rev
        except Exception:
            continue

    return None, None, None


def extract_local_git_commit_date(family_dir: Path) -> Optional[str]:
    """
    Extract last git commit ISO timestamp for the given font family directory.
    Example return: '2026-05-12T14:30:00+00:00'
    """
    try:
        res = subprocess.run(
            ["git", "log", "-1", "--format=%cI", str(family_dir)],
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass
    return None


def extract_local_file_mtime(family_dir: Path) -> Optional[str]:
    """
    Extract latest file modification time across files in family_dir in ISO format.
    """
    try:
        latest_mtime = 0.0
        for f in family_dir.glob("*"):
            if f.is_file():
                m = f.stat().st_mtime
                if m > latest_mtime:
                    latest_mtime = m
        if latest_mtime > 0:
            return datetime.fromtimestamp(latest_mtime).isoformat()
    except Exception:
        pass
    return None


def parse_iso_date(date_str: Optional[str]) -> Optional[datetime]:
    """Parse ISO 8601 date string into timezone-naive UTC datetime."""
    if not date_str:
        return None
    try:
        cleaned = date_str.replace("Z", "+00:00")
        dt = datetime.fromisoformat(cleaned)
        return dt
    except Exception:
        return None


def compare_version_numbers(v1: str, v2: str) -> int:
    """
    Compare numerical version strings v1 vs v2.
    Returns 1 if v1 > v2, -1 if v1 < v2, 0 if v1 == v2.
    Accurately compares component numbers, handling leading zeros (e.g. 2407.24 == 2407.024).
    """
    if not v1 and not v2:
        return 0
    if not v1:
        return -1
    if not v2:
        return 1

    clean1 = v1.strip().lstrip("vV")
    clean2 = v2.strip().lstrip("vV")

    parts1 = [p for p in clean1.split(".") if p]
    parts2 = [p for p in clean2.split(".") if p]

    for p1, p2 in zip(parts1, parts2):
        if p1.isdigit() and p2.isdigit():
            i1 = int(p1.lstrip("0") or "0")
            i2 = int(p2.lstrip("0") or "0")
            if i1 != i2:
                return 1 if i1 > i2 else -1

    if len(parts1) > len(parts2):
        return 1
    elif len(parts1) < len(parts2):
        return -1

    return 0


def compare_local_vs_upstream(
    meta: FamilyMetadata,
    upstream_release: Optional[UpstreamRelease] = None,
    upstream_commit: Optional[str] = None,
    upstream_commit_date: Optional[str] = None,
) -> Tuple[VersionComparisonStatus, Dict[str, Any]]:
    """
    Comprehensive comparison of local installed font versions, modification dates,
    and upstream update timestamps.
    """
    installed_ver = meta.installed_version_num
    installed_rev = meta.installed_font_revision
    installed_commit = meta.source.commit if meta.source else None
    installed_date = meta.installed_git_commit_date or meta.installed_modified_date

    upstream_ver = upstream_release.version if upstream_release else None
    upstream_published = upstream_release.published_at if upstream_release else upstream_commit_date

    info = {
        "installed_version": meta.installed_version,
        "installed_version_num": installed_ver,
        "installed_font_revision": installed_rev,
        "installed_commit": installed_commit,
        "installed_date": installed_date,
        "upstream_version": upstream_ver,
        "upstream_commit": upstream_commit,
        "upstream_published_at": upstream_published,
    }

    # Case 1: Commit Hash Match Check (Highest Priority: Same commit = No Update)
    if upstream_commit and installed_commit:
        if upstream_commit.lower().startswith(installed_commit.lower()) or installed_commit.lower().startswith(upstream_commit.lower()):
            return VersionComparisonStatus.COMMIT_UNCHANGED, info

    # Case 2: Release Version Comparison
    if upstream_ver and installed_ver:
        cmp_res = compare_version_numbers(upstream_ver, installed_ver)
        if cmp_res > 0:
            return VersionComparisonStatus.UPDATE_AVAILABLE, info
        elif cmp_res < 0:
            return VersionComparisonStatus.LOCAL_IS_NEWER, info

    # Case 3: Timestamp Comparison (Upstream published vs Local Git Commit Date)
    if upstream_published and installed_date:
        dt_up = parse_iso_date(upstream_published)
        dt_local = parse_iso_date(installed_date)
        if dt_up and dt_local:
            if dt_up > dt_local:
                return VersionComparisonStatus.UPDATE_AVAILABLE, info
            else:
                return VersionComparisonStatus.UP_TO_DATE, info

    if upstream_commit and upstream_commit != installed_commit:
        return VersionComparisonStatus.UPDATE_AVAILABLE, info

    return VersionComparisonStatus.UP_TO_DATE, info

