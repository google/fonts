
“Parametric Descender Depth” (`YTDE` in CSS) is a [parametric axis](/glossary/parametric_axis), found in some [variable fonts](/glossary/variable_fonts), for specifying and varying the depth of [lowercase](/glossary/uppercase_lowercase) [descenders](/glossary/ascenders_descenders), scaled as negative height.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| -250 | -1000 | 0 | 0 |

<figure>

![Three type specimens, each demonstrating the lowest setting, default setting, and highest setting of the YTDE axis, with an approximation of a variable slider shown beneath each. Blocks of color highlight the measurement affected by the axis.](images/thumbnail.svg)

</figure>

Its four-letter abbreviation, YTDE, is a reference to its logical name, “Y-Transparency for Descenders.” It may be used in conjunction with other axes controlling Y-transparencies (vertical alignment zones), especially the [Parametric Ascender Height axis (YTAS)](/glossary/ytas_axis).

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
