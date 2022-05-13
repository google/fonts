
“Optical Size” (controlled with `font-optical-sizing` or `font-variation-setting: ‘opsz’ VALUE` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). It controls the [font](/glossary/font) file’s [optical size](/glossary/optical_sizes) optimizations.

The [Google Fonts CSS v2 API](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| 14 | 6 | 144 | 0.1 |

<figure>

![Two side-by-side type specimens of the word “glaze”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows a small (or body-like) optical size. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, shows a large (or display-like) optical size, with a shorter x-height and greater stroke contrast.](images/thumbnail.svg)

<figcaption>Typeface: <a href="https://github.com/googlefonts/amstelvar">Amstelvar</a></figcaption>

</figure>

Optical sizes in a variable font are different versions of a [typeface](/glossary/typeface) optimized for use at singular specific sizes, such as 14 pt or 144 pt. Small (or [body](/glossary/body)) optical sizes tend to have less [stroke](/glossary/stroke) [contrast](/glossary/contrast), more open and wider spacing, and a taller [x-height](/glossary/x_height) than those of their large (or [display](/glossary/display)) counterparts.

The concept is that the numeric value for this axis should match the rendered font size in typographic points (1/72nd of an inch) in print, although browsers instead match it to the CSS `px` unit, since they have no concept of physical size. A new CSS attribute was introduced to go along with it: `font-optical-sizing`. The default is `auto`, and this is supported behavior in all modern browsers.

```css
body {
  font-optical-sizing: auto;
}
```

We can force it to `none` if we’d prefer to turn it off, or we can set an explicit `px` value by using `font-variation-settings`, like so:

```css
body {
  font-variation-settings: 'opsz' 16;
}
h1 {
  font-variation-settings: 'opsz' 48;
}
```

The changes made across an Optical Size axis are intended by typeface designers to optimize the type, but parametric axes can be used to further adjust and fine-tune things. Explore more in our article, [“Introducing parametric axes.”](/lesson/introducing_parametric_axes)

In line with the current CSS spec, the four-character code for this axis should be referenced in lowercase (as only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the lowercase axes have to appear first in the URL, followed by the uppercase, each in alphabetical order.
