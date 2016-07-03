# Fontbakery check results
## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/phetsarath/Phetsarath-Bold.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: maxp: bad max_zones: 0



## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/phetsarath: Glyph 0x0020 is called "nonmarkingreturn": Change to "space" or "uni0020"
* ERROR: /home/felipe/devel/github_google/fonts/ofl/phetsarath: Glyph 0x00A0 is called "nonmarkingreturn": Change to "nbsp" or "uni00A0"

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Phetsarath

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'lao']) missing 'latin'

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: This font lacks a POSTSCRIPT_NAME entry (nameID=6) in the name table.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: This font lacks a FULL_FONT_NAME entry (nameID=4) in the name table.

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/phetsarath/Phetsarath-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: maxp: bad max_zones: 0



## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/phetsarath: Glyph 0x0020 is called "nonmarkingreturn": Change to "space" or "uni0020"
* ERROR: /home/felipe/devel/github_google/fonts/ofl/phetsarath: Glyph 0x00A0 is called "nonmarkingreturn": Change to "nbsp" or "uni00A0"

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Phetsarath

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'lao']) missing 'latin'

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: This font lacks a POSTSCRIPT_NAME entry (nameID=6) in the name table.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: This font lacks a FULL_FONT_NAME entry (nameID=4) in the name table.

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

