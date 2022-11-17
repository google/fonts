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
from gflanguages import LoadLanguages


LANGUAGES = LoadLanguages()


@pytest.mark.parametrize("lang_code", LANGUAGES)
@pytest.mark.parametrize(
    "exemplar_name",
    ["base", "auxiliary", "marks", "numerals", "punctuation", "index"]
)
def test_languages_exemplars_duplicates(lang_code, exemplar_name):
    lang = LANGUAGES[lang_code]
    exemplar = getattr(lang.exemplar_chars, exemplar_name).split()
    counter = Counter(exemplar)
    counts = sorted(counter.most_common(), key=lambda pair:
                    exemplar.index(pair[0]))
    assert (counts == [(v, 1) for v in exemplar])
