# Coustard

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Vernon Adams
**METADATA.pb path**: `ofl/coustard/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/vernnobile/coustardFont |
| Commit | `5f54d232ff52d0d43bad509357f03c5ddbdf51fc` |
| Config YAML | N/A (SFD-only sources) |
| Branch | (default) |

## How the Repository URL Was Found

The repository URL `https://github.com/vernnobile/coustardFont` was added to the METADATA.pb source block by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)", 2024-01-14). The repo is under the `vernnobile` GitHub account, which corresponds to Vernon Adams (the original designer) migrated from Google Code. The repo contains the font's SFD sources and TTF binaries.

## How the Commit Hash Was Identified

The commit hash `5f54d232ff52d0d43bad509357f03c5ddbdf51fc` is the only commit in the upstream repository ("migrate from code.google", 2013-03-01). Since there is only one commit, it is trivially the correct reference. The commit hash was added to METADATA.pb in the pending PR branch `felipesanches/sources_info_2026-02-25` (commit `9a14639f3`, "Add source blocks to 602 more METADATA.pb files").

Note: The TTF files in google/fonts differ from those in the upstream repo because the fonts were updated via PR #881 ("hotfix-coustard: v1.001 added", by Marc Foley, 2017-05-08). The v1.001 hotfix updated the binaries without changing the upstream repo. The upstream repo's SFD sources are the original pre-hotfix sources.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository or in the google/fonts family directory. The upstream repo contains only SFD (FontForge) source files:
- `src/Coustard-Regular.sfd`
- `src/Coustard-Regular-TTF.sfd`
- `src/Coustard-Heavy.sfd`
- `src/Coustard-Black-TTF.sfd`

SFD files are not compatible with gftools-builder, so a config.yaml cannot be created without converting the sources to a modern format (e.g., .glyphs or .ufo).

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes (only commit / HEAD)
- Commit date: 2013-03-01 12:53:06 -0800
- Commit message: "migrate from code.google"
- Font files match: No (google/fonts has v1.001 from hotfix PR #881; upstream has original version)
- Source files at commit: SFD files only (`src/Coustard-Regular.sfd`, `src/Coustard-Regular-TTF.sfd`, `src/Coustard-Heavy.sfd`, `src/Coustard-Black-TTF.sfd`)
- Override config.yaml: Not present

## Confidence

**High**: The repository URL is confirmed through the `vernnobile` GitHub organization, which is Vernon Adams's account used for migrating fonts from Google Code. The commit hash is the only commit in the repo, making it unambiguous. The mismatch between upstream TTFs and google/fonts TTFs is explained by the 2017 hotfix (PR #881).

## Open Questions

1. The upstream repo sources (SFD) are from the original version, while google/fonts serves v1.001 from the 2017 hotfix. Where are the sources for the v1.001 hotfix? They may have been generated without updating the upstream repo.
2. No config.yaml can be created from SFD sources without source conversion. This family will remain in `missing_config` status unless the sources are modernized.
