# Fontbakery check results
## Fonts have equal numbers of glyphs?
* ERROR: Fonts have different numbers of glyphs.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Fonts have equal numbers of glyphs?
* ERROR: Fonts have different numbers of glyphs.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## substitute copyright, registered and trademark symbols in name table entries
* HOTFIX: Name table entries were modified to replace unicode symbols such as (c), (r) and TM.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/nanumgothiccoding/NanumGothicCoding-Bold.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 800 to 809 | OS/2 sTypoAscender from 800 to 809 | OS/2 usWinAscent from 800 to 809 | hhea descent from -200 to -207 | OS/2 sTypoDescender from -200 to -207 | OS/2 usWinDescent from 200 to 207

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/nanumgothiccoding: Glyph 0x0020 is called "uni0000": Change to "space" or "uni0020"
* ERROR: /home/felipe/devel/github_google/fonts/ofl/nanumgothiccoding: Glyph 0x00A0 is called "uni0000": Change to "nbsp" or "uni00A0"

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Are there non-ASCII characters in ASCII-only NAME table entries ?
* ERROR: There are 2 strings containing non-ASCII characters in the ASCII-only NAME table entries.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Nanum+Gothic+Coding

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Sandoll Communication' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'korean']) missing 'latin'

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: This font lacks a POSTSCRIPT_NAME entry (nameID=6) in the name table.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: This font lacks a FULL_FONT_NAME entry (nameID=4) in the name table.

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## substitute copyright, registered and trademark symbols in name table entries
* HOTFIX: Name table entries were modified to replace unicode symbols such as (c), (r) and TM.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/nanumgothiccoding/NanumGothicCoding-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 800 to 809 | OS/2 sTypoAscender from 800 to 809 | OS/2 usWinAscent from 800 to 809 | hhea descent from -200 to -207 | OS/2 sTypoDescender from -200 to -207 | OS/2 usWinDescent from 200 to 207

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/nanumgothiccoding: Glyph 0x0020 is called "uni0000": Change to "space" or "uni0020"
* ERROR: /home/felipe/devel/github_google/fonts/ofl/nanumgothiccoding: Glyph 0x00A0 is called "uni0000": Change to "nbsp" or "uni00A0"

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Are there non-ASCII characters in ASCII-only NAME table entries ?
* ERROR: There are 2 strings containing non-ASCII characters in the ASCII-only NAME table entries.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Nanum+Gothic+Coding

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Sandoll Communication' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'korean']) missing 'latin'

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: This font lacks a POSTSCRIPT_NAME entry (nameID=6) in the name table.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: This font lacks a FULL_FONT_NAME entry (nameID=4) in the name table.

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="NanumGothicCoding-Regular.ttf" does not match post_script_name="NanumGothicCoding." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("NanumGothicCoding") with weight 400 must be ended with "Regular" or "Italic"

