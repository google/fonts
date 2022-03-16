
Width (wdth in CSS) is an axis found in some variable fonts. It controls the font file’s width. 

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

Default: 100     Min: 25     Max: 200     Step: 0.1

<figure>

![ALT_TEXT](images/thumbnail.svg)
<figcaption>CAPTION</figcaption>

</figure>

Width is the result of how much horizontal space is taken up by a typeface’s characters. A condensed face takes up considerably less space than a wide one.

In CSS, we can assign a variable width to an element of our choosing using the font-stretch property. (Despite the name, note that the type is never literally “stretched” by browsers. This property name was chosen to make the concept more accessible to a general audience.)

<pre>
p {
  font-stretch: 50%;
}
strong {
  font-stretch: 193%;
}
</pre>

Here, our text will be quite narrow—50% is what the type designer has decided is half of the regular (100%) width—and the strong text will be almost twice the width of the regular. Width values are always above 0, with 100% being the regular width.
