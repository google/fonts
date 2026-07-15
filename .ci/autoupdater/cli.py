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

    args = parser.parse_args()

    if not args.metadata:
        parser.print_help()
        sys.exit(1)

    pipeline = AutoUpdatePipeline(state_db_path=args.db)
    result = pipeline.process_family(args.metadata)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
