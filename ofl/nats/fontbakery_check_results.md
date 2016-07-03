# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/nats/NATS-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking with ot-sanitise
* ERROR: ot-sanitize returned an error code. Output follows :

ERROR: Layout: Lookup flags ask for mark attachment, but there is no GDEF table or it has no mark attachment classes: 256
ERROR: Layout: Failed to parse lookup 9
ERROR: GSUB: Failed to parse lookup list table
Failed to sanitise file!



## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (970) is not equal to 1000.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=NATS

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Purushoth Kumar Guttula' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="NATS-Regular.ttf" does not match post_script_name="NATS." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012 Silicon Andhra (fonts.siliconandhra.org). Copyright (c) 2011-2012, Julieta Ulanovsky (julieta.ulanovsky@gmail.com), with Reserved Font Names 'Montserrat'") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("NATS") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("NATS") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'NATS Regular', u'NATS Italic']] but NATS

