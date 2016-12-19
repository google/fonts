
Google Fonts 2016 Glyph Sets
============================

Three levels of glyph sets were developed in June 2016 as a new baseline standard for fonts in the Google Fonts library. 
Exising fonts in the library can be upgraded to these as part of a drive towards new quality standards. 
All new fonts submitted to the library must now support the Plus level as a minumum requirement.

Three sets are available in this directory: **Plus, Pro and Expert.**

#### Glyphs App Tip

Inside [**filter lists**](filter lists) are text files with a list of glyphs for each set. 
Open Glyphs and in the left bottom sidebar, create a new list filter, and paste the contents of these TXT files to check if your fonts supports these characters. 
A ✓ will indicate you are all set. 
Otherwise **ctrl + click** on the numbers to generate missing glyphs. 

> N.B. If you get an error while creating new glyphs, select all glyphs in your font, from the top menu choose Glyph -> Update Glyph Info. Try again. If updating Glyph Info didn't work make sure [ ] Use custom naming is unckecked in Font Info > Other Settings. 

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for more details.

![Glyphs list filter](tutorials/img/list-filter.png)
![Glyphs list filter](tutorials/img/list-filter-1.png) 

Latin
---------------------------

Structure and Hierarchy of Glyph Sets for Latin:

1. **Core** A Basic Latin set for Western Europe
2. **Plus** For all fonts in the library, an Extended Latin with wide language support (Central and Eastern European languages and Vietnamese)
3. **Pro** For casual and headline fonts that need a little more typographic sophistication, an extra 171 glyphs
4. **Expert** For text and workhorse typefaces that must supply everything typographers need, such as small caps, an additional 300 glyphs

| Glyph Set | Drawn | Composite | Either/Or | From Core | From Core contingency |
|:----------|------:|----------:|----------:|----------:|----------------------:|
| Core      |   150 |        70 |           |           |                       |
| Plus      |   215 |       360 |        19 |        65 |                    19 |
| Pro       |    26 |       116 |         4 |        23 |                    23 |
| Expert    |    62 |       207 |         4 |       153 |                    27 |
| Total     |   303 |       683 |        27 |           |                       |

### GF Latin Plus (568 glyphs total + 25 optional)

  - Western & Central European 
  - Vietnamese  
  - Currencies (₡ ₣ ₤ ₦ ₧ ₩ ₫ ₭ ₱ ₲ ₵ ₹ ₺ ₼ ₽)
  - Alternate Numerals: Proportonal Lining

Includes characters from the following unicode ranges: 

  - Latin-1
  - Latin Extended A 
  - Latin Extended B
  - Latin Extended Additional
  - Latin-1 Supplement
  
Optional additions:

- Uppercase Accents, 25
- Slashed zero (zero.zero)

#### Glyphs App Tip

To quickly create base glyphs for lining figures, press *Cmd + G*, and paste in this code:

| Type           | Paste this code | 
|----------------|-----------------| 
| Lining Figures | `zero=zero.lf one=one.lf two=two.lf three=three.lf four=four.lf five=five.lf six=six.lf seven=seven.lf eight=eight.lf nine=nine.lf` |

See [tutorials/GLYPHS-TIPS.md](tutorials/GLYPHS-TIPS.md) for more details

#### Ligated Dutch IJ

In case your IJ diagraph is really ligated, or has a special form (like shortened I) you will need to add these glyphs: `I_J.loclNLD i_j.loclNLD Iacute_J.loclNLD iacute_j.loclNLD`. Glyphs (versions 2.3.1 or later) will automate the OT code. If your font includes small caps, make sure to add `.sc` glyphs too.

