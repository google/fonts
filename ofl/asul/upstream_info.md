# Asul

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Mariela Monsalve
**METADATA.pb path**: `ofl/asul/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/asul |
| Commit | `687362de82c870100b6003ad71a82c3327e05d90` |
| Config YAML | --- |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was identified during a prior batch investigation and added to `data/gfonts_library_sources.json` with a pending source block addition (commit `9a14639f3` on branch `felipesanches/sources_info_2026-02-25`). The URL `https://github.com/librefonts/asul` points to a repository under the `librefonts` GitHub organization, which hosts many libre font projects originally migrated from Google Fonts. The METADATA.pb on the main branch of google/fonts does not yet contain a source block; one was prepared in the pending branch but has not been merged.

## How the Commit Hash Was Identified

The commit hash `687362de82c870100b6003ad71a82c3327e05d90` was identified during a batch investigation process. The upstream repository appears to be a shallow clone with only this single commit visible. This is the latest (and possibly only) commit in the repository. The commit message is "update .travis.yml" dated 2014-10-17, which predates the last font update in google/fonts (PR #829, "hotfix-asul: v1.002 added", dated 2017-08-07). This suggests the fonts in google/fonts may have been compiled from this commit or from a state that is no longer fully traceable.

The google/fonts PR #829 body was empty, providing no additional upstream reference.

## How Config YAML Was Resolved

There is no `config.yaml` in the upstream repository at the referenced commit. The upstream repo contains only SFD (FontForge) source files (`src/Asul-Bold-TTF.sfd` and `src/Asul-Regular-TTF.sfd`), which are not compatible with gftools-builder. There is also no override `config.yaml` in `google/fonts/ofl/asul/`.

Building from SFD sources would require a different build pipeline or a manual conversion to a gftools-builder-compatible format.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:29:49 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Asul-Bold-TTF.sfd`, `src/Asul-Regular-TTF.sfd` (SFD format only), plus `.travis.yml`, TTX dumps, and `.vfb` files

## Confidence

**Medium**: The repository URL is correct and the commit exists, but the relationship between this commit and the actual fonts in google/fonts is uncertain. The last font file update in google/fonts (PR #829, 2017-08-07) postdates the upstream commit (2014-10-17), and the upstream repo only has SFD sources while google/fonts has TTF binaries. It is likely the fonts were compiled from these SFD sources at some point, but the exact build process is unclear. The SFD-only nature of the sources means a config.yaml cannot be meaningfully created for gftools-builder.

## Open Questions

1. Were the TTF files in google/fonts compiled from the SFD sources in this upstream repo, or were they provided separately by the designer?
2. Is there a different upstream repository with the actual build sources (e.g., .glyphs or .ufo files)?
3. The commit is from 2014 but the font was updated in google/fonts in 2017 -- was a newer version compiled from these same sources with updated tooling?
