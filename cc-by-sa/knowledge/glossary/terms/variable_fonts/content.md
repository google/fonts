
Variable [fonts](/glossary/font)—or, more specifically, [OpenType](/glossary/open_type) Font Variations—are a relatively new font [format](/glossary/font_format) that allow one font file to contain multiple stylistic variations. [Weight](/glossary/weight), [width](/glossary/width), [style](/glossary/style), [optical size](/glossary/optical_sizes), etc. can then be manipulated by the end user (i.e., designer) and thus avoid the strict delineations of “traditional” fonts.

<figure>

![Three different examples of “Aa”, each with a their variable axes adjusted. The first has a light weight and body-like optical size; the second has a heavy weight and display-like optical size (with a higher stroke contrast); the third also has a similarly heavy weight, but with a body-like optical size.](images/thumbnail.svg)
<figcaption>The first example has a light weight and body-like optical size; the second has a heavy weight and display-like optical size (note the higher contrast); the third also has a similarly heavy weight, but with a body-like optical size.</figcaption>

</figure>

There are three main benefits offered by variable fonts:

1. **To compress:** the unified delivery of multiple [instances](/glossary/instance)—such as different weights, widths, optical sizes—in a single font file that is much smaller than the total file size of a collection of individual font files.
2. **To express:** the control given to users to select axes values _directly_, such as a custom weight that is between two named instances of weight. For example, between Regular (400) and Medium (500), a weight of 427 might be just the right one to express a design intent perfectly.
3. **To finesse:** the control given to programs to select axes values _indirectly_, based on context. For example, to automatically select an [optical size](/glossary/optical_sizes) instance using the current [point size](/glossary/point_size).

The variables within variable fonts are controlled by [axes](/glossary/axis_in_variable_fonts) or instances. Any variable in the type design can be assigned to a user-controllable axis by the type designer.
