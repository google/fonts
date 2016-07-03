# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'SUDT' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/misssaintdelafield/MrsSaintDelafield-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does full font name begin with the font family name?
* ERROR: Font family name 'Mrs Saint Delafield' does not begin with full font name 'Mrs Saint Delafield Regular'

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "Mrs Saint Delafield" while METADATA.pb has "Miss Saint Delafield"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "Mrs Saint Delafield" while METADATA.pb has name="Miss Saint Delafield"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb 'name' contains font name in right format ?
* ERROR: METADATA.pb name='Miss Saint Delafield' does not match correct font name format.

## METADATA.pb 'full_name' contains font name in right format ?
* ERROR: METADATA.pb full_name='Mrs Saint Delafield Regular' does not match correct font name format.

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2004 Alejandro Paul (sudtipos@sudtipos.com), with Reserved Font Name "Mrs Saint Delafield"") contains "Reserved Font Name"

## Filename is set canonically?
* ERROR: METADATA.pb: filename field ('MrsSaintDelafield-Regular.ttf') does not match canonical name 'MissSaintDelafield-Regular.ttf'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Mrs Saint Delafield Regular") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Miss Saint Delafield') does not match name table entry 'Mrs Saint Delafield' !

