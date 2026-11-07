#!/usr/bin/env python3
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph
from bumpfontversion.sfnthandler import SFNTHandler
from bumpversion.version_part import VersionPart
import glob

h = SFNTHandler()

for font in glob.glob("*.ttf"):
    ttfont = TTFont(font)
    for table in ttfont["cmap"].tables:
        if table.format == 4:
            table.cmap[ord(" ")] = "space"
            table.cmap[0xA0] = "space"
    glyphs = ttfont.getGlyphOrder()
    glyphs.append("space")
    ttfont.setGlyphOrder(glyphs)

    ttfont["glyf"].glyphs["space"] = Glyph()
    ttfont["hmtx"].metrics["space"] = (280, 0)

    ttfont.save(font)

    current_version = h.current_version(font)
    current_version._values["minor"] = VersionPart("031")
    h.set_version(font, current_version)
