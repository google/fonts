# Fontbakery check results
## Checking OS/2 achVendID
* ERROR: OS/2 VendorID is 'pyrs' but this is registered with different casing. You should check the case.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/rubikmonoone/RubikMonoOne-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking if the font is truly monospaced
* HOTFIX: Font is monospaced but 3 glyphs (0.551470588235%) have a different width. You should check the widths of: ['nonmarkingreturn', '.null', 'NULL'] Fixes: post isFixedPitch from 0 to 1 | OS/2 panose.bProportion from 4 to 9

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 932 to 860 | OS/2 sTypoAscender from 932 to 860 | OS/2 usWinAscent from 932 to 860 | hhea descent from -306 to -211 | OS/2 sTypoDescender from -306 to -211 | OS/2 usWinDescent from 306 to 211

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Does full font name begin with the font family name?
* ERROR: Font family name 'Rubik Mono One' does not begin with full font name 'Rubik Mono One Regular'

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## METADATA.pb: Ensure designer simple short name.
* ERROR: `designer` key must be simple short name

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Rubik Mono One Regular") ends with "Italic"

