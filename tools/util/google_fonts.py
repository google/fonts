"""Helper APIs for interaction with Google Fonts.

Provides APIs to interact with font subsets, codepoints for font or subset.

To run the tests:
$ cd fonts/tools
fonts/tools$ python util/google_fonts.py
# or do:
$ python path/to/fonts/tools/utilgoogle_fonts.py --nam_dir path/to/fonts/tools/encodings/

"""
from __future__ import print_function, unicode_literals

import collections
import contextlib
import errno
import os
import re
import sys
import codecs
from warnings import warn
import unittest

if __name__ == '__main__':
  # some of the imports here wouldn't work otherwise
  sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fontTools import ttLib

import fonts_public_pb2 as fonts_pb2
from google.protobuf import text_format
import gflags as flags
from util import py_subsets

FLAGS = flags.FLAGS
flags.DEFINE_string('nam_dir', 'encodings/', 'nam file dir')

# See https://www.microsoft.com/typography/otspec/name.htm.
NAME_COPYRIGHT = 0
NAME_FAMILY = 1
NAME_UNIQUEID = 3
NAME_FULLNAME = 4
NAME_PSNAME = 6


_PLATFORM_ID_MICROSOFT = 3
_PLATFORM_ENC_UNICODE_BMP = 1
_PLATFORM_ENC_UNICODE_UCS4 = 10
_PLATFORM_ENCS_UNICODE = (_PLATFORM_ENC_UNICODE_BMP, _PLATFORM_ENC_UNICODE_UCS4)

_FAMILY_WEIGHT_REGEX = r'([^/-]+)-(\w+)\.ttf$'

# Matches 4 or 5 hexadecimal digits that are uppercase at the beginning of the
# test string. The match is stored in group 0, e.g:
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234X').groups()[0]
# '1234'
# >>> _NAMELIST_CODEPOINT_REGEX.match('1234A').groups()[0]
# '1234A'
_NAMELIST_CODEPOINT_REGEX = re.compile('^([A-F0-9]{4,5})')

# The canonical [to Google Fonts] name comes before any aliases
_KNOWN_WEIGHTS = collections.OrderedDict([
    ('Thin', 100),
    ('Hairline', 100),
    ('ExtraLight', 200),
    ('Light', 300),
    ('Regular', 400),
    ('', 400),  # Family-Italic resolves to this
    ('Medium', 500),
    ('SemiBold', 600),
    ('Bold', 700),
    ('ExtraBold', 800),
    ('Black', 900)
])


_VALID_STYLES = {'normal', 'italic'}


# (Mask, Name) pairs.
# See https://www.microsoft.com/typography/otspec/os2.htm#fss.
_FS_SELECTION_BITS = [
    (1 << 0, 'ITALIC'),
    (1 << 1, 'UNDERSCORE'),
    (1 << 2, 'NEGATIVE'),
    (1 << 3, 'OUTLINED'),
    (1 << 4, 'STRIKEOUT'),
    (1 << 5, 'BOLD'),
    (1 << 6, 'REGULAR'),
    (1 << 7, 'USE_TYPO_METRICS'),
    (1 << 8, 'WWS'),
    (1 << 9, 'OBLIQUE')
]


# license_dir => license name mappings
_KNOWN_LICENSE_DIRS = {
    'apache': 'APACHE2',
    'ofl': 'OFL',
    'ufl': 'UFL',
}


FileFamilyStyleWeightTuple = collections.namedtuple(
    'FileFamilyStyleWeightTuple', ['file', 'family', 'style', 'weight'])


class Error(Exception):
  """Base for Google Fonts errors."""


class ParseError(Error):
  """Exception used when parse failed."""




def UnicodeCmapTables(font):
  """Find unicode cmap tables in font.

  Args:
    font: A TTFont.
  Yields:
    cmap tables that contain unicode mappings
  """
  for table in font['cmap'].tables:
    if (table.platformID == _PLATFORM_ID_MICROSOFT
        and table.platEncID in _PLATFORM_ENCS_UNICODE):
      yield table



