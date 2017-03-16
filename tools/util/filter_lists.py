#! /usr/bin/env python
# -*- coding=utf-8 -*-
#
# for the glyphsLib dependency do: pip install GlyphsLib

from __future__ import print_function, unicode_literals
from fontTools.misc.py23 import unichr, byteord
import sys, os, subprocess
import re
import codecs
import logging as log
import unittest
from collections import Counter

if __name__ == '__main__':
  # the following imports wouldn't work otherwise
  sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import google_fonts as fonts
from glyphdata import DATA as GlyphData

# There's also the form u1014A for higher unicode codepoints next to uni1234
PURE_UNI_CHR = re.compile('^u(?:ni)?([0-9A-F]{4,6})$', re.IGNORECASE)

FILTER_LISTS_DIR_NAME = 'filter lists'

class MissingCharsetDirectory(Exception):
    pass

def get_namelist_for_filterlist(filterlistFilename):
    dirname, fileName = os.path.split(filterlistFilename)
    # removes the ".txt" that we expect because of the call to find that includes it
    filterlistName = fileName.rsplit('.', 1)[0]

    # Get the parent dir with the charsets:
    # the first above the dir called 'filter lists'.
    namelistDir, markerDir = os.path.split(dirname)
    while(len(markerDir) and markerDir != FILTER_LISTS_DIR_NAME):
        namelistDir, markerDir = os.path.split(namelistDir)
    if markerDir != FILTER_LISTS_DIR_NAME:
        raise MissingCharsetDirectory('charset directory not found in "{path}".'.format(path=dirname))

    # get all the Namelist files from
    for root, dirs, files in os.walk(namelistDir):
        # break to only read the top level dir and to invoke the
        # else clause if this is no dir
        namfiles = [f for f in files if f.endswith('.nam')]
        break
    else:
        namfiles = []
    # longest name first
    namfiles.sort(key=lambda f :-len(f))

    for f in namfiles:

        # removes the 'GF-{language} which is redundant in filter lists
        # due to their location
        namelistBasename = f[:-4].split('-', 2)[-1]
        if filterlistName.startswith(namelistBasename):
            return os.path.join(namelistDir, f)
    return None;

def get_name_by_unicode(search_codepoint, production_name=False):
    """
    Returns None if GlyphsData.xml doesn't contain search_codepoint.
    """
    entry = (None, None)
    glyph = GlyphData.by_unicode.get(search_codepoint, None)
    if glyph is not None:
        entry = (glyph.name, glyph.production_name)
    return entry[1] if production_name else entry[0]

def get_name_by_name(search_name, production_name=False):
    """
    Use this if you don't know what exact type your name is. E.g. when
    the names in your source are mixes friendly names and production names.

    Returns None if GlyphsData.xml doesn't contain search_name.
    """
    entry = (None, None)
    glyph = GlyphData.by_name.get(search_name, None) \
                            or GlyphData.by_prodname.get(search_name, None)
    if glyph is not None:
        entry = (glyph.name, glyph.production_name)
    return entry[1] if production_name else entry[0]

def get_unicode_by_name(name):
    glyph = GlyphData.by_name.get(name, None) \
                                or GlyphData.by_prodname.get(name, None)
    if glyph is not None and glyph.unicode is not None:
        return glyph.unicode
    match = PURE_UNI_CHR.match(name)
    if match is not None:
        return int(match.groups()[0], base=16)
    return None


