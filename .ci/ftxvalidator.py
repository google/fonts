import argparse
import glob
import os
import plistlib
import sys
import subprocess
from collections import defaultdict

from whatchanged import directory_check_types, CheckType

severity_mapping = {
    "kATSFontTestSeverityMinorError": "WARN",
    "kATSFontTestSeverityFatalError": "FAIL",
    "kATSFontTestSeverityInformation": "INFO",
}

default_levels = ["WARN", "FAIL"]


def combine_severity(s1, s2):
    if s1 == "FAIL" or s2 == "FAIL":
        return "FAIL"
    if s1 == "WARN" or s2 == "WARN":
        return "WARN"
    return None


def parse_ftxvalidator_report(contents):
    tree = plistlib.loads(contents)
    worst_severity = None
    for fonts in tree["kATSFontTestFontsTestedKey"]:
        font = fonts["kATSFontTestFontPostScriptNameKey"]
        results = fonts["kATSFontTestArrayKey"]
        for result in results:
            if not result["kATSFontTestResultKey"]:
                continue
            messages = result["kATSFontTestMessagesKey"]
            this_messages = defaultdict(list)
            for message in messages:
                messagetext = message["kATSFontTestMessageTextKey"]
                severity = severity_mapping.get(message["kATSFontTestResultKey"])
                if severity not in default_levels:
                    continue
                this_messages[severity].append(messagetext)
            if not this_messages:
                continue
            print(result["kATSFontTestIdentifierKey"])
            for severity, messages in this_messages.items():
                for message in messages:
                    print(f"  {severity}: {message}")
                    worst_severity = combine_severity(worst_severity, severity)
            print()
    return worst_severity


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--branch", default="origin/main", help="branch to compare current head against"
    )
    args = parser.parse_args()

    worst_severity = None
    for directory, check_type in directory_check_types(args.branch):
        if check_type not in [CheckType.NEW_FAMILY, CheckType.MODIFIED_FAMILY]:
            continue
        fonts = glob.glob(os.path.join(directory, "*.ttf"))
        for font in fonts:
            print(f"Validating {font}")
            result = subprocess.run(
                ["/Library/Apple/usr/bin/ftxvalidator", "-r", font],
                capture_output=True,
                text=False,
                check=True,
            )
            worst_severity = combine_severity(
                worst_severity, parse_ftxvalidator_report(result.stdout)
            )
    if worst_severity == "FAIL":
        sys.exit(1)


if __name__ == "__main__":
    main()
