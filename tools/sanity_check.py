

import collections
import contextlib
import os
import re
import sys


from fontTools import ttLib

from google.apputils import app
import gflags as flags

from util import google_fonts as fonts

FLAGS = flags.FLAGS

flags.DEFINE_boolean('suppress_pass', True, 'Whether to print pass: results')
flags.DEFINE_boolean('check_metadata', True, 'Whether to check METADATA values')
flags.DEFINE_boolean('check_font', True, 'Whether to check font values')
flags.DEFINE_string('repair_script', None, 'Where to write a repair script')
_FIX_TYPE_OPTS = ['all', 'name', 'filename', 'postScriptName', 'fullName',
                  'fsSelection', 'fsType', 'usWeightClass']
flags.DEFINE_multistring('fix_type', 'all',
                         'What types of problems should be fixed by '
                         'repair_script. Choices: ' + ', '.join(_FIX_TYPE_OPTS))


ResultMessageTuple = collections.namedtuple(
    'ResultMessageTuple', ['happy', 'message', 'path', 'repair_script'])


def _HappyResult(message, path):
  return ResultMessageTuple(True, message, path, None)


def _SadResult(message, path, repair_script=None):
  return ResultMessageTuple(False, message, path, repair_script)


def _DropEmptyPathSegments(path):
  """Removes empty segments from the end of path.

  Args:
    path: A filesystem path.
  Returns:
    path with trailing empty segments removed. Eg /duck/// => /duck.
  """
  while True:
    (head, tail) = os.path.split(path)
    if tail:
      break
    path = head
  return path


def _SanityCheck(path):
  """Runs various sanity checks on the font family under path.

  Args:
    path: A directory containing a METADATA.json file.
  Returns:
    A list of ResultMessageTuple's.
  """
  try:
    fonts.Metadata(path)
  except ValueError as e:
    return [_SadResult('Bad METADATA.json: ' + e.message, path)]

  results = []
  if FLAGS.check_metadata:
    results.extend(_CheckLicense(path))
    results.extend(_CheckNameMatching(path))

  if FLAGS.check_font:
    results.extend(_CheckFontInternalValues(path))

  return results


def _CheckLicense(path):
  """Verifies that METADATA.json license is correct under path.

  Assumes path is of the form .../<license>/<whatever>/METADATA.json.

  Args:
    path: A directory containing a METADATA.json file.
  Returns:
    A list with one ResultMessageTuple. If happy, license is good.
  """
  metadata = fonts.Metadata(path)
  lic = metadata['license']
  lic_dir = os.path.basename(os.path.dirname(path))

  # We use /apache for the license Apache2
  if lic_dir == 'apache':
    lic_dir += '2'

  result = _HappyResult('License consistantly %s' % lic, path)
  # if we were Python 3 we'd use casefold(); this will suffice
  if lic_dir.lower() != lic.lower():
    result = _SadResult(
        'Dir license != METADATA license: %s != %s' % (lic_dir, lic), path)

  return [result]


def _CheckNameMatching(path):
  """Verifies the various name fields in the METADATA.json file are sane.

  Args:
    path: A directory containing a METADATA.json file.
  Returns:
    A list of ResultMessageTuple, one per validation performed.
  """
  results = []
  metadata = fonts.Metadata(path)
  name = metadata['name']

  for font in metadata['fonts']:
    # We assume style/weight is correct in METADATA
    style = font['style']
    weight = font['weight']
    correct_values = {
        'name': name,
        'filename': fonts.FilenameFor(name, style, weight, '.ttf'),
        'postScriptName': fonts.FilenameFor(name, style, weight),
        'fullName': fonts.FullnameFor(name, style, weight)
    }

    for key in correct_values:
      expected = correct_values[key]
      actual = font[key]
      if expected != actual:
        results.append(_SadResult(
            '%s METADATA %s/%d %s expected %s, got %s' %
            (name, style, weight, key, expected, actual), path,
            _FixMetadata(style, weight, key, expected)))

  if not results:
    results.append(_HappyResult('METADATA name consistently derived from "%s"'
                                % name, path))

  return results


def _IsItalic(style):
  return style.lower() == 'italic'


def _IsBold(weight):
  """Is this weight considered bold?

  Per Dave C, only 700 will be considered bold.

  Args:
    weight: Font weight.
  Returns:
    True if weight is considered bold, otherwise False.
  """
  return weight == 700


def _ShouldFix(key):
  return (FLAGS.fix_type and (
      key in FLAGS.fix_type or 'all' in FLAGS.fix_type))


def _FixMetadata(style, weight, key, expected):
  if not _ShouldFix(key):
    return None

  if not isinstance(expected, int):
    expected = '\'%s\'' % expected

  return ('[f for f in metadata[\'fonts\'] if f[\'style\'] == \'%s\' '
          'and f[\'weight\'] == %d][0][\'%s\'] = %s') % (
              style, weight, key, expected)


