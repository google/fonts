#!/usr/bin/env python3
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph
import glob

for font in glob.glob("*.ttf"):
    ttfont = TTFont(font)
    for table in ttfont["cmap"].tables:
        if table.format == 4:
            table.cmap[ord(" ")] = "space"
    glyphs = ttfont.getGlyphOrder()
    glyphs.append("space")
    ttfont.setGlyphOrder(glyphs)

    ttfont["glyf"].glyphs["space"] = Glyph()
    ttfont["hmtx"].metrics["space"] = (1024, 0)
    ttfont.save(font)
