Variable fonts are often more efficient than their static counterparts in terms of both total [file size](/glossary/file_size) and [server requests](https://gigapress.net/reduce-http-requests/) since they provide a range of stylistic variations from just one font file as opposed to multiple. But what factors are the most critical? Which specific font qualities make the biggest impact on efficiency?

With so many moving parts involved—for both font technology and web design/development—the most significant factors may change from one project to the next. Having said that, here is a general overview of the most noteworthy aspects involved:

- **What is the quality of the internet connection?** [File sizes](/glossary/file_size) are obviously a major factor in optimizing the speed of any web page. However, another factor that is often overlooked is the *number* of files and [server requests](https://gigapress.net/reduce-http-requests/) involved. Depending on the specifics of a visitor’s internet connection and the settings of the server where the files live, it can sometimes be faster to load a single variable font even if its file size is slightly larger than the total size for a matching set of static fonts.

- **How many glyphs are in the fonts?** It’s no surprise that fonts containing more glyphs will have larger file sizes. The increases are typically less severe for variable fonts though than for a set of matching static fonts.

- **How many stylistic variants are used on the page?** A page that only uses one or two variants (e.g. Regular & Bold) will probably see smaller benefits from variable fonts than a page with multiple weights, widths, italics, etc.

- **How many variable font files are required to match a similar selection of static fonts?** Some typeface families can be stored entirely in a single variable font file, but some must be split into separate files (e.g. for upright and italic variants). And of course separate typeface families will almost always require separate variable fonts.

- **How irregular is the typeface?** Different typeface designs require different amounts of font data. A simple sans-serif typeface can be represented with fewer data points than an elaborate serif typeface. These differences affect the compression and efficiency of font file sizes for static and variable fonts differently.

- **How many axes of variation are involved?** Every [axis](/glossary/axis_in_variable_fonts) of stylistic variation increases file size requirements. A variable font with both weight and width axes will have a larger file size than if it only offered a single weight axis. It is worth noting, however, that fonts with multiple axes of variation typically provide much more efficiency in terms of potential variants per kilobyte.

- **How many source designs were used to produce the variable font?** Almost all variable fonts work by interpolating multiple underlying [source designs](/glossary/masters) that were drawn to be compatible with each other. Some typeface families require more source designs to complete their intended [designspace](https://superpolator.com/designspace.html), which usually results in larger variable font files.

- **How much [hinting](/glossary/hinting) data is included in the fonts, if any?** Minimal hinting for typical modern rendering environments will likely require less data than intense hinting for low-resolution screens and old operating systems.

- **What “flavor” of OpenType font data is used?** Modern variable fonts are generated in the [OpenType](/glossary/open_type) font format. But there are two major standards (or “flavors”) for outline data in OpenType—CFF and TTF—each with different implications for font file sizes, among other things. CFF-flavored variable fonts typically have smaller sizes than their TTF-flavored equivalents, but they aren’t supported quite as widely.

- **What kind of compression is used for the fonts?** Uncompressed .otf or .ttf fonts will have much larger file sizes before they’ve been converted to the [.woff or .woff2 web font formats](https://en.wikipedia.org/wiki/Web_Open_Font_Format). (Side note: All browsers that support variable fonts also support the .woff2 format, so variable web fonts should almost always be delivered as .woff2 files.)

To see how some of these factors play out in real-world comparisons between static and variable fonts, check out the [tables of web font comparisons](/lesson/web_font_comparisons_variable_vs_static).

Some web font services like Google Fonts incorporate intelligent functionality to detect specifics about a user’s system or a page’s design and serve font data in the most efficient way accordingly. For example, if weight and width axes are available but only weight variants are used, a different font with limited functionality and a smaller file size can be served. Or if a page is being viewed in an environment where hinting data is ignored and is thus irrelevant (as is typically the case in macOS web browsers), a font file can be delivered with all hinting removed to minimize data transfer. These kinds of file optimizations and serving techniques can be impractical (or impossible) to set up on your own without access to the fonts’ original source files, but web font services like Google Fonts include them automatically without any extra effort.

Finally, it should be noted that the answer to many of the questions listed above can be difficult or impossible to know or control with any given project. It is rare for font vendors to share specifics about how many source files were used to produce a variable font, or how much hinting data is in each font. But in many cases the design and functionality of the typeface is more important when choosing a typeface than technical details about its production and delivery. Still, having some limited understanding of the moving parts can still be helpful for optimizing the performance of any project.

For more info on using variable fonts, see the [other articles listed under the topic of variable fonts](https://fonts.google.com/knowledge/topics/variable_fonts).
