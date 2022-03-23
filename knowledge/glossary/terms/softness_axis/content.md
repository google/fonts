
“Softness” (`SOFT` in CSS)  is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). At the end of this axis, [letterforms](/glossary/letterform) become more soft and rounded.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 0 | Min: 0 | Max: 100 | Step: 0.01 |

In the [Fraunces](https://fonts.google.com/specimen/Fraunces) [typeface](/glossary/typeface), the softness axis can turn the sharpness and [high-contrast](/glossary/contrast) [serifs](/glossary/serif) into bubble-like forms, and at its softest, the typeface starts to resemble the style of typefaces such as Souvenir or Bookman.

<figure>

![Two side-by-side type specimens of the word “cream”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, show sharper, high-contrast forms. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, is softer, with rounded edges.](images/thumbnail.svg)

</figure>

In line with the current CSS spec, all custom axes should be referenced in UPPERCASE (only the officially registered variable axes should appear in lowercase). Also, when using the Google Fonts API, the uppercase axes have to appear first in the URL.
