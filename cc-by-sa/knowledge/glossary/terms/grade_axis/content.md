
“Grade” (`GRAD` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts) that can be used to alter [stroke](/glossary/stroke) thicknesses (or other forms) without affecting the [type](/glossary/type)’s overall [width](/glossary/width), inter-letter spacing, or [kerning](/glossary/kerning_kerning_pairs)—unlike altering [weight](/glossary/weight). This means there are no changes to line breaks or page layout.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | -1000 | 1000 | 1 |

Negative grade makes the style lighter, while positive grade makes it heavier.

The units are the same as in the [weight (`wght`) axis](/glossary/weight_axis) and it’s important to use the two axes together, systematically. For example, where accessibility guidelines recommend using a Medium (500) weight for a button label to obtain a certain contrast level, using a Regular (400) weight with grade +100 (if the grade axis goes up to 100) will produce the same level of contrast—but without any reflow.

<figure>

![Two side-by-side type specimens of the word “slightly”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a negative value on the axis, shows more contrast. The second specimen, with the slider most of the way to the right to represent a positive value on the axis, shows less contrast.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Roboto+Serif">Roboto Serif</a></figcaption>

</figure>

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
