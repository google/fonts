

import os


from google.apputils import app
import gflags as flags

from util import google_fonts as fonts

FLAGS = flags.FLAGS

flags.DEFINE_integer('min_pct', 0,
                     'What percentage of subset codepoints have to be supported'
                     ' to print.')


def main(argv):
  for arg in argv[1:]:
    for (subset, available, total) in fonts.SubsetsInFont(arg, FLAGS.min_pct):
      print '%s %s %d/%d' % (os.path.basename(arg), subset, available, total)


if __name__ == '__main__':
  app.run()
