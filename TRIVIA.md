# github.com/google/fonts.git repo trivia

## Incomplete greek-ext subsets 

Open Sans (and some others, like Roboto) are advertised as they supporting Extended Greek, but choosing the greek-ext subset will not display Open Sans (or the required font) for this range because they don't actually contain the required characters.
You're welcome to commission these characters, though.

## Google Fonts Repo Wiki

The previous fonts Mercurial repository had a wiki at <https://code.google.com/p/googlefontdirectory/wiki> which is no longer available. 
The contents of the wiki are now available here:

<https://github.com/googlefonts/gf-docs>

## Duplicated fonts

There are some similarly named pairs of directories which each have identically named font files. 
These files are redundant, and exist following the renaming of a family.
The initial directories are kept so that people already using that initial name can continue to do so. 
They are no longer listed in the main www.google.com/fonts directory, but the files exist in this repo since they are still served via the Google Fonts API. 

- `ofl/alefhebrew` and `ofl/alef` contain `Alef-Regular.ttf` and `Alef-Bold.ttf`
- `ofl/mrbedford` and `ofl/mrbedfort` contain `MrBedfort-Regular.ttf`
- `ofl/mrssaintdelafield` and `ofl/misssaintdelafield` contain `MrsSaintDelafield-Regular.ttf`
- `ofl/siamreap` and `ofl/siemreap` contain `Siemreap.ttf`
- `ofl/terminaldosis` and `ofl/dosis` contain the same files (renamed) and `ofl/terminaldosislight` contain `TerminalDosis-Light.ttf`

## Missing METADATA.pb files

Fonts in Early Access do not have METADATA.pb files.

## Install on Windows

You can install all of the fonts using Windows PowerShell. Change directories to the folder where you downloaded the package, and run the following command:
```
$fonts = (New-Object -ComObject Shell.Application).Namespace(0x14)
dir ofl/*/*.ttf | %{ $fonts.CopyHere($_.fullname) }
```

## 3rd Party Directories

The www.google.com/fonts directory is accompanied by a [Google Fonts Developer API](https://developers.google.com/fonts/docs/developer_api) which provides raw data for constructing such a directory in JSON format. 
Here is a list of 3rd party directories:

* <http://font-combinator.com> + <http://chipcullen.com/font-combinator>
* <https://www.typetester.org>
* <http://font-combinator.com>
* <http://somadesign.ca/demos/better-google-fonts>
* <http://fontapp.org>
* <http://fontapp.org/graph>
* <http://katydecorah.com/font-library>
* <http://fontcdn.org>
* <http://googlefontsdirectory.org>
* <https://hail2u.github.io/mn>
* <http://fontflame.com>
* <http://jenniferdewalt.com/gfboom/page>
* <http://fontpair.co>
* <https://typ.io>
* <http://andreasweis.com/webfontblender>
* <http://www.typegenius.com>
* <http://abbychen.me/punch>
* <http://typewonder.com>
* <http://www.localfont.com>
* <http://open-foundry.com>
* <https://typeresources.github.io/glyph-gazer>
* <http://cdn.canelodigital.cl/fonts>
* <http://code.thisarmy.com/fontsinfo>
* <http://www.localfont.com>
* <http://brandmark.io/font-generator>
* <http://archetypeapp.com>
* <https://getflourish.github.io/anatomy-of-typefaces>
* <https://tyffle.ml>
* <https://lepovirta.github.io/Typographer> 
* <https://lepovirta.github.io/Typographer-React>
* <https://jmattthew.github.io/better-font-finder/better-font-finder.html>

There are also handcrafted directories with rich samples:

* <http://hellohappy.org/beautiful-web-type>
* <http://femmebot.github.io/google-type>
* <http://100daysoffonts.com>
* <http://jxnblk.com/type-a>
* <https://jonsuh.com/100-days-of-scriptures>
* <http://codepen.io/nxworld/pen/XKRaRm>
* <https://twitter.com/FontSnek>
* <https://www.reliablepsd.com/ultimate-google-font-pairings>
* <http://fonts.greatsimple.io>

## Rightsholder contacts

This shell command shows all email addresses for font copyright holders listed in the METADATA.pb files:

    grep copyright\: */*/MET* | grep \@ |  perl -ne'if(/[\w\.\-\_]+@([\w\-\_]+\.)+[A-Za-z]{2,4}/g){print "$&\n"}' | sort | uniq

This shell command shows all the families without a contact email address:

    grep copyright\: */*/MET* | grep -v \@ | cut -d\: -f1 | cut -d\/ -f2 | uniq | sort

The copyright holders of those families are mostly Google, SIL, Adobe, Canonical, Naver, and a couple of outliers. 

## Articles about Google Fonts

Some interesting articles about Google Fonts:

* <http://googlecode.blogspot.com/2010/05/introducing-google-font-api-google-font.html>
* <http://googlewebfonts.blogspot.com>
* <https://design.google.com/articles/reimagining-google-fonts>
* <https://medium.com/google-design/introducing-space-mono-a-new-monospaced-typeface-by-colophon-foundry-for-google-fonts-84367eac6dfb>
* <http://www.fastcodesign.com/3033126/roboto-rebooted-why-google-plans-to-update-its-font-like-the-rest-of-its-products>

## Interesting Libre Fonts Not In Google Fonts

Here is a list of some libre fonts made for special purposes (emoij, math, icon, etc) are not available in Google Fonts. 

* <https://material.io/icons>
* <https://github.com/figs-lab/datalegreya>
