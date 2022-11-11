# Vertical spacing & line height in design systems

Digital designers will typically spend hours meticulously fine-tuning their components and pages to look pixel perfect with consistent padding, a beautiful and cohesive color system, and most importantly the [fonts](/glossary/font) we choose to display our content. But as we all know, designs and trends change and so our systems update to match these. A proper design system will scale easily with colors and spacing variables, but when it comes to switching out our [fonts](/glossary/font), all that hard work goes to waste and we need to start from scratch again. This all comes down to inconsistent vertical spacing from typeface to typeface, and how the platforms we are designing for render text.

## Let’s start with a bit of history

In traditional typography, back when things were a bit more physical, typesetters had to space their text using blocks of metal. To make the text more readable they would add literal pieces of lead in between lines to space them out more. These pieces of lead were added directly below any [letters](/glossary/letters), and this is what led to the term [“leading”](/glossary/line_height_leading) in modern typography applications. CSS, Microsoft Word and Google Docs use the alternate terms [“line-height”](/glossary/line_height_leading) and “line-spacing” to mean the vertical distance between lines, including the [leading](/glossary/line_height_leading).

Because physical blocks were used there wasn’t much room for manipulation of the [letters](/glossary/letters), and the blocks that were used to encase the [letters](/glossary/letters) would accommodate the maximum letter height for that typeface. With digital typography, type designers have a lot more freedom to place the [letters](/glossary/letters) anywhere they want, even straying outside of the virtual block that controls their vertical spacing.

<figure>

![Three fonts with their default bounding boxes. One cursive font that sits high, one block font that also sits high, and a basic sans-serif that sits central.](images/default-line-heights.svg)

</figure>
<figcaption>Positioning of [letters](/glossary/letters) from different typefaces within their default bounding box heights. All of the examples are set to the same font size.</figcaption>

### So what’s the big deal?

What all of this means in practice is a lot of discrepancies between different [fonts](/glossary/font). The one rule nearly all [fonts](/glossary/font) follow is every [glyph](/glossary/glyph) sitting on the ‘[baseline](/glossary/baseline).’ There are no rules about where the [cap-height](/glossary/cap_height), [x-height](/glossary/x_height) or [descenders](/glossary/ascenders_descenders) should be drawn in relation to the [line-height](/glossary/line_height_leading), so you get inconsistencies that make vertical alignment tricky. This vertical alignment is necessary to create consistent, scalable designs, but aligning type perfectly can be time-consuming, especially when mixing typefaces.

<figure>

![Three examples of vertical alignment with fonts. Buttons with a non-centered and centered font, alignment of different font sizes to the baseline, and spacing within a simple card component.](images/examples.svg)

</figure>
<figcaption>An overview of various problems that arise from vertical alignment within digital typography.</figcaption>

## Rendering text on different platforms

To complicate matters further, different digital platforms render text in different ways when dealing with [line-height](/glossary/line_height_leading). With the introduction of CSS1 in 1996, text was rendered centered within the total [line-height](/glossary/line_height_leading). That is, "half-leading“ was added above and below the 100% [line-height](/glossary/line_height_leading) to add up to the total [line-height](/glossary/line_height_leading).

<figure>

![Four lines of text, with the default line height highlighted, and 2 half-leading highlights added above and below the default line height.](images/web-render.svg)

</figure>
<figcaption>The web renders text with half-leading above and below the 100% [line-height](/glossary/line_height_leading) for a font.</figcaption>

iOS platforms followed suit with the web standards and neither has changed the way they render text to this day. Android devices however mostly render a paragraph clipped to the default [line-height](/glossary/line_height_leading) for the first and last line. Total [line-height](/glossary/line_height_leading) will still be respected via the lineSpacingMultiplier property, so every line of text still has the correct spacing from [baseline](/glossary/baseline) to [baseline](/glossary/baseline).

<figure>

![Two text boxes side-by-side highlighting the clipped text box rendering found on Android platforms.](images/native-render.svg)

</figure>

<figcaption>iOS and Android render text nodes slightly differently, causing confusion within design tools.</figcaption>

To add to this, web developers don’t (yet) have access to the inner metrics of a typeface when it is loaded, simply because of having to **load** the font file. This means they can’t know where the [glyphs](/glossary/glyph) are positioned, in order to align elements to any diacritics, [cap-height](/glossary/cap_height), [x-height](/glossary/x_height), or default [line-height](/glossary/line_height_leading). In theory, this shouldn’t be a problem for native platforms as the files are pre-loaded within an application. In fact, both iOS and Android platforms have the ability to create padding or space according to the [baseline](/glossary/baseline) of a font, but this is rarely used. On top of all of this, we must also remember that all devices, browsers and platforms will render in slightly different ways across the board, and so no 2 implementations of a design are likely to be the same.

