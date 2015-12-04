"""Utility to compare two font files.

Prints change in glyph count by supported subset and change in size by table.
This is helpful for understanding what is happening when we get a new version of
a font (why is Roboto2 3x larger than Roboto?).

Sample output (abriged run for roboto vs roboto2, at the time slightly smaller):
Subset Coverage Change (codepoints)
  cyrillic -1 (316/320 => 315/320)
  cyrillic-ext -1 (491/653 => 490/653)
  greek -1 (290/363 => 289/363)
  greek-ext -1 (291/619 => 290/619)
  latin -1 (215/219 => 214/219)
  latin-ext -11 (389/1029 => 378/1029)
  vietnamese -1 (300/304 => 299/304)
  all -13 (896 => 883)
Roboto-Regular.ttf (162876) vs Roboto2-Regular.ttf (145256) (-17620)
  Table Changes (delta bytes, from=>to, % change)
    BASE, +0, 0=>0, 0.0%
    CFF , +0, 0=>0, 0.0%
    DSIG, +0, 0=>0, 0.0%
    FFTM, +0, 0=>0, 0.0%
    GDEF, -516, 580=>64, -0.3%
    GPOS, -146, 21028=>20882, -0.1%
    GSUB, -5052, 6120=>1068, -3.1%
    LTSH, +0, 0=>0, 0.0%
    OS/2, +0, 96=>96, 0.0%
    VORG, +0, 0=>0, 0.0%
    cmap, -2634, 4808=>2174, -1.6%
    cvt , +68, 76=>144, 0.0%
    fpgm, +2483, 444=>2927, 1.5%
    gasp, -4, 12=>8, -0.0%
    glyf, -19546, 119606=>100060, -12.0%
    hdmx, -1260, 1260=>0, -0.8%
    head, +0, 54=>54, 0.0%
    hhea, +0, 36=>36, 0.0%
    hmtx, -712, 5000=>4288, -0.4%
    kern, +0, 0=>0, 0.0%
    loca, -356, 2502=>2146, -0.2%
    maxp, +0, 32=>32, 0.0%
    name, +708, 664=>1372, 0.4%
    post, +9437, 32=>9469, 5.8%
    prep, -81, 219=>138, -0.0%
    vhea, +0, 0=>0, 0.0%
    vmtx, +0, 0=>0, 0.0%
    TOTAL, -17611, 162569=>144958, -10.8%
"""

import errno
import os
import sys


from fontTools.ttLib import sfnt

from google.apputils import app
import gflags as flags

from util import google_fonts as fonts


FLAGS = flags.FLAGS
flags.DEFINE_boolean('diff_tables', True, 'Whether to print table size diffs')
flags.DEFINE_boolean('diff_coverage', True, 'Whether to print coverage diffs')

_KNOWN_TABLES = ('BASE', 'CFF ', 'DSIG', 'GDEF', 'GPOS', 'GSUB', 'LTSH',
                 'OS/2', 'VORG', 'cmap', 'cvt ', 'fpgm', 'gasp', 'glyf', 'hdmx',
                 'head', 'hhea', 'hmtx', 'loca', 'maxp', 'name', 'post', 'prep',
                 'FFTM', 'kern', 'vhea', 'vmtx')


def CompareSize(font_filename1, font_filename2):
  """Prints a size comparison for two fonts.

  If so flagged (--diff_tables), prints per-table size change.

  Args:
    font_filename1: The first font to compare.
    font_filename2: The second font to compare.
  Returns:
    String describing size differences.
  Raises:
    OSError: If either argument doesn't point to a file. errno.ENOENT.
  """
  if not (os.path.isfile(font_filename1) and os.path.isfile(font_filename2)):
    raise OSError(errno.ENOENT, 'Missing at least one of %s and %s' % (
        os.path.basename(font_filename1), os.path.basename(font_filename2)))

  font_sz1 = os.stat(font_filename1).st_size
  font_sz2 = os.stat(font_filename2).st_size
  result = '%s (%d) vs %s (%d) (%+d)\n' % (
      os.path.basename(font_filename1), font_sz1,
      os.path.basename(font_filename2), font_sz2, font_sz2 - font_sz1)

  if FLAGS.diff_tables:
    result += DiffTables(font_filename1, font_filename2)

  return result


