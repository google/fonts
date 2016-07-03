# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is '    ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/unifrakturcook/UnifrakturCook-Bold.ttf: Windows-only Opentype-specific StyleName set to "Bold".

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/unifrakturcook space 500 nbsp 333: Fixed nbsp advanceWidth to 500

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Ensure designer simple short name.
* ERROR: `designer` key must be simple short name

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=UnifrakturCook

## According GWF standards font should have Regular style.
* ERROR: This font lacks a Regular (style: normal and weight: 400) as required by GWF standards.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="UnifrakturCook" does not match post_script_name = "UnifrakturCook-Bold"

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2010 j. 'mach' wust (j.mach.wust@gmail.com) with Reserved Font Name UnifrakturCook. Copyright (c) 2009 Peter Wiegel (wiegel@peter-wiegel.de). This Font Software is licensed under the SIL Open Font License, Version 1.1.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("UnifrakturCook") ends with "Italic"

## Check if fontname is not camel cased.
* ERROR: METADATA.pb: '%s' is a CamelCased name. To solve this, simply use spaces instead in the font name.

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'UnifrakturCook Bold', u'UnifrakturCook BoldItalic']] but UnifrakturCook

