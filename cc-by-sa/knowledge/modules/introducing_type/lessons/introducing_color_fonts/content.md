[Color fonts](/glossary/color_fonts) (also known as chromatic fonts) can use multiple colors, including gradients, in a single glyph, rather than the flat, single color used by typical, non-color (monochromatic) fonts. This relatively new technology allows designers to set the color palette within the font to express themselves with color in a way that would previously not be possible outside of advanced graphics applications. 

To use a color font from Google Fonts, simply reference the family as you would any other font:

```css
@import url('https://fonts.googleapis.com/css2?family=Nabla&display=swap');

p {
  font-family: "Nabla";
}
```

<figure>

![A color font specimen showing the word “metal” rendered as intended.](images/color_fonts_1.png)

</figure>

This should render the font with its default color values, which are contained within the font file itself. At the time of writing, browser support for color fonts is not yet universal. This means that the type should always be rendered, but the colors or variable font axes may not appear as intended in browsers that don’t support the [COLRv1](https://caniuse.com/colr-v1) standard. However, the Google Fonts API supports these browsers with SVG fonts and attempts to get as close to the original intent as possible. You can read more about this implementation on [“COLRv1 Color Gradient Vector Fonts in Chrome 98.”](https://developer.chrome.com/blog/colrv1-fonts/)

The type designer has the power to include not just one, but a whole set of default color palettes within the font file. We can make use of these with the `base-palette` declaration, as in this example, where we select the the 3rd palette option:

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

![A color font specimen showing the word “metal” rendered in one of the alternate built-in color palettes.](images/color_fonts_2.png)

</figure>

The number 3 here is the index ID of the 3rd color palette provided by the font itself. (Note that numbering starts at 0.) Of course, if we wish to use colors not defined by the type designer in the base palettes, we can completely customize them ourselves using the [`override-colors`](https://caniuse.com/mdn-css_at-rules_font-palette-values_override-colors) property, or even choose to just override one at a time.

The Nabla font contains multiple index IDs for the color swatches within its palette. Here, we’re using the 3rd base palette and just changing the 6th color swatch:

```css
@font-palette-values --myPalette {
  font-family: "Nabla";
  base-palette: 3;
  override-colors: 6 #FFB978;
}
```

<figure>

![A color font specimen showing the word “metal” rendered as intended, with additional color customizations included to add a different color gradient to the bottom of the main face of the type.](images/color_fonts_3.png)

</figure>

Google Fonts now supports a growing number of color fonts in its library. To narrow the library selection to color fonts, visit [fonts.google.com/?coloronly=true](https://fonts.google.com/?coloronly=true) or press the “Show only color fonts” toggle.
