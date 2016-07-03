# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/blackopsone/BlackOpsOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does full font name begin with the font family name?
* ERROR: Font family name 'Black Ops One' does not begin with full font name 'BlackOpsOne-Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "BlackOpsOne-Regular" while METADATA.pb has "Black Ops One"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Black Ops One" does not match post_script_name = "BlackOpsOne-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com) with Reserved Font Names "Black Ops" and "Black Ops One".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("BlackOpsOne-Regular") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb: Fullname ('Black Ops One') does not match name table entry 'BlackOpsOne-Regular' !

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Black Ops One Regular', u'Black Ops One Italic']] but Black Ops One

