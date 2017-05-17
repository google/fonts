# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## Checking name table for items without platformID = 1 (MACHINTOSH)
* HOTFIX: some name table items with platformID=1 were removed
* HOTFIX: Namerecord 10s (descriptions) were removed (perhaps added by a longstanding FontLab Studio 5.x bug.)

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/josefinsansstdlight/JosefinSansStd-Light.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 750 to 1006 | OS/2 sTypoAscender from 750 to 1006 | hhea descent from -250 to -252 | OS/2 sTypoDescender from -250 to -252

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (2) is not 15

## Does full font name begin with the font family name?
* ERROR: Font family name 'Josefin Sans Std' does not begin with full font name 'Josefin Sans Std Light'

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font has a valid license url ?
* ERROR: LicenseUrl is required and must be a valid URL. Got False instead.

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'hidden' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## Font on disk and in METADATA.pb have the same family name ?
* ERROR: Unmatched family name in font: TTF has "Josefin Sans Std" while METADATA.pb has "Josefin Sans Std Light"

## METADATA.pb fonts 'name' property should be same as font familyname
* ERROR: Unmatched familyname in font: TTF has "Josefin Sans Std" while METADATA.pb has name="Josefin Sans Std Light"

## Filename is set canonically?
* ERROR: METADATA.pb: filename field ('JosefinSansStd-Light.ttf') does not match canonical name 'JosefinSansStdLight-Regular.ttf'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Josefin Sans Std Light") ends with "Italic"

## Metadata key-value match to table name fields?
* ERROR: METADATA.pb Family name 'Josefin Sans Std Light') does not match name table entry 'Josefin Sans Std' !

## Checking OS/2 usWeightClass matches weight specified at METADATA.pb
* HOTFIX: OS/2 usWeightClass matches weight specified at METADATA.pb Fixes: OS/2 usWeightClass from 300 to 400

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("JosefinSansStd-Light") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Josefin Sans Std Regular', u'Josefin Sans Std Italic']] but Josefin Sans Std Light

