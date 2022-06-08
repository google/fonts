
“Italic” (`ital` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). It controls the [font](/glossary/font) file’s [italic](/glossary/italic) parameter, with italics either turned “off” or “on”, rather than gradually changing over a range.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 0.1 |

<figure>

![Two side-by-side type specimens of the word “jumpstart”, each shown with a variable axis represented beneath as an on/off switch. The first specimen, with the switch to the left, uses upright or regular forms. The second specimen, with the switch to the right, uses italic forms.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/EB+Garamond">EB Garamond</a></figcaption>

</figure>

Italic is a [type](/glossary/type) [style](/glossary/style) that’s almost always slanted and is designed to create emphasis in [text](/glossary/text_copy). Originally based on semi-cursive forms, italics are a direct contrast to the [upright](/glossary/regular_upright) style. Unlike [obliques](/glossary/oblique), which are slanted versions of the upright forms, italics have a different structure informed by cursive [handwriting](/glossary/handwriting)—with their own nuances.

Because most italic forms are slanted, for variable fonts, the italic axis and the [slant axis](/glossary/slant_axis) are very closely related. For detailed descriptions on how to use both, please see our [“Styling type on the web with variable fonts”](/lesson/styling_type_on_the_web_with_variable_fonts) article.

In line with the current CSS spec, the four-character code for this axis should be referenced in lowercase (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
