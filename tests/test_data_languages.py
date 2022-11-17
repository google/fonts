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
import pytest
from collections import Counter
from gflanguages import LoadLanguages, languages_public_pb2, LoadScripts


LANGUAGES = LoadLanguages()
SCRIPTS = LoadScripts()


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


SampleText = languages_public_pb2.SampleTextProto().DESCRIPTOR


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
