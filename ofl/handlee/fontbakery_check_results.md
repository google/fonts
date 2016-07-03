# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/handlee/Handlee-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: OS/2 sTypoAscender from 933 to 934 | hhea descent from -401 to -400 | OS/2 sTypoDescender from -401 to -400 | OS/2 usWinDescent from 401 to 400

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does full font name begin with the font family name?
* ERROR: Font family name 'Handlee' does not begin with full font name 'Handlee Regular'

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Admix Designs (http://www.admixdesigns.com joe@admixdesigns.com) with Reserved Font Name Handlee.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Handlee Regular") ends with "Italic"

