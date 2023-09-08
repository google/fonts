### Check the [releases notes](https://github.com/googlefonts/lang/releases), they are up to date and complete. 

## 0.5.0 (2023-Jun-22)
Add Vithkuqi script/language by @simoncozens in #88

## 0.4.9 (2023-Jun-08)
Replace Sanskrit Gunjala Gondi transliteration with new sample by @simoncozens in https://github.com/googlefonts/lang/pull/85

## 0.4.8 (2023-Jun-02)
* Test languages exemplars canonical duplicates by @moyogo in https://github.com/googlefonts/lang/pull/41
* fixup test_canonical_duplicates by @moyogo in https://github.com/googlefonts/lang/pull/75
* Remove U+030D U+030E from Thai marks by @simoncozens in https://github.com/googlefonts/lang/pull/76
* grc_Cprt: add source for samples by @moyogo in https://github.com/googlefonts/lang/pull/79
* Add Makassarese in Old Makasar script by @simoncozens in https://github.com/googlefonts/lang/pull/74
* West Frisian [fy]: remove {ij} and {íj́} from base by @moyogo in https://github.com/googlefonts/lang/pull/78

## 0.4.7 (2023-Apr-17)
- #70 Add Nandinagari

## 0.4.6 (2023-Mar-24)
- #52 Addition of exemplar character sets for Latin-based African Lang
uages
- #53 Adding caps letters to Latin-based African languages that have gflang profiles
- #67 Add kana sample text

## 0.4.5 (2023-Mars-22)
- #65 Add Nag Mundari script

## 0.4.4 (2023-Feb-24)
- #51 Add source and note fields
- #59 Updated Thai specimen
- #60 Fixed CI

## 0.4.3 (2022-Nov-14)
- Add missing script to Chorasmian #47
- Pin protobuf>=3.7.0, <4 like fontbakery

## 0.4.2 (2022-Nov-09)
- Add new script definitions and language samples for the Tangsa and Toto scripts #29 #25
- Fixes to broken circles in sample texts for: 
    -  NP Hmong #34
    -  Limbu #40 #36
    -  Gonjala Gondi #37
    -  Chakma #43
    -  Myanmar (Pwo + S'gaw Karen) #38
    -  Zanabazar Square #39 .
- Remove duplicate characters from languages exemplar_chars #18

## 0.4.1 (2022-Oct-20)
- "CN" region added to Chinese languages #13
- Vietnamese specimen sample text fixes #14
- replace U+2010 HYPHEN with U+002D Hyphen-Minus in sample texts #15
- U+0323 instead of U+329 in yo_Latn #16
- Update README.md, used in gftools and google/fonts #17
- Pin protobuf to 3.19.4 #19
- Corrected a breve dot below with proper codepoint. #21
- Fix Mundari sample text #22
- Add sample_text to bax_Bamu.textproto #27
- actions: add publish-release #28

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
