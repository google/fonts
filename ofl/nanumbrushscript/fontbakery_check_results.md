# Fontbakery check results
## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## Checking OS/2 fsType
* HOTFIX: fsType is zero. Fixes: OS/2 fsType from 8 to 0

## substitute copyright, registered and trademark symbols in name table entries
* HOTFIX: Name table entries were modified to replace unicode symbols such as (c), (r) and TM.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/nanumbrushscript/NanumBrushScript-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking with ot-sanitise
* ERROR: ot-sanitise output follows:

WARNING: name: name records are not sorted.
WARNING: name: name records are not sorted.
WARNING: name: name records are not sorted.
WARNING: name: name records are not sorted.



## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 920 to 802 | OS/2 sTypoAscender from 800 to 802 | OS/2 usWinAscent from 920 to 802 | hhea descent from -230 to -200 | OS/2 usWinDescent from 230 to 200

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/nanumbrushscript: Glyph 0x0020 is called "uni0000": Change to "space" or "uni0020"
* ERROR: /home/felipe/devel/github_google/fonts/ofl/nanumbrushscript: Glyph 0x00A0 is called "uni0000": Change to "nbsp" or "uni00A0"

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: GPOS table lacks kerning information

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Are there non-ASCII characters in ASCII-only NAME table entries ?
* ERROR: There are 6 strings containing non-ASCII characters in the ASCII-only NAME table entries.

## METADATA.pb: Fontfamily is listed in Google Font Directory ?
* ERROR: No family found in GWF in http://fonts.googleapis.com/css?family=Nanum+Brush+Script

## METADATA.pb: Designer exists in GWF profiles.csv ?
* ERROR: METADATA.pb: Designer 'Sandoll Communication' is not listed in profiles.csv (at 'https://github.com/google/fonts/blob/master/designers/profiles.csv')

## METADATA.pb subsets should have at least 'latin'
* ERROR: METADATA.pb subsets ([u'menu', u'korean']) missing 'latin'

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Nanum Brush Script" does not match post_script_name = "NanumBrush"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb filename="NanumBrushScript-Regular.ttf" does not match post_script_name="NanumBrush." (Consider removing the '-Regular' suffix from the filename.)

## METADATA.pb 'postScriptName' contains font name in right format ?
* ERROR: METADATA.pb postScriptName='NanumBrush' does not match correct font name format.

## Copyright notice matches canonical pattern?
* ERROR: METADATA.pb: Copyright notices should match the folowing pattern: 'Copyright 2016 Author Name (name@site.com)'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Nanum Brush Script") ends with "Italic"

## Metadata weight matches postScriptName
* ERROR: METADATA.pb: postScriptName ("NanumBrush") with weight 400 must be ended with "Regular" or "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Nanum Brush Script Regular', u'Nanum Brush Script Italic']] but Nanum Brush Script

