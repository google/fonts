
import contextlib
import os


from fontTools import ttLib

from google.apputils import app
from util import google_fonts as fonts


def _LoadGlyf(font, char, name, problems):
  """Loads a glyf and expands (populates fields) it.

  Args:
    font: A TTFont.
    char: int id of char, e.g. ord('C').
    name: name to use in problems string describing char. e.g. SPACE.
    problems: set to add problems to.
  Returns:
    2-tuple of (cmap_key, glyph). (None, None) if a problem occurred. Adds
    to problems if a problem occurred.
  """
  if 'glyf' not in font:
    problems.add('NO_GLYF_TABLE')
    return (None, None)

  cmap = fonts.UnicodeCmapTables(font).next().cmap
  if char not in cmap:
    problems.add('NO_%s' % name)
    return (None, None)

  key = cmap[char]
  glyph = font['glyf'].glyphs[key]
  glyph.expand(font['glyf'])

  return (key, glyph)


def _HasInk(font, glyph_name):
  """Checks if specified glyph has any ink.

  That is, that it has at least one defined contour associated. Composites are
  considered to have ink if any of their components have ink.

  Args:
    font: A TTFont that has a 'glyf' table.
    glyph_name: The name of the glyph to check for ink.
  Returns:
    True if the font has at least one contour associated with it.
  """
  glyph = font['glyf'].glyphs[glyph_name]
  glyph.expand(font['glyf'])

  if not glyph.isComposite():
    if glyph.numberOfContours == 0:
      return False
    (coords, _, _) = glyph.getCoordinates(font['glyf'])
    # you need at least 3 points to draw
    return len(coords) > 2

  # composite is blank if composed of blanks
  # if you setup a font with cycles you are just a bad person
  for glyph_name in glyph.getComponentNames(glyph.components):
    if _HasInk(font, glyph_name):
      return True

  return False


def _CheckFont(font):
  """Inspects a font for space/nbsp issues.

  Args:
    font: A TTFont.
  Returns:
    A set of strings describing problems found in the font. Empty set if none.
  """
  problems = set()

  (space_cmap, _) = _LoadGlyf(font, 0x0020, 'SPACE', problems)
  (nbsp_cmap, _) = _LoadGlyf(font, 0x00A0, 'NBSP', problems)

  if nbsp_cmap and _HasInk(font, nbsp_cmap):
    problems.add('NBSP_HAS_INK')

  if space_cmap and _HasInk(font, space_cmap):
    problems.add('SPACE_HAS_INK')

  if nbsp_cmap and space_cmap:
    if font['hmtx'][nbsp_cmap][0] != font['hmtx'][space_cmap][0]:
      problems.add('SPACE_NBSP_WIDTH_MISMATCH')

  return set(problems)


def main(argv):
  for filename in argv[1:]:
    with contextlib.closing(ttLib.TTFont(filename)) as font:
      problems = _CheckFont(font)
    if not problems:
      problems.add('OK')
    print '{:48} {}'.format(os.path.basename(filename),
                            ','.join(sorted(problems)))

if __name__ == '__main__':
  app.run()
