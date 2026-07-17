"""
Upstream repository monitoring and update detection module with path-filtered TTF commit checking.
Located internally within google/fonts at .ci/autoupdater/upstream_monitor.py.
"""

import os
import json
import urllib.request
import urllib.error
import re
from typing import Optional, Tuple, List, Dict, Any
from .models import (
    FamilyMetadata,
    UpstreamSource,
    UpstreamRelease,
    ReleaseAsset,
    UpdateCheckResult,
    UpdateType,
    VersionComparisonStatus,
)
from .version_comparator import compare_local_vs_upstream, clean_version_string, compare_version_numbers


def parse_github_repo(url: str) -> Optional[Tuple[str, str]]:
    """Extract (owner, repo) from GitHub URL."""
    if not url:
        return None
    cleaned = url.strip().rstrip("/")
    if cleaned.endswith(".git"):
        cleaned = cleaned[:-4]

    pattern = r"github\.com/([^/]+)/([^/]+)"
    match = re.search(pattern, cleaned)
    if match:
        return match.group(1), match.group(2)
    return None


def is_font_related_file(filepath: str) -> bool:
    """Check if file path relates to TTF fonts or font sources."""
    path_lower = filepath.lower()
    if path_lower.endswith(".ttf") or path_lower.endswith(".ufo") or path_lower.endswith(".glyphs") or path_lower.endswith(".designspace"):
        return True
    if "fonts/" in path_lower or "sources/" in path_lower or "src/" in path_lower:
        return True
    return False


