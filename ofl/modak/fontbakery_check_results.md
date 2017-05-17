# Fontbakery check results
## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'EKTF' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/modak/Modak-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: This font lacks a POSTSCRIPT_NAME entry (nameID=6) in the name table.

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: This font lacks a FULL_FONT_NAME entry (nameID=4) in the name table.

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: This font lacks a FONT_FAMILY_NAME entry (nameID=1) in the name table.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Modak-Regular.ttf" does not match post_script_name="Modak." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Modak") with weight 400 must be ended with "Regular" or "Italic"

