# github.com/google/fonts.git repo trivia

## Duplicated fonts

There are some similarly named pairs of directories which each have identically named font files. 
These files are redundant, and exist following the renaming of a family.
The initial directories are kept so that people already using that initial name can continue to do so. 
They are no longer listed in the main www.google.com/fonts directory, but the files exist in this repo since they are still served via the Google Fonts API. 

- `ofl/mrbedford` and `ofl/mrbedfort` contain `MrBedfort-Regular.ttf`
- `ofl/mrssaintdelafield` and `ofl/misssaintdelafield` contain `MrsSaintDelafield-Regular.ttf`
- `ofl/siamreap` and `ofl/siemreap` contain `Siemreap.ttf`
- `ofl/terminaldosis` and `ofl/dosis` contain the same files (renamed) and `ofl/terminaldosislight` contain `TerminalDosis-Light.ttf`

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
* http://www.typegenius.com/

There are also handcrafted directories with rich samples:

* http://hellohappy.org/beautiful-web-type/
* http://femmebot.github.io/google-type/
* http://100daysoffonts.com
* http://jxnblk.com/type-a/
