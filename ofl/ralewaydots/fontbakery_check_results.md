# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/ralewaydots/RalewayDots-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 918 to 940 | OS/2 sTypoAscender from 918 to 940 | OS/2 usWinAscent from 918 to 940 | hhea descent from -213 to -218 | OS/2 sTypoDescender from -213 to -218 | OS/2 usWinDescent from 213 to 218

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

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

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Multiple Designers' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "Raleway Dots " while METADATA.pb has "Raleway Dots"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "Raleway Dots " while METADATA.pb has "Raleway Dots"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "Raleway Dots " while METADATA.pb has name="Raleway Dots"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Raleway Dots" does not match post_script_name = "RalewayDots-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb 'name' contains font name in right format ?
* ERROR: METADATA.pb name='Raleway Dots' does not match correct font name format.

## METADATA.pb 'full_name' contains font name in right format ?
* ERROR: METADATA.pb full_name='Raleway Dots' does not match correct font name format.

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2010 - 2012, Matt McInerney (matt@pixelspread.com), Pablo Impallari(impallari@gmail.com), Rodrigo Fuenzalida (hello@rfuenzalida.com) and Brenda Gallo(gbrenda1987@gmail.com), with Reserved Font Name "Raleway"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Raleway Dots ") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Raleway Dots') does not match name table entry 'Raleway Dots ' !

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Raleway Dots  Regular', u'Raleway Dots  Italic']] but Raleway Dots

