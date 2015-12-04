"""Helper APIs for interaction with Google Fonts.

Provides APIs to interact with font subsets, codepoints for font or subset.
"""

import collections
import contextlib
import errno
import json
import os
import re
import sys


from fontTools import ttLib

import gflags as flags
from google.apputils import resources

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
  print >> sys.stderr, msg


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
  for f in metadata['fonts']:
    if f['weight'] == 400 and f['style'] == 'normal':
      return os.path.splitext(f['filename'])[0] + '.ttf'
  raise OSError(errno.ENOENT, 'unable to find regular weight')


def ListSubsets():
  """Returns a list of all subset names, in lowercase, except */all and menu."""

  subsets = []

  with resources.GetResourceAsFile(_SUBSET_RESOURCE_PATH) as f:
    for l in f:
      match = _SUBSET_PATTERN.search(l)
      if match and match.group(1) not in ('ALL', 'MENU'):
        subsets.append(match.group(2))

  return subsets


def Metadata(file_or_dir):
  """Returns json object for a metadata file.

  If file_or_dir is a file named METADATA.json, load it. If file_or_dir is a
  directory, load the METADATA.json file in that directory.

  Args:
    file_or_dir: A file or directory.
  Returns:
    Python object loaded from METADATA.json content.
  Raises:
    ValueError: if file_or_dir isn't a METADATA.json file or dir containing one.
  """
  if (os.path.isfile(file_or_dir) and
      os.path.basename(file_or_dir) == 'METADATA.json'):
    metadata_file = file_or_dir
  elif os.path.isdir(file_or_dir):
    metadata_file = os.path.join(file_or_dir, 'METADATA.json')
  else:
    raise ValueError('%s is neither METADATA.json file or a directory' %
                     file_or_dir)

  with open(metadata_file) as f:
    # OrderedDict to avoid shuffling key order
    return json.load(f, object_pairs_hook=collections.OrderedDict)


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
    with open(filename) as f:
      for line in f:
        if not line.startswith('#'):
          cps.add(int(line[2:6], 16))

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


def SubsetsInFont(file_path, min_pct):
  """Finds all subsets for which we support > min_pct of codepoints.

  Args:
    file_path: A file_path to a font file.
    min_pct: Min percent coverage to report a subset. 0 means at least 1 glyph.
    25 means 25%.
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

    if 100.0 * len(overlap) / len(subset_cps) > min_pct:
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
  results = []
  for name in font['name'].names:
    if name.nameID == name_id:
      # name.string is weird. See fontTools/ttLib/tables/_n_a_m_e.py.
      value = name.string
      if name.isUnicode():
        value = value.decode(name.getEncoding()).encode('utf8')
      results.append(value)
  return results


def ExtractName(fontfile, name_id, default):
  """Extracts a name table field (first value if many) from a font.

  Args:
    fontfile: path to a font file.
    name_id: the ID of the name desired. Use NAME_* constant.
    default: result if no value is present.
  Returns:
    The value of the first entry for name_id or default if there isn't one.
  """
  value = default
  with contextlib.closing(ttLib.TTFont(fontfile)) as font:
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
  """Finds all the font directories (based on METADATA.json) under path.

  Args:
    path: A path to search under.
  Yields:
    Directories under path that have a METADATA.json.
  """
  for dir_name, _, _ in os.walk(path):
    if os.path.isfile(os.path.join(dir_name, 'METADATA.json')):
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
