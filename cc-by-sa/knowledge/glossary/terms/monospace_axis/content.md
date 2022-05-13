
“Monospace” (`MONO` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts), which adjusts the [glyphs](/glossary/glyph) from a proportional width to a fixed [width](/glossary/width). In [monospaced typefaces](/glossary/monospaced), or variable fonts set to a monospaced style, all glyphs take up the same amount of horizontal space.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 0.01 |

<figure>

![Two side-by-side type specimens of the word “image”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows proportional letterforms. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, shows monospaced forms, where each glyph takes up the same amount of horizontal space.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Recursive">Recursive</a></figcaption>

</figure>

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