class UpstreamMonitor:
    def __init__(self, github_token: Optional[str] = None):
        self.token = github_token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        self._etag_cache: Dict[str, Tuple[str, Any]] = {}

    def _make_github_request(self, endpoint: str) -> Tuple[Optional[Dict[str, Any]], int, Optional[str]]:
        """Perform authenticated HTTP request to GitHub REST API with Bearer/token support and ETag caching."""
        url = f"https://api.github.com{endpoint}"
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "GoogleFonts-AutoUpdater/1.0.0")
        req.add_header("Accept", "application/vnd.github.v3+json")

        token = self.token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if token:
            if token.startswith("ghs_") or token.startswith("ghp_") or token.startswith("github_pat_"):
                req.add_header("Authorization", f"Bearer {token}")
            else:
                req.add_header("Authorization", f"token {token}")

        cached_etag = None
        if url in self._etag_cache:
            cached_etag, cached_data = self._etag_cache[url]
            req.add_header("If-None-Match", cached_etag)

        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                status = response.status
                etag = response.headers.get("ETag")
                body = response.read().decode("utf-8")
                data = json.loads(body) if body else {}

                if etag:
                    self._etag_cache[url] = (etag, data)
                return data, status, etag
        except urllib.error.HTTPError as e:
            if e.code == 304 and url in self._etag_cache:
                return self._etag_cache[url][1], 304, cached_etag
            err_msg = e.read().decode("utf-8") if e.fp else str(e)
            return None, e.code, err_msg
        except Exception as e:
            return None, 500, str(e)

    def fetch_latest_release(self, owner: str, repo: str) -> Tuple[Optional[UpstreamRelease], Optional[str]]:
        """Fetch latest GitHub release for owner/repo."""
        endpoint = f"/repos/{owner}/{repo}/releases/latest"
        data, status, err = self._make_github_request(endpoint)

        if status == 404:
            return None, "NO_RELEASES"
        if status in (403, 429):
            return None, f"HTTP_{status}: Rate Limit Exceeded"
        if status != 200 or not data:
            return None, f"HTTP_{status}: {err}"

        tag_name = data.get("tag_name", "")
        version = clean_version_string(tag_name)
        html_url = data.get("html_url", "")
        is_prerelease = data.get("prerelease", False)
        published_at = data.get("published_at", "")
        body = data.get("body", "")

        assets: List[ReleaseAsset] = []
        for a in data.get("assets", []):
            assets.append(
                ReleaseAsset(
                    name=a.get("name", ""),
                    download_url=a.get("browser_download_url", ""),
                    size=a.get("size", 0),
                    content_type=a.get("content_type", ""),
                )
            )

        release = UpstreamRelease(
            tag_name=tag_name,
            version=version,
            html_url=html_url,
            assets=assets,
            is_prerelease=is_prerelease,
            published_at=published_at,
            body=body,
        )
        return release, None

    def fetch_head_commit(self, owner: str, repo: str, branch: Optional[str] = None) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """Fetch latest branch HEAD commit hash, author date, and status with automatic main/master fallback."""
        target_branch = branch or "main"
        endpoint = f"/repos/{owner}/{repo}/commits/{target_branch}"
        data, status, err = self._make_github_request(endpoint)

        # Fallback to 'master' if 'main' fails with 404 or 422
        if (status in (404, 422)) and (not branch or branch == "main"):
            target_branch = "master"
            endpoint = f"/repos/{owner}/{repo}/commits/{target_branch}"
            data, status, err = self._make_github_request(endpoint)

        if status in (403, 429):
            return None, None, f"HTTP_{status}: Rate Limit Exceeded"

        if status != 200 or not data:
            return None, None, f"HTTP_{status}: {err}"

        commit_sha = data.get("sha")
        commit_date = None
        commit_obj = data.get("commit", {})
        if "committer" in commit_obj:
            commit_date = commit_obj["committer"].get("date")
        elif "author" in commit_obj:
            commit_date = commit_obj["author"].get("date")

        return commit_sha, commit_date, None

    def check_for_updates(self, meta: FamilyMetadata) -> UpdateCheckResult:
        """Check if an upstream release or commit update is available for meta."""
        if not meta.source or not meta.source.repository_url:
            return UpdateCheckResult(
                family_name=meta.name,
                has_update=False,
                update_type=UpdateType.NONE,
                error="NO_UPSTREAM_REPOSITORY_URL",
            )

        parsed = parse_github_repo(meta.source.repository_url)
        if not parsed:
            return UpdateCheckResult(
                family_name=meta.name,
                has_update=False,
                update_type=UpdateType.NONE,
                repository_url=meta.source.repository_url,
                error="UNSUPPORTED_REPOSITORY_URL_SCHEMA",
            )

        owner, repo = parsed
        
        # Priority 1: Check GitHub Releases
        release, rel_err = self.fetch_latest_release(owner, repo)
        head_sha, head_date, commit_err = self.fetch_head_commit(owner, repo, branch=meta.source.branch)

        # Flag explicit rate limit errors
        is_rate_limited = (
            (rel_err and ("HTTP_403" in rel_err or "HTTP_429" in rel_err)) or
            (commit_err and ("HTTP_403" in commit_err or "HTTP_429" in commit_err))
        )
        if is_rate_limited:
            return UpdateCheckResult(
                family_name=meta.name,
                has_update=False,
                update_type=UpdateType.NONE,
                current_version=meta.installed_version_num or meta.installed_version,
                repository_url=meta.source.repository_url,
                comparison_status=VersionComparisonStatus.UP_TO_DATE,
                error="RATE_LIMITED (GitHub API Rate Limit Exceeded)",
            )


        cmp_status, cmp_info = compare_local_vs_upstream(
            meta=meta,
            upstream_release=release,
            upstream_commit=head_sha,
            upstream_commit_date=head_date,
        )

        has_update = (cmp_status == VersionComparisonStatus.UPDATE_AVAILABLE)
        up_type = UpdateType.RELEASE if release else (UpdateType.COMMIT if head_sha else UpdateType.NONE)

        return UpdateCheckResult(
            family_name=meta.name,
            has_update=has_update,
            update_type=up_type,
            current_version=meta.installed_version_num or meta.installed_version,
            upstream_version=release.version if release else None,
            current_commit=meta.source.commit,
            upstream_commit=head_sha,
            repository_url=meta.source.repository_url,
            release_info=release,
            comparison_status=cmp_status,
            installed_modified_date=meta.installed_git_commit_date or meta.installed_modified_date,
            upstream_published_at=release.published_at if release else head_date,
            error=rel_err if (rel_err and rel_err != "NO_RELEASES") else commit_err,
        )

