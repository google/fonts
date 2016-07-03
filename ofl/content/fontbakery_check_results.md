# Fontbakery check results
## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/content/Content-Bold.ttf: Windows-only Opentype-specific StyleName set to "Bold".

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: maxp: bad max_zones: 0



## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea lineGap from 67 to 0 | OS/2 sTypoLineGap from 307 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/content: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM, prop

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font family name 'Content' does not begin with full font name 'Content Bold'

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font has a valid license url ?
* ERROR: LicenseUrl is required and must be a valid URL. Got False instead.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'khmer']) missing 'latin'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2010, Danh Hong (khmertype.blogspot.com danhhong@gmail.com), with Reserved Font Name Khmer OS Content. This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Content Bold") ends with "Italic"

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/content/Content-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: maxp: bad max_zones: 0



## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea lineGap from 67 to 0 | OS/2 sTypoLineGap from 307 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/content: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM, prop

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font has a valid license url ?
* ERROR: LicenseUrl is required and must be a valid URL. Got False instead.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'khmer']) missing 'latin'

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Content-Regular.ttf" does not match post_script_name="Content." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2010, Danh Hong (khmertype.blogspot.com danhhong@gmail.com), with Reserved Font Name Khmer OS Content. This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Content") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Content") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Content Regular', u'Content Italic']] but Content

