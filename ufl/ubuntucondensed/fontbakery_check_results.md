# Fontbakery check results
## Check font has a license
* ERROR: No license file was found. Please add an OFL.txt or a LICENSE.txt file.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ufl/ubuntucondensed/UbuntuCondensed-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 932 to 973 | OS/2 sTypoAscender from 776 to 973 | OS/2 usWinAscent from 932 to 973 | hhea descent from -189 to -195 | OS/2 sTypoDescender from -185 to -195 | OS/2 usWinDescent from 189 to 195 | hhea lineGap from 28 to 0 | OS/2 sTypoLineGap from 56 to 0

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font has a valid license url ?
* ERROR: LicenseUrl is required and must be a valid URL. Got False instead.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Dalton Maag' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Ubuntu Condensed" does not match post_script_name = "UbuntuCondensed-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Ubuntu Condensed") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Ubuntu Condensed Regular', u'Ubuntu Condensed Italic']] but Ubuntu Condensed

