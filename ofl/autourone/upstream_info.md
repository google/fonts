# Autour One

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Sorkin Type
**METADATA.pb path**: `ofl/autourone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/autourone |
| Commit | `10ccd1eb5ad3e7088ce2dd099debff0ac08daf1c` |
| Config YAML | — |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL is not present in the current METADATA.pb on the main branch (there is no source block). It was identified in the tracking data (`gfonts_library_sources.json`) and exists on a pending PR branch (`sources_info_2026-02-25`, commit `9a14639f3`). The upstream repo at `librefonts/autourone` was verified in the cache with remote URL `https://github.com/librefonts/autourone`.

As with Audiowide, this is a `librefonts` organization mirror typical of early Google Fonts families.

## How the Commit Hash Was Identified

The upstream repository has only a single commit: `10ccd1eb5ad3e7088ce2dd099debff0ac08daf1c` (2014-10-17, "update .travis.yml"). The font was last updated in google/fonts via PR #833 (`592bee48`, "hotfix-autourone: v1.007 added", 2017-08-07) by Marc Foley. The PR body and comments are empty. Since the upstream repo has only one commit, this is the only possible reference point.

## How Config YAML Was Resolved

No `config.yaml` or `builder.yaml` exists in the upstream repository. No override `config.yaml` exists in `google/fonts/ofl/autourone/`.

The source files in the repository are:
- `src/AutourOne-Regular-OTF.sfd` (FontForge SFD)
- `src/AutourOne-Regular-TTF.sfd` (FontForge SFD)
- `src/AutourOne-Regular.vfb` (FontLab binary, not listed in source_types but present)
- Various `.ttx` XML dumps of font tables

SFD files are FontForge's native format and are not directly compatible with gftools-builder. The VFB file is FontLab's proprietary format.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:29:59 +0300
- Commit message: "update .travis.yml"
- Source files at commit:
  - `src/AutourOne-Regular-OTF.sfd` (FontForge format)
  - `src/AutourOne-Regular-TTF.sfd` (FontForge format)
  - `src/AutourOne-Regular.vfb` (FontLab binary)
  - Multiple `.ttx` table dumps (not editable sources)

## Confidence

**Medium**: The repository URL is verified and the commit is the only one available. However, the repo is a librefonts archive with only SFD and VFB sources, not modern buildable formats. The v1.007 hotfix in google/fonts (2017) was made 3 years after the last upstream commit (2014), suggesting the binary was modified independently. Without source conversion, a config.yaml cannot be meaningfully added.

## Open Questions

- Is there an original upstream repository maintained by Sorkin Type (Eben Sorkin)?
- Eben Sorkin maintains the `EbenSorkin` GitHub account and is associated with Sorkin Type. It's worth checking if there's a dedicated Autour One repo under that account.
- Should the SFD sources be converted to UFO or .glyphs format to enable gftools-builder builds?
- The SFD sources include separate OTF and TTF variants, which is an unusual source structure.
