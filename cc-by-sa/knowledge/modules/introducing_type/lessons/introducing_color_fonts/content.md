[Color fonts](/glossary/color_fonts) allow the font to take more control over the drawing process than just "ink of unknown color goes here,"
with the color of the ink set by some external entity.

On the web text is generally drawn in a color specified in CSS. In a document editor the user can typically choose a color
to use for text. The font has no input into the color beyond where to fill and where not to. The font cannot manipulate the color,
such as to define a gradient, it is strictly binary "ink here or not."

We call fonts that only define where ink of an undefined color goes monochromatic or "non-color."

**TODO: should we have a glossary entry for non-color fonts? Switch to Chromatic and Monochromatic?**

Color fonts can draw in many colors and can specify what those colors should be. Often they add additional drawing capabilities like
gradients or partial opacity. The most common example most users interact with is emoji.

**TODO a nice emoji example**

Color can be used for so much more than emoji!

**TODO examples from https://developer.chrome.com/blog/colrv1-fonts/ and IUC45**

**TODO talk about changing colors**

Unfortunately, there are many ways to construct color fonts and no single approach is widely supported by browsers or
operating systems. The Google Fonts Web API looks at the [User-Agent](https://caniuse.com/mdn-http_headers_user-agent)
header and sends font in the best supported color font format to try to make color fonts "Just Work."

**TODO: go into detail? Link out? ...just don't?**