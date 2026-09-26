# BatangChe

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: HanYang I&C Co.
**METADATA.pb path**: `ofl/batangche/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/batang |
| Commit | `6c1e09f93204c963881afbb4e25699095565f2e5` |
| Config YAML | N/A (not applicable) |
| Branch | main |

## How the Repository URL Was Found
BatangChe shares the same upstream repository as Batang: `https://github.com/googlefonts/batang`. The copyright string confirms: "Copyright 2024 The Batang and Gungsuh Project Authors (https://github.com/googlefonts/batang)". The google/fonts onboarding commit 00a32113 (2024-05-15) states: "Taken from the upstream repo https://github.com/googlefonts/batang at commit https://github.com/googlefonts/batang/commit/6c1e09f93204c963881afbb4e25699095565f2e5".

## How the Commit Hash Was Identified
The commit hash `6c1e09f93204c963881afbb4e25699095565f2e5` is recorded in METADATA.pb and confirmed by the google/fonts onboarding commit 00a32113. This is the same commit used for Batang, which is the HEAD of the main branch, titled "updating names" by Aaron Bell on 2024-05-15. Both Batang and BatangChe were onboarded the same day from the same commit.

## How Config YAML Was Resolved
Same situation as Batang: there is no config.yaml in the upstream repo, and this is expected. The BatangChe font is produced by the same custom Python script (`process.py`) that processes all four legacy Korean font families (Batang, BatangChe, Gungsuh, GungsuhChe) from their original TTF source files.

The source file for BatangChe is `sources/BatangChe.ttf`, and the output used by google/fonts is `fonts/ttf/hinted/batangche-Regular.ttf`.

No standard font source files (.glyphs, .ufo, .designspace) exist in the repository, making gftools-builder config.yaml fundamentally inapplicable.

No override config.yaml exists in the google/fonts family directory.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2024-05-15 21:34:44 -0700
- Commit message: "updating names"
- Commit is HEAD of main branch: Yes (no subsequent commits)
- Source file at commit: `sources/BatangChe.ttf`
- Output font file used: `fonts/ttf/hinted/batangche-Regular.ttf`

## Confidence
**High**: The repository URL and commit hash are well-documented and verified. The missing config.yaml is expected because this repo uses a custom build pipeline for legacy Korean fonts. The status correctly reflects the technical reality.

## Open Questions
- Same as Batang: should the status be updated to reflect that config.yaml is not applicable rather than simply missing?
