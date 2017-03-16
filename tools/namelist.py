#!/usr/bin/env python
# Copyright 2015, Google Inc.
# Author: Dave Crossland (dave@understandinglimited.com)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# namelist.py: A fontTools python script for generating namelist files
#
# Usage:
#   # To make a Namelist from a font file.
#   $ namelist.py Font.ttf > NameList.nam
#
#   # To reformat an existing Namelist.
#   $ ./namelist.py reformat  NameList.nam > NameList.nam
#
#   # To reformat all Namelists in a directory.
#   $ find encodings/GF\ Glyph\ Sets/ -type f -name "*.nam" -exec \
#       bash -c './namelist.py reformat "{}" > "{}__tmp" && mv "{}__tmp" "{}"' \;
#
#   # To generate "uni names" and "nice names" filter lists a Namelist
#   # This will create the needed directories if missing
#   $ ./namelist.py generate-filter-lists NameList.nam
#
#   # To generate "uni names" and "nice names" filter lists for all Namelists
#   $ find encodings/GF\ Glyph\ Sets/ -type f -name "*.nam" -exec \
#       ./namelist.py generate-filter-lists "{}" \;
from __future__ import print_function, unicode_literals
import sys
import os
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
import codecs
from util import google_fonts
from util  import filter_lists

def _get_basechar_unicode(name):
    codepoint = filter_lists.get_unicode_by_name(name)
    if codepoint is not None:
        return codepoint;
    if '_' in name:
        # use the first ligature component as base char
        return _get_basechar_unicode(name.split('_')[0])
    if '.' in name:
        return _get_basechar_unicode(name.split('.')[0])
    return None

def _sortkey_namelist_entries(entry):
    codepoint, name, _, _ = entry
    base_codepoint = None
    extension = None

    if name == 'NULL':
        codepoint = -float('inf')

    if name:

        if '.' in name:
            extension = name.split('.')[1]
        base_codepoint = _get_basechar_unicode(name)

    return tuple([
        codepoint if codepoint is not None else float('inf')
          # keep glyphs of one OT-Feature sticking together
        , extension
        , base_codepoint if base_codepoint is not None else float('inf')
        , name
    ])

def reformat_namelist(filename, out=None):
    if out is None:
        out = sys.stdout
    if filename == '-':
        _reformat_namelist(codecs.getreader('utf8')(sys.stdin), out)
        return
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        _reformat_namelist(f, out)

def _reformat_namelist(f, out=None):
    entries = []
    before = []
    header = []
    for line in f:
        line = line.rstrip()
        if (not entries and not before) and line.startswith('#'):
            header.append(line)
            continue
        entry = None
        if line.startswith('0x'):
            # uni chr
            codepoint = google_fonts.get_codepoint_from_line(line)
            entry = (codepoint, None, line)
        elif line.startswith('      '):
            # unencoded name
            name = filter_lists.translate_name(line.rsplit(' ', 1)[1])
            entry = (None, name, line)

        if entry is not None:
            entry += (before, )
            before = []
            entries.append(entry)
        else:
            # these lines will stick before the next entry
            before.append(line)

    entries.sort(key=_sortkey_namelist_entries)
    _print = lambda *args: print(*args,file=out)
    map(_print, header)
    for codepoint, name, original, item_before in entries:
        map(_print, item_before)
        if codepoint is not None:
            _print(format_codepoint(codepoint))
        elif name is not None:
            _print((' '*9 + name))
    # output left over lines at the end of the file
    map(_print, before)


def _names_generator(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('0x'):
                # uni chr
                codepoint = google_fonts.get_codepoint_from_line(line)
                name = filter_lists.get_name_by_unicode(codepoint)
                if name is None:
                    prefix = 'u' if codepoint > 0xFFFF else 'uni'
                    name = '{0}{1:04X}'.format(prefix, codepoint)
                yield name
            elif line.startswith(' ' * 6):
                # unencoded name
                yield line.rsplit(' ', 1)[1]

def _mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if not os.path.isdir(path):
          raise exc

def generate_filter_lists(filename):
    # 'GF-{script}-rest.nam' => {script}-rest
    basename = os.path.basename(filename).split('.', 1)[0].split('-', 2)[-1]
    filerListFileName = '{0}.txt'.format(basename)
    dirname =  os.path.dirname(filename)
    nice_names_filename = os.path.join(dirname, 'filter lists', 'nice names', filerListFileName)
    prod_names_filename = os.path.join(dirname, 'filter lists', 'uni names', filerListFileName)

    _mkdir(os.path.dirname(nice_names_filename))
    _mkdir(os.path.dirname(prod_names_filename))

    with codecs.open(nice_names_filename, 'w', encoding='utf-8') as niceNamesFile, \
            codecs.open(prod_names_filename, 'w', encoding='utf-8') as prodNamesFile:
        for name in _names_generator(filename):
            print(filter_lists.translate_name(name, production_name=False), file=niceNamesFile)
            print(filter_lists.translate_name(name, production_name=True), file=prodNamesFile)

def _format_codepoint(codepoint):
    if 0xE000 <= codepoint <= 0xF8FF:
        item_description = 'PRIVATE USE AREA U+{0:04X}'.format(codepoint)
        char = ' '
    elif codepoint == 0x000D:
        # Special case, this only happens in Latin-core.
        # FIXME: we should consider remover CR from Latin-core
        item_description = 'CR'
        char = ' '
    else:
        item_description = Unicode[codepoint].decode('utf-8')
        char = unichr(codepoint)
    return ('0x{0:04X}'.format(codepoint)
          , char
          , item_description)

def format_codepoint(codepoint):
    return ' '.join(_format_codepoint(codepoint))

def namelist_from_font(file_name, out=None):
    if out is None:
        out = sys.stdout
    excluded_chars = ["????", "SPACE", "NO-BREAK SPACE"]
    font = TTFont(file_name)
    charcodes = set()
    for cmap in font["cmap"].tables:
        if not cmap.isUnicode():
            continue
        charcodes.update(cp for cp,name in cmap.cmap.items())
    charcodes = sorted(charcodes)
    for charcode in charcodes:
        hexchar, char, item_description = _format_codepoint(charcode)
        if item_description not in excluded_chars:
            print(hexchar, char, item_description, file=out)
    font.close()

def main(*args):
    if args[0] == 'reformat':
        reformat_namelist(args[1])
    if args[0] == 'generate-filter-lists':
        generate_filter_lists(args[1])
    else:
        namelist_from_font(args[0])

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main(*sys.argv[1:])
