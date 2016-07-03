# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'Alts' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/gfsdidot/GFSDidot-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 947 to 1145 | OS/2 sTypoAscender from 703 to 1145 | OS/2 usWinAscent from 947 to 1145 | hhea descent from -277 to -336 | OS/2 sTypoDescender from -271 to -336 | OS/2 usWinDescent from 277 to 336 | hhea lineGap from 25 to 0 | OS/2 sTypoLineGap from 50 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/gfsdidot: Glyph 0x00A0 is called "ch202": Change to "nbsp" or "uni00A0"

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/gfsdidot space 352 nbsp 250: Fixed nbsp advanceWidth to 352

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (2) is not 15

## Does full font name begin with the font family name?
* ERROR: Font family name 'GFS Didot' does not begin with full font name 'GFS Didot Regular'

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Greek Font Society' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'greek']) missing 'latin'

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("GFS Didot Regular") ends with "Italic"

