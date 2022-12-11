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
