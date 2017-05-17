# Fontbakery check results
## Checking fsSelection REGULAR bit
* HOTFIX: fsSelection REGULAR bit Fixes: OS/2 fsSelection from 64 to 0

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## Checking name table for items without platformID = 1 (MACHINTOSH)
* HOTFIX: some name table items with platformID=1 were removed
* HOTFIX: Namerecord 10s (descriptions) were removed (perhaps added by a longstanding FontLab Studio 5.x bug.)

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/terminaldosislight/TerminalDosis-Light.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does full font name begin with the font family name?
* ERROR: Font family name 'Terminal Dosis' does not begin with full font name 'Terminal Dosis Light'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'multiple designers' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "Terminal Dosis" while METADATA.pb has "Terminal Dosis Light"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "Terminal Dosis" while METADATA.pb has name="Terminal Dosis Light"

## Filename is set canonically?
* ERROR: METADATA.pb: filename field ('TerminalDosis-Light.ttf') does not match canonical name 'TerminalDosisLight-Regular.ttf'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Terminal Dosis Light") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Terminal Dosis Light') does not match name table entry 'Terminal Dosis' !

## Checking OS/2 usWeightClass matches weight specified at METADATA.pb
* HOTFIX: OS/2 usWeightClass matches weight specified at METADATA.pb Fixes: OS/2 usWeightClass from 300 to 400

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("TerminalDosis-Light") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Terminal Dosis Regular', u'Terminal Dosis Italic']] but Terminal Dosis Light

