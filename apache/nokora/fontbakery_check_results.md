# Fontbakery check results
## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Fonts have equal glyph names?
* ERROR: Fonts have different glyph names.

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## substitute copyright, registered and trademark symbols in name table entries
* HOTFIX: Name table entries were modified to replace unicode symbols such as (c), (r) and TM.

## Check copyright namerecords match license file
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/apache/nokora/Nokora-Bold.ttf: Windows-only Opentype-specific StyleName set to "Bold".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 1907 to 1908 | OS/2 sTypoAscender from 1567 to 1908 | OS/2 usWinAscent from 1907 to 1908 | OS/2 sTypoDescender from -492 to -800 | OS/2 sTypoLineGap from 132 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

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
* ERROR: Font family name 'Nokora' does not begin with full font name 'Nokora Bold'

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'khmer']) missing 'latin'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Nokora Bold") ends with "Italic"

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## substitute copyright, registered and trademark symbols in name table entries
* HOTFIX: Name table entries were modified to replace unicode symbols such as (c), (r) and TM.

## Check copyright namerecords match license file
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/apache/nokora/Nokora-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 1907 to 1908 | OS/2 sTypoAscender from 1567 to 1908 | OS/2 usWinAscent from 1907 to 1908 | OS/2 sTypoDescender from -492 to -800 | OS/2 sTypoLineGap from 132 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

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

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'khmer']) missing 'latin'

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: Unmatched postscript name in font: TTF has "Nokora-Regular" while METADATA.pb has "Nokora"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Nokora-Regular.ttf" does not match post_script_name="Nokora." (Consider removing the '-Regular' suffix from the filename.)

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Nokora") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Nokora") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Nokora Regular', u'Nokora Italic']] but Nokora

