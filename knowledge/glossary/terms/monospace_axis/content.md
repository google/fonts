
“Monospace” (`MONO` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts), which adjusts the [glyphs](/glossary/glyph) from a proportional width to a fixed [width](/glossary/width). In [monospaced typefaces](/glossary/monospaced), or variable fonts set to a monospaced style, all glyphs take up the same amount of horizontal space.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 0 | Min: 0 | Max: 1 | Step: 0.01 |

<figure>

![Two side-by-side type specimens of the word “image”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows proportional letterforms. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, shows monospaced forms, where each glyph takes up the same amount of horizontal space.](images/thumbnail.svg)

</figure>

In line with the current CSS spec, all custom axes should be referenced in UPPERCASE (only the officially registered variable axes should appear in lowercase). Also, when using the Google Fonts API, the uppercase axes have to appear first in the URL.
