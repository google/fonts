# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/hammersmithone/HammersmithOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 1844 to 1843 | OS/2 sTypoAscender from 1844 to 1843 | OS/2 usWinAscent from 1844 to 1843

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/hammersmithone space 679 nbsp 440: Fixed nbsp advanceWidth to 679

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font family name 'HammersmithOne' does not begin with full font name 'HammersmithOne Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "HammersmithOne" while METADATA.pb has "Hammersmith One"

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: Unmatched postscript name in font: TTF has "HammersmithOne-Regular" while METADATA.pb has "HammersmithOne"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "HammersmithOne Regular" while METADATA.pb has "Hammersmith One"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "HammersmithOne" while METADATA.pb has name="Hammersmith One"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="HammersmithOne-Regular.ttf" does not match post_script_name="HammersmithOne." (Consider removing the '-Regular' suffix from the filename.)

## METADATA.pb 'name' contains font name in right format ?
* ERROR: METADATA.pb name='Hammersmith One' does not match correct font name format.

## METADATA.pb 'full_name' contains font name in right format ?
* ERROR: METADATA.pb full_name='Hammersmith One' does not match correct font name format.

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Sorkin Type Co. (www.sorkintype.com eben@eyebytes.com) with Reserved Font Name "Hammersmith One". This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("HammersmithOne Regular") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Hammersmith One') does not match name table entry 'HammersmithOne' !

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("HammersmithOne") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'HammersmithOne Regular', u'HammersmithOne Italic']] but Hammersmith One

