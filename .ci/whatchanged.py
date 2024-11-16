import subprocess
import re
import os
from collections import defaultdict
from enum import Enum


class CheckType(Enum):
    NEW_FAMILY = 1
    MODIFIED_FAMILY = 2
    MODIFIED_FAMILY_METADATA = 3
    DESIGNER = 4


class CheckToken(Enum):
    NEW_FONT = 1
    DESIGNER = 2
    FONT_FAMILY = 3
    MODIFIED_FONTS = 4
    MODIFIED_METADATA = 5


def _parse_git_diff(diff_info: str) -> list[tuple[str, str]]:
    """
    '''
    A    ofl/mavenpro/MavenPro[wght].ttf
    M    ofl/mavenpro/METADATA.pb
    ''' -> [
        ("A", "ofl/mavenpro/MavenPro[wght].ttf"),
        ("M", "ofl/mavenpro/METADATA.pb")
    ]

    """
    parsed = re.findall(r"([A|M|D])(\t)(.*)", diff_info)
    return [(s, p) for s, _, p in parsed]


def directory_check_types(branch="origin/main"):
    git_diff_text = subprocess.run(
        ["git", "diff", branch, "--name-status"], capture_output=True
    ).stdout.decode("utf-8")
    git_diff = _parse_git_diff(git_diff_text)

    # Tokenize each directory git diff has reported
    directories_to_check = defaultdict(set)
    for state, path in git_diff:
        dirpath = (
            os.path.dirname(path)
            if path not in ("to_sandbox.txt", "to_production.txt")
            else path
        )
        # skip article directories. These should be checked on github
        if os.path.basename(dirpath) == "article":
            continue

        dir_tokens = directories_to_check[dirpath]
        if path.startswith("catalog"):
            dir_tokens.add(CheckToken.DESIGNER)

        if path.startswith(("ofl", "ufl", "apache")):
            dir_tokens.add(CheckToken.FONT_FAMILY)

        if path.endswith((".ttf", ".otf")) and state == "A":
            dir_tokens.add(CheckToken.NEW_FONT)

        if path.endswith((".ttf", ".otf")) and (state == "M" or state == "D"):
            dir_tokens.add(CheckToken.MODIFIED_FONTS)

        if path.endswith((".txt", ".pb", ".html")) and state == "M":
            dir_tokens.add(CheckToken.MODIFIED_METADATA)

    # Set each directory's check type
    results = []
    for path, tokens in directories_to_check.items():
        if CheckToken.FONT_FAMILY in tokens:
            if CheckToken.MODIFIED_FONTS in tokens:
                results.append((path, CheckType.MODIFIED_FAMILY))
            elif CheckToken.MODIFIED_METADATA in tokens:
                results.append((path, CheckType.MODIFIED_FAMILY_METADATA))
            else:
                results.append((path, CheckType.NEW_FAMILY))
        if CheckToken.DESIGNER in tokens:
            results.append((path, CheckType.DESIGNER))
    return results
