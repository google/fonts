# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'AAD ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/peddana/Peddana-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font family name 'Peddana' does not begin with full font name 'Peddana Regular'

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (750) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Appaji Ambarisha Darbha' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Peddana Regular" does not match post_script_name = "Peddana"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Peddana-Regular.ttf" does not match post_script_name="Peddana." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012 Andhrapradesh Society for Knowledge Networks (fonts.siliconandhra.org). Copyright (c) 1997-2014, SIL International (http://scripts.sil.org/) with Reserved Font Names "Charis" and "SIL".") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Peddana Regular") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Peddana") with weight 400 must be ended with "Regular" or "Italic"