def get_filterlist_names(filterListFileName):
    with codecs.open(filterListFileName, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

def read_filterlist(filterListFileName):
    names = get_filterlist_names(filterListFileName)
    codepoints = []
    noncodes = []
    for name in names:
        codepoint = get_unicode_by_name(name)
        if codepoint is not None:
            codepoints.append((codepoint, name))
            continue
        noncodes.append(name)
    return codepoints, noncodes

def translate_name(name, production_name=False):
    # The call to get_unicode_by_name at the beginning of this recursive
    # function is more expensive, but it may get fringe cases
    # where names with ".", "-" or "_" have a unicode.

    new_name = get_name_by_name(name,production_name=production_name)
    if new_name is not None:
        return new_name

    codepoint = get_unicode_by_name(name)
    if codepoint is not None:
        new_name = get_name_by_unicode(codepoint, production_name=production_name) \
                                        if codepoint is not None else None
        if new_name is not None:
            return new_name

    if '_' in name:
        return '_'.join(translate_name(component, production_name=production_name)
                                    for component in name.split('_'))
    if '.' in name:
        basename, extension = name.split('.', 1)
        return '.'.join([translate_name(basename, production_name=production_name)
                                                            , extension])
    # "brevecomb-cy" did not produce a friendly name
    if '-' in name:
        basename, extension = name.split('-', 1)
        return '-'.join([translate_name(basename, production_name=production_name)
                                                            , extension])
    return name

def check_filterlist_in_namelist(filterListFileName, namelistCache=None):
    namelistFilename = get_namelist_for_filterlist(filterListFileName)
    if not namelistFilename:
        return False, 'No Namelist file found for {filterlist}'.format(filterlist=filterListFileName), None

    codepoints, noncodes = read_filterlist(filterListFileName)
    useProductionNames = 'uni names' in filterListFileName or 'uni-names' in filterListFileName
    if useProductionNames:
        prod_noncodes = noncodes;
        noncodes = [translate_name(name) for name in noncodes]
        noncodes2prodcodes = dict(zip(noncodes, prod_noncodes))

    namelist = fonts.readNamelist(namelistFilename, cache=namelistCache)

    message = []

    missingChars = []
    for codepoint in codepoints:
        if codepoint[0] not in namelist['charset']:
            missingChars.append(codepoint)
    if len(missingChars):
        names = ', '.join(['0x{0:04X} {1}'.format(c, name)
                                        for c, name in missingChars])
        message.append('Unicode chars not in Namelist but in filter list:' \
                       '\n[{names}]'.format(names=names))

    missingNoncodes = []
    namelistNoCharcode = set(translate_name(name) for name in namelist['noCharcode'])
    for noncode in noncodes:
        if noncode not in namelistNoCharcode:
            missingNoncodes.append(noncode)
    if len(missingNoncodes):
        if useProductionNames:
            missingNoncodes = ['{0} as {1}'.format(noncode, noncodes2prodcodes[noncode])
                                            for noncode in missingNoncodes]
        message.append('None-Unicode not in Namelist but in filter list:' \
                       '\n[{names}]\n'.format(names=', '.join(missingNoncodes)))

    if len(message):
        return False, '\n'.join(message), namelistFilename
    return True, None, namelistFilename


def _build_filterlists_in_namelists(f):
    """
        Checking filterlists in namelists.
    """
    test_name = 'test_filterlists_in_namelists {0}'.format(f)
    def test_filterlists_in_namelists(self):
        passed, message, namelist = check_filterlist_in_namelist(f, self._cache)
        if passed:
            return
        self.assertTrue(passed, msg=message)
    return test_name, test_filterlists_in_namelists

def build_filterlists_in_namelists(files):
    for f in files:
        yield _build_filterlists_in_namelists(f);


def check_filterlist_equals_namelist(filterlist, namelistFilename, namelistCache=None):
    codepoints, noncodes = read_filterlist(filterlist)
    namelist = fonts.readNamelist(namelistFilename, cache=namelistCache)
    message = []
    codepoints_set = set(c for c, _ in codepoints)
    if codepoints_set != namelist['ownCharset']:
        formatCodePoints = '0x{0:04X}'.format
        codepoints_not_in_namelist = codepoints_set - namelist['ownCharset']
        if len(codepoints_not_in_namelist):
            message.append('Unicode in filter list missing in Namelist:\n{0}'\
                        .format(', '.join(formatCodePoints(c) for c
                                    in sorted(codepoints_not_in_namelist))))
        codepoints_not_in_filterlist = namelist['ownCharset'] - codepoints_set
        if len(codepoints_not_in_filterlist):
            message.append('Unicode in Namelist missing in filter list:\n{0}'\
                        .format(', '.join(formatCodePoints(c) for c
                                    in sorted(codepoints_not_in_filterlist))))

    noncodes_set = set(noncodes)
    if noncodes_set != namelist['ownNoCharcode']:
        noncodes_not_in_namelist = noncodes_set - namelist['ownNoCharcode']
        if len(noncodes_not_in_namelist):
            message.append('Unencoded chars in filter list missing in Namelist:\n{0}'\
                        .format(', '.join(sorted(noncodes_not_in_namelist))))
        noncodes_not_in_filterlist = namelist['ownNoCharcode'] - noncodes_set
        if len(noncodes_not_in_filterlist):
            message.append('Unencoded in Namelist missing in filter list:\n{0}'\
                        .format(', '.join(sorted(noncodes_not_in_filterlist))))

    if len(message):
        message.insert(0, 'Namelist and Filter-List are out of sync.'\
                    '\n{0}\n{1}'.format(namelistFilename, filterlist))
        return False, '\n'.join(message), namelistFilename
    return True, None, namelistFilename

def _build_filterlists_equal_namelists(filterlist, namelistFilename):
    """
    Checks if a Namelist e.g. "GF-latin-plus_unique-glyphs.nam" and the
    filter-list with the exact matching name i.e. "filter lists/plus_unique-glyphs.txt"
    contain the same set of glyphs.

    "filter lists/plus_unique-glyphs.txt" should be the same set.
    """
    test_name = 'test_filterlist_equals_namelist {0}'.format(filterlist)
    def test_filterlist_equals_namelist(self):
        passed, message, namelist = check_filterlist_equals_namelist(filterlist, namelistFilename, self._cache)
        if passed:
            return
        self.assertTrue(passed, msg=message)
    return test_name, test_filterlist_equals_namelist


def build_filterlists_equal_namelists(files):
    for filterlist in files:
        if 'uni names' in filterlist or 'uni-names' in filterlist:
            # Only checking nice names. uni-names must be the same set as their
            # nice names pendant, we have a test for that.
            continue
        try:
            namelist = get_namelist_for_filterlist(filterlist)
        except MissingCharsetDirectory:
            # will be reported via the tests using check_filterlist_in_namelist
            continue
        # must be a full match, if there's more at the end of filterlist
        # than at the end of namelist it's likely a specialized subset.
        fl_name = os.path.basename(filterlist).split('.', 1)[0]
        nl_name = namelist.split('.', 1)[0]
        if nl_name.endswith(fl_name):
            yield _build_filterlists_equal_namelists(filterlist, namelist);


def _build_friendly_names_production_names_equal(pathparts, prod_names_file, nice_names_file):
    test_name = 'test_nice_names_uni_names_equal {0}'.format('{marker dir}'.join(pathparts))
    def test_friendly_names_production_names_equal(self):
        message = []
        log_message = lambda *args: message.append(' '.join(args))

        log_message('uni names filter list:', prod_names_file)
        log_message('nice names filter list:', nice_names_file)

        prod_names = get_filterlist_names(prod_names_file)
        nice_prod_names = [translate_name(name)
                                                    for name in prod_names]
        nice_names = get_filterlist_names(nice_names_file)

        prod_names_set = set(nice_prod_names)
        nice_names_set = set(nice_names)

        not_in_both = nice_names_set ^ prod_names_set
        if not len(not_in_both):
            return

        log_message('# uni names', len(prod_names))
        log_message('# nice names', len(nice_names))

        dupes_in_prod_names = len(prod_names) - len(prod_names_set)
        dupes_in_nice_names = len(nice_names) - len(nice_names_set)

        if dupes_in_prod_names:
            log_message('# duplicates in uni names', dupes_in_prod_names, '\n'
                    , *[item for item, count in Counter(prod_names).items() if count > 1])
        if dupes_in_nice_names:
            log_message('# duplicates in nice names', dupes_in_nice_names, '\n'
                    , *[item for item, count in Counter(nice_names).items() if count > 1])


        self.assertTrue(dupes_in_prod_names == 0 and dupes_in_nice_names == 0
                                                ,  msg='\n'.join(message))

        not_in_nice = sorted(not_in_both - nice_names_set)
        not_in_prod = sorted(not_in_both - prod_names_set)

        if len(not_in_prod):
            log_message('Entries in nice names but not in uni names(#{1}):\n{0}\n' \
                                .format(', '.join(not_in_prod), len(not_in_prod)))

        if len(not_in_nice):
            nice2prod = dict(zip(nice_prod_names, prod_names))
            items = ','.join('{0} as {1}'.format(nice2prod[n],n)
                                                    for n in not_in_nice)
            log_message('Entries in uni names but not in nice names (#{1}):\n{0}\n' \
                                    .format(items, len(not_in_nice)))

        self.assertTrue(False, msg='\n'.join(message))
    return test_name, test_friendly_names_production_names_equal


def build_friendly_names_production_names_equal(files):
    """
        Check if nice names and uni names filter lists are in sync.
    """
    nice_names_dir = 'nice names'
    prod_names_dir = 'uni names'
    nice_names_parts = {tuple(f.split(nice_names_dir, 1)) for f in files
                                                if nice_names_dir in f}
    prod_names_parts = {tuple(f.split(prod_names_dir, 1)) for f in files
                                                if prod_names_dir in f}

    # filter to check only files that have a counterpart
    matches = sorted(list(nice_names_parts & prod_names_parts))
    for pathparts in matches:
        prod_names_file = prod_names_dir.join(pathparts)
        nice_names_file = nice_names_dir.join(pathparts)
        yield _build_friendly_names_production_names_equal(pathparts, prod_names_file, nice_names_file)

def initTestProperties(cls, files):
  initialized = []
  for test_generator in (build_filterlists_in_namelists
                       , build_friendly_names_production_names_equal
                       , build_filterlists_equal_namelists):
    for testName, test in test_generator(files):
        setattr(cls, testName, test)

class TestFilterLists(unittest.TestCase):
  def setUp(self):
    self._cache = {}

  def tearDown(self):
    self._cache = None


def main(args):
    if len(args) < 2:
        raise Exception('The first argument must be the search directory'\
                                                        ' for nam files.')
    searchDirectory = args[1]
    files = subprocess.check_output(['find', searchDirectory, '-type', 'f', '-path', '*/filter lists/*.txt']).decode("utf-8")
    files = list(filter(len, files.split('\n')))
    initTestProperties(TestFilterLists, files)
    unittest.main(argv=args[:1] + args[2:], verbosity=2)


if __name__ == '__main__':
    main(sys.argv)
