#!/usr/bin/python3
import subprocess
import os
import argparse
from glob import glob

from whatchanged import directory_check_types, CheckType


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

        # we only want args.render to do the above two conditions
        elif args.render:
            continue

        elif check_type == CheckType.NEW_FAMILY:
            print(f"Checking new family: {directory}")
            subprocess.run(
                qa_cmd_prefix + ["--fontbakery", "--interpolations"], check=True
            )

        elif check_type == CheckType.MODIFIED_FAMILY:
            print(f"Checking modified family: {directory}")
            subprocess.run(
                qa_cmd_prefix
                + ["-gfb", "--fontbakery", "--diffenator", "--interpolations"],
                check=True,
            )

        elif check_type == CheckType.MODIFIED_FAMILY_METADATA:
            print(f"Checking modified family metadata: {directory}")
            subprocess.run(qa_cmd_prefix + ["--fontbakery", "-o", out], check=True)

        elif check_type == CheckType.DESIGNER:
            print(f"Checking designer profile: {directory}")
            subprocess.run(["pytest", profile_test_file, directory], check=True)

        else:
            print(f"Skipping directory {directory}")


if __name__ == "__main__":
    main()
