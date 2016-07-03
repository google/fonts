# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/prostoone/ProstoOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/prostoone: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

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

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Multiple Designers' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Prosto One" does not match post_script_name = "ProstoOne-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, Jovanny Lemonad (http://www.jovanny.ru), Copyright (c) 2012, Pavel Emelyanov (zakachka2006@mail.ru), with Reserved Font Name "Prosto" and "Prosto One".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Prosto One") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Prosto One Regular', u'Prosto One Italic']] but Prosto One

