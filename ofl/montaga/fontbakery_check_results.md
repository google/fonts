# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/montaga/Montaga-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/montaga: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Alejandra Rodriguez' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Montaga" does not match post_script_name = "Montaga-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Alejandra Rodriguez (ale_guez@yahoo.com.ar http://twitter.com/ale_guez), with Reserved Font Name "Montaga"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Montaga") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Montaga Regular', u'Montaga Italic']] but Montaga

