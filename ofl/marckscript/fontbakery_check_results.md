# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/marckscript/MarckScript-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Marck Script" does not match post_script_name = "MarckScript-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011, Denis Masharov <denis.masharov@gmail.com>, Marck Fogel, with Reserved Font Names "Marck Script".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Marck Script") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Marck Script Regular', u'Marck Script Italic']] but Marck Script

