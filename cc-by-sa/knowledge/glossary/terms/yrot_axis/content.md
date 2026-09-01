
“Rotation in Y” (`YROT` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts) that can be used to alter the letterforms so that they appear to rotate in the Y dimension, giving the impression that they can interact in a three-dimensional space. 

The [Google Fonts CSS v2 API](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | -180 | 180 | 1 |

<figure>

![An image showing three type specimens, each with an axis slider underneath. The specimen on the left shows the effects of the axis’ lowest value. The specimen in the middle shows the effects of the axis’ default value. The specimen on the right shows the effects of the axis’ highest value.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Tilt+Prism">Tilt Prisim</a></figcaption>
</figure>

Leaving the axis at its default value of 0 results in the character appearing face-on; manipulating it to its minimum value results in it appearing to turn upwards; manipulating it to its maximum value results in it appearing to turn downwards.

It may be used in conjunction with other axes controlling Y-transparencies (vertical alignment zones), especially the [Parametric Uppercase Height axis](/glossary/ytuc_axis) (`YTUC`) and [Parametric Descender Depth axis](/glossary/ytde_axis) (`YTDE`).