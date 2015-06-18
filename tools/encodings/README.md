This directory contains 'namelist' files, that list unicode characters followed by glyph names or glyph descriptions. 

The Google Fonts API uses these files in combination with [pyftsubset](https://github.com/behdad/fonttools/blob/master/Lib/fontTools/subset.py) to generate script subsets from the full `.ttf` files in this repository.

That use requires that each line must start with `0x` and then have 4 **uppercase** hex digits; what follows is an arbitrary description to the end of the line.
Comments are lines starting with `#`.

A python script, `[namelist.py](namelist.py)` can generate these files:

    namelist.py Font.ttf > NameList.nam

The `[wgl-latin.enc]` file can be used by [Fontlab Studio 5](http://www.fontlab.com), and represented Microsoft's [Windows Glyph List 4](https://en.wikipedia.org/wiki/Windows_Glyph_List_4) glyph set.
