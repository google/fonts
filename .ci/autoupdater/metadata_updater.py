"""
METADATA.pb updater module for serializing updated font family metadata text files.
Located internally within google/fonts at .ci/autoupdater/metadata_updater.py.
"""

from pathlib import Path
from typing import List, Optional
from .models import FamilyMetadata, UpstreamSource, FontFile, AxisConfig


def update_metadata_pb(
    family_meta: FamilyMetadata,
    new_commit: Optional[str] = None,
    new_version: Optional[str] = None,
    new_font_files: Optional[List[str]] = None,
) -> str:
    """
    Generate updated text format METADATA.pb string for a font family.
    """
    lines = []
    lines.append(f'name: "{family_meta.name}"')
    if family_meta.designer:
        lines.append(f'designer: "{family_meta.designer}"')
    lines.append(f'license: "{family_meta.license}"')
    lines.append(f'category: "{family_meta.category}"')
    if family_meta.date_added:
        lines.append(f'date_added: "{family_meta.date_added}"')

    # Fonts
    for font in family_meta.fonts:
        lines.append("fonts {")
        lines.append(f'  name: "{font.name}"')
        lines.append(f'  style: "{font.style}"')
        lines.append(f"  weight: {font.weight}")
        lines.append(f'  filename: "{font.filename}"')
        if font.post_script_name:
            lines.append(f'  post_script_name: "{font.post_script_name}"')
        if font.full_name:
            lines.append(f'  full_name: "{font.full_name}"')
        if font.copyright:
            lines.append(f'  copyright: "{font.copyright}"')
        lines.append("}")

    # Subsets
    for subset in family_meta.subsets:
        lines.append(f'subsets: "{subset}"')

    # Source block
    if family_meta.source or new_commit:
        src = family_meta.source or UpstreamSource()
        commit_val = new_commit or src.commit or ""
        lines.append("source {")
        if src.repository_url:
            lines.append(f'  repository_url: "{src.repository_url}"')
        if commit_val:
            lines.append(f'  commit: "{commit_val}"')
        if src.archive_url:
            lines.append(f'  archive_url: "{src.archive_url}"')
        if src.branch:
            lines.append(f'  branch: "{src.branch}"')

        for file_map in src.files:
            lines.append("  files {")
            lines.append(f'    source_file: "{file_map.source_file}"')
            lines.append(f'    dest_file: "{file_map.dest_file}"')
            lines.append("  }")
        lines.append("}")

    # Axes
    for axis in family_meta.axes:
        lines.append("axes {")
        lines.append(f'  tag: "{axis.tag}"')
        lines.append(f"  min_value: {axis.min_value}")
        lines.append(f"  max_value: {axis.max_value}")
        lines.append("}")

    return "\n".join(lines) + "\n"
