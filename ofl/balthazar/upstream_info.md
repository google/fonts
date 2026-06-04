# Balthazar

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Dario Manuel Muhafara
**METADATA.pb path**: `ofl/balthazar/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/balthazar |
| Commit | `baa08c6f633b0fda1a83141ce7515441c56e9868` |
| Config YAML | N/A (no config.yaml exists; sources are not gftools-builder compatible) |
| Branch | `master` |

## How the Repository URL Was Found
The METADATA.pb has no `source {}` block at all. The repository URL was found via the upstream repo cache at `upstream_repos/fontc_crater_cache/librefonts/balthazar/`. The remote URL `https://github.com/librefonts/balthazar` matches the expected pattern for librefonts-hosted legacy Google Fonts projects.

## How the Commit Hash Was Identified
The upstream repo has only a single commit: `baa08c6f633b0fda1a83141ce7515441c56e9868` (2014-10-17, "update .travis.yml" by hash3g). This is the only possible reference point. The tracking file already had this commit recorded.

## How Config YAML Was Resolved
No `config.yaml` exists anywhere in the upstream repository. The repository contains only legacy source formats:
- `.vfb` (FontLab Studio format) - proprietary, cannot be used by gftools-builder
- `.sfd` (FontForge format) - not directly supported by gftools-builder
- `.ttx` (TTX/FontTools XML dumps)

The font was onboarded to Google Fonts in the very early era (date_added: 2011-12-13, initial commit in google/fonts: 2015-03-07). There is no way to build this font with gftools-builder without first converting the sources to .glyphs or .ufo format.

No override config.yaml exists in the google/fonts family directory either.

## Verification
- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2014-10-17 13:30:20 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Balthazar-Regular.vfb`, `src/Balthazar-Regular-TTF.sfd`, various `.ttx` files
- TTFs last updated in google/fonts: 2015-04-27 (commit 321eeddad, "Updating ofl/balthazar/*ttf with nbspace and fsType fixes")
- The font binary was likely patched in google/fonts directly, not rebuilt from source

## Confidence
**High**: The repository URL and commit are confirmed. The status is correctly "missing_config" because the upstream repo lacks both a config.yaml and gftools-builder-compatible source formats.

## Open Questions
- This is a legacy font with only .vfb/.sfd sources. To make it buildable with gftools-builder, the sources would need to be converted to .glyphs or .ufo format. This is a significant effort and may not be prioritized.
- The METADATA.pb has no `source {}` block. A source block with repository_url and commit could be added, though config_yaml would still be absent.
