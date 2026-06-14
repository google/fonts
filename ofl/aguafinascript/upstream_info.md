# Aguafina Script

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Sudtipos
**METADATA.pb path**: `ofl/aguafinascript/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/aguafinascript |
| Commit | `45a8ce768b4cca138c10ff7a7a9f55778fd02c9d` |
| Config YAML | -- |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL is NOT present in the METADATA.pb -- there is no source block at all. The URL https://github.com/librefonts/aguafinascript was identified from prior research and is recorded in the tracking file `data/gfonts_library_sources.json`. The `librefonts` organization on GitHub hosts many legacy Google Fonts sources that were migrated from earlier infrastructure. The upstream repo is cached locally at `librefonts/aguafinascript`.

## How the Commit Hash Was Identified

The commit `45a8ce768b4cca138c10ff7a7a9f55778fd02c9d` is the HEAD (and only commit in the shallow clone) of the upstream repository. It is dated 2014-10-17 with the message "update .travis.yml". This predates even the last font modification in google/fonts (2015-04-27, "Updating ofl/aguafinascript/*ttf with nbspace and fsType fixes"), which suggests it is from the era when the font was being maintained.

The font was added to Google Fonts on 2011-11-30 (per `date_added` in METADATA.pb). The initial commit in google/fonts (`90abd17b4`, 2015-03-07) was part of a bulk import. The upstream repo's commit from 2014-10-17 is the latest available and represents the last state of the librefonts mirror.

## How Config YAML Was Resolved

There is no config.yaml in the upstream repo, and no override config.yaml in the google/fonts family directory. The upstream repository contains only legacy source formats:

- `src/AguafinaScript-Regular-TTF.sfd` -- FontForge SFD format
- `src/Aguafina-Regular-OTF.vfb` -- FontLab VFB format (binary, not usable with gftools-builder)

These formats are not compatible with gftools-builder, which requires `.glyphs`, `.glyphspackage`, `.ufo`, or `.designspace` source files. A config.yaml would require a conversion of the sources to a supported format first, or the creation of an override config.yaml that uses a different build approach.

The repo also contains TTX table dumps of the font, METADATA.json, and a DESCRIPTION.en_us.html file.

## Verification

- Commit exists in upstream repo: Yes (it is HEAD of the shallow clone)
- Commit date: 2014-10-17 13:27:47 +0300
- Commit message: "update .travis.yml"
- Source files at commit:
  - `src/AguafinaScript-Regular-TTF.sfd` (FontForge format)
  - `src/Aguafina-Regular-OTF.vfb` (FontLab format)

## Confidence

**Medium**: The repository URL is reasonably established -- `librefonts` is a known organization hosting legacy Google Fonts sources. The commit hash is the latest available in the repo. However, the font was originally designed by Sudtipos (Angel Koziupa and Alejandro Paul) and the librefonts repo is a mirror/archive, not the original source. There is no source block in METADATA.pb, so this data has not been formally recorded in the google/fonts repository yet.

## Open Questions

1. Is there a more authoritative upstream source for this font? Sudtipos is a commercial type foundry, and their original sources (likely in FontLab VFB format) may not be publicly available.
2. Should a source block be added to METADATA.pb pointing to the librefonts repo, even though there is no config.yaml and the sources are in legacy formats?
3. Could the SFD source be converted to a modern format (e.g., UFO) to enable gftools-builder compatibility, or is this font effectively in a "legacy binary only" state?
4. The copyright lists reserved font name "Aguafina Script" -- does this affect any potential source modifications?
