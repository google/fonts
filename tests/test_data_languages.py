#!/usr/bin/env python3
#
# Copyright 2022 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import defaultdict, Counter
import re
import unicodedata

from gflanguages import LoadLanguages, languages_public_pb2, LoadScripts, LoadRegions
import pytest
import youseedee


LANGUAGES = LoadLanguages()
SCRIPTS = LoadScripts()
REGIONS = LoadRegions()

CLDR_SCRIPT_TO_UCD_SCRIPT = {
    "Bangla": "Bengali",
    "Traditional Han": "Han",
    "Simplified Han": "Han",
    "Korean": "Hangul",
    "Odia": "Oriya",
    "Ol Chiki": "Ol_Chiki",
}

SKIP_EXEMPLARS = {
    "ja_Jpan": "Contains multiple scripts",
    "aii_Cyrl": "Does indeed use Latin glyphs while writing Cyrillic",
    "sel_Cyrl": "Does indeed use Latin glyphs while writing Cyrillic",
    "coo_Latn": "Does indeed use Greek glyphs while writing Latin",
    "hur_Latn": "Does indeed use Greek glyphs while writing Latin",
    "kwk_Latn": "Does indeed use Greek glyphs while writing Latin",
    "thp_Latn": "Does indeed use Greek glyphs while writing Latin",
    "dnj_Latn": "Does use future Unicode 16 Latin glyphs",
}

SKIP_REGION = {
    "cpf_Latn": "French-based creole languages is a group of languages.",
    "gem_Latn": "Germanic languages is a group of languages.",
    "sla_Latn": "Slavic languages is a group of languages.",
    "hmn_Latn": "Homnic languages is a group of languages.",
    "ie_Latn": "Interlingue is an artifical language.",
    "io_Latn": "Ido is an artifical language.",
    "jbo_Latn": "Lobjan is an artifical language.",
    "tlh_Latn": "Klingon is an artifical language.",
}


@pytest.mark.parametrize("lang_code", LANGUAGES)
@pytest.mark.parametrize(
    "exemplar_name", ["base", "auxiliary", "marks", "numerals", "punctuation", "index"]
)
def test_languages_exemplars_canonical_duplicates(lang_code, exemplar_name):
    lang = LANGUAGES[lang_code]
    exemplar = getattr(lang.exemplar_chars, exemplar_name).split()
    normalized = defaultdict(set)

    for g in exemplar:
        if g[0] == "{" and g[-1] == "}":
            g = g.lstrip("{").rstrip("}")
        normalized[unicodedata.normalize("NFC", g)].add(g)

    result = [(len(gs), n) for n, gs in normalized.items()]
    expected = [(1, n) for n, _ in normalized.items()]
    assert result == expected


@pytest.mark.parametrize("lang_code", LANGUAGES)
@pytest.mark.parametrize(
    "exemplar_name", ["base", "auxiliary", "marks", "numerals", "punctuation", "index"]
)
def test_languages_exemplars_duplicates(lang_code, exemplar_name):
    lang = LANGUAGES[lang_code]
    exemplar = getattr(lang.exemplar_chars, exemplar_name).split()
    counter = Counter(exemplar)
    counts = sorted(counter.most_common(), key=lambda pair: exemplar.index(pair[0]))
    assert counts == [(v, 1) for v in exemplar]


@pytest.mark.parametrize("lang_code", LANGUAGES.keys())
@pytest.mark.parametrize(
    "exemplar_name", ["base", "auxiliary", "numerals", "punctuation", "index"]
)
def test_exemplars_bracketed_sequences(lang_code, exemplar_name):
    lang = LANGUAGES[lang_code]
    if lang.script != "Latn":
        return
    exemplar = getattr(lang.exemplar_chars, exemplar_name).split()
    for chars in exemplar:
        if len(chars) > 1:
            assert chars.startswith("{") and chars.endswith("}")
            assert len(chars[1:-1]) > 1


SampleText = languages_public_pb2.SampleTextProto().DESCRIPTOR
ExemplarChars = languages_public_pb2.ExemplarCharsProto().DESCRIPTOR


@pytest.mark.parametrize("lang_code", LANGUAGES.keys())
def test_language_samples(lang_code):
    # Although marked as optional in the protobuf file, all
    # SampleText fields (except note) are required, so make
    # sure they are present.
    lang = LANGUAGES[lang_code]
    if not lang.sample_text.ListFields():
        pytest.skip("No sample text for language " + lang_code)
        return

    for field in SampleText.fields:
        if field.name == "note":
            continue
        assert getattr(lang.sample_text, field.name)


@pytest.mark.parametrize("lang_code", LANGUAGES.keys())
def test_script_is_known(lang_code):
    lang = LANGUAGES[lang_code]
    script = lang.script
    assert script in SCRIPTS, f"{lang_code} used unknown script {lang.script}"


@pytest.mark.parametrize("lang_code", LANGUAGES)
def test_region_is_known(lang_code):
    lang = LANGUAGES[lang_code]
    if lang.id in SKIP_REGION:
        pytest.skip(SKIP_REGION[lang.id])
        return
    regions = lang.region
    for region in regions:
        assert region in REGIONS.keys()


@pytest.mark.parametrize("lang_code", LANGUAGES.keys())
def test_exemplars_are_in_script(lang_code):
    lang = LANGUAGES[lang_code]
    script_name = SCRIPTS[lang.script].name
    script_name = CLDR_SCRIPT_TO_UCD_SCRIPT.get(script_name, script_name)
    if not lang.exemplar_chars.ListFields():
        pytest.skip("No exemplars for language " + lang_code)
        return
    if lang.id in SKIP_EXEMPLARS:
        pytest.skip(SKIP_EXEMPLARS[lang.id])
        return
    out_of_script = {}
    for field in ExemplarChars.fields:
        if field.name == "auxiliary" or field.name == "index":
            continue
        exemplars = getattr(lang.exemplar_chars, field.name)
        group_of_chars = re.findall(r"(\{[^}]+\}|\S+)", exemplars)
        for chars in group_of_chars:
            for char in chars:
                char_script = youseedee.ucd_data(ord(char)).get("Script")
                if char_script == "Common" or char_script == "Inherited":
                    continue
                if char_script != script_name:
                    out_of_script[chars] = char_script
                    break
    assert not out_of_script, (
        f"{lang_code} exemplars contained out-of-script characters"
        f": {', '.join(out_of_script.keys())}"
        f" from scripts {', '.join(set(out_of_script.values()))}"
    )
