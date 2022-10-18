[Color fonts](/glossary/color_fonts) (also known as chromatic fonts) can use multiple colors, including gradients, in a single glyph, rather than the flat, single color used by typical, non-color (monochromatic) fonts. This relatively new technology allows designers to set the color palette within the font to express themselves with color in a way that would previously not be possible outside of advanced graphics applications. 

To use a color font from Google Fonts, simply reference the family as you would any other font:

```css
@import url('https://fonts.googleapis.com/css2?family=Nabla&display=swap');

p {
  font-family: "Nabla";
}
```

<figure>

![INSERT_ALT](images/color_fonts_1.png)

</figure>

This should render the font with its default color values, which are contained within the font file itself. At the time of writing, browser support for color fonts is not yet universal. This means that the type should always be rendered, but the colors or variable font axes may not appear as intended in browsers that don’t support the [COLRv1](https://caniuse.com/colr-v1) standard. However, thankfully the Google Fonts API supports these browsers with SVG fonts and attempts to get as close to the original intent as possible. You can read more about this implementation on [“COLRv1 Color Gradient Vector Fonts in Chrome 98.”](https://developer.chrome.com/blog/colrv1-fonts/)

The type designer has the power to include not just one, but a whole set of default color palettes within the font file. We can make use of these with the base-palette declaration, as in this example, where we select the a particular palette option:

```css
p {
  font-family: "Nabla";
  font-palette: --myPalette;
}

@font-palette-values --myPalette {
  font-family: "Nabla";
  base-palette: 3;
}
```

<figure>

![INSERT_ALT](images/color_fonts_2.png)

</figure>

The number 3 here is the index ID of the fifth (numbering starts at 0) color palette provided by the font itself.
Of course, if we wish to use colors not defined by the type designer in the base palettes, we can completely customize them ourselves using the [`override-colors`](https://caniuse.com/mdn-css_at-rules_font-palette-values_override-colors) property:

```css
@font-palette-values --myPalette {
  font-family: "Nabla";
  base-palette: 3;
  override-colors: 6 #FFB978;
}
```

This font contains multiple index IDs for the color swatches within the palette. Here, we’re just changing swatch 6.

<figure>

![INSERT_ALT](images/color_fonts_3.png)

</figure>

Google Fonts now supports a growing number of color fonts in its library, which can be found at [fonts.google.com](https://fonts.google.com/?coloronly=true).