Below are the most important changes from each release.

## 0.4.0 (2022-Mar-09)
### Release notes
  - Use default `DATA_DIR` if user passes `base_dir=None`, to make it easier to use the API and to avoid problems like this: https://github.com/googlefonts/gftools/pull/511#issuecomment-1060398562


## 0.3.0 (2022-Mar-04)
### Release notes
  - Simplify API by removing the `lang_support` module. Now one does `from gflanguages import LoadLanguages` instead of `from gflanguages.lang_support import LoadLanguages` (issue #6)
  - Also, all `Load_*` methods now accept base_dir as optional argument. (motivated by: https://github.com/googlefonts/gftools/pull/511#issuecomment-1059081028)


## 0.2.0 (2022-Feb-18)
### Release notes
  - dropped hyperglot dependency due to licensing. See below.
  - Removed SupportedLanguages method as it relies on hyperglot, which is under the GPLv3, to keep gftranslate under Apache 2.0
  - The method is still available as a separate code-snippet (not part of gflanguages itself), and any program using that snippet will need to comply with the GPLv3.
  - For more details, see: https://github.com/googlefonts/fontbakery/pull/3617#issuecomment-1044898812


## 0.1.1 (2022-Feb-18)
### Bugfix
  - updated and simplified the textproto definition to workaround this kind of problem when using the module on projects that also import `fonts_public_pb2.py`: https://github.com/protocolbuffers/protobuf/issues/3002


## 0.1.0 (2022-Feb-16)
### Release notes
  - Initial release of the `gflanguages` python module.
  - Most of the code was copied from the `gftools` repository (https://github.com/googlefonts/gftools/) so that language/region/script data can be easily available to all our tools without having to also get the large dependency tree of `gftools`. The most immediate user of this module is `Font Bakery`, which needs to validate language support on font binaries being checked. (see https://github.com/googlefonts/fontbakery/issues/3605)
  - The second obvious user of this `gflanguages` module will be `gftools` itself. I'll be sending a pull request soon.
  - Language/region/script definitions are still being gradualy updated on the `google/fonts` repo, on its **lang/** directory (https://github.com/google/fonts/tree/main/lang) and this `gflanguages` module will try to be kept in sync.
  - Ideally at some point this module would become the main place to update these definitions, avoiding data duplication and guaranteeing uniformity across tools. But that will require coordination with the Google Fonts team, so I hope this module can serve, for now, as a prototype for such proposed integration.
