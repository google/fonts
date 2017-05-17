# Fontbakery check results
## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## Checking name table for items without platformID = 1 (MACHINTOSH)
* HOTFIX: some name table items with platformID=1 were removed
* HOTFIX: Namerecord 10s (descriptions) were removed (perhaps added by a longstanding FontLab Studio 5.x bug.)

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/abyssinicasil/AbyssinicaSIL-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 1729 to 2034 | OS/2 sTypoAscender from 1729 to 2034 | hhea descent from -319 to -682 | OS/2 sTypoDescender from -319 to -682 | hhea lineGap from 512 to 0 | OS/2 sTypoLineGap from 512 to 0

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/abyssinicasil: Glyph 0x00A0 is called "NoBreakSpace": Change to "nbsp" or "uni00A0"

## Whitespace glyphs have ink?
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/abyssinicasil space 922 nbsp 600: Fixed nbsp advanceWidth to 922

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## Font contains unique glyph names?
* ERROR: The following glyph IDs occur twice: ['nonmarkingreturn']

## No glyph is incorrectly named?
* ERROR: The following glyph IDs are incorrectly named: ['uniE50F']

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Abyssinica+SIL

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'SIL International' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## Checks METADATA.pb 'postScriptName' matches TTF 'postScriptName'
* ERROR: Unmatched postscript name in font: TTF has "AbyssinicaSIL-Regular" while METADATA.pb has "AbyssinicaSIL"

## METADATA.pb 'fullname' value matches internal 'fullname' ?
* ERROR: Unmatched fullname in font: TTF has "Abyssinica SIL" while METADATA.pb has "Abyssinica SIL Regular"

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Abyssinica SIL Regular" does not match post_script_name = "AbyssinicaSIL"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="AbyssinicaSIL-Regular.ttf" does not match post_script_name="AbyssinicaSIL." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notice is okay, but it lacks an email address. Expected pattern is: 'Copyright 2016 Author Name (name@site.com)'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Abyssinica SIL") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb: Fullname ('Abyssinica SIL Regular') does not match name table entry 'Abyssinica SIL' !

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("AbyssinicaSIL") with weight 400 must be ended with "Regular" or "Italic"

