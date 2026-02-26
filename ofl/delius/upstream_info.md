# Delius - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Delius |
| Designer | Natalia Raices |
| License | OFL |
| Repository URL | https://github.com/librefonts/delius |
| Commit Hash | 5bd1633b6b5175d36e260f3f6d06686482d32212 |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |
| Date Added | 2011-07-27 |

## How URL Found

The repository URL `https://github.com/librefonts/delius` was identified through the librefonts GitHub organization, which hosts many of the older Google Fonts projects. The URL was added to the tracking data and a source block was prepared (commit `9a14639f3`, currently on a PR branch `sources_info_2026-02-25`, not yet merged to main).

## How Commit Determined

The commit `5bd1633b6b5175d36e260f3f6d06686482d32212` is the HEAD of the master branch in the upstream repo (the only visible commit in the shallow clone: "update .travis.yml"). This is a legacy font from the initial google/fonts commit (2015-03-07). The font has been in the catalog since 2011-07-27.

The TTF file in google/fonts was last modified in the deploy commit `76adaf1d2` (2021-11-01, "deploy: c7e2740...") which was a bulk deployment affecting many fonts. Before that, it was in the initial commit `90abd17b4`.

Since this is a legacy font with SFD-only sources, the commit hash serves mainly to reference the state of the upstream repository rather than a specific build commit. The upstream repo contains:
- `src/Delius-Regular-TTF.sfd` (FontForge source)
- `src/Delius-Regular.vfb` (FontLab source)
- TTX decompositions of the font tables
- No modern build sources (.glyphs, .ufo, .designspace)

## Config YAML Status

- No `config.yaml` exists in the upstream repository
- No override `config.yaml` exists in google/fonts at `ofl/delius/`
- The upstream repo only contains SFD (FontForge) and VFB (FontLab) source formats
- These formats are not compatible with gftools-builder
- A config.yaml cannot be created without converting the sources to a modern format first

## Verification

- Repository URL is valid and accessible
- Upstream repo cloned at `upstream_repos/fontc_crater_cache/librefonts/delius/` (shallow clone)
- Commit `5bd1633` verified as HEAD of master
- No modern source files found (.glyphs, .ufo, .designspace)
- METADATA.pb in google/fonts main branch currently has no source block (a PR branch adds one)

## Confidence Level

**High** for repository URL (well-established librefonts organization). **Medium** for commit hash (it's the HEAD of the repo, but it's a shallow clone so we can't verify the full history). **N/A** for config_yaml (sources are in legacy format only).

## Open Questions

- The font sources would need to be converted to a modern format (e.g., .glyphs or .ufo) before a config.yaml could be created.
- The source block for METADATA.pb has been prepared on branch `sources_info_2026-02-25` but is not yet merged.
- Since this is a very old font (2011) with SFD sources, it may not be a priority for source documentation.
