"""
Command Line Interface (CLI) for Google Fonts Auto-Updater.
Located internally within google/fonts at .ci/autoupdater/cli.py.
"""

import sys
import argparse
import json
from pathlib import Path

# Ensure .ci is in sys.path
ci_dir = str(Path(__file__).parent.parent)
if ci_dir not in sys.path:
    sys.path.insert(0, ci_dir)

from autoupdater.orchestrator import AutoUpdatePipeline
from autoupdater.report_generator import generate_family_verification_report, package_out_of_date_reports


def main():
    parser = argparse.ArgumentParser(
        description="Google Fonts Automated Upstream Update System (GFAU)"
    )
    parser.add_argument(
        "--metadata",
        "-m",
        type=str,
        help="Path to family METADATA.pb file to check and process.",
    )
    parser.add_argument(
        "--db",
        default="gf_autoupdater_state.db",
        help="Path to SQLite state database file (default: gf_autoupdater_state.db).",
    )
    parser.add_argument(
        "--create-pr",
        action="store_true",
        default=False,
        help="Create git feature branch and open Pull Request on GitHub (DISABLED by default).",
    )
    parser.add_argument(
        "--base-branch",
        default="main",
        help="Base branch for PR (default: main).",
    )
    parser.add_argument(
        "--report-out",
        default="family_verification_report.md",
        help="Output filepath for generated Markdown verification report (default: family_verification_report.md).",
    )

    args = parser.parse_args()

    if not args.metadata:
        parser.print_help()
        sys.exit(1)

    pipeline = AutoUpdatePipeline(state_db_path=args.db)
    result = pipeline.process_family(args.metadata, create_pr=args.create_pr, base_branch=args.base_branch)

    # Generate verification report
    report_md = generate_family_verification_report(result, output_filepath=args.report_out)
    result["report_markdown_path"] = args.report_out

    if result.get("has_update"):
        zip_path, gen_files = package_out_of_date_reports([result])
        result["zip_archive_path"] = zip_path
        print(f"📦 Packaged out-of-date verification report into '{zip_path}'.")

    # Print summary result JSON
    printable_result = {k: v for k, v in result.items() if k not in ("pr_body", "updated_pb_content", "candidate_ttf_fonts")}
    print(json.dumps(printable_result, indent=2))
    print(f"\n📄 Verification report generated: {args.report_out}")



if __name__ == "__main__":
    main()

