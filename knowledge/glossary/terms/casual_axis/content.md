“Casual” (`CASL` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). Along this axis, letterforms adjust from a more serious style to a more casual style, in a manner determined by the type designer. This can mean adjustments in stroke curvature, contrast, and terminals to go from a sturdy, rational “linear” style to a friendly, energetic “casual” style.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 0 | Min: 0 | Max: 1 | Step: 0.01 |

<figure>

![Two side-by-side type specimens of the word “suited”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows straighter letterforms. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, exhibits curvier shapes.](images/thumbnail.svg)

</figure>

In line with the current CSS spec, all custom axes should be referenced in UPPERCASE (only the officially registered variable axes should appear in lowercase). Also, when using the Google Fonts API, the uppercase axes must appear first in the URL.
