
“Parametric Thin Strokes” (`YOPQ` in CSS) is a [parametric axis](/glossary/parametric_axis), found in some [variable fonts](/glossary/variable_fonts), for specifying and varying thin [stroke](/glossary/stroke) weights, such as bars and hairlines.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 116 | -1000 | 2000 | 0 |

<figure>

![Three type specimens, each demonstrating the lowest setting, default setting, and highest setting of the YOPQ axis, with an approximation of a variable slider shown beneath each. Blocks of color highlight the measurement affected by the axis.](images/thumbnail.svg)

</figure>

Its four-letter abbreviation, XOPQ, is a reference to its logical name, “X Opaque”, which describes how it alters the opaque stroke forms of glyphs typically in the X dimension, such as the weight of the thicker vertical stems in an “H”. However, often the thick strokes are not perfectly aligned to the cartesian grid, such as in the letter “X” or “O” when there is an angle of stress. It’s logically related to both the other opaque axis, [Parametric Thin Stroke (YOPQ)](/glossary/yopq_axis), and the other X dimension axis, [Parametric Counter Width (XTRA)](/glossary/xtra_axis).

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the uppercase axes have to appear first in the URL.
