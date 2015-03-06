subset.py - A script for subsetting a font, using FontForge
===========================================================

Version 1.01 - Released 2012-03-27

This directory contains a simple tool for subsetting fonts. It
currently supports creating subsets of Latin, Extended Latin,
Vietnamese, Greek, Extended Greek, Cyrillic and Extended Cyrillic
and can be extended to other scripts.

To use it, FontForge must be installed from source with the 
python extension enabled and installed:

    fontforge$ ./configure --enable-pyextension;
    fontforge$ sudo make install_py;

Usage
---------------

    subset.py [--options] input-font.ttf output-font.ttf

Options include:

  --subset=: Include glyphs of the named subsets. Several subsets 
    can be included, naming each with a '+'. Eg,

      --subset=cyrillic+latin

    The list of subsets is:

        latin
        latin-ext
        vietnamese
        greek
        greek-ext
        cyrillic
        cyrillic-ext

  --nmr: Include the 'nonmarkingreturn' glyph. Recommended.

  --null: Include the '.null' glyph. Recommended.

  --roundtrip: FontForge contains a bug where it incorrectly calculates
    the advanceWidthMax in the hhea table, and a workaround is to 
    "roundtrip" the font - to open and re-generate it. Recommended.

  --script: Run the subset as a separate .pe (FontForge's own 
    scripting language) file. Conceptually it should make no 
    difference, but it's a workaround for fontforge segfaults in 
    the Python interface. Recommended.

  --namelist: Generate a FontForge NameList file (.nam)
    Note that any unencoded (referenced) glyphs are not included 
    in the namelist.

  --new: create subset by creating new blank font and copying over
    relevant fields. This _definitely_ has the risk of missing things
    that are important. The default behaviour, when not used, is to
    delete unused glyphs from the font.

  --string=: Generate subset for just the specified string. Useful for
    creating a menu subset. Generally we use subset.pl from Font
    Optimizer for this, however.

  --simplify: Make font filesizes much smaller, by stripping out 
    hints, doing curve optimization, and rounding all points to 
    integers. The trade-off is a quality degradation on Windows 
    machines because of the lack of hinting.

  --strip_names: Strips most name tables from the font. Use with
    caution, as the result may not satisfy adequate attribution and
    licensing requirements.

Things to watch for
-------------------

The kerning tables (and very likely other OpenType tables) are
sometimes left with hanging references to deleted glyphs. Generally
that's fairly harmless, but it does increase file size and create
warnings.

Examples
-------------------

To use it to subset Latin, simply run:

    tools$ python subset.py --script Large-Font.ttf Latin-Font.ttf

To subset all the TTF fonts to Greek in the current directory, use
norma shell scripting: 

    $ for font in `ls -1 *ttf | cut -d. -f1`; 
      do python /path/to/subset.py --script $font.ttf $font.latin;
      done;

To subset all the TTF fonts in a 'FAMILYDIR' subdirectory of your
home directory, use this shell script:

    $ for family in ~/FAMILYDIR; do \
          for font in `ls -1 $family/*ttf | cut -d. -f1`; do \
              for subset in \
                  latin latin-ext \
                  greek greek-ext \
                  cyrillic cyrillic-ext \
                  vietnamese; do \
                  echo subset.py --null --nmr --roundtrip --script \
                      --subset=$subset $font.ttf $font.$subset; \
                  python tools/subset/subset.py --null --nmr \
                      --roundtrip --script --subset=$subset \
                      $font.ttf $font.$subset > $font.$subset.log; \
              done; \
          done; \
      done; \
      cd ~/FAMILYDIR/; \
