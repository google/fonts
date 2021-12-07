
Line height is the vertical distance between two lines of [type](/glossary/type), measured from the [baseline](/glossary/baseline) of one line of type to the baseline of the next. Traditionally, in metal type, this was the combined measurement of the font size and the strips of lead that were inserted between each row (called “leading”) of type.

<figure>

![A paragraph of text with two background rectangles highlighting one of the lines. The shortest rectangle emulates the the traditional notion of leading; i.e., the extra space between lines. The tallest rectangle represents line height; i.e., the combination of the line itself *and* the additional spacing between lines.](images/thumbnail.svg)

</figure>

Line height has a direct impact on the [readability](/glossary/legibility_readability) of [text](/glossary/text_copy), so understanding it is one of the most fundamental [typographic](/glossary/typography) practices.

It’s possible to set the line height value in a number of [units](/glossary/unit), as with font size, although those units could be different. For instance, we might set our `font-size` in pixels, but then declare the `line height` with a percentage value:

```css
p {
	font-size: 16px;
	line height:150%; /* Equivalent to 24px */
}
```