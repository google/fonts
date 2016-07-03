# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'PfEd', a font editor default. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/bentham/Bentham-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 879 to 878 | OS/2 sTypoAscender from 768 to 878 | OS/2 usWinAscent from 879 to 878 | OS/2 sTypoDescender from -256 to -260 | hhea lineGap from 92 to 0 | OS/2 sTypoLineGap from 92 to 0

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (2) is not 15

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (1024) is not equal to 1000.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Bentham" does not match post_script_name = "Bentham-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 1999-2010, Ben Weiner (ben@readingtype.org.uk), with Reserved Font Name Bentham.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Bentham") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Bentham Regular', u'Bentham Italic']] but Bentham

