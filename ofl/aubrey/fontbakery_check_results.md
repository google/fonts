# Fontbakery check results
## Checking OS/2 achVendID
* Warning: OS/2 VendorID is '    ' but this is not registered with Microsoft. You should register it at https://www.microsoft.com/typography/links/vendorlist.aspx

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## Checking name table for items without platformID = 1 (MACHINTOSH)
* HOTFIX: some name table items with platformID=1 were removed
* HOTFIX: Namerecord 10s (descriptions) were removed (perhaps added by a longstanding FontLab Studio 5.x bug.)

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/aubrey/Aubrey-Regular.ttf: Windows-only Opentype-specific StyleName set to "Regular".

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## Font contains unique glyph names?
* ERROR: The following glyph IDs occur twice: ['nonmarkingreturn']

## No glyph is incorrectly named?
* ERROR: The following glyph IDs are incorrectly named: ['foundryicon']

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

## METADATA.pb 'fullName' matches 'postScriptName' ?
* ERROR: METADATA.pb full_name="Aubrey" does not match post_script_name = "Aubrey-Regular"

## METADATA.pb 'filename' matches 'postScriptName' ?
* ERROR: METADATA.pb postScriptName field ends with '-Regular'

## METADATA.pb font.style `normal` matches font internals?
* ERROR: Font macStyle indicates a non-Italic font but nameID 4 ("Aubrey") ends with "Italic"

## METADATA.pb lists fonts named canonicaly?
* ERROR: Canonical name in font expected: [[u'Aubrey Regular', u'Aubrey Italic']] but Aubrey

