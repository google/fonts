# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'free' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Checking fsSelection REGULAR bit
* HOTFIX: fsSelection REGULAR bit Fixes: OS/2 fsSelection from 129 to 193

## Checking that italicAngle <= 0
* HOTFIX: post table italicAngle from 16.5 to -16.5

## Checking if italicAngle matches font style
* HOTFIX: post table italicAngle matches style name Fixes: post italicAngle from -16.5 to 0

## Checking fsSelection ITALIC bit
* HOTFIX: fsSelection ITALIC bit Fixes: OS/2 fsSelection from 193 to 192

## Checking macStyle ITALIC bit
* HOTFIX: macStyle ITALIC bit Fixes: head macStyle from 2 to 0

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/miama/Miama-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Miama

## According GWF standards font should have Regular style.
* ERROR: This font lacks a Regular (style: normal and weight: 400) as required by GWF standards.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Miama" does not match post_script_name = "Miama-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2008-2011, Linus Romer, with Reserved Font Name Miama. This Font Software is licensed under the SIL Open Font License, Version 1.1.") contains "Reserved Font Name"

## Filename is set canonically?
* ERROR: METADATA.pb: filename field ('Miama-Regular.ttf') does not match canonical name 'Miama-Italic.ttf'

## METADATA.pb font.style `italic` matches font internals?
* ERROR: METADATA.pb style has been set to italic but font macStyle is improperly set

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Miama Regular', u'Miama Italic']] but Miama

## Font styles are named canonically?
* ERROR: Miama-Regular.ttf: The font style is italic but it should be normal

