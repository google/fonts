Below are the most important changes from each release.

## 0.1.0 (2022-Feb-16)
### Release notes
  - Initial release of the `languages` python module.
  - Most of the code was copied from the `gftools` repository (https://github.com/googlefonts/gftools/) so that language/region/script data can be easily available to all our tools without having to also get the large dependency tree of `gftools`. The most immediate user of this module is `Font Bakery`, which needs to validate language support on font binaries being checked. (see https://github.com/googlefonts/fontbakery/issues/3605)
  - The second obvious user of this `languages` module will be `gftools` itself. I'll be sending a pull request soon.
  - Language/region/script definitions are still being gradualy updated on the `google/fonts` repo, on its **lang/** directory (https://github.com/google/fonts/tree/main/lang) and this `languages` module will try to be kept in sync.
  - Ideally at some point this module would become the main place to update these definitions, avoiding data duplication and guaranteeing uniformity across tools. But that will require coordination with the Google Fonts team, so I hope this module can serve, for now, as a prototype for such proposed integration.
