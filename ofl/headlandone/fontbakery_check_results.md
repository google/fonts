# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/headlandone/HeadlandOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/headlandone space 758 nbsp 683: Fixed nbsp advanceWidth to 758

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font family name 'HeadlandOne' does not begin with full font name 'HeadlandOne-Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Are there non-ASCII characters in ASCII-only NAME table entries ?
* ERROR: There are 2 strings containing non-ASCII characters in the ASCII-only NAME table entries.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Gary Lonergan' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "HeadlandOne" while METADATA.pb has "Headland One"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "HeadlandOne-Regular" while METADATA.pb has "Headland One"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "HeadlandOne" while METADATA.pb has name="Headland One"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Headland One" does not match post_script_name = "HeadlandOne-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb 'name' contains font name in right format ?
* ERROR: METADATA.pb name='Headland One' does not match correct font name format.

## METADATA.pb 'full_name' contains font name in right format ?
* ERROR: METADATA.pb full_name='Headland One' does not match correct font name format.

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011-2012, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com), with Reserved Font Name "Headland"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("HeadlandOne-Regular") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Headland One') does not match name table entry 'HeadlandOne' !

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'HeadlandOne Regular', u'HeadlandOne Italic']] but Headland One

