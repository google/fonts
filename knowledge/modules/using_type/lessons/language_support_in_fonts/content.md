
Each written language uses its own set of [characters](INSERT_URL). And if our UI uses multiple languages, then our [typography](INSERT_URL) should vary depending on the language.

[Scripts, or writing systems](INSERT_URL), are groups that contain characters used by one or more languages. For instance, although English, French, German, Norwegian, and Portuguese are distinct languages—with their own alphabets, conventions, and [diacritic](INSERT_URL) usage—they all use the [Latin script](INSERT_URL). Other writing systems include Greek (upon which Latin is based), Cyrillic, Arabic, Korean, Thai, the various scripts of Africa, the closely related Devanagari and Bengali, and the Han characters in use in various Asian languages, including Chinese and also Japanese.

<figure>

![A collage of different scripts.](images/language_support_in_fonts_1.svg)

</figure>

Word length can vary greatly across languages, even those that use the same [glyphs](INSERT_URL), such as English and German.

<figure>

![English text set alongside a translated German version, showing how German words are longer and therefore take up more vertical space.](images/thumbnail.svg)

</figure>

English is often shorter than other European languages. For instance, German has many compound words that are longer, requiring more lines or different line spacing settings.

## Alignment & direction
Some writing systems, such as Arabic and Hebrew, are displayed with characters appearing from right to left.

<figure>

![Left-to-right English text set alongside right-to-left Hebrew.](images/language_support_in_fonts_3.svg)

</figure>

UIs for languages that are read from right-to-left (RTL), such as Arabic and Hebrew, should be mirrored to ensure content is easy to understand. For more information, please read [Bidirectionality on Material Design](INSERT_URL).

Many writing systems might require different [line-height](INSERT_URL) and spacing adjustments. Line length, line spacing, and character spacing can vary within a script that is used for many languages.

## Height

Many writing systems require more vertical space than English, so our UI should provide sufficient vertical space to account for this. For instance, while Vietnamese is written with Latin, it has accents that add height to some letters, such as Ớ.

<figure>

![The word “New” set in different languages and scripts: English, Latin Vietnamese, Devanagari Marathi, Bengali, and Khmer.](images/language_support_in_fonts_4.svg)

</figure>

## Vertical typesetting

Vertical typesetting, though less commonly used, can display characters vertically instead of horizontally.
The typography of China, Japan, and Korea is typically monospaced, which means each letter occupies the same amount of space. It is often set left-to-right, top-to-bottom. It can also be set vertically: top-to-bottom and right-to-left.

More than one typeface may need to be used in the same UI to display multilingual content when each language uses a different writing system.

<figure>

![Type set in three columns: Korean, Chinese (Simplified), and Japanese. In each column, type is set left-to-right and top-to-bottom, then vertically, top-to-bottom and right-to-left.](images/language_support_in_fonts_5.svg)
<figcaption>Above: Type set left-to-right and top-to-bottom. Below: Type set vertically, top-to-bottom and right-to-left.</figcaption>

</figure>

For ease of internationalization, Google has categorized languages into three categories: | English-like |, tall, and dense.

**| English-like | typefaces:** The languages of Western, Central, and Eastern Europe and many parts of Africa are typically written in the Latin script. Vietnamese is a notable exception in that, while it uses a localized form of the Latin writing system, its accented glyphs can be much taller than those found in Western European languages. The Greek and Cyrillic writing systems are very similar to Latin in their vertical proportions.

**Tall typefaces:** These are the scripts that require extra line height to accommodate larger glyphs, including South and Southeast Asian and Middle-Eastern languages, like Arabic, Hindi, Telugu, Thai, and Vietnamese.

**Dense typefaces:** These are the scripts that require extra line height to accommodate larger glyphs, including Chinese, Japanese, and Korean.

## Noto

In Android, Noto fonts are the default typefaces for all languages not covered by the original Roboto. The set is designed to be visually harmonious across languages and scripts, with compatible heights and stroke thicknesses. The project covers over 150 scripts, each defined in Unicode.

For more about Noto, please visit [the Noto page on Google Fonts](INSERT_URL).

