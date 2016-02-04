

import os


from google.apputils import app
import gflags as flags

from util import google_fonts as fonts

FLAGS = flags.FLAGS

flags.DEFINE_integer('min_pct', 0,
                     'What percentage of subset codepoints have to be supported'
                     ' for a non-ext subset.')
flags.DEFINE_integer('min_pct_ext', 0,
                     'What percentage of subset codepoints have to be supported'
                     ' for a -ext subset.')


def main(argv):
  for arg in argv[1:]:
    subsets = fonts.SubsetsInFont(arg, FLAGS.min_pct, FLAGS.min_pct_ext)
    for (subset, available, total) in subsets:
      print '%s %s %d/%d' % (os.path.basename(arg), subset, available, total)


if __name__ == '__main__':
  app.run()
