"""
Artifact fetcher and packaging module for acquiring verbatim upstream TTF font binaries.
Located internally within google/fonts at .ci/autoupdater/artifact_fetcher.py.
"""

import os
import zipfile
import hashlib
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple
from .models import UpstreamRelease, FamilyMetadata, ReleaseAsset


def compute_sha256(filepath: str) -> str:
    """Compute SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def is_font_file(filename: str) -> bool:
    """
    Check if file is a font binary (.ttf, .otf, .ttc, .woff, .woff2).
    """
    return Path(filename).suffix.lower() in [".ttf", ".otf", ".ttc", ".woff", ".woff2"]


def compare_ttf_dir_hashes(existing_ttf_dir: Path, candidate_fonts: List[Tuple[Path, str]]) -> bool:
    """
    Compare candidate TTF SHA256 hashes against existing TTF files in Google Fonts family folder.
    Returns True if at least one TTF file has binary differences or is new/changed.
    Returns False if all candidate TTF files are 100% byte-for-byte identical.
    """
    if not candidate_fonts or not existing_ttf_dir.exists():
        return True

    has_differences = False
    for candidate_path, candidate_hash in candidate_fonts:
        existing_path = existing_ttf_dir / candidate_path.name
        if not existing_path.exists():
            return True
        existing_hash = compute_sha256(str(existing_path))
        if existing_hash != candidate_hash:
            has_differences = True
            break

    return has_differences


class ArtifactFetcher:
    def __init__(self, download_dir: Optional[str] = None):
        self.download_dir = Path(download_dir) if download_dir else Path(os.getcwd()) / "download_cache"
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def download_asset(self, asset: ReleaseAsset, target_path: Optional[str] = None) -> Path:
        """Download a release asset to local directory without modifying content."""
        if not target_path:
            dest_file = self.download_dir / asset.name
        else:
            dest_file = Path(target_path)
            dest_file.parent.mkdir(parents=True, exist_ok=True)

        req = urllib.request.Request(
            asset.download_url,
            headers={"User-Agent": "GoogleFonts-AutoUpdater/1.0.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as response, open(dest_file, "wb") as out_f:
            while chunk := response.read(65536):
                out_f.write(chunk)

        return dest_file

    def extract_font_files_from_zip(self, zip_path: Path, output_dir: Path) -> List[Tuple[Path, str]]:
        """
        Extract TTF font binaries from a ZIP archive directly without modifications.
        Returns list of (extracted_file_path, sha256_hash).
        """
        extracted_fonts: List[Tuple[Path, str]] = []
        output_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_path, "r") as archive:
            for member in archive.infolist():
                if member.is_dir():
                    continue
                filename = Path(member.filename).name
                if is_font_file(filename):
                    out_path = output_dir / filename
                    with archive.open(member) as source_f, open(out_path, "wb") as target_f:
                        content = source_f.read()
                        target_f.write(content)

                    file_hash = compute_sha256(str(out_path))
                    extracted_fonts.append((out_path, file_hash))

        return extracted_fonts

    def acquire_upstream_binaries(
        self, release: Optional[UpstreamRelease], family_meta: FamilyMetadata, output_dir: Path, upstream_commit: Optional[str] = None
    ) -> List[Tuple[Path, str]]:
        """
        Acquire candidate update TTF font binaries from release assets or commit archives verbatim.
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        acquired_fonts: List[Tuple[Path, str]] = []

        if release and release.assets:
            zip_assets = [a for a in release.assets if a.name.endswith(".zip")]
            font_assets = [a for a in release.assets if is_font_file(a.name)]

            if zip_assets:
                asset = zip_assets[0]
                downloaded_zip = self.download_asset(asset)
                extracted = self.extract_font_files_from_zip(downloaded_zip, output_dir)
                if extracted:
                    return extracted
            elif font_assets:
                for asset in font_assets:
                    out_file = output_dir / asset.name
                    self.download_asset(asset, target_path=str(out_file))
                    file_hash = compute_sha256(str(out_file))
                    acquired_fonts.append((out_file, file_hash))
                if acquired_fonts:
                    return acquired_fonts

        # Fallback for commit updates or missing release assets: Download repository archive zip
        archive_url = None
        if family_meta.source:
            if family_meta.source.archive_url:
                archive_url = family_meta.source.archive_url
            elif family_meta.source.repository_url and upstream_commit:
                repo_url = family_meta.source.repository_url.rstrip("/")
                if "github.com" in repo_url:
                    archive_url = f"{repo_url}/archive/{upstream_commit}.zip"
                elif "gitlab.com" in repo_url:
                    archive_url = f"{repo_url}/-/archive/{upstream_commit}/archive.zip"

        if archive_url:
            try:
                asset = ReleaseAsset(name="archive.zip", download_url=archive_url)
                downloaded_zip = self.download_asset(asset)
                extracted = self.extract_font_files_from_zip(downloaded_zip, output_dir)
                if extracted:
                    return extracted
            except Exception:
                pass

        return acquired_fonts
