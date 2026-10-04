# Bangers

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Vernon Adams
**METADATA.pb path**: `ofl/bangers/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/bangers |
| Commit | `ca6d2f15db343ee373e9c62a127f3a48cd251228` (fontc_crater target; see below) |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found
The repository URL is documented in the METADATA.pb `source {}` block and confirmed by the gftools-packager commit message (cf67eacb4, 2023-06-22): "taken from the upstream repo https://github.com/googlefonts/bangers".

## How the Commit Hash Was Identified
The gftools-packager commit message states: "at commit https://github.com/googlefonts/bangers/commit/7b1747307aeb617957a216213de28b14d3281d9d". This is the **true onboarding commit** (2023-06-22, "Merge pull request #2 from emmamarichal/main" by Emma Marichal).

However, the commit hash currently in METADATA.pb (`ca6d2f15db343ee373e9c62a127f3a48cd251228`) is a DIFFERENT, NEWER commit (2025-02-24, "add sources/config.yaml" by Felipe Sanches). This commit was added to METADATA.pb via the fontc_crater targets batch (commit 19cdcec59, 2025-03-31).

The reason: at the original onboarding commit (7b17473), no `config.yaml` existed. Felipe Sanches later added `sources/config.yaml` to the upstream repo (ca6d2f1), and the fontc_crater target pointed to this latest commit.

## How Config YAML Was Resolved
`sources/config.yaml` was added to the upstream repo by Felipe Sanches in commit `ca6d2f15db343ee373e9c62a127f3a48cd251228` (2025-02-24). It is a simple config that builds from `Bangers.glyphs`. This config did NOT exist at the original onboarding commit (7b17473).

## Verification
- Commit ca6d2f1 exists in upstream repo: Yes
- Commit date: 2025-02-24 22:40:58 -0300
- Commit message: "add sources/config.yaml"
- Original onboarding commit 7b17473 exists: Yes (after unshallowing)
- Original onboarding commit date: 2023-06-22 15:17:31 +0200
- Original onboarding commit message: "Merge pull request #2 from emmamarichal/main"
- Source files at ca6d2f1: `sources/Bangers.glyphs`, `sources/config.yaml`
- Source files at 7b17473: `sources/Bangers.glyphs` (no config.yaml)
- TTFs last updated in google/fonts: 2023-06-22 (commit cf67eacb4, PR by gftools-packager)
- No override config.yaml in google/fonts family directory

## Confidence
**High**: The repository URL, config.yaml, and current commit hash are all verified. The commit in METADATA.pb (ca6d2f1) is the fontc_crater target commit, not the original onboarding commit (7b17473). For fontc_crater rebuild purposes, ca6d2f1 is correct because it includes the config.yaml needed for building.

## Open Questions
- The METADATA.pb commit (ca6d2f1) differs from the original onboarding commit (7b17473). The ca6d2f1 commit adds config.yaml but does not change the font sources. This is acceptable for fontc_crater but does not reflect the original onboarding state.
- The `files` entries in METADATA.pb reference `fonts/ttf/Bangers-Regular.ttf` which existed at the onboarding commit (7b17473), where the fonts were pre-built in the repo.
