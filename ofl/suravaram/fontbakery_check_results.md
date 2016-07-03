# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is '    ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/suravaram/Suravaram-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/suravaram space 177 nbsp 197: Fixed space advanceWidth to 197

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
* ERROR: font em size (980) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Purushoth Kumar Guttula' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Suravaram-Regular.ttf" does not match post_script_name="Suravaram." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012 Silicon Andhra (fonts.siliconandhra.org). Copyright (c) 2011 by vernon adams (vern@newtypography.co.uk) with Reserved Font Name 'Tienne'") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Suravaram") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Suravaram") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Suravaram Regular', u'Suravaram Italic']] but Suravaram

