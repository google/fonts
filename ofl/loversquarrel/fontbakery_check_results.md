# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/loversquarrel/LoversQuarrel-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: OS/2 sTypoDescender from -400 to -401

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

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'TypeSETit' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Lovers Quarrel" does not match post_script_name = "LoversQuarrel-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012 TypeSETit, LLC (typesetit@att.net), with Reserved Font Name "Lovers Quarrel"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Lovers Quarrel") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Lovers Quarrel Regular', u'Lovers Quarrel Italic']] but Lovers Quarrel