_displayed_errors = set()
def ShowOnce(msg):
  global _displayed_errors
  if msg in _displayed_errors:
    return
  _displayed_errors.add(msg)
  print(msg, file=sys.stderr)


def UniqueSort(*args):
  """Returns a sorted list of the unique items from provided iterable(s).

  Args:
    *args: Iterables whose items will be merged, sorted and de-duplicated.
  Returns:
    A list.
  """
  s = set()
  for arg in args:
    s.update(arg)
  return sorted(s)


def RegularWeight(metadata):
  """Finds the filename of the regular (normal/400) font file.

  Args:
    metadata: The metadata to search for the regular file data.
  Returns:
    The name of the regular file, usually Family-Regular.ttf.
  Raises:
    OSError: If regular file could not be found. errno.ENOENT.
  """
  for f in metadata.fonts:
    if f.weight == 400 and f.style == 'normal':
      return os.path.splitext(f.filename)[0] + '.ttf'

  name = '??'
  if metadata.HasField('name'):
    name = metadata.name
  raise OSError(errno.ENOENT, 'unable to find regular weight in %s' % name)


def ListSubsets():
  """Returns a list of all subset names, in lowercase."""
  return py_subsets.SUBSETS


def Metadata(file_or_dir):
  """Returns fonts_metadata.proto object for a metadata file.

  If file_or_dir is a file named METADATA.pb, load it. If file_or_dir is a
  directory, load the METADATA.pb file in that directory.

  Args:
    file_or_dir: A file or directory.
  Returns:
    Python object loaded from METADATA.pb content.
  Raises:
    ValueError: if file_or_dir isn't a METADATA.pb file or dir containing one.
  """
  if (os.path.isfile(file_or_dir) and
      os.path.basename(file_or_dir) == 'METADATA.pb'):
    metadata_file = file_or_dir
  elif os.path.isdir(file_or_dir):
    metadata_file = os.path.join(file_or_dir, 'METADATA.pb')
  else:
    raise ValueError('%s is neither METADATA.pb file or a directory' %
                     file_or_dir)

  msg = fonts_pb2.FamilyProto()
  with codecs.open(metadata_file, encoding='utf-8') as f:
    text_format.Merge(f.read(), msg)

  return msg


def CodepointsInSubset(subset, unique_glyphs=False):
  """Returns the set of codepoints contained in a given subset.

  Args:
    subset: The lowercase name of a subset, e.g. latin.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
  Returns:
    A set containing the glyphs in the subset.
  """
  if unique_glyphs:
    filenames = [CodepointFileForSubset(subset)]
  else:
    filenames = CodepointFiles(subset)

  filenames = [f for f in filenames if f is not None]

  if not filenames:
    return None

  cps = set()
  for filename in filenames:
    with codecs.open(filename, encoding='utf-8') as f:
      for line in f:
        if not line.startswith('#'):
          match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7])
          if match is not None:
            cps.add(int(match.groups()[0], 16))

  return cps

def CodepointsInFont(font_filename):
  """Returns the set of codepoints present in the font file specified.

  Args:
    font_filename: The name of a font file.
  Returns:
    A set of integers, each representing a codepoint present in font.
  """

  font_cps = set()
  with contextlib.closing(ttLib.TTFont(font_filename)) as font:
    for t in UnicodeCmapTables(font):
      font_cps.update(t.cmap.keys())

  return font_cps


def CodepointFileForSubset(subset):
  """Returns the full path to the file of codepoints unique to subset.

  This API does NOT return additional codepoint files that are normally merged
  into the subset. For that, use CodepointFiles.

  Args:
    subset: The subset we want the codepoint file for.
  Returns:
    Full path to the file containing the codepoint file for subset or None if it
    could not be located.
  Raises:
    OSError: If the --nam_dir doesn't exist. errno.ENOTDIR.
  """
  # expanduser so we can do things like --nam_dir=~/oss/googlefontdirectory/
  enc_path = os.path.expanduser(FLAGS.nam_dir)
  if not os.path.exists(enc_path):
    raise OSError(errno.ENOTDIR, 'No such directory', enc_path)

  filename = os.path.join(enc_path, '%s_unique-glyphs.nam' % subset)
  if not os.path.isfile(filename):
    ShowOnce('no cp file for %s found at %s'
             % (subset, filename[len(enc_path):]))
    return None

  return filename


