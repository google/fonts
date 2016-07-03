# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'PfEd', a font editor default. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/vt323/VT323-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* ERROR: Font is missing the GASP table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Peter Hull' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="VT323" does not match post_script_name = "VT323-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Peter Hull (peter.hull@oikoi.com), with Reserved Font Name "VT323".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("VT323") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'VT323 Regular', u'VT323 Italic']] but VT323

## Monospace font has hhea.advanceWidthMax equal to each glyph's advanceWidth ?
* ERROR: Glyph advanceWidth must be same across all glyphs

