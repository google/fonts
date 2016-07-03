# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/lilitaone/LilitaOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: OS/2 sTypoAscender from 922 to 923 | OS/2 sTypoDescender from -219 to -220

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="LilitaOne-Regular.ttf" does not match post_script_name="LilitaOne." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011 Juan Montoreano (juan@remolacha.biz), with Reserved Font Names "Lilita One"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Lilita One") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("LilitaOne") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Lilita One Regular', u'Lilita One Italic']] but Lilita One

