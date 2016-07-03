# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/carme/Carme-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: gasp: changed the version number to 1



## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does full font name begin with the font family name?
* ERROR: Font family name 'Carme' does not begin with full font name 'Carme Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* Warning: Failed to fetch 'https://raw.githubusercontent.com/google/fonts/master/designers/profiles.csv'

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Carme Regular" does not match post_script_name = "Carme"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="Carme-Regular.ttf" does not match post_script_name="Carme." (Consider removing the '-Regular' suffix from the filename.)

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2010-2011, Ruben Prol (ipanemagrafica@gmail.com|www.ipanemagrafica.com), with Reserved Font Name Carme.") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Carme Regular") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("Carme") with weight 400 must be ended with "Regular" or "Italic"

