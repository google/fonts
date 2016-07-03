# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is 'newt' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/oxygenmono/OxygenMono-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Checking if the font is truly monospaced
* HOTFIX: Font is monospaced but 3 glyphs (0.828729281768%) have a different width. You should check the widths of: ['nonmarkingreturn', '.notdef', 'afii00208'] Fixes: post isFixedPitch from 0 to 1

## Checking vertical metrics
* HOTFIX: Vertical metrics. Fixes: hhea ascent from 2015 to 2104 | OS/2 sTypoAscender from 2015 to 2104 | OS/2 usWinAscent from 2015 to 2104 | hhea descent from -672 to -678 | OS/2 sTypoDescender from -672 to -678 | OS/2 usWinDescent from 672 to 678

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Are there unwanted tables?
* HOTFIX: Unwanted tables were present in the font and were removed: FFTM

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## Glyph names are all valid?
* ERROR: The following glyph names do not comply with naming conventions: ['.ttfautohint'] A glyph name may be up to 31 characters in length, must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) _(underscore). and must not start with a digit or period. There are a few exceptions such as the special character ".notdef". The glyph names "twocents", "a1", and "_" are all valid, while "2cents" and ".twocents" are not.

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Font names are consistent across platforms?
* ERROR: Entries in "name" table are not the same across specific platforms.

## Is font em size (ideally) equal to 1000?
* ERROR: font em size (2048) is not equal to 1000.

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Oxygen Mono" does not match post_script_name = "OxygenMono-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## Copyright notice does not contain Reserved Font Name
* ERROR: METADATA.pb: copyright field ("Copyright (c) 2012, vernon adams (vern@newtypography.co.uk), with Reserved Font Names 'Oxygen'") contains "Reserved Font Name"

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Oxygen Mono") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Oxygen Mono Regular', u'Oxygen Mono Italic']] but Oxygen Mono

## Monospace font has hhea.advanceWidthMax equal to each glyph's advanceWidth ?
* ERROR: Glyph advanceWidth must be same across all glyphs

