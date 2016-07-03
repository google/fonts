# Fontbakery check results
## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/hanuman/Hanuman-Bold.ttf: Windows-only Opentype-specific StyleName set to "Bold".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 2000 to 2004 | OS/2 sTypoAscender from 2000 to 2004 | OS/2 usWinAscent from 2000 to 2004 | hhea descent from -1000 to -1032 | OS/2 sTypoDescender from -1000 to -1032 | OS/2 usWinDescent from 1000 to 1032 | hhea lineGap from 87 to 0 | OS/2 sTypoLineGap from 87 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/hanuman: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font family name 'Hanuman' does not begin with full font name 'Hanuman Bold'

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

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Hanuman Bold") ends with "Italic"

## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'ldsc' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Checking OS/2 usWeightClass
* HOTFIX: OS/2 usWeightClass Fixes: OS/2 usWeightClass from 300 to 400

## Checking fsSelection REGULAR bit
* HOTFIX: fsSelection REGULAR bit Fixes: OS/2 fsSelection from 0 to 64

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/hanuman/Hanuman-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 2000 to 2004 | OS/2 sTypoAscender from 2000 to 2004 | OS/2 usWinAscent from 2000 to 2004 | hhea descent from -1000 to -1032 | OS/2 sTypoDescender from -1000 to -1032 | OS/2 usWinDescent from 1000 to 1032 | hhea lineGap from 87 to 0 | OS/2 sTypoLineGap from 87 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/hanuman: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

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
* ERROR: METADATA.pb filename="Hanuman-Regular.ttf" does not match post_script_name="Hanuman." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Hanuman") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Hanuman") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Hanuman Regular', u'Hanuman Italic']] but Hanuman

