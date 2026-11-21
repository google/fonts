# Barriecito

**Date investigated**: 2026-02-26
**Status**: complete (commit hash corrected)
**Designer**: Omnibus-Type
**METADATA.pb path**: `ofl/barriecito/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Omnibus-Type/Barrio |
| Commit | a65aa86a745f39053a1ac892cf917cdcc1cacdf3 |
| **Config YAML** | Override in google/fonts |
| Branch | master |

## How the Repository URL Was Found
The METADATA.pb does not have a source block, but the copyright string says "Copyright 2018 The Barriecito Project Authors (https://github.com/Omnibus-Type/Barrio/Barriecito)". PR #1673 ("barriecito: v1.001 added", by Marc Foley, merged 2019-06-12) explicitly states: "Taken from the upstream repo https://github.com/Omnibus-Type/Barrio". The Barriecito sources live in a `Barriecito/` subdirectory within the Omnibus-Type/Barrio repository.

## How the Commit Hash Was Identified
PR #1673 body explicitly states: "Taken from the upstream repo https://github.com/Omnibus-Type/Barrio at commit https://github.com/Omnibus-Type/Barrio/commit/a65aa86a745f39053a1ac892cf917cdcc1cacdf3".

This commit (2018-08-07, "Fixed glyph names and vertical metrics") was made by Marc Foley and is the exact commit referenced in the onboarding PR. The previous tracking data incorrectly listed commit `8f33bf1` (HEAD of master, from 2019-03-12, "Update README.md") which is a later commit not related to the onboarding.

## How Config YAML Was Resolved
No `config.yaml` exists in the upstream repository at any commit. No override `config.yaml` exists in the google/fonts `ofl/barriecito/` directory. The Barriecito sources are in `Barriecito/sources/Barriecito.glyphs` and `Barriecito/sources/Barriecito.ufo/` at the onboarding commit.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2018-08-07
- Commit message: "Fixed glyph names and vertical metrics"
- Source files at commit: `Barriecito/sources/Barriecito.glyphs`, `Barriecito/sources/Barriecito.ufo/`, `Barriecito/sources/Backup/1138_Barriecito.glyphs`
- PR #1673 references this exact commit: Yes

## Confidence
**High**: The PR body explicitly references this exact commit hash. This is the strongest possible evidence.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - Barriecito/sources/Barriecito.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions
- The METADATA.pb lacks a source block. A PR should add `source { repository_url: "https://github.com/Omnibus-Type/Barrio" commit: "a65aa86a745f39053a1ac892cf917cdcc1cacdf3" }`.
- A config.yaml needs to be created. The Barriecito source is in a subdirectory (`Barriecito/sources/`) of the Barrio repository, which complicates config.yaml paths.
