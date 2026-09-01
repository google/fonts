# Audiowide

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Astigmatic
**METADATA.pb path**: `ofl/audiowide/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/audiowide |
| Commit | `eccbd790f5c851314d6c4409a2058156a3186782` |
| Config YAML | — |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL is not present in the current METADATA.pb on the main branch (there is no source block at all). It was identified in the tracking data (`gfonts_library_sources.json`) and exists on a pending PR branch (`sources_info_2026-02-25`, commit `9a14639f3`). The upstream repo at `librefonts/audiowide` was verified in the cache with remote URL `https://github.com/librefonts/audiowide`.

Note: The `librefonts` GitHub organization contains archived copies of many Google Fonts sources. This is a common pattern for early Google Fonts families.

## How the Commit Hash Was Identified

The upstream repository has only a single commit: `eccbd790f5c851314d6c4409a2058156a3186782` (2014-10-17, "update .travis.yml"). The font was last updated in google/fonts via PR #832 (`1b455676`, "hotfix-audiowide: v1.003 added", 2017-08-07) by Marc Foley. The PR body and comments are empty. Since the upstream repo has only one commit, this is the only possible reference point.

## How Config YAML Was Resolved

No `config.yaml` or `builder.yaml` exists in the upstream repository. No override `config.yaml` exists in `google/fonts/ofl/audiowide/`.

The source files in the repository are:
- `src/Audiowide-Regular-OTF.vfb` (FontLab binary)
- `src/Audiowide-Regular-TTF.vfb` (FontLab binary)
- `src/Audiowide-Regular.vfb` (FontLab binary)
- Various `.ttx` XML dumps of font tables

VFB files are proprietary FontLab Studio format and are not compatible with gftools-builder. The TTX files are XML representations of compiled font tables, not editable design sources.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:29:55 +0300
- Commit message: "update .travis.yml"
- Source files at commit:
  - `src/Audiowide-Regular.vfb` (FontLab binary)
  - `src/Audiowide-Regular-OTF.vfb` (FontLab binary)
  - `src/Audiowide-Regular-TTF.vfb` (FontLab binary)
  - Multiple `.ttx` table dumps (not editable sources)

## Confidence

**Medium**: The repository URL is verified and the commit is the only one available. However, the upstream repo appears to be an archived librefonts mirror with only VFB binary sources and TTX dumps, not modern buildable sources. The v1.003 hotfix in google/fonts (2017) was made 3 years after the last upstream commit (2014), suggesting the font binary was modified independently. The lack of any gftools-compatible source format means a config.yaml cannot be meaningfully created without source conversion.

## Open Questions

- The `librefonts/audiowide` repo appears to be an archived mirror. Is there an original upstream repository maintained by Astigmatic (Brian J. Bonislawsky)?
- Should the VFB sources be converted to UFO or .glyphs format to enable gftools-builder builds?
- The font has only VFB sources. Without conversion, there is nothing that can be referenced in a config.yaml.
