"""
Data models for Google Fonts Automated Upstream Update System (GFAU).
Located internally within google/fonts at .ci/autoupdater/models.py.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


class UpdateType(Enum):
    NONE = "NONE"
    RELEASE = "RELEASE"
    COMMIT = "COMMIT"


class SafetyTier(Enum):
    AUTO_APPROVE = "AUTO_APPROVE"
    NEEDS_REVIEW = "NEEDS_REVIEW"
    BLOCKED = "BLOCKED"


class VersionComparisonStatus(Enum):
    UPDATE_AVAILABLE = "UPDATE_AVAILABLE"
    UP_TO_DATE = "UP_TO_DATE"
    LOCAL_IS_NEWER = "LOCAL_IS_NEWER"
    COMMIT_UNCHANGED = "COMMIT_UNCHANGED"
    UNKNOWN = "UNKNOWN"


@dataclass
class SourceFileMapping:
    source_file: str
    dest_file: str


@dataclass
class UpstreamSource:
    repository_url: Optional[str] = None
    archive_url: Optional[str] = None
    branch: Optional[str] = "main"
    commit: Optional[str] = None
    files: List[SourceFileMapping] = field(default_factory=list)


@dataclass
class FontFile:
    name: str
    style: str = "normal"
    weight: int = 400
    filename: str = ""
    post_script_name: str = ""
    full_name: str = ""
    copyright: str = ""


@dataclass
class AxisConfig:
    tag: str
    min_value: float
    max_value: float


@dataclass
class FamilyMetadata:
    name: str
    designer: str = ""
    license: str = "OFL"
    category: str = "SANS_SERIF"
    date_added: str = ""
    subsets: List[str] = field(default_factory=list)
    fonts: List[FontFile] = field(default_factory=list)
    source: Optional[UpstreamSource] = None
    axes: List[AxisConfig] = field(default_factory=list)
    raw_filepath: Optional[str] = None
    installed_version: Optional[str] = None
    installed_version_num: Optional[str] = None
    installed_font_revision: Optional[float] = None
    installed_modified_date: Optional[str] = None
    installed_git_commit_date: Optional[str] = None


@dataclass
class ReleaseAsset:
    name: str
    download_url: str
    size: int = 0
    content_type: str = ""


@dataclass
class UpstreamRelease:
    tag_name: str
    version: str
    commit_hash: Optional[str] = None
    html_url: str = ""
    assets: List[ReleaseAsset] = field(default_factory=list)
    is_prerelease: bool = False
    published_at: str = ""
    body: str = ""


@dataclass
class UpdateCheckResult:
    family_name: str
    has_update: bool
    update_type: UpdateType
    current_version: Optional[str] = None
    upstream_version: Optional[str] = None
    current_commit: Optional[str] = None
    upstream_commit: Optional[str] = None
    repository_url: Optional[str] = None
    release_info: Optional[UpstreamRelease] = None
    comparison_status: VersionComparisonStatus = VersionComparisonStatus.UNKNOWN
    installed_modified_date: Optional[str] = None
    upstream_published_at: Optional[str] = None
    error: Optional[str] = None
