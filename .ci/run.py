#!/usr/bin/python3
import subprocess
import os
import argparse
from pathlib import Path
from glob import glob

from whatchanged import directory_check_types, CheckType


RELEVANT_GLOBS = [
    "METADATA.pb",
    "OFL.txt",
    "LICENSE.txt",
    "DESCRIPTION.en_us.html",
    "article/*",
]


def all_relevant_files(fonts):
    files = []
    for font in fonts:
        path = Path(font)
        files.append(str(path))
        for g in RELEVANT_GLOBS:
            for f in path.parent.glob(g):
                if str(f) not in files:
                    files.append(str(f))
    return files


def run_fontspector(fonts, out, pr_number=None):
    report_dir = os.path.join(out, "Fontspector")
    os.makedirs(report_dir, exist_ok=True)
    report = os.path.join(report_dir, "report.md")
    cmd = (
        ["fontspector", "--profile", "googlefonts", "-l", "info",
         "--succinct", "-e", "error"]
        + all_relevant_files(fonts)
        + ["--ghmarkdown", report]
    )
    process = subprocess.run(cmd, check=False)
    if pr_number and os.path.isfile(report):
        with open(report, encoding="utf8") as f:
            msg = f.read()
        if msg.strip():
            subprocess.run(
                ["gh", "pr", "comment", str(pr_number), "--body", msg],
                check=False,
            )
    return process.returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--branch", default="origin/main", help="branch to compare current head against"
    )
    parser.add_argument(
        "--render", action="store_true", help="Check rendering of families only"
    )
    parser.add_argument("--pr-number", help="PR to output fontspector report to")
    parser.add_argument(
        "--pr-url-body", default="https://www.github.com/google/fonts/pull/%s"
    )
    args = parser.parse_args()

    profile_test_file = os.path.join(os.path.dirname(__file__), "test_profiles.py")

    for directory, check_type in directory_check_types(args.branch):
        out = os.path.join("out", os.path.basename(directory))
        fonts = glob(os.path.join(directory, "*.ttf"))
        if not fonts:
            print(f"Skipping {directory} because no fonts were found")
            continue

        qa_cmd_prefix = ["gftools", "qa", "--rust", "-f"] + fonts + ["-o", out]
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

        elif args.render:
            continue

        elif check_type == CheckType.NEW_FAMILY:
            print(f"Checking new family: {directory}")
            run_fontspector(fonts, out, args.pr_number)
            subprocess.run(
                qa_cmd_prefix + ["--interpolations"], check=True
            )

        elif check_type == CheckType.MODIFIED_FAMILY:
            print(f"Checking modified family: {directory}")
            run_fontspector(fonts, out, args.pr_number)
            subprocess.run(
                qa_cmd_prefix
                + ["-gfb", "--diffenator", "--interpolations"],
                check=True,
            )

        elif check_type == CheckType.MODIFIED_FAMILY_METADATA:
            print(f"Checking modified family metadata: {directory}")
            run_fontspector(fonts, out, args.pr_number)

        elif check_type == CheckType.DESIGNER:
            print(f"Checking designer profile: {directory}")
            subprocess.run(["pytest", profile_test_file, directory], check=True)

        else:
            print(f"Skipping directory {directory}")


if __name__ == "__main__":
    main()
