# Basic

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Magnus Gaarde
**METADATA.pb path**: `ofl/basic/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/EbenSorkin/Basic |
| Commit | 202e65ac93bd6977e83b2f10db6b1467e0b348db |
| **Config YAML** | Override in google/fonts |
| Branch | master |

## How the Repository URL Was Found
The METADATA.pb already contains `repository_url: "https://github.com/EbenSorkin/Basic"`. The copyright says "Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com)". Eben Sorkin is the foundry principal at Sorkin Type who commissioned the design from Magnus Gaarde.

## How the Commit Hash Was Identified
Basic is a very early Google Fonts family (added 2011-12-15). The last commit to modify .ttf files in `ofl/basic/` was `9db9820a4304b094946a98f3c71cc93c68e37b6f` (2015-04-27, "Updating ofl/basic/*ttf with nbspace and fsType fixes"), which was a batch maintenance fix applied across many families, not a proper onboarding from upstream sources.

The upstream repo's commit history shows that `202e65ac93bd6977e83b2f10db6b1467e0b348db` (2015-01-28, "smaller file size - new TTFA hinting") is the last meaningful commit before the google/fonts TTF update. This is the best available upstream reference, though the exact relationship between this commit and the google/fonts binaries is uncertain -- the google/fonts batch fix may have applied post-hoc modifications to the TTFs.

The initial commit to google/fonts was `90abd17b4` ("Initial commit") which predates the upstream GitHub repository, and the TTF was then updated via `9db9820a4` with technical fixes.

## How Config YAML Was Resolved
No `config.yaml` exists in the upstream repository at any commit. No override `config.yaml` exists in the google/fonts `ofl/basic/` directory. The source at commit `202e65a` is `Basic-Regular.ufo/`. A `.glyphspackage` file was added much later in 2024 (commit `da415d7`, "start a weight test"), but this is unrelated to the current Google Fonts version.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2015-01-28
- Commit message: "smaller file size - new TTFA hinting"
- Source files at commit: `Basic-Regular.ufo/`, `Basic-Regular.otf`, `Basic-Regular.ttf`
- Note: The upstream repo contains pre-built TTF/OTF binaries, not just sources

## Confidence
**Medium**: The commit hash `202e65a` is the best available approximation for the upstream state corresponding to the google/fonts binaries. However, this is a very early font (2011) that predates modern gftools-based onboarding workflows. The google/fonts binaries may have been compiled separately or modified with batch fixes after import. The commit hash is already correctly recorded in the tracking data.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - Basic-Regular.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions
- Basic is a single-weight family with a simple UFO source. A config.yaml could be created to build it, but the 2024 .glyphspackage addition ("start a weight test") suggests the designer may be working on expanding the family.
- Since the font predates modern onboarding workflows, the exact provenance of the current google/fonts binary is uncertain.
