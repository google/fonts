# Covered By Your Grace

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Kimberly Geswein
**METADATA.pb path**: `ofl/coveredbyyourgrace/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/coveredbyyourgrace |
| Commit | `eca9fdc2d5ae964ff4838cb850b215d9ea703801` |
| Config YAML | N/A (SFD-only sources) |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/coveredbyyourgrace` is from the `librefonts` GitHub organization, which is a collection of archived Google Fonts sources migrated from earlier hosting. The URL was added to METADATA.pb in the pending PR branch `felipesanches/sources_info_2026-02-25` (commit `9a14639f3`, "Add source blocks to 602 more METADATA.pb files"). The main branch of google/fonts does not yet have a source block for this family.

## How the Commit Hash Was Identified

The commit hash `eca9fdc2d5ae964ff4838cb850b215d9ea703801` is the only commit in the upstream repository ("update .travis.yml", 2014-10-17). Since this is a single-commit repo, it is trivially the correct and only possible reference. The font was first added to Google Fonts on 2010-12-07 (per `date_added` in METADATA.pb) and has never been modified in google/fonts since the initial commit `90abd17b4` (2015-03-07, which imported the entire existing catalog).

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository or in the google/fonts family directory. The upstream repo contains:
- `src/CoveredByYourGrace-TTF.sfd` (FontForge SFD format)
- `src/CoveredByYourGrace.vfb` (FontLab VFB format)
- Various TTX decomposition files

SFD and VFB files are not compatible with gftools-builder, so a config.yaml cannot be created without converting the sources to a modern format.

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes (only commit / HEAD)
- Commit date: 2014-10-17 13:33:46 +0300
- Commit message: "update .travis.yml"
- Source block on main: No (pending PR branch only)
- Source files at commit: SFD and VFB files only
- Override config.yaml: Not present

## Confidence

**High**: The librefonts organization is a well-known archive of Google Fonts sources. The repo has only one commit, making the hash unambiguous. The font has never been updated in google/fonts since the initial catalog import.

## Open Questions

1. The source block (repository_url and commit hash) has not yet been merged to google/fonts main -- it is on the pending branch `felipesanches/sources_info_2026-02-25`.
2. No config.yaml can be created from SFD/VFB sources without source conversion. This family will remain in `missing_config` status unless the sources are modernized.
