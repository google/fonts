#!/usr/bin/env python3
"""
lang-sample-text

Adds sample text for a given language using the specified UDHR translation.

Usage:

lang-sample-text -l ./languages/en.textproto ./udhr_translations/en.xml

"""

from gflanguages import LoadLanguages, languages_public_pb2
from gftools.util.google_fonts import ReadProto, WriteProto
from gflanguages.udhr import Udhr
from lxml import etree
import os
import re
import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Update UDHR sample text for a given language"
    )
    parser.add_argument(
        "-l",
        "--lang",
        help="Language proto file to update",
        required=True,
    )
    parser.add_argument(
        "-u",
        "--udhr",
        help="Path to UDHR translation (XML)",
        required=True,
    )
    args = parser.parse_args(argv)

    language = ReadProto(languages_public_pb2.LanguageProto(), args.lang)

    udhr_data = etree.parse(args.udhr)
    head = udhr_data.getroot()
    for name, value in head.attrib.items():
        if re.search(r"\{.*\}lang", name):
            bcp47 = value.replace("-", "_")
    udhr = Udhr(
        key=head.get("key"),
        iso639_3=head.get("iso639-3"),
        iso15924=head.get("iso15924"),
        bcp47=bcp47,
        direction=head.get("dir"),
        ohchr=None,
        stage=4,
        loc=None,
        name=head.get("n"),
    )
    udhr.Parse(udhr_data)

    language.sample_text.MergeFrom(udhr.GetSampleTexts())
    WriteProto(language, args.lang)


if __name__ == "__main__":
    main()
