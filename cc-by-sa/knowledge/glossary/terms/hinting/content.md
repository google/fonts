
Hinting is the process of including programmatic data in a [font](/glossary/font) file to help text rendering software represent a [typeface](/glossary/typeface) legibly at small sizes, on low-resolution screens.

<figure>

![“Aa” set in a sans serif typeface, placed in the background, with a pixelated version overlaid in the foreground. This pixelated version represents the “hints” given to the software.](images/thumbnail.svg)

</figure>

Until recently, with the arrival of high-resolution displays, hinting was a considerable concern when working with [type](/glossary/type) on screen. 72dpi monitors were incapable of rendering the subtleties of type at small sizes, and hinting instructions were required to offer the rasterizer “hints” about which pixels to draw the type on. 

Anti-aliasing technology improved the look of this rendering by allowing the software to define whether a pixel would be on (0; i.e., black), off (255; i.e., white), or any value in between. These grey pixels would soften the harshness of the black and white bitmaps. A similar technology called subpixel antialiasing allowed for only part of the pixel (the red, blue, or green component) to be turned on, thus achieving a similar effect with color.

Including hinting instructions within a font is generally recommended; however, because of the ubiquity of hi-res displays, it’s less of a concern today than it once was.
