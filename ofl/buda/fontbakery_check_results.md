# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'PfEd', a font editor default. You should set it to your own 4 character code, and register that code with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx

## Checking OS/2 usWeightClass
* HOTFIX: OS/2 usWeightClass Fixes: OS/2 usWeightClass from 400 to 300

## Checking fsSelection REGULAR bit
* HOTFIX: fsSelection REGULAR bit Fixes: OS/2 fsSelection from 64 to 0

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/buda/Buda-Light.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 1836 to 1862 | OS/2 sTypoAscender from 1519 to 1862 | OS/2 usWinAscent from 1836 to 1862 | hhea descent from -724 to -446 | OS/2 sTypoDescender from -529 to -446 | OS/2 usWinDescent from 724 to 446 | OS/2 sTypoLineGap from 512 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* ERROR: Font is missing the GASP table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Buda

## METADATA.pb: Designer exists in GWF profiles.csv ?
* Warning: Failed to fetch 'https://raw.githubusercontent.com/google/fonts/master/designers/profiles.csv'

## According GWF standards font should have Regular style.
* ERROR: This font lacks a Regular (style: normal and weight: 400) as required by GWF standards.

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Buda-Light.ttf" does not match post_script_name="Buda."

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Buda") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Buda") with weight 300 must be ended with "LightItalic" or "Light"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Buda LightItalic', u'Buda Light']] but Buda

