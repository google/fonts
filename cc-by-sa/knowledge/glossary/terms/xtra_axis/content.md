
“Parametric Counter Width” (`XTRA` in CSS) is a [parametric axis](/glossary/parametric_axis), found in some [variable fonts](/glossary/variable_fonts), that varies counter widths in the X dimension. It can be used for fine-tuning [justification](/glossary/alignment_justification) (as demonstrated in [TypeNetwork’s example](https://variablefonts.typenetwork.com/topics/spacing/variations)) by affecting the number of [characters](/glossary/character) per line.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 400 | -1000 | 2000 | 0 |

<figure>

![Three type specimens, each demonstrating the lowest setting, default setting, and highest setting of the XTRA axis, with an approximation of a variable slider shown beneath each. Blocks of color highlight the measurement affected by the axis.](images/thumbnail.svg)

</figure>

Its four-letter abbreviation, XTRA, is a reference to its logical name, “X-Transparent,” which describes how it alters a font’s transparent spaces (also known as negative shapes) inside and around all [glyphs](/glossary/glyph) along the X dimension. (In pre-digital type, many of the spaces that this axis controls were known as counters.) For example, it can widen or narrow the space inside an “H” between the two stems—without changing the stroke weights of the “H,” or any vertical alignments or spaces. This isolated change is what makes it a parametric axis and different to the [Width](/glossary/width) axis.

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
