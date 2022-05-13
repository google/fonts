
“Wonky” (`WONK` in CSS)  is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts), and, like the [italic axis](/glossary/italic_axis), is binary. It’s used to control the substitution of “wonky” forms.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 1 |

In the [Fraunces](https://fonts.google.com/specimen/Fraunces) [typeface](/glossary/typeface), setting wonky to “on” (1) introduces the quirkier leaning of the lowercase n/m/h upright characters, or the bulbous flags of the lowercase b/d/h/k/l italic characters. In static fonts, wonky is also available as an [OpenType stylistic set](/glossary/stylistic_sets).

<figure>

![Two side-by-side type specimens of the two-word phrase “song key”, each shown with a variable axis represented beneath as an on/off switch. The first specimen, with the switch to the left, uses the default forms. The second specimen, with the switch to the right, modified the “s”, “n”, and “k” to use a more unusual, off-kilter design.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Fraunces">Fraunces</a></figcaption>

</figure>

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
