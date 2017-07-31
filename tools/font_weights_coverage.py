"""Tool to check codepoint coverage in all font weights.

Ex: If FamilyName-Regular.ttf supports codepoints A-D
       FamilyName-Bold.ttf supports codepoints B-E
       FamilyName-Light.ttf supports codepoints A-E

$ python tools/font_weights_coverage.py ofl/familyname
FamilyName-Regular.ttf failed
0x0045
FamilyName-Bold.ttf failed
0x0041
FamilyName-Light.ttf passed
"""


import os
from os import listdir
import sys

from google.apputils import app
from util import google_fonts as fonts


def main(argv):
  if len(argv) != 2 or not os.path.isdir(argv[1]):
    sys.exit('Must have one argument, a directory containing font files.')

  dirpath = argv[1]
  cps = set()
  for f in _GetFontFiles(dirpath):
    cps.update(fonts.CodepointsInFont(os.path.join(dirpath, f)))

  for f in _GetFontFiles(dirpath):
    diff = cps - fonts.CodepointsInFont(os.path.join(dirpath, f))
    if bool(diff):
      print '%s failed' % (f)
      for c in diff:
        print '0x%04X' % (c)
    else:
      print '%s passed' % (f)


def _GetFontFiles(path):
  """Returns list of font files in a path.

  Args:
    path: directory path
  Returns:
    Set of font files
  """
  return [f for f in listdir(path)
          if os.path.splitext(f)[1] in ('.ttf', '.otf')]

if __name__ == '__main__':
  app.run()