Read more about this in the [GlyphsApp Ligated Dutch IJ Tutorial](https://www.glyphsapp.com/tutorials/localize-your-font-accented-dutch-ij)

**Language support for the following Latin-based languages:** Abenaki, Afaan Oromo, Afar, Afrikaans, Albanian, Alsatian, Amis, Anuta, Aragonese, Aranese, Aromanian, Arrernte, Arvanitic (Latin), Asturian, Atayal, Aymara, Azerbaijani, Bashkir (Latin), Basque, Belarusian (Latin), Bemba, Bikol, Bislama, Bosnian, Breton, Cape Verdean Creole, Catalan, Cebuano, Chamorro, Chavacano, Chichewa, Chickasaw, Cimbrian, Cofán, Cornish, Corsican, Creek, Crimean Tatar (Latin), Croatian, Czech, Danish, Dawan, Delaware, Dholuo, Drehu, Dutch, English, Esperanto, Estonian, Faroese, Fijian, Filipino, Finnish, Folkspraak, French, Frisian, Friulian, Gagauz (Latin), Galician, Ganda, Genoese, German, Gikuyu, Gooniyandi, Greenlandic (Kalaallisut), Guadeloupean Creole, Gwich’in, Haitian Creole, Hän, Hawaiian, Hiligaynon, Hopi, Hotcąk (Latin), Hungarian, Icelandic, Ido, Igbo, Ilocano, Indonesian, Interglossa, Interlingua, Irish, Istro-Romanian, Italian, Jamaican, Javanese (Latin), Jèrriais, Kaingang, Kala Lagaw Ya, Kapampangan (Latin), Kaqchikel, Karakalpak (Latin), Karelian (Latin), Kashubian, Kikongo, Kinyarwanda, Kiribati, Kirundi, Klingon, Kurdish (Latin), Ladin, Latin, Latino sine Flexione, Latvian, Lithuanian, Lojban, Lombard, Low Saxon, Luxembourgish, Maasai, Makhuwa, Malay, Maltese, Manx, Māori, Marquesan, Megleno-Romanian, Meriam Mir, Mirandese, Mohawk, Moldovan, Montagnais, Montenegrin, Murrinh-Patha, Nagamese Creole, Nahuatl, Ndebele, Neapolitan, Ngiyambaa, Niuean, Noongar, Norwegian, Novial, Occidental, Occitan, Old Icelandic, Old Norse, Onĕipŏt, Oshiwambo, Ossetian (Latin), Palauan, Papiamento, Piedmontese, Polish, Portuguese, Potawatomi, Q’eqchi’, Quechua, Rarotongan, Romanian, Romansh, Rotokas, Sami (Inari Sami), Sami (Lule Sami), Sami (Northern Sami), Sami (Southern Sami), Samoan, Sango, Saramaccan, Sardinian, Scottish Gaelic, Serbian (Latin), Seri, Seychellois Creole, Shawnee, Shona, Sicilian, Silesian, Slovak, Slovenian, Slovio (Latin), Somali, Sorbian (Lower Sorbian), Sorbian (Upper Sorbian), Sotho (Northern), Sotho (Southern), Spanish, Sranan, Sundanese (Latin), Swahili, Swazi, Swedish, Tagalog, Tahitian, Tetum, Tok Pisin, Tokelauan, Tongan, Tshiluba, Tsonga, Tswana, Tumbuka, Turkish, Turkmen (Latin), Tuvaluan, Tzotzil, Uzbek (Latin), Venetian, Vepsian, Volapük, Võro, Wallisian, Walloon, Waray-Waray, Warlpiri, Wayuu, Welsh, Wik-Mungkan, Wiradjuri, Wolof, Xavante, Xhosa, Yapese, Yindjibarndi, Zapotec, Zarma, Zazaki, Zulu, Zuni

### GF Latin Pro (+145 for 713 glyphs total + 37 optional .case, .sinf, and .sups)

- Math symbols and Units of Measure (∆ Ω π ℓ ℮ ∞ ∂ ∫ √ ∑ ∏ ◊ ∅)
- Latin General Use Extensions (U+1E08 to U+1EC9)
- Superiors and Inferiors (⁰ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉)
- Scientific Inferiors as *".subs"* (₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉)
- Spacing Modifier Letters (ʻ ʼ ʾ ʿ ˈ ˊ ˋ ˌ)
- Typographic Spaces (figure, punctuation, thin, hair, zero-width)
- Additional General Punctuation (‐ ‒ ― ′ ″)
- Alternate Punctuation Glyphs for Capitals
- Numerators and Denominators

Instructions for OT code in the GF Latin Pro set:

| feature name | created  | sub one by ... |
|--------------|----------|----------------|
| `.sups`      | auto     | `onesuperior`  |
| `.subs`      | auto     | `one.subs`     |
| `.sinf`      | manually | `one.subs`     |

#### Optional glyphs in the GF Latin Pro set include:

- Unencoded Scientific Inferiors `.sinf`
- Unencoded Superscript Figures `.sups` 
- Case Punctuation `.case`

Instructions for OT code in the optional set:

| feature name | created  | sub one by ... |
|--------------|----------|----------------|
| `.sups`      | manually | `one.sups`     |
| `.subs`      | auto     | `one.subs`     |
| `.sinf`      | manually | `one.sinf`     |


### GF Latin Expert (+271 for 984 total)

- Additional Unicode Fractions (⅓ ⅔ ⅛ ⅜ ⅝ ⅞)
- Arrows (← ↑ → ↓)
- Geometric Shapes (■ □ ▲ △ ▶ ▷ ▼ ▽ ◀ ◁ ◆ ◇)
- Small Capitals
- Discretionary Ligatures (T_h c_t c_h s_t)

* * * 

Cyrillic
-------------------

Structure and Hierarchy of Glyph Sets for Cyrillic:

1. **Core** is the existing default set, a Basic Cyrillic
3. **Plus** includes added language coverage for Slavic, Non-Slavic, and Uralic languages
3. **Pro** for Headline typefaces, with language support for historic Cyrillic and some Non-Slavic languages
4. **Expert** for text and workhorse typefaces, includes Small Caps

### GF Cyrillic Core

**Supports the following Cyrillic languages:** Balkar, Belarusian (Cyrillic), Bosnian (Cyrillic), Bulgarian, Croatian (Cyrillic), Erzya, Karachay, Kumyk, Macedonian, Moksha, Montenigrin, Nanai, Nogai, Russian, Rusyn, Serbian (Cyrillic), Ukrainian.

### GF Cyrillic Plus (184 + 40 localized variants for 228 total)

**Supports the following Cyrillic languages:** Adyghe, Agul, Altay, Avar, Azerbaijani (Cyrillic), Balkar, Bashkir, Belarusian (Cyrillic), Bosnian (Cyrillic), Bulgarian, Buryat, Chechen, Chuvash, Crimean Tatar (Cyrillic), Croatian (Cyrillic), Dargin, Dungan, Erzya, Gagauz (Cyrillic), Ingush, Kabardian, Kalmyk, Karachay, Karakalpak, Kazakh, Khakas (Cyrillic), Khinalugh, Komi, Kumyk, Kurdish (Cyrillic), Kyrgyz (Cyrillic), Lak, Lezgian, Macedonian, Mari (Hill and Meadow), Moksha, Moldovan (Cyrillic), Mongolian (Cyrillic), Montenigrin, Nanai, Nogai, Ossetian, Russian, Rusyn, Rutul, Sakha/Yakut, Serbian (Cyrillic), Tabasaran, Tajik, Talysh (Cyrillic), Tat, Tatar, Turkmen, Tuvan, Udi, Udmurt, Ukrainian, Uyghur (Cyrillic), Uzbek (Cyrillic), Yukaghir (Northern and Southern).

Includes currencies: ₮, ₴, ₸.

The ruble sign (₽ U+20BD) is not included, since it is already present in the Latin Plus set.

### GF Cyrillic Pro (+58 glyphs for 286 glyphs total)

Additional characters in this set provide support for the following languages: Abkhaz, Chukchi, Enets, Itelmen, Nenets, Orok, Kanty, Kildin Sami, Tati

**Full list of supported Cyrillic languages:** Abkhaz, Agul, Altay Enets, Azerbaijani (Cyrillic), Balkar Adyghe, Bashkir, Belarusian (Cyrillic), Bosnian (Cyrillic), Bulgarian Avar, Chukchi, Croatian (Cyrillic), Dungan, Erzya Buryat, Gagauz (Cyrillic), Ingush, Itelmen, Kabardian, Kalmyk, Kanty, Karachay Chechen, Karakalpak, Kazakh, Khakas (Cyrillic), Khinalugh, Kildin, Komi, Kumyk Chuvash, Kurdish (Cyrillic), Kyrgyz (Cyrillic), Lak, Lezgian, Macedonian Crimean Tatar (Cyrillic), Mari (Hill and Meadow), Moksha Dargin, Moldovan (Cyrillic), Mongolian (Cyrillic), Montenigrin, Nanai, Nenets, Nogai, Orok, Ossetian, Russian, Rusyn, Rutul, Sakha/Yakut, Sami, Serbian (Cyrillic), Tabasaran, Tajik, Talysh (Cyrillic), Tat, Tatar, Tati, Turkmen, Tuvan, Udi, Udmurt, Ukrainian, Uyghur (Cyrillic), Uzbek (Cyrillic), Yukaghir (Northern and Southern).

### GF Cyrillic Historical (Optional 37 glyphs )

Provides support for Pre-Petrine Old Church Slavonic Texts.

### Recommended Additions

See [RECOMMENDED.md](RECOMMENDED.md)

### Acknowledgements:

GF Glyph Sets defined by Alexei Vanyashin (@alexeiva) and Kalapi Gajjar (@kalapi) from 2016-06-27 to 2016-10-11, with input from
Dave Crossland, 
Frank Grießhammer, 
Georg Seifert, 
Gunnar Vilhjálmsson, 
Jacques Le Bailly, 
Nhung Nguyen (Vietnamese lists), 
Pablo Impallari (Impallari Encoding), 
Rainer Erich Scheichelbauer (@mekkablue), 
Thomas Jockin,
Thomas Phinney 
(Adobe Cyrillic lists), and
Underware (Latin Plus Encoding)
