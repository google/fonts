This directory contains 'namelist' files, that list unicode characters followed by glyph names or glyph descriptions. 

Typically all the Unicodes in each file are in each font. 
If the fonts go beyond that list, those additional characters will not be available to Fonts API end users.

The Google Fonts API uses these files in combination with [pyftsubset](https://github.com/behdad/fonttools/blob/master/Lib/fontTools/subset.py) to generate script subsets from the full `.ttf` files in this repository.

The subsetting requires that each line must start with `0x` and then have 4 **uppercase** hex digits; what follows is an arbitrary description to the end of the line.
Comments are lines starting with `#`.

A python script, `tools/namelist.py` can generate these files:

    namelist.py Font.ttf > NameList.nam

The `[wgl-latin.enc]` file can be used by [Fontlab Studio 5](http://www.fontlab.com), and represented Microsoft's [Windows Glyph List 4](https://en.wikipedia.org/wiki/Windows_Glyph_List_4) glyph set.

A python script, `tools/unicode_names.py` can reformat these files: 

    python unicode_names.py --nam_file=encodings/latin_unique-glyphs.nam;
    0x0020    SPACE
    0x0021  ! EXCLAMATION MARK
    0x0022  " QUOTATION MARK
    0x0023  # NUMBER SIGN
    ...