def CodepointFiles(subset):
  """Returns the codepoint files that contain the codepoints in a merged subset.

  If a subset X includes codepoints from multiple files, this function
  returns all those files while CodepointFileForSubset returns the single
  file that lists the codepoints unique to the subset. For example, greek-ext
  contains greek-ext, greek, and latin codepoints. This function would return
  all three files whereas CodepointFileForSubset would return just greek-ext.

  Args:
    subset: The subset we want the codepoint files for.
  Returns:
    A list of 1 or more codepoint files that make up this subset.
  """
  files = [subset]

  # y-ext includes y
  # Except latin-ext which already has latin.
  if subset != 'latin-ext' and subset.endswith('-ext'):
    files.append(subset[:-4])

  # almost all subsets include latin.
  if subset not in ('khmer', 'latin'):
    files.append('latin')

  return map(CodepointFileForSubset, files)


def SubsetsInFont(file_path, min_pct, ext_min_pct=None):
  """Finds all subsets for which we support > min_pct of codepoints.

  Args:
    file_path: A file_path to a font file.
    min_pct: Min percent coverage to report a subset. 0 means at least 1 glyph.
    25 means 25%.
    ext_min_pct: The minimum percent coverage to report a -ext
    subset supported. Used to admit extended subsets with a lower percent. Same
    interpretation as min_pct. If None same as min_pct.
  Returns:
    A list of 3-tuples of (subset name, #supported, #in subset).
  """
  all_cps = CodepointsInFont(file_path)

  results = []
  for subset in ListSubsets():
    subset_cps = CodepointsInSubset(subset, unique_glyphs=True)
    if not subset_cps:
      continue

    # Khmer includes latin but we only want to report support for non-Latin.
    if subset == 'khmer':
      subset_cps -= CodepointsInSubset('latin')

    overlap = all_cps & subset_cps

    target_pct = min_pct
    if ext_min_pct is not None and subset.endswith('-ext'):
      target_pct = ext_min_pct

    if 100.0 * len(overlap) / len(subset_cps) > target_pct:
      results.append((subset, len(overlap), len(subset_cps)))

  return results

def FamilyName(fontname):
  """Attempts to build family name from font name.

  For example, HPSimplifiedSans => HP Simplified Sans.

  Args:
    fontname: The name of a font.
  Returns:
    The name of the family that should be in this font.
  """
  # SomethingUpper => Something Upper
  fontname = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', fontname)
  # Font3 => Font 3
  fontname = re.sub('([a-z])([0-9]+)', r'\1 \2', fontname)
  # lookHere => look Here
  return re.sub('([a-z0-9])([A-Z])', r'\1 \2', fontname)


def StyleWeight(styleweight):
  """Breaks apart a style/weight specifier into a 2-tuple of (style, weight).

  Args:
    styleweight: style/weight string, e.g. Bold, Regular, or ExtraLightItalic.
  Returns:
    2-tuple of style (normal or italic) and weight.
  """
  if styleweight.endswith('Italic'):
    return ('italic', _KNOWN_WEIGHTS[styleweight[:-6]])

  return ('normal', _KNOWN_WEIGHTS[styleweight])


def FileFamilyStyleWeight(filename):
  """Extracts family, style, and weight from Google Fonts standard filename.

  Args:
    filename: Font filename, eg Lobster-Regular.ttf.
  Returns:
    FileFamilyStyleWeightTuple for file.
  Raises:
    ParseError: if file can't be parsed.
  """
  m = re.search(_FAMILY_WEIGHT_REGEX, filename)
  if not m:
    raise ParseError('Could not parse %s' % filename)
  sw = StyleWeight(m.group(2))
  return FileFamilyStyleWeightTuple(filename, FamilyName(m.group(1)), sw[0],
                                    sw[1])


