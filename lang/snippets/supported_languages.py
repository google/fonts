#!/usr/bin/env python3
#
# Copyright 2022 The Google Fonts Tools Authors.
# Copyright 2017,2022 Google LLC All Rights Reserved.
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
# =======================================================================
# =======   This code-snippet uses hyperglot, which is licensed   =======
# =======   under the GNU GPLv3. So, the resulting license for    =======
# =======   any program using this snippet will also have to be   =======
# =======   the GNU GPLv3.                                        =======
# =======================================================================

from gflanguages import LoadLanguages
from hyperglot import parse as hyperglot_parse


def _ParseFontChars(path):
    """
    Open the provided font path and extract the codepoints encoded in the font
    @return list of characters
    """
    from fontTools.ttLib import TTFont
    font = TTFont(path, lazy=True)
    cmap = font["cmap"].getBestCmap()
    font.close()

    # The cmap keys are int codepoints
    return [chr(c) for c in cmap.keys()]


def SupportedLanguages(font_path, languages=None):
    """
    Get languages supported by given font file.

    Languages are pulled from the given set. Based on whether exemplar character
    sets are present in the given font.

    Logic based on Hyperglot:
    https://github.com/rosettatype/hyperglot/blob/3172061ca05a62c0ff330eb802a17d4fad8b1a4d/lib/hyperglot/language.py#L273-L301
    """
    if languages is None:
        languages = LoadLanguages()

    chars = _ParseFontChars(font_path)

    supported = []
    for lang in languages.values():
        if not lang.HasField('exemplar_chars') or \
           not lang.exemplar_chars.HasField('base'):
            continue

        base = hyperglot_parse.parse_chars(lang.exemplar_chars.base,
                                           decompose=False,
                                           retainDecomposed=False)
        if set(base).issubset(chars):
            supported.append(lang)

    return supported


def portable_path(p):
    import os
    return os.path.join(*p.split('/'))


def TEST_FILE(f):
    return portable_path("data/test/" + f)


def test_SupportedLanguages():
    font = TEST_FILE('nunito/Nunito-Regular.ttf')
    supported = SupportedLanguages(font)
    langs = [supported[i].name for i, _ in enumerate(supported)]
    assert len(langs) == 225
    assert 'Lithuanian' in langs
