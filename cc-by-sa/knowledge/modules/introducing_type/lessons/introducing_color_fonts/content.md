[Color fonts](/glossary/color_fonts) (also known as chromatic fonts) can use multiple colors, including gradients, in a single glyph, rather than the flat, single color used by typical, non-color (monochromatic) fonts. This relatively new technology allows designers to set the color palette within the font to express themselves with color in a way that would previously not be possible outside of advanced graphics applications. 
[ILLO: color fonts montage]
To use a color font from Google Fonts, simply reference the family as you would any other font:

```css
@import url(https://fonts.googleapis.com/css2?family=Bungee+Spice);

p {
  font-family: "Bungee Spice";
  font-palette: --elliot1;
}
```

[ILLO showing output of code]

This should render the font with its default color values, which are contained within the font file itself. At the time of writing, browser support for color fonts is not yet universal. This means that the type should always be rendered, but the colors or variable font axes may not appear as intended in browsers that don’t support the [COLRv1](https://caniuse.com/colr-v1) standard. However, thankfully the Google Fonts API supports these browsers with SVG fonts and attempts to get as close to the original intent as possible. You can read more about this implementation at [INSERT].

The type designer has the power to include not just one, but a whole set of default color palettes within the font file. We can make use of these with the base-palette declaration, as in this example, where we select the a particular palette option:

```css
@font-palette-values --elliot1 {
  font-family: "Bungee Spice";
  base-palette: 3; /* WHY IS THIS NOT DOING ANYTHING? */
}
```

[ILLO showing output of code]

[FRO: see also https://codepen.io/elliotjaystocks/pen/xxjNgrv]

The number 3 here is the index ID of the fifth (numbering starts at 0) color palette provided by the font itself.
Of course, if we wish to use colors not defined by the type designer in the base palettes, we can completely customize them ourselves using the [`override-colors`](https://caniuse.com/mdn-css_at-rules_font-palette-values_override-colors) property:

```css
.alt {
  font-palette: --elliot2;
}

@font-palette-values --elliot2 {
  font-family: "Bungee Spice";
  base-palette: 3;
  override-colors: 0 #FF6D7F, 1 #1A73E8, 2 #3C4043;
}
```

The numbers 0, 1, and 2 here are the index IDs for the color swatches within the palette.

[ILLO showing output of code] 

Most people will first encounter color fonts via emoji, and emoji is a great example of how gradients can provide even more expression over flat color. In this example, let’s use CSS to turn a simple smiley purple and blue:

```css
INSERT CSS HERE
```

[ILLO showing output of code]

Google Fonts now supports a growing number of color fonts in its library, which can be found at [fonts.google.com](https://fonts.google.com/?coloronly=true). For more information on color fonts, please read this introductory post on the Chrome Developers blog, COLRv1 Color Gradient Vector Fonts in Chrome 98.