Noto Chinese, Japanese, and Korean (CJK) typefaces each have seven weights that match the original Roboto, with the same weight settings as English.


<figure>

![A small specimen of Chinese (Simplified) text and Japanese text.](images/language_support_in_fonts_6.svg)

</figure>

In CJK scripts, line height is slightly larger than Latin-based characters.

<figure>

![Two paragraphs, one at a large font size and the other small, set in Chinese (Simplified) text and Japanese text.](images/language_support_in_fonts_7.svg)

</figure>

## Tall script considerations

Noto supports tall scripts used in South and Southeast Asian and Middle Eastern languages, including Arabic, Hindi, and Thai. Try using the Regular weight, as the Medium weight is unavailable in Noto.

<figure>

![Thai text and Devanagari text.](images/language_support_in_fonts_8.svg)

</figure>

In Thai and Devanagari, the tall script line height is slightly larger than Latin-based characters.

<figure>

![Thai text and Devanagari text.](images/language_support_in_fonts_9.svg)

</figure>

## Language categories reference

|Code | Description | Category |
| --- | --- | --- |
| af | Afrikaans | English-like |
| am | Amharic | English-like |
| ar | Arabic (Modern Standard) | Tall |
| az | Azerbaijani | English-like |
| bg | Bulgarian | English-like |
| bn | Bengali | Tall |
| ca | Catalan | English-like |
| cs | Czech | English-like |
| cy | Welsh| English-like |
| da | Danish | English-like |
| de | German | English-like |
| el | Greek | English-like |
| en | English (US) | English-like |
| en-GB | English (UK) | English-like |
| es | Spanish (European) | English-like |
| es-419 | Spanish (Latin American) | English-like |
| et | Estonian | English-like |
| eu | Basque | English-like |
| fa | Persian | Tall |
| fi | Finnish | English-like |
| fil | Filipino | English-like |
| fr | French (European) | English-like |
| fr-CA | French (Canadian) | English-like |
| gl | Galician | English-like |
| gu | Gujarati | Tall |
| hi | Hindi | Tall |
| hr | Croatian | English-like |
| hu | Hungarian | English-like |
| hy | Armenian | English-like |
| id | Indonesian | English-like |
| is | Icelandic | English-like |
| it | Italian | English-like |
| iw | Hebrew | English-like |
| ja | Japanese | Dense
| ka | Georgian | English-like |
| kk | Kazakh | English-like |
| km | Khmer | Tall |
| kn | Kannada | Tall |
| ko | Korean | Dense
| ky | Kirghiz | English-like |
| lo | Lao | English-like |
| lt | Lithuanian | English-like |
| lv | Latvian | English-like |
| mk | Macedonian | English-like |
| ml | Malayalam | Tall |
| mn | Mongolian | English-like |
| mr | Marathi | Tall |
| ms | Malay | English-like |
| my | Burmese (Myanmar) | Tall |
| ne | Nepali | Tall |
| nl | Dutch | English-like |
| no | Norwegian (Bokmål) | English-like |
| pa | Punjabi | Tall |
| pl | Polish | English-like |
| pt | Portuguese (Brazilian) | English-like |
| pt-PT | Portuguese (European) | English-like |
| ro | Romanian | English-like |
| ru | Russian | English-like |
| si | Sinhala | Tall |
| sk | Slovak | English-like |
| sl | Slovenian | English-like |
| sq | Albanian | English-like |
| sr | Serbian (Cyrillic) | English-like |
| sr-Latn | Serbian (Latin) | English-like |
| sv | Swedish | English-like |
| sw | Swahili | English-like |
| ta | Tamil | Tall |
| te | Telugu | Tall |
| th | Thai | Tall |
| tr | Turkish | English-like |
| uk | Ukrainian | English-like |
| ur | Urdu | Tall |
| uz | Uzbek | English-like |
| vi | Vietnamese | Tall |
| zh-Hans | Chinese (Simplified) | Dense
| zh-Hant | Chinese (Traditional) | Dense |
| zu | Zulu | English-like |
