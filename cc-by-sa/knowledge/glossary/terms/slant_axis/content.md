
Slant (`slnt` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). It controls the [font](/glossary/font) file’s [slant](/glossary/slant_axis) parameter for [oblique](/glossary/oblique) [styles](/glossary/style).

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | -90 | 90 | 1 |

<figure>

![Two side-by-side type specimens of the word phrase “lean-to”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the right to represent a higher value on the axis, shows upright forms. The second specimen, with the slider more to the left to represent a low-to-mid value on the axis, shows more slanted forms.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Recursive">Recursive</a></figcaption>

</figure>

Oblique [characters](/glossary/character) follow the structure of the [upright](/glossary/regular_upright) styles, while [italics](/glossary/italic) have a different structure, typically informed by cursive [writing](/glossary/handwriting). Obliques are not necessarily merely [digitally slanted](https://fonts.google.com/knowledge/introducing_type/introducing_weights_styles#avoiding-fake-weights-and-styles)—optical corrections are often made to avoid distortions and an incorrect distribution of weight. Generally, obliques are less common than italics.

[//]: # (TO-DO: Turn that article link above into a regular Markdown format URL once there’s support for heading IDs in Markdown URLs.)

For variable fonts, the [italic axis](/glossary/italic_axis) and the slant axis are very closely related. For detailed descriptions on how to use both, please see our [“Styling type on the web with variable fonts”](/lesson/styling_type_on_the_web_with_variable_fonts) article.

In line with the current CSS spec, the four-character code for this axis should be referenced in lowercase (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
