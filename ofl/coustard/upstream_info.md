# Coustard

**Date investigated**: 2026-02-26 (initial); 2026-04-27 (post-migration update)
**Status**: complete (was missing_config)
**Designer**: Vernon Adams
**METADATA.pb path**: `ofl/coustard/METADATA.pb`
**Model**: Claude Opus 4.6 (initial) / Claude Opus 4.7 (1M context) (update)

## Source Data (current — post 2026-03-20 repo migration)

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/coustardFont (migrated; was vernnobile/coustardFont) |
| Commit | `84d4ef2fbb8e87ba843d49308b98eeb4a874be91` (was `5f54d232ff52d0d43bad509357f03c5ddbdf51fc`) |
| Config YAML | `sources/config.yaml` (added 2026-04-27 by this commit; upstream now ships a gftools-builder config) |
| Branch | `master` |

## Source Data (original — pre-migration, kept for historical reference)

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

## Recent upstream/main activity (post-investigation)

The original (2026-02-26) investigation flagged `missing_config` because the only known upstream `vernnobile/coustardFont` had SFD-only sources. Both issues raised in Open Questions have now been resolved by an upstream repo migration:

- **2026-03-20** — Emma Marichal, commit [`a0db74464`](https://github.com/google/fonts/commit/a0db74464) ("Coustard: Version 1.100; ttfautohint (v1.8.4.16-eb64) added"): updated to v1.100 and migrated the recorded upstream from `vernnobile/coustardFont` to a new canonical fork at `googlefonts/coustardFont`. Emma developed the modernization upstream (PR #1 from `emmamarichal/master` was merged to `googlefonts/coustardFont` as commit `84d4ef2fb`); the new repo includes:
  - Modern `.glyphs` source: `sources/Coustard.glyphs`
  - gftools-builder `sources/config.yaml`
  - Pre-built TTF/OTF/WOFF2 in `fonts/ttf/`, `fonts/otf/`, `fonts/webfonts/`
  - Original SFD sources preserved under `sources/archives/`

The shipping `Coustard-Regular.ttf` (75432 bytes, md5 `1b81850f782640f19b5cc3244e629ade`) is byte-identical to upstream `fonts/ttf/Coustard-Regular.ttf` at commit `84d4ef2fb`. `head.fontRevision = 1.1000`, `name` ID 5 = "Version 1.100; ttfautohint (v1.8.4.16-eb64)".

### Updated source-of-truth fields

- **Repository URL**: `https://github.com/googlefonts/coustardFont` (was `https://github.com/vernnobile/coustardFont`).
- **Commit**: `84d4ef2fbb8e87ba843d49308b98eeb4a874be91` (the merge of upstream PR #1, 2026-03-20).
- **Config YAML**: `sources/config.yaml` (added 2026-04-27 by this commit; the upstream config exists at the recorded commit and is fully functional).
- **Branch**: `master`.
- **Status**: **complete** (was missing_config).
- **Confidence**: HIGH (md5-verified shipping binary).

### Original Repository (dormant)

The original `vernnobile/coustardFont` repo (Vernon Adams's GitHub account, `5f54d232f` "migrate from code.google" 2013-03-01) is preserved as historical context above. It remains accessible online but is superseded by the `googlefonts/coustardFont` fork as the source-of-truth for current Coustard onboarding. Per policy, full details of the original repo are kept in this report.

### Follow-up note

The new copyright string in METADATA.pb (added by Emma's commit a0db74464) reads `"Copyright 2011 The Coustard Project Authors (https://github.com/googlefonts/bangers)"` — the URL `googlefonts/bangers` appears to be a typo (Bangers is a different family). The likely correct URL is `https://github.com/googlefonts/coustardFont`. This is outside the source-block sync scope but worth flagging for a future fix.
