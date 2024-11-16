
“Element Grid” (`ELGR` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some modular [variable fonts](/glossary/variable_fonts) where [letterforms](/glossary/letterform) are composed using multiple copies of the same element. In these fonts, the Element Grid axis can be used to control how many of the elements are used.

The [Google Fonts CSS v2 API](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 1 | 1 | 2 | 0.1 |

<figure>

![An image showing three type specimens, each with an axis slider underneath. The specimen on the left shows the effects of the axis’ lowest value. The specimen in the middle shows the effects of the axis’ middle value. The specimen on the right shows the effects of the axis’ highest value.](images/thumbnail.svg)

<figcaption> The letters ‘thx’ in the <a href="https://fonts.google.com/specimen/Handjet">Handjet</a> typeface are shown three times, with different Element Grid axis locations positioning the elements that construct the letterforms as one per grid unit, two elements overlapping, and two-by-two per grid unit.</figcaption> 
</figure>

As with the [Element Shape](/glossary/elsh_axis) axis, Element Grid alters the structure of the letterforms in a way that may change the minimum font size at which the typeface is legible. These two axes can be combined to produce unique patterns and pleasant visual effects.

The unit system of the axis is “per grid unit”, so each element for a value of 1 is replaced by 4 elements in a two-by-two pattern for a value of 2.

The axis tag starts with `EL`, which is an abbreviation of ‘Element’. This prefix is used for the group of axes (ELSH, ELGR, ELXP) that are related to modular typefaces — those with glyphs composed of elements.

This axis was first introduced in the [Handjet](https://fonts.google.com/specimen/Handjet) typeface.