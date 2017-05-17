# Fontbakery check results
## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'PfEd', a font editor default. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx

## Checking OS/2 usWeightClass
* HOTFIX: OS/2 usWeightClass Fixes: OS/2 usWeightClass from 500 to 400

## Checking fsSelection REGULAR bit
* HOTFIX: fsSelection REGULAR bit Fixes: OS/2 fsSelection from 1 to 65

## Checking if italicAngle matches font style
* HOTFIX: post table italicAngle matches style name Fixes: post italicAngle from -1.70001 to 0

## Checking fsSelection ITALIC bit
* HOTFIX: fsSelection ITALIC bit Fixes: OS/2 fsSelection from 65 to 64

## Checking macStyle ITALIC bit
* HOTFIX: macStyle ITALIC bit Fixes: head macStyle from 2 to 0

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/averiagruesalibre/AveriaGruesaLibre-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 1952 to 1884 | OS/2 sTypoAscender from 1952 to 1884 | OS/2 usWinAscent from 1952 to 1884 | hhea descent from -492 to -460 | OS/2 sTypoDescender from -492 to -460 | OS/2 usWinDescent from 492 to 460

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (2) is not 15

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Averia Gruesa Libre" does not match post_script_name = "AveriaGruesaLibre-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Dan Sayers (i@iotic.com), with Reserved Font Name 'Averia' and 'Averia Libre'.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Averia Gruesa Libre") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Averia Gruesa Libre Regular', u'Averia Gruesa Libre Italic']] but Averia Gruesa Libre

