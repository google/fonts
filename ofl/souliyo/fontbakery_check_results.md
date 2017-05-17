# Fontbakery check results
## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## substitute copyright, registered and trademark symbols in name table entries
* HOTFIX: Name table entries were modified to replace unicode symbols such as (c), (r) and TM.

## Check copyright namerecords match license file
* HOTFIX: Font lacks NameID 13. A proper licensing entry was set.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/souliyo/Souliyo-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: maxp: bad max_zones: 0



## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 2240 to 2281 | OS/2 sTypoAscender from 1434 to 2281 | OS/2 usWinAscent from 2240 to 2281 | hhea descent from -600 to -627 | OS/2 sTypoDescender from -410 to -627 | OS/2 usWinDescent from 600 to 627 | OS/2 sTypoLineGap from 205 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font contains glyphs for whitespace characters?
* ERROR: Font is missing the following glyphs: nbsp (0x00A0).

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (3) is not 15

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Font has a valid license url ?
* ERROR: LicenseUrl is required and must be a valid URL. Got False instead.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

