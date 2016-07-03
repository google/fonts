# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/bubblerone/BubblerOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: OS/2 usWinDescent from 65273 to 263

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="BubblerOne-Regular.ttf" does not match post_script_name="BubblerOne." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2011 by Brenda Gallo (gbrenda1987@gmail.com), with Reserved Font Name "Bubbler"") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Bubbler One") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("BubblerOne") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Bubbler One Regular', u'Bubbler One Italic']] but Bubbler One

