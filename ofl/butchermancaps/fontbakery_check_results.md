# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'typm' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/butchermancaps/ButchermanCaps-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 2592 to 2600 | OS/2 sTypoAscender from 2592 to 2600 | OS/2 usWinAscent from 2592 to 2600 | hhea descent from -1412 to -1363 | OS/2 sTypoDescender from -1412 to -1363 | OS/2 usWinDescent from 1412 to 1363

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font family name 'Butcherman Caps' does not begin with full font name 'Butcherman Caps Regular'

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Typomondo' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Vernon Adams DBA Typomondo (vern@newtypography.co.uk), with Reserved Font Name "Butcherman".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Butcherman Caps Regular") ends with "Italic"

