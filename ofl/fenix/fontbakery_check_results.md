# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/fenix/Fenix-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* Warning: Failed to fetch 'https://raw.githubusercontent.com/google/fonts/master/designers/profiles.csv'

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: Unmatched postscript name in font: TTF has "Fenix" while METADATA.pb has "Fenix-Regular"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Fenix" does not match post_script_name = "Fenix-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, Fernando Diaz (www.ferfolio.com fer@ferfolio.com) with Reserved Font Name 'Fenix'") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Fenix") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Fenix Regular', u'Fenix Italic']] but Fenix

