This python module provides an API with data about languages/regions/scripts for use in the language-support categorization of the font families in the Google Fonts collection.

You can also directly access the raw **textproto** files on the `Lib/gflanguages/data` directory:
* [`languages`](https://github.com/googlefonts/lang/tree/main/Lib/gflanguages/data/languages)
* [`regions`](https://github.com/googlefonts/lang/tree/main/Lib/gflanguages/data/regions)
* [`scripts`](https://github.com/googlefonts/lang/tree/main/Lib/gflanguages/data/scripts)

Most of the code in this project was copied from the `gftools` repository (https://github.com/googlefonts/gftools/) so that language/region/script data can be easily available to all our tools without having to also get the large dependency tree of `gftools`.

The most immediate user of this module is the Google Fonts catalog (https://fonts.google.com/), which uses the language/region/script data to categorize the font families in the collection, and to provide information about language support on the family pages. See the (Google Fonts Catalog)[#google-fonts-catalog] section below to understand how the data is used in the catalog.

The second most obvious user of this module is [shaperglot](https://github.com/googlefonts/shaperglot), which needs to validate language support on font binaries being checked.

Language/region/script definitions and the `gflanguages` modules are used as a subtree in the `google/fonts` repo, on its **lang/** directory (https://github.com/google/fonts/tree/main/lang).

This module is the main place to update these definitions, avoiding data duplication and guaranteeing uniformity across tools.

To learn more about how *lang* metadata affects downstream, see [gf-guide/lang](https://googlefonts.github.io/gf-guide/lang).

## Data Types

The data in this repository is defined by the following protobuf messages.

### Region

| Field | Description |
| :--- | :--- |
| `id` | Region code, as defined by CLDR. |
| `name` | The name of the region. |
| `population` | The population of the region. |
| `region_group` | The region group(s) this region belongs to. |

### Script

| Field | Description |
| :--- | :--- |
| `id` | ISO 15924 Script code. (See https://en.wikipedia.org/wiki/ISO_15924#List_of_codes) |
| `name` | The name of the script. |
| `historical` | Whether the script is historical. |
| `fictional` | Whether the script is fictional. |
| `family` | The family the script belongs to. |
| `summary` | A summary of the script, to be used when displaying script information on the Noto web pages. |

### Language

| Field | Description |
| :--- | :--- |
| `id` | The ID of the language, in the format `${lang}(_${variant})?_${script}(_${region})?`. |
| `language` | The BCP 47 code for the language. |
| `script` | The script code. |
| `name` | The name of the language. |
| `preferred_name` | The preferred name of the language. |
| `autonym` | The name of the language as written in that language. |
| `population` | The population of speakers of the language. |
| `region` | The region(s) where the language is spoken. |
| `exemplar_chars` | Exemplar characters for the language. See [Exemplar Chars Rules](#exemplar-chars-rules) below. |
| `sample_text` | Sample text for the language. See [Sample Text Rules](#sample-text-rules) below. |
| `historical` | Whether the language is historical. |
| `source` | The source(s) of the language data. |
| `note` | A note about the language. |

## Exemplar chars rules

The exemplar characters for a language has been adopted from the Unicode CLDR project, but with some modifications to better suit the needs of Google Fonts.

| Field | Description |
| :--- | :--- |
| `base` | Main letters used in the language. |
| `auxiliary` | Additional characters for common foreign words, technical usage. |
| `marks` | Marks used in the language. (See below.) |
| `numerals` | The characters needed to display the common number formats: decimal, percent, and currency. |
| `punctuation` | Common punctuation. |
| `index` | Characters for the header of an index. |
| `not_required` | Base characters which can be ignored when determining language support. |

See the following notes from UTS#35:

> The basic exemplar character sets (main and auxiliary) contain the commonly used letters for a given modern form of a language, which can be for testing and for determining the appropriate repertoire of letters for charset conversion or collation. ("Letter" is interpreted broadly, as anything having the property Alphabetic in the [UAX44], which also includes syllabaries and ideographs.) It is not a complete set of letters used for a language, nor should it be considered to apply to multiple languages in a particular country. Punctuation and other symbols should not be included in the main and auxiliary sets. In particular, format characters like CGJ are not included.

> There are five sets altogether: main, auxiliary, punctuation, numbers, and index. The main set should contain the minimal set required for users of the language, while the auxiliary exemplar set is designed to encompass additional characters: those non-native or historical characters that would customarily occur in common publications, dictionaries, and so on. Major style guidelines are good references for the auxiliary set. So, for example, if Irish newspapers and magazines would commonly have Danish names using å, for example, then it would be appropriate to include å in the auxiliary exemplar characters; just not in the main exemplar set. 

> For a given language, there are a few factors that help for determining whether a character belongs in the auxiliary set, instead of the main set:

> * The character is not available on all normal keyboards.
> * It is acceptable to always use spellings that avoid that character.

> For example, the exemplar character set for en (English) is the set [a-z]. This set does not contain the accented letters that are sometimes seen in words like "résumé" or "naïve", because it is acceptable in common practice to spell those words without the accents. The exemplar character set for fr (French), on the other hand, must contain those characters: [a-z é è ù ç à â ê î ô û æ œ ë ï ÿ]. The main set typically includes those letters commonly "alphabet".

> The punctuation set consists of common punctuation characters that are used with the language (corresponding to main and auxiliary). Symbols may also be included where they are common in plain text, such as ©. It does not include characters with narrow technical usage, such as dictionary punctuation/symbols or copy-edit symbols. 

### Exemplar Syntax

The following section is copied from UTS#35, with some modifications to reflect our use of the `marks` list.

> In all of the exemplar characters, the list of characters is in the Unicode Set format, which normally allows boolean combinations of sets of letters and Unicode properties.

> Sequences of characters that act like a single letter in the language — especially in collation — are included within braces, such as [a-z á é í ó ú ö ü ő ű {cs} {dz} {dzs} {gy} ...]. The characters should be in normalized form (NFC). The characters should be in normalized form (NFC). Where combining marks are used generatively, and apply to a large number of base characters (such as in Indic scripts), the individual combining marks should be added to the `marks` list. Where they are used with only a few base characters, the specific combinations should be included. Wherever there is not a precomposed character (for example, single codepoint) for a given combination, that must be included within braces... When in doubt use braces, since it does no harm to include them around single code points: for example, [a-z {é} {è} {ù} ...].

> If the letter 'z' were only ever used in the combination 'tz', then we might have [a-y {tz}] in the main set.

### The marks list

There is currently, unfortunately, an [inconsistency](https://github.com/googlefonts/lang/issues/32) in the way that we are using the `marks` list. The intention is that `marks` should be any individual combining marks which are used generatively and apply to a range of base characters. If a mark is needed to form a distinct character in the language (for example, the dieresis accent in French is used to form ë and ï), it should *not* be added to `marks`, but the formed characters (ë and ï) should be included in the `base` list.

However, certain marks in scripts such as Arabic (such as fatha) or Devanagari (nukta) can be applied to a wide range of characters, or applied in multiple combinations, and it would be impractical to list all of the combinations. In these cases, the marks are included in the `marks` list, and the base characters are listed in the `base` list.

Where you find non-generative marks in the `marks` list, please consider whether they should be moved to the `base` list instead. If you are not sure, please open an issue on the [googlefonts/lang](https://github.com/googlefonts/lang/issues) repository.

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

## Google Fonts Catalog

A language is deemed supported (binary) by the Google Fonts Catalog if any of the following rules match:

* The family has an assigned primary language exactly equal to the identifier of the language.
* The family supports all `base` characters for a language with the `not_required` characters removed.
* The family supports all characters in all sample text for the language except puncutation and spaces.