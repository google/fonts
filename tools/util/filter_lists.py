#! /usr/bin/env python
# -*- coding=utf-8 -*-
#
# for the glyphsLib dependency do: pip install GlyphsLib

from __future__ import print_function, unicode_literals
from glyphsLib import glyphdata, glyphdata_generated
from fontTools.misc.py23 import unichr, byteord
import sys, os, subprocess
import re
import codecs

if __name__ == '__main__':
  # some of the imports here wouldn't work otherwise
  sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import google_fonts as fonts



PURE_UNI_CHR = re.compile('^uni([0-9A-F]{4,5})$', re.IGNORECASE)

# Discussion: https://github.com/schriftgestalt/GlyphsInfo/issues/10#issuecomment-283217683
EXCEPTIONS = {
    'f_f': 0xFB00
  , 'f_f_i': 0xFB03
  , 'f_f_l': 0xFB04
  , 'longs_t': 0xFB05
  , 's_t': 0xFB06
}

NO_CODE_EXCEPTIONS = set(
# This is used to localize for Turkish and some other languages, unfortunately
# it's not in Latin_Plus, where it seems to belong, but without Unicode!
# I'll collect cases like this here and later communicate them in the backlog.
'idotaccent'
)

FILTER_LISTS_DIR_NAME = 'filter lists'

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
        raise Exception('charset directory not fond in "{path}".'.format(path=dirname))

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

_UNICDE2GLYPHNAME = {}
def get_name_by_unicode(search_codepoint, production_name=False):
    if not len(_UNICDE2GLYPHNAME):
        for name in glyphdata_generated.PRODUCTION_NAMES:
            pname = glyphdata_generated.PRODUCTION_NAMES[name]
            codepoint = glyphdata.get_glyph(name).unicode
            if codepoint is not None:
                _UNICDE2GLYPHNAME[byteord(codepoint)] = (name, pname)

        for name in glyphdata_generated.IRREGULAR_UNICODE_STRINGS:
            codepoint = glyphdata.get_glyph(name).unicode
            if codepoint is not None:
                _UNICDE2GLYPHNAME[byteord(codepoint)] = (name, None)

    entry = _UNICDE2GLYPHNAME.get(search_codepoint, (None, None))
    index = 1 if production_name else 0
    return entry[index]

def get_unicode_by_name(name):
    codepoint = glyphdata.get_glyph(name).unicode
    if codepoint is not None:
        return byteord(codepoint)
    match = PURE_UNI_CHR.match(name)
    if match is not None:
        return int(match.groups()[0], base=16)
    if name in EXCEPTIONS:
        return EXCEPTIONS[name]
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
        # I'm not sure if this assertion holds, but with the current data
        # from our name lists it seems to do so.
        # hmm, maybe we'll have to allow a - as well, as it used to mark
        # localized alternates, like {name}-cy for cyrillic.
        assert name not in NO_CODE_EXCEPTIONS or '.' in name, 'A suffix '\
                'beginning with a ".", to indicate this is a character '\
                'used via GSUB, is expected in {name}.'.format(name=name)
        noncodes.append(name)
    return codepoints, noncodes

def production_name_to_friendly_name(name):
    if '_' in name:
        return '_'.join(production_name_to_friendly_name(component)
                                    for component in name.split('_'))
    if '.' in name:
        basename, extension = name.split('.', 1)
        return '.'.join([production_name_to_friendly_name(basename), extension])
    # "brevecomb-cy" did not produce a friendly name
    if '-' in name:
        basename, extension = name.split('-', 1)
        return '-'.join([production_name_to_friendly_name(basename), extension])
    # no '.' no '_' no '-'
    codepoint = get_unicode_by_name(name)
    friendly_name = get_name_by_unicode(codepoint, production_name=False)
    return friendly_name if friendly_name is not None else name


def check_filterlist_in_namelist(filterListFileName, namelistCache=None):
    namelistFilename = get_namelist_for_filterlist(filterListFileName)
    if not namelistFilename:
        return False, 'No Namelist file found for {filterlist}'.format(filterlist=filterListFileName), None

    codepoints, noncodes = read_filterlist(filterListFileName)
    useProductionNames = 'uni names' in filterListFileName or 'uni-names' in filterListFileName
    if useProductionNames:
        prod_noncodes = noncodes;
        noncodes = [production_name_to_friendly_name(name) for name in noncodes]
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
    for noncode in noncodes:
        if noncode not in namelist['noCharcode']:
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

def check_filterlists_in_namelists(files):
    print('*'*30)
    print('Checking filterlists in namelists...')
    print('*'*30)
    namelistCache = {}
    for f in files:
        print('='*30)
        print ('Checking filter list:', f)
        passed, message, namelist = check_filterlist_in_namelist(f, namelistCache)
        print ('Namelist:', namelist)
        if not passed:
            print('Failed')
            print(message)
        else:
            print('Passed')

def check_friendly_names_production_names_equal(files):
    print('*'*30)
    print('Check if nice names and uni names filter lists are in sync.')
    print('*'*30)
    nice_names_dir = 'nice names'
    prod_names_dir = 'uni names'
    nice_names_parts = {tuple(f.split(nice_names_dir, 1)) for f in files
                                                if nice_names_dir in f}
    prod_names_parts = {tuple(f.split(prod_names_dir, 1)) for f in files
                                                if prod_names_dir in f}

    # filter to check only files that have a counterpart
    matches = sorted(list(nice_names_parts & prod_names_parts))
    for pathparts in matches:
        print('='*30)
        prod_names_file = prod_names_dir.join(pathparts)
        nice_names_file = nice_names_dir.join(pathparts)
        print('uni names filter list:', prod_names_file)
        print('nice names filter list:', nice_names_file)

        prod_names = get_filterlist_names(prod_names_file)
        nice_prod_names = [production_name_to_friendly_name(name)
                                                    for name in prod_names]
        nice_names = get_filterlist_names(nice_names_file)

        prod_names_set = set(nice_prod_names)
        nice_names_set = set(nice_names)

        not_in_both = nice_names_set ^ prod_names_set
        if not len(not_in_both):
            print('PASS\n')
            continue

        print('FAIL')
        print('# uni names', len(prod_names), '# duplicates', len(prod_names) - len(prod_names_set))
        print('# nice names', len(nice_names), '# duplicates',len(nice_names) - len(nice_names_set))

        not_in_nice = sorted(not_in_both - nice_names_set)
        not_in_prod = sorted(not_in_both - prod_names_set)

        if len(not_in_prod):
            print ('Entries in nice names but not in uni names(#{1}):\n{0}\n' \
                                .format(', '.join(not_in_prod), len(not_in_prod)))

        if len(not_in_nice):
            nice2prod = dict(zip(nice_prod_names, prod_names))
            items = ','.join('{0} as {1}'.format(nice2prod[n],n)
                                                    for n in not_in_nice)
            print ('Entries in uni names but not in nice names (#{1}):\n{0}\n' \
                                        .format(items, len(not_in_nice)))


def check_files(files):
    check_filterlists_in_namelists(files)
    check_friendly_names_production_names_equal(files)

def main(args):
    if len(args) < 1:
        raise Excepion('The first argument must be the search directory'\
                                                        ' for nam files.')
    searchDirectory = args[0]
    files = subprocess.check_output(['find', searchDirectory, '-type', 'f', '-path', '*/filter lists/*.txt']);
    check_files( filter(len, files.split('\n')) )

if __name__ == '__main__':
    main(sys.argv[1:])

