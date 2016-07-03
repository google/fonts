# Fontbakery check results
## Font has post table version 2 ?
* ERROR: Post table should be version 2 instead of 3.0.More info at https://github.com/google/fonts/issues/215

## substitute copyright, registered and trademark symbols in name table entries
* HOTFIX: Name table entries were modified to replace unicode symbols such as (c), (r) and TM.

## Check copyright namerecords match license file
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.
* HOTFIX: License file OFL.txt exists but NameID value is not specified for that.

## StyleName recommendation
* HOTFIX: /home/felipe/devel/github_google/fonts/ofl/jejumyeongjo/JejuMyeongjo-Regular.ttf: Warning: Windows-only Opentype-specific StyleName set to "Regular" as a default value. Please verify if this is correct.

## Checking if the font is truly monospaced
* HOTFIX: Font is monospaced but 315 glyphs (1.7199017199%) have a different width. You should check the widths of: ['four', 'second', 'k', 'currency', 'A', 'Zeta', 'uni20A9', 'X', 'union', 'Iota', 'Phi', 'o', 'asterisk', 'minute', 'Tau', 'uni2252', 'Mu', 'Ldot', 'uni2113', 'one', 'uni043D', 'uni043A', 'uni043B', 'uni0438', 'uni0439', 'uni0434', 'uni0437', 'uni0430', 'uni0432', 'uni0433', 's', 'uni0445', 'uni0447', 'uni0446', 'uni0440', 'uni0443', 'breve', 'uni0394', 'I', 'Gamma', 'oslash', 'Nu', 'ae', 'at', 'daggerdbl', 'thorn', 'uni044B', 'dotlessi', 'section', 'uni041F', 'uni041D', 'uni041E', 'uni041B', 'uni041C', 'uni041A', 'uni0417', 'uni0414', 'uni0415', 'uni0412', 'uni0413', 'uni0410', 'uni0411', 'uni0418', 'uni0419', 'asciicircum', 'male', 'Eta', 'w', 'existential', 'M', 'uniBB18', 'Hbar', 'd', 'OE', 'caron', 'integral', 'Lambda', 'kgreenlandic', 'uni0451', 'Q', 'comma', 'iota', 'uni2083', 'uni2082', 'uni2084', 'napostrophe', 'h', 'Pi', 'eta', 'eth', 'lslash', 'uni00AD', 'phi', 'infinity', 'less', 'five', 'parenright', 'bracketright', 'U', 'uni3153', 'seven', 'ordmasculine', 'l', 'quoteright', 'Tbar', 'B', 'grave', 'partialdiff', 'periodcentered', 'Y', 'uni2081', 'omega', 'p', 'uni02D0', 'asciitilde', 'F', 'product', 'Chi', 'space', 'xi', 'ring', 'uni03A9', 'Beta', 'psi', 't', 'E', 'hungarumlaut', 'lambda', 'J', 'ogonek', 'equivalence', 'uni327F', 'uni3011', 'uni3010', 'uni3015', 'uni3014', 'uni300A', 'uni300C', 'arrowdown', 'uni043F', 'nine', 'arrowupdn', 'a', 'Eng', 'quotedbl', 'rho', 'alpha', 'copyright', 'x', 'hbar', 'N', 'slash', 'uni0435', 'uni0436', 'underscore', 'bracketleft', 'exclamdown', 'R', 'Psi', 'i', 'intersection', 'universal', 'V', 'tbar', 'Rho', 'dcroat', 'm', 'bar', 'C', 'three', 'ij', 'quotesingle', 'numbersign', 'uni212B', 'Z', 'semicolon', 'ampersand', 'uni043E', 'uni043C', 'q', 'uni0427', 'uni0426', 'uni0425', 'uni0424', 'uni0423', 'uni0422', 'uni0421', 'uni0420', 'uni0431', 'uni042F', 'uni042D', 'uni042C', 'uni042B', 'uni042A', 'germandbls', 'G', 'quoteleft', 'Sigma', 'uni2109', 'uni2103', 'Thorn', 'beta', 'sigma', 'Kappa', 'quotedblleft', 'kappa', 'uniC218', 'uni0401', 'AE', 'musicalnote', 'dagger', 'parenleft', 'e', 'u', 'dollar', 'quotedblright', 'zero', 'dotaccent', 'two', 'upsilon', 'paragraph', 'P', 'arrowup', 'Upsilon', 'b', 'Theta', 'Alpha', 'ordfeminine', 'braceleft', 'Oslash', 'zeta', 'braceright', 'y', 'uni00B3', 'uni00B2', 'uni00B9', 'O', 'proportional', 'uni0449', 'uni0448', 'uni0444', 'uni0441', 'uni0442', 'Omicron', 'uni044E', 'uni044D', 'uni044F', 'uni044A', 'uni044C', 'tau', 'chi', 'f', 'greater', 'uni03BC', 'eight', 'S', 'uni223D', 'female', 'dieresis', 'j', 'uniC870', 'eng', 'W', 'Lslash', 'ldot', 'Omega', 'K', 'uni266D', 'uni266C', 'n', 'D', 'epsilon', 'nu', 'backslash', 'r', 'uni207F', 'uni2074', 'H', 'period', 'colon', 'IJ', 'Eth', 'acute', 'oe', 'uni2010', 'v', 'uni3132', 'L', 'uni3008', 'uni3009', 'uni300B', 'uni300D', 'uni300E', 'uni300F', 'radical', 'questiondown', 'Epsilon', 'Xi', 'omicron', 'c', 'pi', 'perpendicular', 'uni2669', 'gamma', 'delta', 'z', 'degree', 'summation', 'six', 'cedilla', 'g', 'angle', 'theta', 'hyphen', 'T'] Fixes: post isFixedPitch from 0 to 1 | OS/2 panose.bProportion from 0 to 9

## Digital Signature exists?
* HOTFIX: The font does not have an existing digital signature (DSIG), so we just added one.

## Font has **proper** whitespace glyph names?
* ERROR: /home/felipe/devel/github_google/fonts/ofl/jejumyeongjo: Glyph 0x00A0 is called "space": Change to "nbsp" or "uni00A0"

## Version format is correct in NAME table?
* ERROR: The NAMEID_VERSION_STRING (nameID=5) value must follow the pattern Version X.Y. Current value: False

## EPAR table present in font?
* ERROR: Font is missing EPAR table.

## Does GPOS table have kerning information?
* ERROR: Font is missing a "GPOS" table

## Does full font name begin with the font family name?
* ERROR: Font lacks a NAMEID_FONT_FAMILY_NAME entry in the name table.

## Font has 'EURO SIGN' character?
* ERROR: Font lacks the 'EURO SIGN' character.

## Font contains magic code in PREP table?
* ERROR: Failed to find correct magic code in PREP table.

## Are there non-ASCII characters in ASCII-only NAME table entries ?
* ERROR: There are 2 strings containing non-ASCII characters in the ASCII-only NAME table entries.

