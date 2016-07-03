# Fontbakery check results
## Checking OS/2 usWeightClass
* HOTFIX: OS/2 usWeightClass Fixes: OS/2 usWeightClass from 300 to 400

## Checking fsSelection REGULAR bit
* HOTFIX: fsSelection REGULAR bit Fixes: OS/2 fsSelection from 0 to 64

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/pathwaygothicone/PathwayGothicOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: OS/2 sTypoAscender from 740 to 954 | OS/2 sTypoDescender from -180 to -198

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does full font name begin with the font family name?
* ERROR: Font family name 'Pathway Gothic One' does not begin with full font name 'Pathway Gothic One Regular'

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: Unmatched postscript name in font: TTF has "PathwayGothicOne-Book" while METADATA.pb has "PathwayGothicOne-Regular"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "Pathway Gothic One Regular" while METADATA.pb has "Pathway Gothic One"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Pathway Gothic One" does not match post_script_name = "PathwayGothicOne-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2013, Eduardo Tunni (http://www.tipo.net.ar edu@tipo.net.ar), with Reserved Font Name 'Pathway'") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Pathway Gothic One Regular") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb: Fullname ('Pathway Gothic One') does not match name table entry 'Pathway Gothic One Regular' !

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Pathway Gothic One Regular', u'Pathway Gothic One Italic']] but Pathway Gothic One