def _FixFsSelectionBit(key, expected):
  """Write a repair script to fix a bad fsSelection bit.

  Args:
    key: The name of an fsSelection flag, eg 'ITALIC' or 'BOLD'.
    expected: Expected value, true/false, of the flag.
  Returns:
    A python script to fix the problem.
  """
  if not _ShouldFix('fsSelection'):
    return None

  op = '|='
  verb = 'set'
  mask = bin(fonts.FsSelectionMask(key))
  if not expected:
    op = '&='
    verb = 'unset'
    mask = '~' + mask

  return 'ttf[\'OS/2\'].fsSelection %s %s  # %s %s' % (op, mask, verb, key)


def _FixFsType(expected):
  if not _ShouldFix('fsType'):
    return None
  return 'ttf[\'OS/2\'].fsType = %d' % expected


def _FixWeightClass(expected):
  if not _ShouldFix('usWeightClass'):
    return None
  return 'ttf[\'OS/2\'].usWeightClass = %d' %  expected


def _FixBadNameRecord(friendly_name, name_id, expected):
  if not _ShouldFix(friendly_name):
    return None

  return ('for nr in [n for n in ttf[\'name\'].names if n.nameID == %d]:\n'
          '  nr.string = \'%s\'.encode(nr.getEncoding())  # Fix %s'
          % (name_id, expected, friendly_name))


def _FixMissingNameRecord(friendly_name, name_id, expected):
  if not _ShouldFix(friendly_name):
    return None

  return ('nr = ttLib.tables._n_a_m_e.NameRecord()\n'
          'nr.nameID = %d  # %s'
          'nr.langID = 0x409\n'
          'nr.platEncID = 1\n'
          'nr.platformID = 3\n'
          'nr.string = \'%s\'.encode(nr.getEncoding())\n'
          'ttf[\'name\'].names.append(nr)\n' % (
              name_id, friendly_name, expected))


def _CheckFontOS2Values(path, font, ttf):
  """Check sanity of values hidden in the 'OS/2' table.

  Notably usWeightClass, fsType, fsSelection.

  Args:
    path: Path to directory containing font.
    font: A font record from a METADATA.json.
    ttf: A fontTools.ttLib.TTFont for the font.
  Returns:
    A list of ResultMessageTuple for tests performed.
  """
  results = []

  font_file = font['filename']
  full_font_file = os.path.join(path, font_file)
  expected_style = font['style']
  expected_weight = font['weight']

  os2 = ttf['OS/2']
  fs_selection_flags = fonts.FsSelectionFlags(os2.fsSelection)
  actual_weight = os2.usWeightClass
  fs_type = os2.fsType

  marked_oblique = 'OBLIQUE' in fs_selection_flags
  marked_italic = 'ITALIC' in fs_selection_flags
  marked_bold = 'BOLD' in fs_selection_flags

  # fsSelection flags (see thread http://shortn/_FEOPPU691a)
  expect_italic = _IsItalic(expected_style)
  expect_bold = _IsBold(expected_weight)
  # Per Dave C, we should NEVER set oblique, use 0 for italic
  expect_oblique = False

  results.append(ResultMessageTuple(
      marked_italic == expect_italic,
      '%s %s/%d fsSelection marked_italic %d' % (
          font_file, expected_style, expected_weight, marked_italic),
      full_font_file, _FixFsSelectionBit('ITALIC', expect_italic)))
  results.append(ResultMessageTuple(
      marked_bold == expect_bold,
      '%s %s/%d fsSelection marked_bold %d' %
      (font_file, expected_style, expected_weight, marked_bold), full_font_file,
      _FixFsSelectionBit('BOLD', expect_bold)))

  results.append(ResultMessageTuple(
      marked_oblique == expect_oblique,
      '%s %s/%d fsSelection marked_oblique %d' % (
          font_file, expected_style, expected_weight, marked_oblique),
      full_font_file, _FixFsSelectionBit('OBLIQUE', expect_oblique)))

  # For weight < 300, just confirm 250<weight<300
  # TODO(user): we should also verify ordering is correct
  weight_ok = expected_weight == actual_weight
  weight_msg = str(expected_weight)
  if expected_weight < 300:
    weight_ok = actual_weight > 250 and actual_weight < 300
    weight_msg = '(250, 300)'

  results.append(ResultMessageTuple(
      weight_ok,
      '%s %s/%d weight expected: %s usWeightClass: %d' %
      (font_file, expected_style, expected_weight, weight_msg, actual_weight),
      full_font_file, _FixWeightClass(expected_weight)))

  expected_fs_type = 0
  results.append(ResultMessageTuple(
      expected_fs_type == fs_type,
      '%s %s/%d fsType expected: %d fsType: %d' %
      (font_file, expected_style, expected_weight, expected_fs_type, fs_type),
      full_font_file, _FixFsType(expected_fs_type)))

  return results


