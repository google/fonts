# Experimental for local testing.
# Usage:
#  python make_kit.py some_font.ttf some_other_font.ttf

import contextlib
import os
import sys
from fontTools import subset
from fontTools import ttLib

def makeKit(font_path):
  # put the result into a directory named file_name.kit
  dest_dir = os.path.splitext(font_path)[0] + '.kit'
  if os.path.isdir(dest_dir):
    print 'FAILURE: dest %s already exists' % dest_dir
    return False
  os.makedirs(dest_dir)
  print 'Making a kit for %s in %s' % (font_path, dest_dir)

  # crack open the font
  # equivalent  pyftsubset /tmp/Lobster-Regular.ttf --unicodes='*' --obfuscate_names
  options = subset.Options()
  with contextlib.closing(subset.load_font(font_path, options)) as font:
    unicodes = []
    for t in font['cmap'].tables:
      if t.isUnicode():
        unicodes.extend(t.cmap.keys())
    options.unicodes = unicodes

    # mangle 'name' so the font can't be installed
    options.obfuscate_names

    # apply our subsetting, most notably trashing 'name'
    subsetter = subset.Subsetter(options=options)
    subsetter.populate()

    # write [ot]tf, woff, and woff2 editions with 'name' mangled
    font_name_noext = os.path.splitext(os.path.basename(font_path))[0]
    font_ext = os.path.splitext(os.path.basename(font_path))[1]
    for fmt in [font_ext, '.woff', '.woff2']:
      dest_file = os.path.join(dest_dir, font_name_noext + fmt)
      options.flavor = None
      if fmt.startswith('.woff'):
        options.flavor = fmt[1:]
      print 'Writing %s' % dest_file
      with open(dest_file, 'wb') as f:
        subset.save_font(font, f, options)

    # write a sample somewhat (no early Android, IE) bulletproof css
    dest_file = os.path.join(dest_dir, 'bulletproof.css')
    os2 = font['OS/2']
    font_style = 'normal'
    if os2.fsSelection & 1:
      font_style = 'italic'
    with open(dest_file, 'w') as f:
      f.write("@font-face {\n")
      f.write("  font-family: '%s';\n" % font_name_noext)
      f.write("  font-style: %s;\n" % font_style)
      f.write("  font-weight: %d;\n" % os2.usWeightClass)
      f.write("  src:\n")
      f.write("    url('./%s.woff2') format('woff2'),\n" % font_name_noext)
      f.write("    url('./%s.woff') format('woff'),\n" % font_name_noext)
      if font_ext == '.otf':
        f.write("    url('./%s.otf') format('opentype')" % font_name_noext)
      else:
        f.write("    url('./%s.ttf') format('truetype')" % font_name_noext)
      f.write(";\n")
      f.write("}\n")

  return True

def main():
  for font_path in sys.argv[1:]:
    makeKit(font_path)


if __name__ == "__main__":
    # execute only if run as a script
    main()