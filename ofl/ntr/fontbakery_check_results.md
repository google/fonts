# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is '    ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/ntr/NTR-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (1024) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Purushoth Kumar Guttula' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="NTR-Regular.ttf" does not match post_script_name="NTR." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012 Silicon Andhra (fonts.siliconandhra.org). Copyright (c) 2011, Joe Prince, Admix Designs (http://www.admixdesigns.com/) with Reserved Font Name Varela Round.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("NTR") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("NTR") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'NTR Regular', u'NTR Italic']] but NTR

