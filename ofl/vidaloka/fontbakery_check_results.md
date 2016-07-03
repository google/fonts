# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is '    ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/vidaloka/Vidaloka-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## Font contains unique glyph names?
* ERROR: The following glyph IDs occur twice: ['periodcentered']

## No glyph is incorrectly named?
* ERROR: The following glyph IDs are incorrectly named: ['tilde.case']

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font has a valid license url ?
* ERROR: LicenseUrl is required and must be a valid URL. Got  http://scripts.sil.org/OFL instead.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "Vidaloka " while METADATA.pb has "Vidaloka"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "Vidaloka " while METADATA.pb has name="Vidaloka"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Vidaloka " does not match post_script_name = "Vidaloka-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb 'name' contains font name in right format ?
* ERROR: METADATA.pb name='Vidaloka' does not match correct font name format.

## METADATA.pb 'full_name' contains font name in right format ?
* ERROR: METADATA.pb full_name='Vidaloka ' does not match correct font name format.

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Cyreal (www.cyreal.org a@cyreal.org) with Reserved Font Name "Vidaloka".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Vidaloka ") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Vidaloka') does not match name table entry 'Vidaloka ' !

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Vidaloka  Regular', u'Vidaloka  Italic']] but Vidaloka 

