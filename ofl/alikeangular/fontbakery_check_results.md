# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is '    ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/alikeangular/AlikeAngular-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 984 to 977 | OS/2 sTypoAscender from 984 to 977 | OS/2 usWinAscent from 984 to 977

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

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

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Alike Angular" does not match post_script_name = "AlikeAngular-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Cyreal (www.cyreal.org a@cyreal.org) with Reserved Font Name "Alike" and "Alike Angular".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Alike Angular") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Alike Angular Regular', u'Alike Angular Italic']] but Alike Angular

