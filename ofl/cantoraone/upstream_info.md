# Cantora One

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Impallari Type (Pablo Impallari, Rodrigo Fuenzalida)
**METADATA.pb path**: `ofl/cantoraone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/cantoraone |
| Commit | `45d202afe1668a05e0afd870e124d72c2b82143c` |
| Config YAML | -- |
| Branch | master |

## How the Repository URL Was Found

The METADATA.pb file for Cantora One has no `source` block and no `repository_url` field. The upstream repo was found at `librefonts/cantoraone` in the fontc_crater_cache. A GitHub search for "cantoraone" confirmed that `https://github.com/librefonts/cantoraone` is the only upstream repository for this font. It was created on 2014-07-16 by the librefonts community effort (contributors: vitalyvolkov, xen) to preserve font sources from the Google Fonts library. The repo contains TTX decomposed font files and original VFB (FontLab) source files.

## How the Commit Hash Was Identified

The upstream repository contains only a single commit:

- `45d202a` (2014-10-17, by hash3g): "update .travis.yml"

This sole commit added all files to the repo in one go -- the TTX files, VFB sources, DESCRIPTION.en_us.html, METADATA.json, OFL.txt, and a .travis.yml. The font version in the upstream repo is **1.001** (seen in the `_name` TTX: "Version 1.001; ttfautohint (v0.8) -G 200 -r 50" and in `_head` TTX: fontRevision 1.00100708008).

**Important note**: The current font in google/fonts is **version 1.002**, updated by PR #5355 (merged 2022-10-07 by Rosalie Wagner). This HOTFIX was created directly in the google/fonts repo to fix a ligature bug (issue #3089: `ffu` ligature in words like "diffusion" incorrectly rendered as `ffh`). The HOTFIX also corrected naming inconsistencies between the font file (CantoraOne) and the API name (Cantora One). The upstream librefonts repo was **never updated** with the v1.002 HOTFIX.

Therefore, the commit `45d202a` represents the original v1.001 sources, not the current v1.002 binary in google/fonts. The v1.002 changes were made directly in google/fonts PR #5355 without corresponding upstream changes.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository and none can be created. The source files are:

- `src/CantoraOne-Regular.vfb` -- FontLab 5 binary source
- `src/CantoraOne-Regular-TTF.vfb` -- FontLab 5 binary (TTF version)
- `src/CantoraOne-Regular-OTF.vfb` -- FontLab 5 binary (OTF version)
- `src/CantoraOne-Regular.otf.*.ttx` -- TTX decomposed OTF tables
- `CantoraOne-Regular.ttf.*.ttx` -- TTX decomposed TTF tables (at repo root)

VFB is the proprietary FontLab 5 binary format. It is **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources. There are no open-format editable sources available for this font. An override config.yaml cannot be created because there are no compatible source files to reference.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17
- Commit message: "update .travis.yml"
- Source files at commit: `src/CantoraOne-Regular.vfb`, `src/CantoraOne-Regular-TTF.vfb`, `src/CantoraOne-Regular-OTF.vfb`, plus TTX files and `src/FONTLOG.txt`

## Additional Context

- **Font added to Google Fonts**: 2012-07-30 (per METADATA.pb `date_added`)
- **Initial google/fonts commit**: 90abd17b (2015-03-07, by Dave Crossland) -- "Initial commit" that created the entire google/fonts repo
- **HOTFIX PR #5355**: Merged 2022-10-07 by Rosalie Wagner. Fixed ligature bug from issue #3089 and corrected metadata. The font binary was updated from v1.001 to v1.002 directly in google/fonts.
- **librefonts repo**: Created 2014-07-16, last pushed 2014-10-17. This is a community archive, not an active development repo. It was never updated with the v1.002 fix.
- **Original designer**: Pablo Impallari (impallari@gmail.com) and Rodrigo Fuenzalida (hello@rfuenzalida.com), with spacing/kerning by Igino Marini

## Confidence

**MEDIUM**: The repository URL is confirmed as the only known upstream source for Cantora One. However, the upstream repo only contains v1.001 sources while google/fonts has v1.002 (from a direct HOTFIX). The source files are in VFB format, which is incompatible with gftools-builder, so no config.yaml can be created. The commit hash is the only commit in the repo and represents the pre-HOTFIX state. A complete rebuild from source would require converting the VFB files to an open format first.