def ExtractNames(font, name_id):
  return [n.string.decode(n.getEncoding()).encode('ascii', 'ignore')
          for n in font['name'].names if n.nameID == name_id]


def ExtractName(font_or_file, name_id, default):
  """Extracts a name table field (first value if many) from a font.

  Args:
    font_or_file: path to a font file or a TTFont.
    name_id: the ID of the name desired. Use NAME_* constant.
    default: result if no value is present.
  Returns:
    The value of the first entry for name_id or default if there isn't one.
  """
  value = default
  names = []
  if type(font_or_file) is ttLib.TTFont:
    names = ExtractNames(font_or_file, name_id)
  else:
    with contextlib.closing(ttLib.TTFont(font_or_file)) as font:
      names = ExtractNames(font, name_id)

  if names:
    value = names[0]

  return value


def NamePartsForStyleWeight(astyle, aweight):
  """Gives back the parts that go into the name for this style/weight.

  Args:
    astyle: The style name, eg "normal" or "italic"
    aweight: The font weight
  Returns:
    Tuple of parts that go into the name, typically the name for the weight and
    the name for the style, if any ("normal" typically doesn't factor into
    names).
  Raises:
    ValueError: If the astyle or aweight isn't a supported value.
  """
  astyle = astyle.lower()
  if astyle not in _VALID_STYLES:
    raise ValueError('unsupported style %s' % astyle)

  correct_style = None
  if astyle == 'italic':
    correct_style = 'Italic'

  correct_name = None
  for name, weight in _KNOWN_WEIGHTS.iteritems():
    if weight == aweight:
      correct_name = name
      break

  if not correct_name:
    raise ValueError('unsupported weight: %d' % aweight)

  return tuple([n for n in [correct_name, correct_style] if n])


def _RemoveAll(alist, value):
  while value in alist:
    alist.remove(value)


def FilenameFor(family, style, weight, ext=''):
  family = family.replace(' ', '')
  style_weight = list(NamePartsForStyleWeight(style, weight))
  if 'Italic' in style_weight:
    _RemoveAll(style_weight, 'Regular')

  style_weight = ''.join(style_weight)
  return '%s-%s%s' % (family, style_weight, ext)


def FullnameFor(family, style, weight):
  name_parts = [family]
  name_parts.extend(list(NamePartsForStyleWeight(style, weight)))
  _RemoveAll(name_parts, 'Regular')
  return ' '.join(name_parts)


def FontDirs(path):
  """Finds all the font directories (based on METADATA.pb) under path.

  Args:
    path: A path to search under.
  Yields:
    Directories under path that have a METADATA.pb.
  """
  for dir_name, _, _ in os.walk(path):
    if os.path.isfile(os.path.join(dir_name, 'METADATA.pb')):
      yield dir_name




def FsSelectionMask(flag):
  """Get the mask for a given named bit in fsSelection.

  Args:
    flag: Name of the flag per otspec, eg ITALIC, BOLD, etc.
  Returns:
    Bitmask for that flag.
  Raises:
    ValueError: if flag isn't the name of any fsSelection bit.
  """
  for (mask, name) in _FS_SELECTION_BITS:
    if name == flag:
      return mask
  raise ValueError('No mask for %s' % flag)


def FsSelectionFlags(fs_selection):
  """Get the named flags enabled in a given fsSelection.

  Args:
    fs_selection: An fsSelection value.
  Returns:
    List of names of flags enabled in fs_selection.
  """
  names = []
  for (mask, name) in _FS_SELECTION_BITS:
    if fs_selection & mask:
      names.append(name)
  return names


def _EntryForEndOfPath(path, answer_map):
  segments = [s.lower() for s in path.split(os.sep)]
  answers = [answer_map[s] for s in segments
             if s in answer_map]
  if len(answers) != 1:
    raise ValueError('Found %d possible matches: %s' % (
        len(answers), answers))
  return answers[0]


