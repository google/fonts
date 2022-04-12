
The easiest way to implement [web fonts](/glossary/web_font) on our website is to use a font delivery service, such as Google Fonts or Adobe Fonts, so that most of the heavy lifting is done for us. Typically, all this involves is choosing a [typeface](/glossary/typeface) or [family](/glossary/family_or_type_family_or_font_family), and then copying a line or two of code into our website.

In this article we’ll first look at the process of adding fonts from a font delivery service, and then delve into the CSS that’s provided.

<figure>

![An abstract representation showing a font selected from a group of possibilities, and then two code blocks required to load and style the type, respectively. This is then followed by a device showing the type rendered correctly.](images/thumbnail.svg)

</figure>

## Loading web fonts

Once we’ve browsed the font library and made our selection(s), we’ll need to copy the code provided by the delivery service into the `<head>` of our HTML. Google Fonts provides something like this:

```
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=FAMILY_NAME:wght@WEIGHT_OR_RANGE&display=swap" rel="stylesheet">
```

Or, if we'd like to use fonts in HTML email, we’ll use the `@import` link, which usually looks like this:

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=FAMILY_NAME:wght@WEIGHT_OR_RANGE&display=swap');
</style>
```

For more information on the Google Fonts API, please see [developers.google.com/fonts/docs/css2](https://developers.google.com/fonts/docs/css2).

For Adobe Fonts, the process is very similar, but the important differentiation is that the URL uses a “web project ID”. Please refer to [the Adobe Fonts documentation](https://helpx.adobe.com/fonts/user-guide.html/fonts/using/add-fonts-website.ug.html) for full details.

Google Fonts and Adobe Fonts are the two major font delivery services, but there are of course others, and most offer a similar method for getting their web fonts onto our websites. However, for specifics, refer to the documentation provided by the other providers.

## Exploring the CSS served by the font delivery services

If we take a look at the CSS file (in the URL above) that’s been served to us by Google Fonts, Adobe Fonts, or another provider, we’ll notice that it includes an `@font-face` declaration to load the font file and match it to a [family](/glossary/family_or_type_family_or_font_family), a [style](/glossary/style) (either `normal` or `italic`), and a [weight](/glossary/weight). In its most basic form, the CSS will look something like this, and it’s effectively the exact same CSS we’d have written ourselves if we were [*not* using a font delivery network](/lesson/self_hosting_web_fonts):

```
@font-face {
  font-family: 'FAMILY_NAME';
  font-style: NORMAL_OR_ITALIC;
  font-weight: NUMERIC_WEIGHT_VALUE;
  src: url(FONT_FILE_NAME.woff2) format('woff2');
}
```

[//]: # (There are many other things we’re likely to find in these CSS files, but we’ll explore them in our more advanced article “Defining custom mapping for weights and styles in CSS”.)

See our article [“Using web fonts”](/lesson/using_web_fonts) for some general guidelines on web fonts as a whole, including how to counter [the flash of unstyled text or FOUT](/glossary/fout).

From this point, the process of defining our typographic styles in CSS is exactly the same, regardless of where the font file itself is hosted.
