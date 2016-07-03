# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'newt' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/bowlbyonesc/BowlbyOneSC-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does full font name begin with the font family name?
* ERROR: Font family name 'Bowlby One SC' does not begin with full font name 'Bowlby One SC Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, vernon adams (vern@newtypography.co.uk), with Reserved Font Names "Bowlby"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Bowlby One SC Regular") ends with "Italic"

