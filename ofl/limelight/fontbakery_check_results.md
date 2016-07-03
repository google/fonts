# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/limelight/Limelight-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea descent from -629 to -636 | OS/2 sTypoDescender from -634 to -636 | OS/2 usWinDescent from 629 to 636

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font family name 'Limelight' does not begin with full font name 'Limelight Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: Unmatched postscript name in font: TTF has "Limelight-Regular" while METADATA.pb has "Limelight"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "Limelight Regular" while METADATA.pb has "Limelight"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Limelight-Regular.ttf" does not match post_script_name="Limelight." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2010 by Sorkin Type Co (eben@eyebytes.com) with Reserved Font Name Limelight. This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Limelight Regular") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb: Fullname ('Limelight') does not match name table entry 'Limelight Regular' !

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Limelight") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Limelight Regular', u'Limelight Italic']] but Limelight

