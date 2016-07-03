# Fontbakery check results
## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'newt' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/cutive/Cutive-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking if the font is truly monospaced
* HOTFIX: Font is not monospaced. Fixes: hhea advanceWidthMax from 3564 to 3570

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 1473 to 2364 | OS/2 sTypoAscender from 2363 to 2364 | OS/2 usWinAscent from 2363 to 2364 | hhea descent from -575 to -785 | OS/2 sTypoDescender from 804 to -785 | OS/2 usWinDescent from 804 to 785 | hhea lineGap from 200 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Cutive" does not match post_script_name = "Cutive-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, vernon adams (vern@newtypography.co.uk), with Reserved Font Names "Cutive"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Cutive") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Cutive Regular', u'Cutive Italic']] but Cutive

