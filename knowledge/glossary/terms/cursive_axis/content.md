“Cursive” (`CRSV` in CSS)  is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts), and controls the substitution of cursive forms. “Off” (0) maintains upright letterforms such as a double-storey a and g, “auto” (0.5) allows for cursive substitution of cursive forms when combined with the [slant axis](/glossary/slant_axis), and “on” (1) asserts cursive forms even in upright text with a slant of 0.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 0.5 | Min: 0 | Max: 1 | Step: 0.1 |

<figure>

![Two side-by-side type specimens of the characters “gwayvz”, each shown with a variable axis represented beneath as an on/off switch. The second specimen, with the switch to the right, uses different forms: A single-storey “g” and “a”, and curvier lines for “w”, “y”, “v”, and “z”.](images/thumbnail.svg)

</figure>

In line with the current CSS spec, all custom axes should be referenced in UPPERCASE (only the officially registered variable axes should appear in lowercase). Also, when using the Google Fonts API, the uppercase axes have to appear first in the URL.
