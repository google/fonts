
[Variable fonts](/glossary/variable_fonts)—officially known as [OpenType](/glossary/open_type) Font Variations—remove the explicit distinctions between different [weights](/glossary/weight) and [styles](/glossary/style), which have existed since the early days of typesetting. It’s no exaggeration to say that this represents a huge leap forward in [font](/glossary/font) technology in recent years.

With variable fonts, the choice of exactly how heavy or slanted or wide (or any other parameter) type should be is placed into the hands of the user, rather than having those decided for us by the [type designer](/glossary/type_designer). Traditionally, all possible weights and styles have been separated out into different font files, whereas variable fonts combine all of those variations into one. Because of this, overall [file size](/glossary/file_size) is greatly reduced compared to loading multiple individual font files—and that’s a key consideration for [web typography](/lesson/using_web_fonts).

(Did you know you can browse for *just* variable fonts using the “Show only variable fonts” checkbox on [Google Fonts](https://fonts.google.com/?vfonly=true)?)

<figure>

![An abstract representation of multiple non-variable font files versus on single variable font file. On the left, multiple individual font files are shown, each displaying the character “a” in varying weights and widths. On the right, a single font file showing many more width and weight variations.](images/thumbnail.svg)

</figure>

The simplest way to think of variable fonts is to imagine a slider (actually called an [axis](/glossary/axis_in_variable_fonts)), with the lightest weight (usually called something like thin or extra light) at one end, regular in the middle, and the heaviest weight (usually called something like black or ultra) at the other. Where traditionally we’ve had to choose weights from specific points on that scale—determined by the [type designer](/glossary/type_designer) during font production—we can now choose *any* point on the scale. Rather than decide between using a bold font at the value of 700 (which might not feel heavy enough), or an extra bold font at the value of 800 (which might feel *too* heavy), we can now choose somewhere in the middle, such as 742 (just right!).

<figure>

![A range showing font-weight, from the lightest at 0 on the left, to the heaviest at 1000 on the right. One weight is highlighted with the value of 742 on the scale.](images/1.8.2.svg)

</figure>

However, the real power of variable fonts is that you can have *any* axis for any variable the type designer chooses. Slant? Yes. Width? Yes. [Optical size](/glossary/optical_sizes)? Yes. *[Temperature?!?](https://codepen.io/mandymichael/pen/pxXNbr)* Yes!

By the way, it’s important to note that those traditional points—bold, regular, extra bold, etc. for weight; upright and italic for style; body and display for optical sizing—still appear as styles in font menus (they’re referred to as “named [instances](/glossary/instance)”), so using variable fonts doesn’t mean waving goodbye to the labels and conveniently-shared variants that we’ve been used to.

<figure>

![A range showing font-weight, from the lightest at 0 on the left, to the heaviest at 1000 on the right. Two named instances—“Regular” and “Bold” are highlighted on the scale.](images/1.8.3.svg)

</figure>

The best way to understand variable fonts is to start playing with them—and in a way that doesn’t require you to install any [font files](/glossary/font) or write any code. So we’ve put together a few recommendations on what to try and the results to look out for.

Go to [etceteratype.co/epilogue](https://etceteratype.co/epilogue) and play with the **weight** axis of Epilogue to see how it affects the overall spacing of the type:

<figure>

![The word “thicken” is rendered twice: on the left, it appears in a light font-weight; on the right, a heavy one. The heavier weight also takes up more horizontal space. Beneath both versions are representations of the variable axes.](images/1.8.4.svg)

</figure>

Now go to [etceteratype.co/grandstander](https://etceteratype.co/grandstander) and compare that with Grandstander, which was designed to take up the same amount of horizontal space regardless of changes made to the weight axis.

<figure>

![The word “occupy” is rendered twice: on the left, it appears in a light font-weight; on the right, a heavy one. Both versions, despite their difference in weight, occupy the same horizontal space. Beneath both versions are representations of the variable axes.](images/1.8.5.svg)

</figure>

Go to [etceteratype.co/anybody](https://etceteratype.co/anybody) and play with the **width** axis on Anybody to see how it affects the width of each character:

<figure>

![The word “spacious” is rendered twice: on the left, it appears in a narrow form; on the right, a wide one. Each version occupies a radically different amount of horizontal space. Beneath both versions are representations of the variable axes.](images/1.8.6.svg)

</figure>

Go to [etceteratype.co/imbue](https://etceteratype.co/imbue) and play with the **optical size** axis of Imbue to see how the [contrast](/glossary/contrast) increases or decreases as you move the slider:

<figure>

![The word “subtlety” is rendered twice: on the left, it appears with low stroke contrast; on the right, the contrast is greater and the spacing between each character is reduced. Beneath both versions are representations of the variable axes.](images/1.8.7.svg)

</figure>

Go to [fonts.google.com/specimen/EB+Garamond](https://fonts.google.com/specimen/EB+Garamond) and play with the **[italic](/glossary/italic)** axis of EB Garamond to see how the design “snaps” between roman and italic styles, with no intermediate values:

<figure>

![The word “jumpstart” is rendered twice: on the left, it appears in an upright form; on the right, it’s italicized. Beneath both versions are representations of the variable axes, but—unlike the other illustrations on this page—the colors used suggest the “snap” between the upright and italic forms rather than a graduation.](images/1.8.8.svg)

</figure>

Go to [recursive.design](https://www.recursive.design/) and play with the “casual” axis of Recursive to see how the outlines become more curvy and playful. Note that this is an example of a [custom axis](/lesson/styling_type_on_the_web_with_variable_fonts).

<figure>

![The word “suited” is rendered twice: on the left, the strokes are straight; on the right, they flair out, with grater contrast between the thicks and thins—a much more playful style. Beneath both versions are representations of the variable axes.](images/1.8.9.svg)

</figure>

Go to [very-able-fonts.com](http://www.very-able-fonts.com/) and play with the “latin to braille” axis of Safari Braille to see how the type changes from—you guessed it—Latin to Braille. Note that this is another example of a [custom axis](/lesson/styling_type_on_the_web_with_variable_fonts), and, while more of a technical demonstration than something that could be used day-to-day, it’s a great illustration of what’s possible with variable fonts.

<figure>

![The letters “abcde” are rendered twice: on the left, they’re recognisable as their Latin forms; on the right, they resemble braille. Beneath both versions are representations of the variable axes.](images/1.8.10.svg)

</figure>

For more chances to play around with variable fonts directly in your browser, consider visiting these websites:

- [Axis-Praxis](https://www.axis-praxis.org/specimens/__DEFAULT__)
- [Font Playground](https://play.typedetail.com)
- [Variable Fonts](https://v-fonts.com)
- [Very Able Fonts](http://www.very-able-fonts.com)
- [Variablefonts.io](http://variablefonts.io/)
