# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.
* HOTFIX: License file LICENSE.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/apache/calligraffitti/Calligraffitti-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: OS/2 sTypoAscender from 866 to 986 | OS/2 sTypoDescender from -457 to -607 | hhea lineGap from 14 to 0 | OS/2 sTypoLineGap from 28 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (1024) is not equal to 1000.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Calligraffitti" does not match post_script_name = "Calligraffitti-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Calligraffitti") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Calligraffitti Regular', u'Calligraffitti Italic']] but Calligraffitti

