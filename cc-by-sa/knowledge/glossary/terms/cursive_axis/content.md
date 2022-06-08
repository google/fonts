“Cursive” (`CRSV` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts) that controls the substitution of cursive forms. “Off” (0) maintains upright [letterforms](/glossary/letterform) such as the double-storey "a" and "g," “auto” (0.5) allows for cursive substitution of cursive forms when combined with the [slant axis](/glossary/slant_axis), and “on” (1) asserts cursive forms even in [upright](/glossary/regular_upright) text with a slant of 0.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0.5 | 0 | 1 | 0.1 |

<figure>

![Two side-by-side type specimens of the characters “gwayvz”, each shown with a variable axis represented beneath as an on/off switch. The second specimen, with the switch to the right, uses different forms: A single-storey “g” and “a”, and curvier lines for “w”, “y”, “v”, and “z”.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Recursive">Recursive</a></figcaption>

</figure>

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
