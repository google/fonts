"Shadow Length" (`SHLN` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts) that controls the length of a shadow applied to the letterforms, allowing typographers to add depth and dimension to a typeface.

The [Google Fonts CSS v2 API](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 50 | 0 | 100 | 1 |

<figure>

![An image showing two type specimens, each with an axis slider underneath. The specimen on the left shows the effects of the axis' lowest value. The specimen on the right shows the effects of the axis' highest value.](images/thumbnail.svg)

<figcaption>A letterform from the <a href="https://github.com/EkType/Honk">Honk</a> typeface is shown twice, once with a minimum value of the Shadow Length axis applied (no shadow), and again with the maximum value applied (full shadow).</figcaption>
</figure>

Changes along the Shadow Length axis extend or retract the shadow cast by each letterform. At 0%, no shadow is visible, while at 100% the shadow reaches its maximum extent as defined by each family's design. The default value of 50% places the shadow at a midpoint between these extremes.

The number system of the axis is a percentage relative to each family's design: 0% produces no shadow, and 100% applies the maximum shadow length intended by the type designer.