# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'DINR' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.

## Checking name table for items without platformID = 1 (MACHINTOSH)
* HOTFIX: some name table items with platformID=1 were removed
* HOTFIX: Namerecord 10s (descriptions) were removed (perhaps added by a longstanding FontLab Studio 5.x bug.)

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/apache/rochester/Rochester-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

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

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Rochester" does not match post_script_name = "Rochester-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Rochester") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Rochester Regular', u'Rochester Italic']] but Rochester