Within common design tools such as Sketch or Figma, text will be rendered in the same way as web and iOS. This is to help cover the majority of bases with text rendering, to enable consistent handover between design and engineering. Unfortunately no design tools today yet show the default [line-height](/glossary/line_height_leading) clipping for a paragraph or line of text, so it’s more of a manual process to figure it out. Thankfully, Marcin Wichary created [this handy tool](https://aresluna.org/line-height-playground/) to visualize the differences in platform text rendering.

## So what can you do about all this?

### Manual spacing

To ensure consistent design across your applications, the most common method would be to just space everything manually. You can look into all of your components and designs, and ensure that any text node is spaced to the exact pixel. It removes all the guesswork out of the equation, but becomes a very manual process. Misaligning spacing becomes inevitable with all the work needed, and there is no way to truly systemise your process. Finally, it becomes particularly tricky when you need to update your typeface to a new one, and you have to go through the whole process again.

<figure>

![A simple card component with equal vertical spacing, shown with visual spacing values, and text-box spacing values.](images/manual-spacing.svg)

</figure>
<figcaption>Vertical [rhythm](/glossary/rhythm) by aligning to [cap-height](/glossary/cap_height) and [baseline](/glossary/baseline) becomes a very manual, and non-systematic process.</figcaption>

### Equally spaced font files

One way to combat a lot of the issues with vertical spacing is to ensure you choose a typeface that has equal spacing above and below the [glyphs](/glossary/glyph) within the line height. A lot of [fonts](/glossary/font) won’t be spaced centrally within their default line height, and the larger the font size the more this becomes obvious. Choosing one that is exactly centered within its default line height means that no matter the line height it will always be centered, making it much easier to create a vertical [rhythm](/glossary/rhythm) with your text.

Choosing such a font can be difficult, but luckily most design tools will show the bounding box of any text layer. Some [fonts](/glossary/font) are obviously misaligned from the start, but others will need a little more investigation. Simply reduce the [line-height](/glossary/line_height_leading) of any text layer bit by bit until the bounding box matches your [glyph](/glossary/glyph) height. A general rule of thumb for a vertically centered font is to align to the [cap-height](/glossary/cap_height) and [baseline](/glossary/baseline). This will ensure your text looks centered to other elements within your designs. Read more about the idea of “equal” metrics in [this twitter thread by @romanshamin_en](https://twitter.com/romanshamin_en/status/1562801657691672576).

<figure>

![Two example fonts with their default line height and vertical centering highlighted. One font is rendered high within it's line-height, and the other is perfectly centered.](images/equal-spacing.svg)

</figure>
<figcaption>An example of how [letters](/glossary/letters) can and can’t be aligned to the true center of a default [line-height](/glossary/line_height_leading).</figcaption>

There are two main benefits to choosing a font like this: first, centering the text vertically to other objects, and second, ensuring a consistent space above and below a text node. It’s common to include text next to an icon or shape in plenty of components, and so no matter the line height used the text can always be easily aligned to the same center line. With equal spacing there is also a more reliable space between elements when changing font size. This makes vertical [rhythm](/glossary/rhythm) within a page or component and aligning to a [baseline](/glossary/baseline) grid much more achievable.

<figure>

![Examples of two fonts, one with equal metrics, and the other without. One example is a button, the other example is text with an icon.](images/equal-spacing-benefits.svg)

</figure>
<figcaption>The benefits of choosing a font that is equally centered to it’s [line-height](/glossary/line_height_leading).</figcaption>

### Upcoming CSS feature, leading-trim

For web, a CSS feature called leading-trim is currently in proposal that actually trims a text node to pre-defined properties. You can choose from [cap-height](/glossary/cap_height), [x-height](/glossary/x_height), [baseline](/glossary/baseline), [descender](/glossary/ascenders_descenders), or default [line-height](/glossary/line_height_leading) to clip the top and bottom of the node to these values, much like you can do on Android. This will help ensure consistent spacing and even introduce the ability for better [baseline](/glossary/baseline) alignment within the web.

<figure>

![A line of text with it's line-height highlighted, and a line denoting where leading-trim would trim to the cap-height and baseline.](images/leading-trim.svg)

</figure>
<figcaption>How leading-trim can cut a text node on the web, to allow for better [cap-height](/glossary/cap_height) and [baseline](/glossary/baseline) positioning.</figcaption>

### Be specific with calculations

Finally, you could even calculate the clipping needed to apply to any text node using CSS variables. The ratio of [cap-height](/glossary/cap_height) or [baseline](/glossary/baseline) to the bounding box will always be the same for a single font, despite the font size, so if you know the ratio, you can calculate how much you need to clip the node above and below. Nathan Curtis alludes to this idea and links to a CSS mixin in [a fantastic article on space in design systems](https://medium.com/eightshapes-llc/space-in-design-systems-188bcbae0d62#:~:text=Solve%20Collisions%20like%20Line%20Height%20Systematically).

<figure>

![Two sizes of the same font with cap-height and baseline to line-height ratios highlighted to be the same for both sizes.](images/ratio.svg)

</figure>
<figcaption>The ratio of [cap-height](/glossary/cap_height) and [baseline](/glossary/baseline) to a [line-height](/glossary/line_height_leading) will always be the same no matter what text-size is used.</figcaption>

## **What to take away from all this?**

With a good vertical [rhythm](/glossary/rhythm), your typography helps your customers to read content with ease, and you can create beautiful, consistent designs that bring calmness and clarity. There’s no denying it, perfecting a vertical [rhythm](/glossary/rhythm) is by no means trivial, but by spending time on the details, scalability and a systematic type system will come. Use the tools and processes outlined within this article to help you create products and websites that have great vertical [rhythm](/glossary/rhythm), and your customers will thank you for it.
