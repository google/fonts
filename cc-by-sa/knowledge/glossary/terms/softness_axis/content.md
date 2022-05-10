
“Softness” (`SOFT` in CSS)  is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). At the end of this axis, [letterforms](/glossary/letterform) become more soft and rounded.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | 0 | 100 | 0.1 |

In the [Fraunces](https://fonts.google.com/specimen/Fraunces) [typeface](/glossary/typeface), the softness axis can turn the sharp and [high-contrast](/glossary/contrast) [serifs](/glossary/serif) into bubble-like forms. At its softest, Fraunces starts to resemble the style of typefaces such as Souvenir or Bookman.

<figure>

![Two side-by-side type specimens of the word “cream”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, show sharper, high-contrast forms. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, is softer, with rounded edges.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Fraunces">Fraunces</a></figcaption>

</figure>

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
