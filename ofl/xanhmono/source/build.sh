#!/bin/sh

#===========================================================================
#Update this variable ==========================================================

thisFont="XanhMono"  #must match the name in the font file

#===========================================================================
#Generating fonts ==========================================================

#source ../env/bin/activate
set -e


echo ".
GENERATING STATIC TTF
."
rm -rf ../fonts/ttf
mkdir -p ../fonts/ttf

fontmake -g $thisFont.glyphs -i -o ttf --output-dir ../fonts/ttf
fontmake -g $thisFont-Italic.glyphs -i -o ttf --output-dir ../fonts/ttf

echo ".
GENERATING STATIC OTF
."
rm -rf ../fonts/otf
mkdir -p ../fonts/otf

fontmake -g $thisFont.glyphs -i -o otf --output-dir ../fonts/otf
fontmake -g $thisFont-Italic.glyphs -i -o otf --output-dir ../fonts/otf

#============================================================================
#Post-processing fonts ======================================================

echo ".
POST-PROCESSING TTF
."
ttfs=$(ls ../fonts/ttf/*.ttf)
for font in $ttfs
do
	gftools fix-dsig --autofix $font
	ttfautohint $font $font.fix
	[ -f $font.fix ] && mv $font.fix $font
	gftools fix-hinting $font
	[ -f $font.fix ] && mv $font.fix $font
done

echo ".
POST-PROCESSING OTF
."
otfs=$(ls ../fonts/otf/*.otf)
for font in $otfs
do
	gftools fix-dsig --autofix $font
done


#============================================================================
#Build woff and woff2 fonts =================================================
#requires https://github.com/bramstein/homebrew-webfonttools

echo ".
BUILD WEBFONTS
."
rm -rf ../fonts/webfonts
mkdir -p ../fonts/webfonts

ttfs=$(ls ../fonts/ttf/*.ttf)
for font in $ttfs
do
  woff2_compress $font
  sfnt2woff-zopfli $font
done

woffs=$(ls ../fonts/ttf/*.woff*)
for font in $woffs
do
	mv $font ../fonts/webfonts
done

rm -rf master_ufo/ instance_ufo/


echo ".
COMPLETE!
."
