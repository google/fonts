# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/underdog/Underdog-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 909 to 915 | OS/2 sTypoAscender from 909 to 915 | OS/2 usWinAscent from 909 to 915

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## Glyph names are all valid?
* ERROR: The following glyph names do not comply with naming conventions: ['.ttfautohint'] A glyph name may be up to 31 characters in length, must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). and must not start with a digit or period. There are a few exceptions such as the special character ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not.

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Multiple Designers' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Underdog" does not match post_script_name = "Underdog-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, Sergey Steblina (sergey@steblina.com), Jovanny Lemonad (lemonad@jovanny.ru), with Reserved Font Name 'Underdog'") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Underdog") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Underdog Regular', u'Underdog Italic']] but Underdog

