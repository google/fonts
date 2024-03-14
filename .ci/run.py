#!/usr/bin/python3
import subprocess
import re
import os
import argparse
from collections import defaultdict
from enum import Enum
from glob import glob


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--branch", default="origin/main", help="branch to compare current head against"
    )
    parser.add_argument(
        "--render", action="store_true", help="Check rendering of families only"
    )
    parser.add_argument("--pr-number", help="PR to output fontbakery report to")
    parser.add_argument("--pr-url-body", default="https://www.github.com/google/fonts/pull/%s")
    args = parser.parse_args()

    profile_test_file = os.path.join(os.path.dirname(__file__), "test_profiles.py")

    for directory, check_type in directory_check_types(args.branch):
        out = os.path.join("out", os.path.basename(directory))
        fonts = glob(os.path.join(directory, "*.ttf"))

        qa_cmd_prefix = ["gftools", "qa", "-f"] + fonts + ["-o", out]
        if args.pr_number:
            if not args.pr_url_body.endswith("/"):
                args.pr_url_body += "/"
            url = "%s%s" % (args.pr_url_body, args.pr_number)
            qa_cmd_prefix += ["--out-url", url]

        if args.render and check_type == CheckType.NEW_FAMILY:
            print(f"Rendering new family: {directory}")
            subprocess.run(qa_cmd_prefix + ["-gfb", "--render", "--imgs"])

        elif args.render and check_type == CheckType.MODIFIED_FAMILY:
            print(f"Rendering modified family: {directory}")
            subprocess.run(qa_cmd_prefix + ["-gfb", "--render", "--imgs"])
        
        # we only want args.render to do the above two conditions
        elif args.render: 
            continue

        elif check_type == CheckType.NEW_FAMILY:
            print(f"Checking new family: {directory}")
            subprocess.run(qa_cmd_prefix + ["--fontbakery", "--interpolations"], check=True)

        elif check_type == CheckType.MODIFIED_FAMILY:
            print(f"Checking modified family: {directory}")
            subprocess.run(qa_cmd_prefix + ["-gfb", "--fontbakery", "--diffenator", "--interpolations"], check=True)

        elif check_type == CheckType.MODIFIED_FAMILY_METADATA:
            print(f"Checking modified family metadata: {directory}")
            subprocess.run(qa_cmd_prefix + ["--fontbakery", "-o", out], check=True)

        elif check_type == CheckType.DESIGNER:
            print(f"Checking designer profile: {directory}")
            subprocess.run(["pytest", profile_test_file, directory])

        else:
            print(f"Skipping directory {directory}")


if __name__ == "__main__":
    main()
