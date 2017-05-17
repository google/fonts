# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/cantoraone/CantoraOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "CantoraOne" while METADATA.pb has "Cantora One"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "CantoraOne" while METADATA.pb has "Cantora One"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "CantoraOne" while METADATA.pb has name="Cantora One"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Cantora One" does not match post_script_name = "CantoraOne-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb 'name' contains font name in right format ?
* ERROR: METADATA.pb name='Cantora One' does not match correct font name format.

## METADATA.pb 'full_name' contains font name in right format ?
* ERROR: METADATA.pb full_name='Cantora One' does not match correct font name format.

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, Pablo Impallari (www.impallari.com|impallari@gmail.com), Rodrigo Fuenzalida (www.rfuenzalida.com|hello@rfuenzalida.com) with Reserved Font Name Cantora.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("CantoraOne") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Cantora One') does not match name table entry 'CantoraOne' !

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'CantoraOne Regular', u'CantoraOne Italic']] but Cantora One

