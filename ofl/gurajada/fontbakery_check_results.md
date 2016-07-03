# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is '    ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/gurajada/Gurajada-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## Font contains unique glyph names?
* ERROR: The following glyph IDs occur twice: ['uni0C15_uni0C4D_uni0C37_uni0C4D.akhn']

## No glyph is incorrectly named?
* ERROR: The following glyph IDs are incorrectly named: ['uni0C15_uni0C46_uni0C56_uni0C37_uni0C4D.akhn_uni0C15_uni0C4D_uni0C37_uni0C4D.akhn.blws']

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (1070) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Purushoth Kumar Guttula' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Gurajada-Regular.ttf" does not match post_script_name="Gurajada." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Gurajada") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Gurajada") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Gurajada Regular', u'Gurajada Italic']] but Gurajada

