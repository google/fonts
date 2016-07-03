# Fontbakery check results
## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'PfEd', a font editor default. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx

## Checking OS/2 usWeightClass
* HOTFIX: OS/2 usWeightClass Fixes: OS/2 usWeightClass from 500 to 400

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/pressstart2p/PressStart2P-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking if the font is truly monospaced
* HOTFIX: Font is monospaced. Fixes: OS/2 panose.bProportion from 3 to 9

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

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

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (1024) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'CodeMan38' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Press Start 2P" does not match post_script_name = "PressStart2P-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, Cody "CodeMan38" Boisclair (cody@zone38.net), with Reserved Font Name "Press Start 2P"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Press Start 2P") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Press Start 2P Regular', u'Press Start 2P Italic']] but Press Start 2P

