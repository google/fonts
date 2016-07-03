# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'euro' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/akronim/Akronim-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 785 to 989 | OS/2 sTypoAscender from 785 to 989 | hhea descent from -314 to -404 | OS/2 sTypoDescender from -314 to -404 | hhea lineGap from 43 to 0 | OS/2 sTypoLineGap from 43 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## Glyph names are all valid?
* ERROR: The following glyph names do not comply with naming conventions: ['.notdef#1'] A glyph name may be up to 31 characters in length, must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). and must not start with a digit or period. There are a few exceptions such as the special character ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not.

## Font contains unique glyph names?
* ERROR: The following glyph IDs occur twice: ['.notdef']

## No glyph is incorrectly named?
* ERROR: The following glyph IDs are incorrectly named: ['Dcroat']

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* ERROR: Font is missing the GASP table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Akronim" does not match post_script_name = "Akronim-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012 Grzegorz Klimczewski, Fonty.PL (www.fonty.pl grzegorz@fonty.pl), with Reserved Font Name 'Akronim'") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Akronim") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Akronim Regular', u'Akronim Italic']] but Akronim

