“Fill” (`FILL` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts) that can be used to turn transparent forms opaque. (Sometimes the corresponding interior opaque forms become transparent to maintain contrasting shapes.) Transitions often occur from the center, a side, or a corner, but can go in any direction. This can be useful in animation or interaction to convey a state transition. The numbers indicate proportion filled, from 0 (no treatment) to 1 (completely filled).

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 0.01 |

This is currently implemented in Google’s Material icons:

<figure>

![Two side-by-side icon specimens, each shown with a variable axis represented beneath as an on/off switch. The first specimen, with the switch to the left, shows the icon shapes outlined. The second specimen, with the switch to the right, shows the icon shapes filled with solid color.](images/thumbnail.svg)

</figure>

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
