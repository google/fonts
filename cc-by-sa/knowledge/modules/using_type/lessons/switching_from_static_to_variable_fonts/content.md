For many designers, implementing variable fonts on a website might mean treating the project as a blank canvas, and using a brand new typeface to experiment with the possibilities variable fonts offer. However, swapping out your static fonts for variable ones can be a useful way of dipping your toes into this new world. Plus, moving from a typeface’s static fonts to its variable cousins offers some advantages:

1. With the overall typographic system tried and tested, we’re not actually changing that much; it’s more of a case of finessing.
2. Seeing what works and what doesn’t work with the current system makes it easier to make more informed decisions about the variable implementation.

Let’s test this out and make the move from Roboto to Roboto Flex. Although Roboto Flex offers many axes to use (including parametric axes), we’ll keep things simple and focus on weight (`wght`), slant (`slnt`), and optical size (`opsz`). But but before we get into the axes, first we need to actually load the variable fonts. Assuming we’re using the Google Fonts API (of course, we could also download the font files and self-host them), we’ll update the line in our HTML’s `head`—which is currently using the Regular (400), Regular Italic, Bold (700), and Bold Italic styles—from this:

```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
```

To this:

```html
<link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:**opsz,slnt,wght@8..144,-10..0,100..1000**&display=swap" rel="stylesheet">
```

As well as switching over to the new family, we’re also defining three variable axes to use and a range of values for each:

- opsz: 8 to 144
- slnt: -10 to 0
- wght: 100 to 1000

Let’s get the real basics out of the way first (for more information, see [“Styling type on the web with variable fonts”](https://fonts.google.com/knowledge/using_type/styling_type_on_the_web_with_variable_fonts)):

```css
body {
  font-family: 'Roboto Flex', sans-serif;
}
```

Weight is probably the most straightforward place to start. Whereas before we might’ve had `font-weight` declarations that look something like this:

```css
body {
  font-weight: 400;
}

strong,
b {
  font-weight: 700;
}
```

We’re now going to switch them to the variable versions using `font-variation-settings`: [insert note on why we’re using the low level]

```css
body {
  font-variation-settings: 'wght' 400;
}

strong,
b {
  font-variation-settings: 'wght' 700;
}
```

Let’s get a bit more inventive and harness the power of variable fonts to tweak those weights a bit. We’ll make our body text a little lighter and our strong text ever so slightly heavier:

```css
body {
  font-variation-settings: 'wght' 310;
}

strong,
b {
  font-variation-settings: 'wght' 740;
}
```

Next, let’s style our italics. Whereas before we might’ve had declarations that look something like this:

```css
body {
  font-style: normal;
}

em,
i {
  font-style: italic;
}
```

We’ll now once again employ `font-variation-settings`:

```css
body {
  font-variation-settings: 'slnt' 0;
}

em,
i {
  font-variation-settings: 'slnt' -10;
}
```

Unfortunately, though, we now have a problem: The `slnt` declaration will override `wght` (or vice versa if placed in the opposite order), and we’ll need to re-declare each like so:

```css
body {
  font-variation-settings: 'slnt' 0, 'wght' 310;
}

em,
i {
  font-variation-settings: 'slnt' -10, 'wght' 310;
}

strong,
b {
  font-variation-settings: 'slnt' 0, 'wght' 740;
}
```

However, this is not only inconvenient, but it’ll also mean our CSS will get messy fast, especially once we introduce further axes into the mix. This issue is outlined in depth in [“Boiling eggs and fixing the variable font inheritance problem”](https://pixelambacht.nl/2019/fixing-variable-font-inheritance/) by Roel Nieskens.

As Roel suggests, we can overcome this problem and simplify our usage of `font-variation-settings` by using a CSS custom property (also known as a CSS variable) so that we can alter only the axis’ value without having to redeclare the entire `font-variation-settings` string:

```css
/* Declare the custom property on :root */
:root {
  --custom-opsz: 0;
  --custom-slnt: 0;
  --custom-wght: 0;
}

/* Apply the variables to every HTML element */
* {
  font-variation-settings:
		'opsz' var(--custom-opsz),
		'slnt' var(--custom-slnt),
		'wght' var(--custom-wght);
}

/* Change the axes on specific elements */
body {
	--custom-opsz: 0;
	--custom-slnt: 1;
	--custom-wght: 310;
}

strong,
b {
	--custom-wght: 740;
}

em,
i {
	--custom-slnt: -10;
}
```

We’ve not yet tackled `opsz`, and that’s because it’s an axis that works a little differently, given that it’s controlled automatically in most modern browsers. Just to be sure, let’s make sure automatic optical sizing is turned on:

```css
body {
  font-optical-sizing: auto;
}
```

Where supported, the appropriate optical size will be set; i.e., 8px type will use the `opsz` value of 8, and 144px type will use the `opsz` value of 144. (8 and 144 are the extreme ends of the axis in this particular font.) **[Add note about how this is actually calculated]**

However, for ultimate control, we can also set our optical size manually, like so:

```css
h1 {
  font-variation-settings: 'opsz' 60;
}
```

Again, so that we don’t encounter the inheritance problem, we’ll improve our CSS by using the custom property we set earlier:

```css
h1 {
	--custom-opsz: 60;
}
```

On a responsive website, where we use media queries to change the layout as the viewport’s size grows or shrinks, it’s a sensible idea to adjust optical size when the `font-size` changes, too:

```css
h1 {
	font-size: 2em;
	--custom-opsz: 60;
}

@media screen and (min-width:40em) {

	h1 {
		font-size: 3em;
		--custom-opsz: 72;
	}

}
```

From here, we can start to tweak our typographic system further by exploring other values on each axis, honing each according to the browser’s dimensions by introducing more media queries, and of course even adding further refinement by introducing more of the axes available in this variable font. The possibilities are almost limitless.
