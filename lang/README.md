This python module provides an API with data about languages/regions/scripts for use in the language-support categorization of the font families in the Google Fonts collection.

You can also directly access the raw **textproto** files on the `Lib/gflanguages/data` directory:
* [`languages`](https://github.com/googlefonts/lang/tree/main/Lib/gflanguages/data/languages)
* [`regions`](https://github.com/googlefonts/lang/tree/main/Lib/gflanguages/data/regions)
* [`scripts`](https://github.com/googlefonts/lang/tree/main/Lib/gflanguages/data/scripts)

Most of the code in this project was copied from the `gftools` repository (https://github.com/googlefonts/gftools/) so that language/region/script data can be easily available to all our tools without having to also get the large dependency tree of `gftools`. The most immediate user of this module is `Font Bakery`, which needs to validate language support on font binaries being checked. (see https://github.com/googlefonts/fontbakery/issues/3605)

The second obvious user of this `gflanguages` module is `gftools` itself.

Language/region/script definitions and the `gflanguages` modules are used as a subtree in the `google/fonts` repo, on its **lang/** directory (https://github.com/google/fonts/tree/main/lang).

This module is the main place to update these definitions, avoiding data duplication and guaranteeing uniformity across tools.

To learn more about how *lang* metadata affects downstream, see [gf-guide/lang](https://googlefonts.github.io/gf-guide/lang).

## Sample text rules

If there is a `sample_text` field for a language, it should contain all of the following fields:

* `masthead_full`: show off four glyphs
* `masthead_partial`: show off two glyphs
* `styles`: a phrase of 40-60 characters
* `tester`: a phrase of 60-90 characters
* `poster_sm`: a word or phrase of 10-17 characters
* `poster_md`: a word or phrase of 6-12 characters
* `poster_lg`: a word or phrase of 3-8 characters
* `specimen_48`: a sentence of 50-80 characters
* `specimen_36`: a paragraph of 100-120 characters
* `specimen_32`: a paragraph of 140-180 characters
* `specimen_21`: one or more paragraphs totalling 300-500 characters
* `specimen_16`: one or more paragraphs totalling 550-750 characters

Generally the sample text should be taken from the UN Declaration of Human Rights; if using Eric Muller's XML translations, `snippets/lang_sample_text.py` will convert the XML into textproto.

If the UDHR is not available in the language, the sample text should be a "neutral" text (not political or religious) - folk tales are generally good sources. (We recognise that for some liturgical languages, religious texts may be the only extant samples.) In these cases, please add a `note:` field with the source of the sample text.
