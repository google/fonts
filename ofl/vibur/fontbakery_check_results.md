# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/vibur/Vibur-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: OS/2 sTypoAscender from 1638 to 1960 | OS/2 sTypoDescender from -410 to -792 | hhea lineGap from 184 to 0 | OS/2 sTypoLineGap from 184 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/vibur space 797 nbsp 796: Fixed nbsp advanceWidth to 797

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* ERROR: Font is missing the GASP table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Vibur-Regular.ttf" does not match post_script_name="Vibur." (Consider removing the '-Regular' suffix from the filename.)

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Vibur") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Vibur") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Vibur Regular', u'Vibur Italic']] but Vibur

