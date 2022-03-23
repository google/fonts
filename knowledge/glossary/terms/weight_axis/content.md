
Weight (`wght` in CSS) is an axis found in many variable fonts. It controls the [font](/glossary/font) file’s [weight](/glossary/weight) parameter.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 400 | Min: 1 | Max: 1000 | Step: 1 |

<figure>

![Two side-by-side type specimens of the word “thicken”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows a light weight with thin strokes. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, shows a heavy weight with thick strokes.](images/thumbnail.svg)

</figure>

Weight is the overall thickness of a [typeface](/glossary/typeface)’s [strokes](/glossary/stroke) in any given font. The most common weights are [regular](/glossary/regular_upright) and [bold](/glossary/bold), but weights can cover extremes from the very light to the very heavy. With the weight axis in variable fonts, the number of instances or weights is effectively unlimited.

In CSS, we can assign a variable weight property to an element of our choosing:

<pre>
p {
  font-weight: 350;
}
strong {
  font-weight: 780;
}
</pre>

Unlike in non-variable fonts, the `font-weight` values no longer have to be declared in units of 100. Rather than have body copy set in a regular weight, which would usually sit at 400, we can set it a little lighter, at 350. Similarly, whereas `strong` text would usually be set in a bold weight, most often with a value of 700, we’re setting it at 780: heavier than a bold, but not quite as heavy as an extra bold.