def LicenseFromPath(path):
  """Try to figure out the license for a given path.

  Splits path and looks for known license dirs in segments.

  Args:
    path: A filesystem path, hopefully including a license dir.
  Returns:
    The name of the license, eg OFL, UFL, etc.
  Raises:
    ValueError: if 0 or >1 licenses match path.
  """
  return _EntryForEndOfPath(path, _KNOWN_LICENSE_DIRS)

def _parseNamelistHeader(lines):
  includes = set()
  for line in lines:
    if not line.startswith('#$'):
      # not functional line, regular comment
      continue
    keyword, args = line.rstrip()[2:].lstrip().split(' ', 1)
    if keyword == 'include':
      includes.add(args)
  return {
      'lines': list(lines)
    , 'includes': includes
  }


def get_codepoint_from_line(line):
  assert line.startswith('0x')
  match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7])
  if match is None:
    match = _NAMELIST_CODEPOINT_REGEX.match(line[2:7].upper())
    if match is not None:
      # Codepoints must be uppercase, it's documented
      warn('Found a codepoint with lowercase unicode hex value: 0x{0}'.format(match.groups()[0]))
    return None
  return int(match.groups()[0], 16)

def _parseNamelist(lines):
  cps = set()
  noncodes = set()
  headerLines = []
  readingHeader = True
  for line in lines:
    if readingHeader:
      if not line.startswith('#'):
        # first none comment line ends the header
        readingHeader = False
      else:
        headerLines.append(line)
        continue
    # reading the body, i.e. codepoints

    if line.startswith('0x'):
      codepoint = get_codepoint_from_line(line)
      if codepoint is None:
        # ignore all lines that we don't understand
        continue
      cps.add(codepoint)
      # description
      # line[(2+len(codepoint)),]
    elif line.startswith('      '):
      noncode = line.strip().rsplit(' ')[-1]
      if len(noncode):
        noncodes.add(noncode)

  header = _parseNamelistHeader(headerLines)
  return cps, header, noncodes

def parseNamelist(filename):
  """Parse filename as Namelist and return a tuple of
    (Codepoints set, header data dict)
  """
  with codecs.open(filename, encoding='utf-8') as namFile:
    return _parseNamelist(namFile)

def _loadNamelistIncludes(item, unique_glyphs, cache):
  """Load the includes of an encoding Namelist files.

  This is an implementation detail of readNamelist.
  """
  includes = item["includes"] = []
  charset = item["charset"] = set() | item["ownCharset"]

  noCharcode = item["noCharcode"] = set() | item["ownNoCharcode"]

  dirname =  os.path.dirname(item["fileName"])
  for include in item["header"]["includes"]:
    includeFile = os.path.join(dirname, include)
    try:
      includedItem = readNamelist(includeFile, unique_glyphs, cache)
    except NamelistRecursionError:
      continue
    if includedItem in includes:
      continue
    includes.append(includedItem)
    charset |= includedItem["charset"]
    noCharcode |= includedItem["ownNoCharcode"]
  return item

def __readNamelist(cache, filename, unique_glyphs):
  """Return a dict with the data of an encoding Namelist file.

  This is an implementation detail of readNamelist.
  """
  if filename in cache:
    item = cache[filename]
  else:
    cps, header, noncodes = parseNamelist(filename)
    item = {
      "fileName": filename
    , "ownCharset": cps
    , "header": header
    , "ownNoCharcode": noncodes
    , "includes": None # placeholder
    , "charset": None # placeholder
    , "noCharcode": None
    }
    cache[filename] = item

  if unique_glyphs or item["charset"] is not None:
    return item

  # full-charset/includes are requested and not cached yet
  _loadNamelistIncludes(item, unique_glyphs, cache)
  return item

class NamelistRecursionError(Error):
  """Exception to control infinite recursion in Namelist includes"""
  pass


