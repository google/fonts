“Bounce” (`BNCE` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts) that can be used to reposition letterforms vertically, away from the baseline, creating a more handwritten or organic style.

The [Google Fonts CSS v2 API](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | -100 | 100 | 1 |

<figure>

![The letters “sha” shown three times, with the central instance showing a default baseline position and the axis range shown below it at a default value of 50%, and then to the left with “s” below the baseline and “a” above, with the axis value shown decreased to 0%, and then to the right with “s” above the baseline and “a” below, with the axis value shown increased to 95%.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://fonts.google.com/specimen/Shantell+Sans">Shantell Sans</a></figcaption>
</figure>

How the letters bounce will relate to each typeface's needs or concept. For example, in [Shantell Sans](https://fonts.google.com/specimen/Shantell+Sans), adjusting the axis to its minimum value shifts the “s” character down, but the “a” character up; the “h” character moves only slightly in each direction. This semi-unpredictable behaviour results in the type appearing more like handwriting, and the effect can be further exaggerated by manipulating other axes (in the case of Shantell Sans, [Informality](/glossary/infm_axis) (`INFM`) and [Spacing](/glossary/spac_axis) (`SPAC`) in tandem. 
