# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/fruktur/Fruktur-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea descent from -540 to -537 | OS/2 sTypoDescender from -540 to -537 | OS/2 usWinDescent from 540 to 537

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: This font lacks a POSTSCRIPT_NAME entry (nameID=6) in the name table.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: This font lacks a FULL_FONT_NAME entry (nameID=4) in the name table.

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Fruktur" does not match post_script_name = "Fruktur-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2013, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com) with Reserved Font Name 'Fruktur'") contains "Reserved Font Name"

## Font styles are named canonically?
* ERROR: Fruktur-Regular.ttf: The font style is normal but it should be italic

