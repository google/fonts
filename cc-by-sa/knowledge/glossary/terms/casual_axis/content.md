“Casual” (`CASL` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). Along this axis, [letterforms](/glossary/letterform) adjust from a more serious style to a more casual style, in a manner determined by the [type designer](/glossary/type_designer). For example, adjusting [stroke](/glossary/stroke) curvature, [contrast](/glossary/contrast), and [terminals](/glossary/terminal) can turn a sturdy and linear (serious) style into a friendly and energetic (casual) style.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 0.01 |

<figure>

![Two side-by-side type specimens of the word “suited”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows straighter letterforms. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, exhibits curvier shapes.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Recursive">Recursive</a></figcaption>

</figure>

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
