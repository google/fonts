
Optical size (controlled with `font-optical-sizing` or `font-variation-setting: ‘opsz’ VALUE` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). It controls the [font](INSERT_URL) file’s [optical size](INSERT_URL) optimizations.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 14 | Min: 6 | Max: 144 | Step: 0.1 |

<figure>

![Two side-by-side type specimens of the word “glaze”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows a small (or body-like) optical size. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, shows a large (or display-like) optical size, with a shorter x-height and greater stroke contrast.](images/thumbnail.svg)

</figure>

Optical sizes in a variable font are different versions of a [typeface](INSERT_URL) optimized for use at singular specific sizes, such as 14 pt or 144 pt. Small (or [body](/glossary/body)) optical sizes tend to have less [stroke](/glossary/stroke) [contrast](/glossary/contrast), more open spacing, and taller [x-heights](/glossary/x_height) than those of their large (or display) counterparts.

The concept is that the numeric value for this axis should match the rendered font size in typographic points (1/72nd of an inch) in print, although browsers instead match it to the CSS px unit, since they have no concept of physical size. A new CSS attribute was introduced to go along with it: `font-optical-sizing`. The default is `auto` (or we can force it to `none` if we’d prefer to turn it off), and this is supported behavior in all modern browsers.

<pre>
body {
  font-optical-sizing: auto;
}
</pre>

Alternatively, we can set an explicit value by using `font-variation-settings`, like so:

<pre>
body {
  font-variation-settings: 'opsz' 16;
}
h1 {
  font-variation-settings: 'opsz' 48;
}
</pre>
