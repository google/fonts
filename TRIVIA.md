# github.com/google/fonts.git repo trivia

## Google Fonts Repo Wiki

The previous fonts Mercurial repository had a wiki at <https://code.google.com/p/googlefontdirectory/wiki> which is no longer available. 
The contents of the wiki are now available here:

<https://github.com/googlefonts/gf-docs>

## Duplicated fonts

There are some similarly named pairs of directories which each have identically named font files. 
These files are redundant, and exist following the renaming of a family.
The initial directories are kept so that people already using that initial name can continue to do so. 
They are no longer listed in the main www.google.com/fonts directory, but the files exist in this repo since they are still served via the Google Fonts API. 

- `ofl/mrbedford` and `ofl/mrbedfort` contain `MrBedfort-Regular.ttf`
- `ofl/mrssaintdelafield` and `ofl/misssaintdelafield` contain `MrsSaintDelafield-Regular.ttf`
- `ofl/siamreap` and `ofl/siemreap` contain `Siemreap.ttf`
- `ofl/terminaldosis` and `ofl/dosis` contain the same files (renamed) and `ofl/terminaldosislight` contain `TerminalDosis-Light.ttf`

## Missing METADATA.pb files

Fonts in Early Access do not have METADATA.pb files.

### Install on Windows

You can install all of the fonts using Windows PowerShell. Change directories to the folder where you downloaded the package, and run the following command:
```
$fonts = (New-Object -ComObject Shell.Application).Namespace(0x14)
dir ofl/*/*.ttf | %{ $fonts.CopyHere($_.fullname) }
```

## 3rd Party Directories

The www.google.com/fonts directory is accompanied by a [Google Fonts Developer API](https://developers.google.com/fonts/docs/developer_api) which provides raw data for constructing such a directory in JSON format. 
Here is a list of 3rd party directories:

* http://font-combinator.com / http://chipcullen.com/font-combinator
* https://www.typetester.org
* http://font-combinator.com
* http://somadesign.ca/demos/better-google-fonts
* http://fontapp.org
* http://fontapp.org/graph
* http://katydecorah.com/font-library
* http://fontcdn.org
* http://googlefontsdirectory.org
* https://hail2u.github.io/mn
* http://fontflame.com
* http://jenniferdewalt.com/gfboom/page
* http://fontpair.co
* https://typ.io
* http://andreasweis.com/webfontblender
* http://www.typegenius.com
* http://abbychen.me/punch
* http://typewonder.com
* http://www.localfont.com
* http://open-foundry.com

There are also handcrafted directories with rich samples:

* http://hellohappy.org/beautiful-web-type/
* http://femmebot.github.io/google-type/
* http://100daysoffonts.com
* http://jxnblk.com/type-a/
* https://jonsuh.com/100-days-of-scriptures/

## Rightsholder contacts

This shell command shows all email addresses for font copyright holders listed in the METADATA.pb files:

    grep copyright\: */*/MET* | grep \@ |  perl -ne'if(/[\w\.\-\_]+@([\w\-\_]+\.)+[A-Za-z]{2,4}/g){print "$&\n"}' | sort | uniq

This shell command shows all the families without a contact email address:

    grep copyright\: */*/MET* | grep -v \@ | cut -d\: -f1 | cut -d\/ -f2 | uniq | sort

The copyright holders of those families are mostly Google, SIL, Adobe, Canonical, Naver, and a couple of outliers. 
