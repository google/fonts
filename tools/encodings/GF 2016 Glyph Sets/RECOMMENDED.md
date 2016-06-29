
Recommended additions 
====================================================
to [Google Fonts 2016 Glyph Sets](README.md)

Although **Plus, Pro and Expert** sets provide extensive language coverage there may be particular design cases where additional characters would be helpful to have. 

Here is a list of popular ligatures that are recommended for addition on a case-to-case basis:

	f_b
	f_f_b
	f_h
	f_f_h
	f_j
	f_f_j
	f_k
	f_f_k
	f_t
	f_f_t
	c_k
	c_p
	e_t
	l_l
	s_p
	t_h
	t_t
	t_z

Armenian Dram currency symbol is a recommended addition to any Cyrillic-supporting fonts, due to popular use of Russian in Armenian community

	0x058F  ֏ dram-arm
	
	
***
### STRASSE or Straße? ###

The Google Lating Plus encoding includes **ẞ Germandbls U+1E9E**. 

Does your font include Small Capitals?
For better compatibility you may consider adding the germandbls.calt glyph to access ẞ U+1E9E in Small Caps fonts. In Glyphs go to *Glyph > Add Glyphs*, and paste this code:

	Germandbls=germandbls.calt
	
Add this calt feature:

	sub @Uppercase germandbls' @Uppercase by germandbls.calt;
	sub @Uppercase @Uppercase germandbls' by germandbls.calt;

Recommended links for further reading: 

 * [How to draw a Capital Sharp S](https://typography.guru/journal/how-to-draw-a-capital-sharp-s-r18/) by Ralf Herrmann

 * [Localize Your Font: German Capital Sharp S](https://www.glyphsapp.com/tutorials/localize-your-font-german-capital-sharp-s) by Rainer Erich Scheichelbauer  

N.B. The question of German Uppercase Capital Sharp S is still highly debatable, and its usage hasn't passed into the official orthography. 


### Recommended links: ###

Pablo Impallari's [Latin encoding](https://github.com/impallari/Impallari-Fontlab-Encodings/tree/master/Impallari%20Latin)