def DiffTables(font_filename1, font_filename2):
  """Prints a table-by-table size comparison of two fonts.

  Args:
    font_filename1: The first font to compare.
    font_filename2: The second font to compare.
  Returns:
    String describing size difference. One line per unique table in either font.
  """
  result = ['  Table Changes (delta bytes, from=>to, % change)']
  sfnt1 = sfnt.SFNTReader(open(font_filename1))
  sfnt2 = sfnt.SFNTReader(open(font_filename2))

  font_sz1 = os.stat(font_filename1).st_size

  sum_tables1 = 0
  sum_tables2 = 0

  table_l1_l2s = []
  for t in fonts.UniqueSort(sfnt1.tables, sfnt2.tables, _KNOWN_TABLES):
    table1_sz = sfnt1.tables[t].length if sfnt1.has_key(t) else 0
    table2_sz = sfnt2.tables[t].length if sfnt2.has_key(t) else 0
    sum_tables1 += table1_sz
    sum_tables2 += table2_sz
    table_l1_l2s.append((t, table1_sz, table2_sz))

  for (table, table1_sz, table2_sz) in table_l1_l2s:
    delta_pct = float(table2_sz - table1_sz) / font_sz1 * 100
    result.append('    %s, %+d, %d=>%d, %.1f%%' % (
        table, table2_sz - table1_sz, table1_sz, table2_sz, delta_pct))

  delta_pct = float(sum_tables2 - sum_tables1) / font_sz1 * 100
  result.append('    TOTAL, %+d, %d=>%d, %.1f%%' % (
      sum_tables2 - sum_tables1, sum_tables1, sum_tables2, delta_pct))

  return '\n'.join(result)


def DiffCoverage(font_filename1, font_filename2, subset):
  """Prints a comparison of the coverage of a given subset by two fonts.

  Args:
    font_filename1: The first font to compare.
    font_filename2: The second font to compare.
    subset: The lowercase name of the subset to compare coverage of.
  """
  f1cps = fonts.CodepointsInFont(font_filename1)
  f2cps = fonts.CodepointsInFont(font_filename2)

  if subset != 'all':
    subset_cps = fonts.CodepointsInSubset(subset)
    f1cps &= subset_cps
    f2cps &= subset_cps
  else:
    subset_cps = None

  subset_cp_str = ('/%d' % len(subset_cps)) if subset_cps is not None else ''

  print '  %s %+d (%d%s => %d%s)' % (
      subset, len(f2cps) - len(f1cps), len(f1cps), subset_cp_str, len(f2cps),
      subset_cp_str)


def CompareDirs(font1, font2):
  """Compares fonts by assuming font1/2 are dirs containing METADATA.json."""
  m1 = fonts.Metadata(font1)
  m2 = fonts.Metadata(font2)
  subsets_to_compare = fonts.UniqueSort(m1['subsets'], m2['subsets'])
  subsets_to_compare.remove('menu')
  subsets_to_compare.append('all')

  font_filename1 = os.path.join(font1, fonts.RegularWeight(m1))
  font_filename2 = os.path.join(font2, fonts.RegularWeight(m2))

  if FLAGS.diff_coverage:
    print 'Subset Coverage Change (codepoints)'
    for subset in subsets_to_compare:
      DiffCoverage(font_filename1, font_filename2, subset)

  print CompareSize(font_filename1, font_filename2)


def CompareFiles(font1, font2):
  """Compares fonts assuming font1/2 are font files."""
  print CompareSize(font1, font2)


def main(_):
  if len(sys.argv) < 3:
    raise app.UsageError('Must pass at least two arguments, font file or font'
                         ' dir to diff')

  font1 = sys.argv[1]
  font2 = sys.argv[2]
  dirs = os.path.isdir(font1) and os.path.isdir(font2)
  files = os.path.isfile(font1) and os.path.isfile(font2)

  if not dirs and not files:
    print '%s and %s must both point to directories or font files' % (
        font1, font2)
    sys.exit(1)

  if dirs:
    CompareDirs(font1, font2)

  if files:
    CompareFiles(font1, font2)


if __name__ == '__main__':
  app.run()
