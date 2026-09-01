
Kerning is the manual adjustment of the spacing between two specific [glyphs](/glossary/glyph). A kerning pair is the same adjustment, but determined by the [type designer](/glossary/type_designer)—with the instructions embedded directly within in a [font](/glossary/font) file.

<figure>

![The word “WAVE" shown with some manual kerning adjustments to make the spaces between the letterforms more visually pleasing.](images/thumbnail.svg)

</figure>

Novice [typographers](/glossary/typographer) mistakenly talk about kerning when they actually mean [tracking (or “letter-spacing” in CSS)](/glossary/tracking_letter_spacing). Kerning is all about the customized spacing between two particular glyphs, whereas tracking is the spacing between glyphs applied to an entire piece of text.

Kerning was originally only applied in pairs, but most modern fonts use class kerning. Letters with related shapes form a class so they can be kerned as a group, resulting in much more kerning with much less data stored in the font. For example, instead of just kerning V to A, V and W might be in one class, and A and all its accented variants in another class.

[Turning on “kerning” via OpenType in CSS](/lesson/manual_kerning_is_rarely_required) enables the kerning pair data already in the font file. Note that it’s turned on by default in most modern browsers, but can be disabled with `font-kerning: none;`.
