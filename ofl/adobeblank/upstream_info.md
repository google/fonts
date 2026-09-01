# Adobe Blank

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Dr. Ken Lunde
**METADATA.pb path**: `ofl/adobeblank/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/adobe-fonts/adobe-blank |
| Commit | `19279e6f6707408fd93091d157b7836259bcbd21` |
| Config YAML | -- |
| Branch | -- |

## How the Repository URL Was Found

The METADATA.pb file contains **no source block** at all. The repository URL `https://github.com/adobe-fonts/adobe-blank` was discovered through research. The copyright notice in METADATA.pb states "Copyright 2013, 2015 Adobe Systems Incorporated", and the `adobe-fonts` GitHub organization is Adobe's official repository for open-source fonts. The URL has been verified as accessible (HTTP 200).

The font was added to google/fonts by Dave Crossland in commit `54875d8a` (2016-03-21: "Adding Adobe Blank") with no PR reference or upstream commit recorded.

## How the Commit Hash Was Identified

The upstream repo contains only **one commit**:

- `19279e6f6707408fd93091d157b7836259bcbd21` (2019-12-03): "Update README.md"

This is the sole commit in the repository. Note: this commit (2019-12-03) is **after** the font was added to google/fonts (2016-03-21), meaning the repo was likely force-pushed or recreated at some point. The original state of the repo at the time of onboarding cannot be verified from current git history.

## How Config YAML Was Resolved

**No config.yaml exists or can be created** -- Adobe Blank uses a completely non-standard build process:

The font is built using **AFDKO's `makeotf`** command-line tool with CID-keyed PostScript sources. The build process (documented in `COMMANDS.txt`) is:

```
makeotf -f cidfont.ps -omitMacNames -ff features -fi cidfontinfo -mf FontMenuNameDB -r -stubCmap4 -ch UnicodeAll-UTF32-H
sfntedit -d VORG,vhea,vmtx AdobeBlank.otf
sfntedit -a DSIG=DSIG.bin AdobeBlank.otf
```

Source files in the repo:
- `cidfont.ps` -- CID-keyed PostScript font data
- `features` -- OpenType feature file
- `cidfontinfo` -- CID font metadata
- `FontMenuNameDB` -- Font menu name database
- `UnicodeAll-UTF32-H` -- Unicode CMap
- `DSIG.bin` -- Digital signature binary
- Pre-built binaries: `AdobeBlank.otf`, `AdobeBlank.ttf`, `AdobeBlank.eot`, `.woff` files

There are **no** `.glyphs`, `.ufo`, or `.designspace` files. This font uses a specialized Adobe CID-keyed workflow that is incompatible with gftools-builder. No override `config.yaml` exists in `ofl/adobeblank/` in google/fonts.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2019-12-03 12:28:22 -0500
- Commit message: "Update README.md"
- Source files at commit: `cidfont.ps`, `features`, `cidfontinfo`, `FontMenuNameDB`, `UnicodeAll-UTF32-H`, `DSIG.bin` (CID-keyed PostScript workflow -- not compatible with gftools-builder)

## Confidence

**Medium**: The repository URL is confirmed valid and is the obvious canonical source for Adobe Blank. The commit reference is unambiguous (only one commit). However, the commit post-dates the google/fonts addition by 3+ years, indicating the repo was rewritten. The font uses a CID-keyed build process that cannot be represented in a gftools-builder config.yaml.

## Open Questions

1. Should the METADATA.pb be updated to include a `source { repository_url }` block pointing to `https://github.com/adobe-fonts/adobe-blank`?
2. Adobe Blank is a special-purpose font (renders all glyphs as blank). Is it expected to remain permanently outside the gftools-builder workflow?
3. The METADATA.pb classifies this as `category: "MONOSPACE"` which seems unusual for a blank font -- is this classification intentional?
4. Adobe has released "Adobe Blank 2" as a separate project -- should google/fonts track that as well?
