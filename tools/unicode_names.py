# -*- coding: utf-8 -*-

import unicodedata, sys

from google.apputils import app
import gflags as flags

FLAGS = flags.FLAGS

flags.DEFINE_string('nam_file', sys.argv[1], 'Location of file containing the codepoints')


def main(_):
  with open(FLAGS.nam_file, 'r') as f:
    for line in f:
      print _ReformatLine(line)


def _ReformatLine(line):
  if line.startswith('0x'):
    codepoint = int(line[2:6], 16)
    out = unichr(codepoint) + ' ' + unicodedata.name(unichr(codepoint), '')
    return '0x%04X  %s' % (codepoint, out)
  else:
    return line

if __name__ == '__main__':
  app.run()
