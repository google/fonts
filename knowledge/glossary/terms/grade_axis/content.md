
“Grade” (`GRAD` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). Changing [grade](/glossary/grade) allows us to finesse the style from lighter to heavier in typographic [color](/glossary/color) by varying [stroke](/glossary/stroke) thicknesses (or other forms) without any changes to the [type](/glossary/type)’s overall [width](width), inter-letter spacing, or [kerning](/glossary/kerning)—unlike altering [weight](/glossary/weight). This means there are no changes to line breaks or page layout.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 0 | Min: -1000 | Max: 1000 | Step: 1 |

Negative grade makes the style lighter, while positive grade makes it heavier. The units are the same as in the weight (`wght`) axis.

<figure>

![Two side-by-side type specimens of the word INSERT, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, INSERT. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, INSERT.](](images/thumbnail.svg)

</figure>

In line with the current CSS spec, all custom axes should be referenced in UPPERCASE (only the officially registered variable axes should appear in lowercase). Also, when using the Google Fonts API, the uppercase axes have to appear first in the URL.
