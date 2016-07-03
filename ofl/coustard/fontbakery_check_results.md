# Fontbakery check results
## Fonts have equal numbers of glyphs?
* ERROR: Fonts have different numbers of glyphs.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Fonts have equal numbers of glyphs?
* ERROR: Fonts have different numbers of glyphs.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'newt' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Checking fsSelection BOLD bit
* HOTFIX: fsSelection BOLD bit Fixes: OS/2 fsSelection from 32 to 0

## Checking macStyle BOLD bit
* HOTFIX: macStyle BOLD bit Fixes: head macStyle from 1 to 0

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## Checking name table for items without platformID = 1 (MACHINTOSH)
* HOTFIX: some name table items with platformID=1 were removed
* HOTFIX: Namerecord 10s (descriptions) were removed (perhaps added by a longstanding FontLab Studio 5.x bug.)

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/coustard/Coustard-Black.ttf: Windows-only Opentype-specific StyleName set to "Bold".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/coustard space 442 nbsp 250: Fixed nbsp advanceWidth to 442

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: GPOS table seems to be corrupted.

## Does full font name begin with the font family name?
* ERROR: Font family name 'Coustard' does not begin with full font name 'Coustard-Black'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## Copyright notice is the same in all fonts ?
* ERROR: METADATA.pb: Copyright field value is inconsistent across family

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Vernon Adams (vern@newtypography.co.uk) with Reserved Font Names "Coustard" and "Coustard Black". This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Coustard-Black") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Coustard BlackItalic', u'Coustard Black']] but Coustard-Black

## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'newt' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## Checking name table for items without platformID = 1 (MACHINTOSH)
* HOTFIX: some name table items with platformID=1 were removed
* HOTFIX: Namerecord 10s (descriptions) were removed (perhaps added by a longstanding FontLab Studio 5.x bug.)

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/coustard/Coustard-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/coustard space 500 nbsp 86: Fixed nbsp advanceWidth to 500

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: GPOS table seems to be corrupted.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## Copyright notice is the same in all fonts ?
* ERROR: METADATA.pb: Copyright field value is inconsistent across family

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Coustard-Regular.ttf" does not match post_script_name="Coustard." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Vernon Adams (vern@newtypography.co.uk) with Reserved Font Names "Coustard" and "Coustard Regular". This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Coustard") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Coustard") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Coustard Regular', u'Coustard Italic']] but Coustard

