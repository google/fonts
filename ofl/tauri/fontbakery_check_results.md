# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/tauri/Tauri-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font family name 'Tauri' does not begin with full font name 'Tauri-Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Are there non-ASCII characters in ASCII-only NAME table entries ?
* ERROR: There are 4 strings containing non-ASCII characters in the ASCII-only NAME table entries.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* Warning: Failed to fetch 'https://raw.githubusercontent.com/google/fonts/master/designers/profiles.csv'

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: Unmatched postscript name in font: TTF has "TauriRegular" while METADATA.pb has "Tauri-Regular"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "Tauri-Regular" while METADATA.pb has "Tauri Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com) with Reserved Font Name 'Tauri'.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Tauri-Regular") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb: Fullname ('Tauri Regular') does not match name table entry 'Tauri-Regular' !

