
A web font is any [font](/glossary/font) used in a website’s design that isn’t installed by default on the end user’s device—a counterpart to a [system font](/glossary/system_font_web_safe_font).

<figure>

![An abstract representation showing the letter M placed on a file icon.](images/thumbnail.svg)

</figure>

The widespread adoption of web fonts happened around 2009–2011 thanks to mainstream browsers’ increased support for two things: `@font-face` declarations in CSS and the WOFF file format.

WOFF (and its successor WOFF2) are compressed [file formats](/glossary/font_format) created specifically for web fonts. Although regular [OpenType](/glossary/open_type) fonts (TTF and OTF files) can be used as web fonts, such usage is not recommended as it usually contravenes [license](/glossary/licensing) agreements—and the files are significantly larger. WOFF and WOFF2 fonts cannot usually be installed on desktop computers.

Note that web fonts are assets that need downloading, and therefore affect the overall performance of page load times; i.e., the more web fonts we use, the longer it’ll take for our websites to load. This is potentially offset with the use of [variable fonts](/glossary/variable_fonts).
