
“Bleed” (BLED in CSS) is an axis found in some variable fonts that can be used to adjust the text’s overall darkness or typographic color by altering its glyphs’ shapes such as strokes (or other forms). Because it’s only the individual shapes that are changed, there are no changes to the type’s overall width, letter spacing, or kerning. Therefore, manipulating this axis will not result in altered line breaks or page layout changes.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | 0 | 100 | 1 |

<figure>

![An image showing two type specimens, each with an axis slider underneath. The specimen on the left shows the effects of the axis’ lowest value. The specimen on the right shows the effects of the axis’ highest value.](images/thumbnail.svg)

</figure>

<figcaption>In the typeface Workbench, note how moving the Bleed axis towards its maximum value expands the width of each individual scanline without altering the actual glyph width or spacing of the letters.</figcaption>

Negative values make the text appear lighter, while positive values make it darker, similarly to the effects of ink bleed or dot gain on paper.