
Optical size (controlled with font-optical-sizing or font-variation-setting: ‘opsz’ VALUE in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). It controls the font file’s optical size optimizations. 

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

Default: 14     Min: 6     Max: 144     Step: 0.1

<figure>

![ALT_TEXT](images/thumbnail.svg)
<figcaption>CAPTION</figcaption>

</figure>

Optical sizes in a variable font are different versions of a typeface optimized for use at singular specific sizes, such as 14 pt or 144 pt. Small (or body) optical sizes tend to have less stroke contrast, more open spacing, and taller x-heights than those of their large (or display) counterparts. 

The concept is that the numeric value for this axis should match the rendered font size in typographic points (1/72nd of an inch) in print, although browsers instead match it to the CSS px unit, since they have no concept of physical size. A new CSS attribute was introduced to go along with it: font-optical-sizing. The default is auto (or we can force it to none if we’d prefer to turn it off), and this is supported behavior in all modern browsers.

<pre>
body {
  font-optical-sizing: auto;
}
</pre>

Alternatively, we can set an explicit value by using font-variation-settings, like so:

<pre>
body {
  font-variation-settings: 'opsz' 16;
}
h1 {
  font-variation-settings: 'opsz' 48;
}
</pre>



