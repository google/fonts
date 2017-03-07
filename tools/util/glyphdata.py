# coding=UTF-8
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Parts of this file where initially taken from
# https://github.com/googlei18n/glyphsLib/blob/master/MetaTools/generate_glyphdata.py


from __future__ import (print_function, division, absolute_import,
                        unicode_literals)

import os
import xml.etree.ElementTree as etree

from collections import namedtuple


# Data tables which we put into the generated Python file.
# See comments in generate_python_source() below for documentation.
GlyphData = namedtuple('GlyphData', [
    'by_name'
  , 'by_unicode'
  , 'by_prodname'
    ])

GlyphInfo = namedtuple('GlyphInfo', [
    'name'
  , 'production_name'
  , 'unicode'
])

FILE_DIR = os.path.dirname(os.path.realpath(__file__))


def _fetch_all_glyphs():
    glyphs = {}
    for filename in ("GlyphData.xml", "GlyphData_Ideographs.xml"):
        full_filename = os.path.join(FILE_DIR, 'GlyphsInfo', filename)
        for glyph in etree.parse(full_filename).findall("glyph"):
            glyphName = glyph.attrib["name"]
            assert glyphName not in glyphs, "multiple entries for " + glyphName
            glyphs[glyphName] = glyph.attrib
    return glyphs


def _build_data(glyphs):
    by_name = {}
    by_unicode = {}
    by_prodname = {}
    for name, glyph in glyphs.items():
        prodname = glyph.get("production", name)
        unistr = glyph.get("unicode")
        charcode = int(unistr, 16) if unistr else None
        glyphInfo = GlyphInfo(name, prodname, charcode)
        by_name[name] = glyphInfo
        if unistr is not None:
            by_unicode[charcode] = glyphInfo
        by_prodname[prodname] = glyphInfo
    return GlyphData(by_name, by_unicode, by_prodname)

DATA = _build_data(_fetch_all_glyphs())