def _CheckFontNameValues(path, name, font, ttf):
  """Check sanity of values in the 'name' table.

  Specifically the fullname and postScriptName.

  Args:
    path: Path to directory containing font.
    name: The name of the family.
    font: A font record from a METADATA.json.
    ttf: A fontTools.ttLib.TTFont for the font.
  Returns:
    A list of ResultMessageTuple for tests performed.
  """
  results = []

  style = font['style']
  weight = font['weight']
  full_font_file = os.path.join(path, font['filename'])

  expectations = [
      ('family', fonts.NAME_FAMILY, name),
      ('postScriptName', fonts.NAME_PSNAME,
       fonts.FilenameFor(name, style, weight)),
      ('fullName', fonts.NAME_FULLNAME, fonts.FullnameFor(name, style, weight))]

  for (friendly_name, name_id, expected) in expectations:
    # If you have lots of name records they should ALL have the right value
    actuals = fonts.ExtractNames(ttf, name_id)
    for (idx, actual) in enumerate(actuals):
      results.append(ResultMessageTuple(
          expected == actual,
          '%s %s/%d \'name\' %s[%d] expected %s, got %s' %
          (name, style, weight, friendly_name, idx, expected, actual),
          full_font_file,
          _FixBadNameRecord(friendly_name, name_id, expected)))

    # should have at least one actual
    if not actuals:
      results.append(_SadResult(
          '%s %s/%d \'name\' %s has NO values' %
          (name, style, weight, friendly_name), full_font_file,
          _FixMissingNameRecord(friendly_name, name_id, expected)))

  return results


def _CheckFontInternalValues(path):
  """Validates fonts internal metadata matches METADATA.json values.

  In particular, checks 'OS/2' {usWeightClass, fsSelection, fsType} and 'name'
  {fullName, postScriptName} values.

  Args:
    path: A directory containing a METADATA.json file.
  Returns:
    A list of ResultMessageTuple, one per validation performed.
  """
  results = []
  metadata = fonts.Metadata(path)
  name = metadata['name']

  for font in metadata['fonts']:
    font_file = font['filename']
    with contextlib.closing(ttLib.TTFont(os.path.join(path, font_file))) as ttf:
      results.extend(_CheckFontOS2Values(path, font, ttf))
      results.extend(_CheckFontNameValues(path, name, font, ttf))

  return results




def _WriteRepairScript(dest_file, results):
  with open(dest_file, 'w') as out:
    out.write('import collections\n')
    out.write('import contextlib\n')
    out.write('import json\n')
    out.write('import re\n')
    out.write('from fontTools import ttLib\n')
    out.write('\n')

    # group by path
    by_path = collections.defaultdict(list)
    for result in results:
      if result.happy or not result.repair_script:
        continue
      if result.repair_script not in by_path[result.path]:
        by_path[result.path].append(result.repair_script)

    for path in sorted(by_path.keys()):
      out.write('# repair %s\n' % os.path.basename(path))
      _, ext = os.path.splitext(path)


      prefix = ''
      if ext == '.ttf':
        prefix = '  '
        out.write('with contextlib.closing(ttLib.TTFont(\'%s\')) as ttf:\n'
                  % path)
      elif os.path.isdir(path):
        metadata_file = os.path.join(path, 'METADATA.json')
        out.write('with open(\'%s\', \'r\') as f:\n' % metadata_file)
        out.write('  metadata = json.load(f, '
                  'object_pairs_hook=collections.OrderedDict)\n')
      else:
        raise ValueError('Not sure how to script %s' % path)

      for repair in by_path[path]:
        out.write(prefix)
        out.write(re.sub('\n', '\n' + prefix, repair))
        out.write('\n')

      if ext == '.ttf':
        out.write('  ttf.save(\'%s\')\n' % path)

      if os.path.isdir(path):
        out.write('with open(\'%s\', \'w\') as f:\n' % metadata_file)
        # pylint: disable=anomalous-backslash-in-string
        out.write('  f.write(re.sub(r\'\s+\\n\', \'\\n\', '
                  'json.dumps(metadata, indent=2)))\n')
        # pylint: enable=anomalous-backslash-in-string

      out.write('\n')


def main(argv):
  result_code = 0
  all_results = []
  paths = [_DropEmptyPathSegments(os.path.expanduser(p)) for p in argv[1:]]
  for path in paths:
    if not os.path.isdir(path):
      raise ValueError('Not a directory: %s' % path)

  for path in paths:
    for font_dir in fonts.FontDirs(path):
      results = _SanityCheck(font_dir)
      all_results.extend(results)
      for result in results:
        result_msg = 'pass'
        if not result.happy:
          result_code = 1
          result_msg = 'FAIL'
        if not result.happy or not FLAGS.suppress_pass:
          print '%s: %s (%s)' % (result_msg, result.message, font_dir)

  if FLAGS.repair_script:
    _WriteRepairScript(FLAGS.repair_script, all_results)

  sys.exit(result_code)


if __name__ == '__main__':
  app.run()
