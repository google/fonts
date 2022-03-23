
Width (`wdth` in CSS) is an [axis](/glossary/axis_in_variable_fonts) found in some [variable fonts](/glossary/variable_fonts). It controls the [font](/glossary/font) file’s [width](/glossary/width) parameter.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: 100 | Min: 25 | Max: 200 | Step: 0.1 |

<figure>

![Two side-by-side type specimens of the word “spacious”, each shown with a variable axis represented beneath as a horizontal slider. The first specimen, with the slider most of the way to the left to represent a lower value on the axis, shows a very condensed version, taking up very little horziontal space. The second specimen, with the slider most of the way to the right to represent a higher value on the axis, is very wide.](images/thumbnail.svg)

</figure>

Width is the result of how much horizontal space is taken up by a [typeface](/glossary/typeface)’s [characters](/glossary/character). A [condensed](/glossary/condensed_narrow_compressed) face takes up considerably less space than a [wide](/glossary/wide_extended) one.

In CSS, we can assign a variable width to an element of our choosing using the `font-stretch` property. (Despite the name, note that the type is never literally “stretched” by browsers. This property name was chosen to make the concept more accessible to a general audience.)

<pre>
p {
  font-stretch: 50%;
}
strong {
  font-stretch: 193%;
}
</pre>

Here, our text will be quite narrow—50% is what the type designer has decided is half of the regular (100%) width—and the `strong` text will be almost twice the width of the regular. Width values are always above 0, with 100% being the regular width.