def _readNamelist(currentlyIncluding, cache, namFilename, unique_glyphs):
  """ Detect infinite recursion and prevent it.

  This is an implementation detail of readNamelist.

  Raises NamelistRecursionError if namFilename is in the process of being included
  """
  # normalize
  filename = os.path.abspath(os.path.normcase(namFilename))
  if filename in currentlyIncluding:
    raise NamelistRecursionError(filename)
  currentlyIncluding.add(filename)
  try:
    result = __readNamelist(cache, filename, unique_glyphs)
  finally:
    currentlyIncluding.remove(filename)
  return result

def readNamelist(namFilename, unique_glyphs=False, cache=None):
  """
  Args:
    namFilename: The path to the  Namelist file.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
    cache: Optional, a dict used to cache loaded Namelist files

  Returns:
  A dict with following keys:
  "fileName": (string) absolut path to namFilename
  "ownCharset": (set) the set of codepoints defined by the file itself
  "header": (dict) the result of _parseNamelistHeader
  "includes":
      (set) if unique_glyphs=False, the resulting dicts of readNamelist
            for each of the include files
      (None) if unique_glyphs=True
  "charset":
      (set) if unique_glyphs=False, the union of "ownCharset" and all
            "charset" items of each included file
      (None) if unique_glyphs=True

  If you are using  unique_glyphs=True and an external cache, don't expect
  the keys "includes" and "charset" to have a specific value.
  Depending on the state of cache, if unique_glyphs=True the returned
  dict may have None values for its "includes" and "charset" keys.
  """
  currentlyIncluding = set()
  if not cache:
    cache = {}
  return _readNamelist(currentlyIncluding, cache, namFilename, unique_glyphs)

def codepointsInNamelist(namFilename, unique_glyphs=False, cache=None):
  """Returns the set of codepoints contained in a given Namelist file.

  This is a replacement CodepointsInSubset and implements the "#$ include"
  header format.

  Args:
    namFilename: The path to the  Namelist file.
    unique_glyphs: Optional, whether to only include glyphs unique to subset.
  Returns:
    A set containing the glyphs in the subset.
  """
  key = 'charset' if not unique_glyphs else 'ownCharset'
  result = readNamelist(namFilename, unique_glyphs, cache)
  return result[key]

### unit tests ###

def makeTestMethod(subset, namelistFilename):
  testName = 'test_legacy_subsets_{0}'.format(subset.replace('-', '_'))
  def test(self):
    """Compare if the old function CodepointsInSubset and the new function
    codepointsInNamelist return the same sets.
    This will only work as long as the #$inlcude statements in the Namelist
    files reproduce the old dependency logic implemented in CodepointFiles
    """
    charsetOldMethod = set(hex(c) for c in CodepointsInSubset(subset
                                    , unique_glyphs=self.unique_glyphs))

    charsetNewMethod = set(hex(c) for c in codepointsInNamelist(
          namelistFilename, unique_glyphs=self.unique_glyphs, cache=self._cache))
    self.assertTrue(len(charsetOldMethod) > 0)
    self.assertEqual(charsetOldMethod, charsetNewMethod);
  return testName, test

def initTestProperties(cls):
  initialized = []
  for subset in ListSubsets():
    namelistFilename = CodepointFileForSubset(subset)
    if namelistFilename is None:
      continue
    testName, test = makeTestMethod(subset, namelistFilename)
    setattr(cls, testName, test)
    initialized.append(testName)
  return initialized


class TestCodepointReading(unittest.TestCase):
  unique_glyphs = True
  _cache = None

  @classmethod
  def setUpClass(cls):
    cls._cache = {}

  @classmethod
  def tearDownClass(cls):
    cls._cache = None


def main(argv):
  # CodepointFileForSubset needs gflags to be parsed and that happens in
  # app.run(). Thus, we can't dynamically build our test cases before.
  initTestProperties(TestCodepointReading)
  unittest.main(argv=argv, verbosity=2)
if __name__ == '__main__':
  from google.apputils import app
  app.run()
