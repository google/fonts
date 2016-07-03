# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'PfEd', a font editor default. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/digitalnumbers/DigitalNumbers-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking if the font is truly monospaced
* HOTFIX: Font is monospaced but 3 glyphs (1.1673151751%) have a different width. You should check the widths of: ['comma', '.notdef', 'period'] Fixes: post isFixedPitch from 0 to 1 | OS/2 panose.bProportion from 3 to 9

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (2) is not 15

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Digital+Numbers

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Stephan Ahlf' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: This font lacks a POSTSCRIPT_NAME entry (nameID=6) in the name table.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: This font lacks a FULL_FONT_NAME entry (nameID=4) in the name table.

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Digital Numbers" does not match post_script_name = "DigitalNumbers-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Monospace font has hhea.advanceWidthMax equal to each glyph's advanceWidth ?
* ERROR: Glyph advanceWidth must be same across all glyphs

