# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/archivoblack/ArchivoBlack-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 2254 to 1959 | OS/2 sTypoAscender from 1466 to 1959 | OS/2 usWinAscent from 2254 to 1959 | hhea descent from -634 to -547 | OS/2 sTypoDescender from -434 to -547 | OS/2 usWinDescent from 634 to 547 | OS/2 sTypoLineGap from 291 to 0

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

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Archivo Black" does not match post_script_name = "ArchivoBlack-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, Omnibus-Type (www.omnibus-type.com|omnibus.type@gmail.com),with Reserved Font Name: Archivo") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Archivo Black") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Archivo Black Regular', u'Archivo Black Italic']] but Archivo Black

