# Creepster

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Sideshow (Font Diner)
**METADATA.pb path**: `ofl/creepster/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/creepster |
| Commit | `f6eec0d741fd8ecba905f403d77c073f2e8be7f6` |
| Config YAML | N/A (SFD-only sources) |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/creepster` is from the `librefonts` GitHub organization, which archives Google Fonts sources migrated from earlier hosting. The URL was added to METADATA.pb in the pending PR branch `felipesanches/sources_info_2026-02-25` (commit `9a14639f3`, "Add source blocks to 602 more METADATA.pb files"). The main branch of google/fonts does not yet have a source block for this family.

## How the Commit Hash Was Identified

The commit hash `f6eec0d741fd8ecba905f403d77c073f2e8be7f6` is the only commit in the upstream repository ("update .travis.yml", 2014-10-17). Since this is a single-commit repo, it is trivially the correct and only possible reference. The font was first added to Google Fonts on 2011-12-19 (per `date_added` in METADATA.pb) and the TTF file has never been modified in google/fonts since the initial commit `90abd17b4` (2015-03-07, which imported the existing catalog).

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository or in the google/fonts family directory. The upstream repo contains only:
- `src/Creepster-Regular-TTF.sfd` (FontForge SFD format)

SFD files are not compatible with gftools-builder, so a config.yaml cannot be created without converting the sources to a modern format.

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes (only commit / HEAD)
- Commit date: 2014-10-17 13:33:48 +0300
- Commit message: "update .travis.yml"
- Source block on main: No (pending PR branch only)
- Source files at commit: SFD file only (`src/Creepster-Regular-TTF.sfd`)
- Override config.yaml: Not present

## Confidence

**High**: The librefonts organization is a well-known archive of Google Fonts sources. The repo has only one commit, making the hash unambiguous. The font binary has never been updated in google/fonts since the initial catalog import.

## Open Questions

1. The source block (repository_url and commit hash) has not yet been merged to google/fonts main -- it is on the pending branch `felipesanches/sources_info_2026-02-25`.
2. No config.yaml can be created from SFD sources without source conversion. This family will remain in `missing_config` status unless the sources are modernized.
3. The copyright mentions "Font Diner, Inc DBA Sideshow" -- the designer credit uses "Sideshow" as the key in METADATA.pb.
