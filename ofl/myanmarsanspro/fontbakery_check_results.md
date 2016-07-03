# Fontbakery check results
## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/myanmarsanspro/MyanmarSansPro-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: maxp: bad max_zones: 0



## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 984 to 979 | OS/2 sTypoAscender from 750 to 979 | OS/2 usWinAscent from 984 to 979 | hhea descent from -273 to -294 | OS/2 sTypoDescender from -250 to -294 | OS/2 usWinDescent from 273 to 294 | hhea lineGap from 67 to 0 | OS/2 sTypoLineGap from 307 to 0

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/myanmarsanspro: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Is GASP table correctly set?
* HOTFIX: gaspRange[65535] value (2) is not 15

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

