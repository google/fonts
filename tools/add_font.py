
import errno
import glob
import os
import re
import sys
import time

import fonts_public_pb2 as fonts_pb2
from google.protobuf import text_format
from google.apputils import app
import gflags as flags

from util import google_fonts as fonts

FLAGS = flags.FLAGS

flags.DEFINE_integer('min_pct', 50,
                     'What percentage of subset codepoints have to be supported'
                     ' for a non-ext subset.')
flags.DEFINE_integer('min_pct_ext', 10,
                     'What percentage of subset codepoints have to be supported'
                     ' for a -ext subset.')




def _FileFamilyStyleWeights(fontdir):
  """Extracts file, family, style, weight 4-tuples for each font in dir.

  Args:
    fontdir: Directory that supposedly contains font files for a family.
  Returns:
    List of fonts.FileFamilyStyleWeightTuple ordered by weight, style
    (normal first).
  Raises:
    OSError: If the font directory doesn't exist (errno.ENOTDIR) or has no font
    files (errno.ENOENT) in it.
    RuntimeError: If the font directory appears to contain files from multiple
    families.
  """
  if not os.path.isdir(fontdir):
    raise OSError(errno.ENOTDIR, 'No such directory', fontdir)

  files = glob.glob(os.path.join(fontdir, '*.ttf'))
  if not files:
    raise OSError(errno.ENOENT, 'no font files found')

  result = [fonts.FileFamilyStyleWeight(f) for f in files]
  def _Cmp(r1, r2):
    return cmp(r1.weight, r2.weight) or -cmp(r1.style, r2.style)
  result = sorted(result, _Cmp)

  family_names = {i.family for i in result}
  if len(family_names) > 1:
    raise RuntimeError('Ambiguous family name; possibilities: %s'
                       % family_names)

  return result


def _MakeMetadata(fontdir):
  """Builds a dictionary matching a METADATA.pb file.

  Args:
    fontdir: Directory containing font files for which we want metadata.
  Returns:
    OrderedDict of a complete METADATA.pb structure.
  """
  file_family_style_weights = _FileFamilyStyleWeights(fontdir)

  first_file = file_family_style_weights[0].file
  subsets = ['menu'] + [s[0] for s in fonts.SubsetsInFont(first_file,
                                                          FLAGS.min_pct,
                                                          FLAGS.min_pct_ext)]

  font_license = fonts.LicenseFromPath(fontdir)


  metadata = fonts_pb2.FamilyProto()
  metadata.name = file_family_style_weights[0].family
  metadata.designer = 'Unknown'
  metadata.category = 'SANS_SERIF'
  metadata.license = font_license
  subsets = sorted(subsets)
  for subset in subsets:
    metadata.subsets.append(subset)
  metadata.date_added = time.strftime('%Y-%m-%d')

  for (fontfile, family, style, weight) in file_family_style_weights:
    filename = os.path.basename(fontfile)
    font_psname = fonts.ExtractName(fontfile, fonts.NAME_PSNAME,
                                    os.path.splitext(filename)[0])
    font_copyright = fonts.ExtractName(fontfile, fonts.NAME_COPYRIGHT, '???.')

    font_metadata = metadata.fonts.add()
    font_metadata.name = family
    font_metadata.style = style
    font_metadata.weight = weight
    font_metadata.filename = filename
    font_metadata.post_script_name = font_psname
    default_fullname = os.path.splitext(filename)[0].replace('-', ' ')
    font_metadata.full_name = fonts.ExtractName(fontfile, fonts.NAME_FULLNAME,
                                                default_fullname)
    font_metadata.copyright = font_copyright

  return metadata


def _WriteTextFile(filename, text):
  """Write text to file.

  Nop if file exists with that exact content. This allows running against files
  that are in Piper and not marked for editing; you will get an error only if
  something changed.

  Args:
    filename: The file to write.
    text: The content to write to the file.
  """
  if os.path.isfile(filename):
    with open(filename, 'r') as f:
      current = f.read()
    if current == text:
      print 'No change to %s' % filename
      return

  with open(filename, 'w') as f:
    f.write(text)
  print 'Wrote %s' % filename




def main(argv):
  if len(argv) != 2:
    sys.exit('One argument, a directory containing a font family')
  fontdir = argv[1]

  metadata = _MakeMetadata(fontdir)
  text_proto = text_format.MessageToString(metadata)

  desc = os.path.join(fontdir, 'DESCRIPTION.en_us.html')
  if os.path.isfile(desc):
    print 'DESCRIPTION.en_us.html exists'
  else:
    _WriteTextFile(desc, 'N/A')

  _WriteTextFile(os.path.join(fontdir, 'METADATA.pb'), text_proto)



if __name__ == '__main__':
  app.run()
