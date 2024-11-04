"""
Regenerate ttx dumps. Run this is the axis registry files in
Lib/axisregistry/data/*.textproto have been updated.
"""

from fontTools.ttLib import TTFont
from fontTools.misc.testTools import getXML, parseXML
from glob import glob
import os


def dump(table, ttFont=None):
    return "\n".join(getXML(table.toXML, ttFont))


CWD = os.path.dirname(__file__)
DATA_DIR = os.path.join(CWD, "data")
font_fps = glob(os.path.join(DATA_DIR, "*.ttf"))

# Dump STATs
for fp in font_fps:
    font = TTFont(fp)
    try:
        stat = dump(font["STAT"], font)
        stat_fp = os.path.join(
            DATA_DIR, font.reader.file.name.replace(".ttf", "_STAT.ttx")
        )
        with open(stat_fp, "w") as doc:
            doc.write(stat)
    except:
        all
