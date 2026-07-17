"""
Protobuf text format parser for Google Fonts METADATA.pb files, with local TTF version and date extraction.
Located internally within google/fonts at .ci/autoupdater/metadata_parser.py.
"""

import re
import glob
from pathlib import Path
from typing import Dict, Any, List, Union, Optional, Tuple
from .models import (
    FamilyMetadata,
    UpstreamSource,
    SourceFileMapping,
    FontFile,
    AxisConfig,
)
from .version_comparator import (
    extract_local_font_version,
    extract_local_git_commit_date,
    extract_local_file_mtime,
)


def _tokenize(text: str) -> List[str]:
    """Tokenize protobuf text format string."""
    tokens = []
    lines = []
    for line in text.splitlines():
        comment_idx = line.find('#')
        if comment_idx != -1:
            line = line[:comment_idx]
        lines.append(line)
    clean_text = "\n".join(lines)

    token_pattern = re.compile(r'(?:"(?:\\.|[^"\\])*"|\{|\}|:|[^\s\{\}:]+)')
    for match in token_pattern.finditer(clean_text):
        tokens.append(match.group(0))
    return tokens


def _parse_tokens(tokens: List[str], index: int = 0) -> tuple[Dict[str, Any], int]:
    """Recursively parse tokens into nested dictionary."""
    result: Dict[str, Any] = {}
    i = index
    n = len(tokens)

    while i < n:
        tok = tokens[i]
        if tok == "}":
            return result, i + 1

        key = tok
        i += 1
        if i >= n:
            break

        if tokens[i] == ":":
            i += 1
            if i < n and tokens[i] == "{":
                i += 1
                child_dict, i = _parse_tokens(tokens, i)
                _append_value(result, key, child_dict)
            elif i < n:
                val = _parse_scalar(tokens[i])
                _append_value(result, key, val)
                i += 1
        elif tokens[i] == "{":
            i += 1
            child_dict, i = _parse_tokens(tokens, i)
            _append_value(result, key, child_dict)

    return result, i


def _parse_scalar(tok: str) -> Union[str, int, float, bool]:
    """Parse scalar token string into typed Python object."""
    if tok.startswith('"') and tok.endswith('"'):
        s = tok[1:-1]
        s = s.replace(r'\"', '"').replace(r'\n', '\n').replace(r'\\', '\\')
        return s
    if tok.lower() == "true":
        return True
    if tok.lower() == "false":
        return False
    try:
        if "." in tok:
            return float(tok)
        return int(tok)
    except ValueError:
        return tok


def _append_value(d: Dict[str, Any], key: str, val: Any) -> None:
    """Helper to handle repeated fields in protobuf dict."""
    if key in d:
        if isinstance(d[key], list):
            d[key].append(val)
        else:
            d[key] = [d[key], val]
    else:
        d[key] = val


def parse_metadata_pb(content: str, filepath: str = None) -> FamilyMetadata:
    """Parse text format METADATA.pb content into FamilyMetadata object."""
    tokens = _tokenize(content)
    raw_dict, _ = _parse_tokens(tokens)

    name = str(raw_dict.get("name", ""))
    designer = str(raw_dict.get("designer", ""))
    license_type = str(raw_dict.get("license", "OFL"))
    category = str(raw_dict.get("category", "SANS_SERIF"))
    date_added = str(raw_dict.get("date_added", ""))

    subsets_raw = raw_dict.get("subsets", [])
    if isinstance(subsets_raw, str):
        subsets = [subsets_raw]
    elif isinstance(subsets_raw, list):
        subsets = [str(s) for s in subsets_raw]
    else:
        subsets = []

    fonts: List[FontFile] = []
    fonts_raw = raw_dict.get("fonts", [])
    if isinstance(fonts_raw, dict):
        fonts_raw = [fonts_raw]
    for f in fonts_raw:
        if isinstance(f, dict):
            fonts.append(
                FontFile(
                    name=str(f.get("name", "")),
                    style=str(f.get("style", "normal")),
                    weight=int(f.get("weight", 400)),
                    filename=str(f.get("filename", "")),
                    post_script_name=str(f.get("post_script_name", "")),
                    full_name=str(f.get("full_name", "")),
                    copyright=str(f.get("copyright", "")),
                )
            )

    source_obj = None
    source_raw = raw_dict.get("source")
    if isinstance(source_raw, dict):
        file_mappings: List[SourceFileMapping] = []
        files_raw = source_raw.get("files", [])
        if isinstance(files_raw, dict):
            files_raw = [files_raw]
        for fm in files_raw:
            if isinstance(fm, dict):
                file_mappings.append(
                    SourceFileMapping(
                        source_file=str(fm.get("source_file", "")),
                        dest_file=str(fm.get("dest_file", "")),
                    )
                )

        source_obj = UpstreamSource(
            repository_url=source_raw.get("repository_url"),
            archive_url=source_raw.get("archive_url"),
            branch=source_raw.get("branch", "main"),
            commit=source_raw.get("commit"),
            files=file_mappings,
        )

    axes: List[AxisConfig] = []
    axes_raw = raw_dict.get("axes", [])
    if isinstance(axes_raw, dict):
        axes_raw = [axes_raw]
    for ax in axes_raw:
        if isinstance(ax, dict):
            axes.append(
                AxisConfig(
                    tag=str(ax.get("tag", "")),
                    min_value=float(ax.get("min_value", 0.0)),
                    max_value=float(ax.get("max_value", 0.0)),
                )
            )

    meta = FamilyMetadata(
        name=name,
        designer=designer,
        license=license_type,
        category=category,
        date_added=date_added,
        subsets=subsets,
        fonts=fonts,
        source=source_obj,
        axes=axes,
        raw_filepath=filepath,
    )

    if filepath:
        family_dir = Path(filepath).parent
        ver_str, ver_num, rev = extract_local_font_version(family_dir)
        meta.installed_version = ver_str
        meta.installed_version_num = ver_num
        meta.installed_font_revision = rev
        meta.installed_git_commit_date = extract_local_git_commit_date(family_dir)
        meta.installed_modified_date = extract_local_file_mtime(family_dir)

        # Inventory catalog font files (lightweight file listing without binary hashing)
        from .models import CatalogFontFileInfo

        catalog_files = []
        font_map = {f.filename: f for f in fonts if f.filename}
        for ttf_path in sorted(list(family_dir.glob("*.ttf"))):
            fname = ttf_path.name
            fobj = font_map.get(fname)
            catalog_files.append(
                CatalogFontFileInfo(
                    filename=fname,
                    filepath=str(ttf_path.absolute()),
                    post_script_name=fobj.post_script_name if fobj else None,
                    style=fobj.style if fobj else "normal",
                    weight=fobj.weight if fobj else 400,
                )
            )
        meta.catalog_font_files = catalog_files


    return meta



def load_metadata_pb(filepath: str) -> FamilyMetadata:
    """Load and parse METADATA.pb from a local file path."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"METADATA.pb not found at: {filepath}")
    content = path.read_text(encoding="utf-8")
    return parse_metadata_pb(content, filepath=str(path.absolute()))
