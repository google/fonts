# Batang

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: HanYang I&C Co.
**METADATA.pb path**: `ofl/batang/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/batang |
| Commit | `6c1e09f93204c963881afbb4e25699095565f2e5` |
| Config YAML | N/A (not applicable) |
| Branch | main |

## How the Repository URL Was Found
The repository URL `https://github.com/googlefonts/batang` is documented in the METADATA.pb `source { }` block. It is also confirmed by the copyright string: "Copyright 2024 The Batang and Gungsuh Project Authors (https://github.com/googlefonts/batang)". The google/fonts onboarding commit 6e2ac37a (2024-05-15) explicitly states: "Taken from the upstream repo https://github.com/googlefonts/batang at commit https://github.com/googlefonts/batang/commit/6c1e09f93204c963881afbb4e25699095565f2e5".

## How the Commit Hash Was Identified
The commit hash `6c1e09f93204c963881afbb4e25699095565f2e5` is recorded in METADATA.pb and confirmed by the google/fonts onboarding commit 6e2ac37a. The commit is the HEAD of the main branch (the latest commit in the repository), titled "updating names" by Aaron Bell on 2024-05-15.

## How Config YAML Was Resolved
There is no config.yaml in the upstream repo, and this is expected. The Batang repository does not use gftools-builder for compilation. Instead, it uses a custom Python script (`process.py`) with a Makefile-based build system.

The repository contains legacy Korean TTF source files (`sources/Batang.ttf`, `sources/BatangChe.ttf`, `sources/Gungsuh.ttf`, `sources/GungsuhChe.ttf`) which are processed through a custom pipeline that:
1. Removes control characters from cmap tables
2. Fixes naming and copyright metadata
3. Creates TTC (TrueType Collection) files
4. Subsets fonts into bitmap, hinted, and unhinted variants
5. Uses `gftools fix-hinting` and `dehinter` for post-processing

There are no standard font source files (.glyphs, .ufo, .designspace) in the repository. The build process operates on pre-existing TTF binaries, making a gftools-builder config.yaml fundamentally inapplicable.

No override config.yaml exists in the google/fonts family directory either.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2024-05-15 21:34:44 -0700
- Commit message: "updating names"
- Commit is HEAD of main branch: Yes (no subsequent commits)
- Source files at commit: `sources/Batang.ttf`, `sources/BatangChe.ttf`, `sources/Gungsuh.ttf`, `sources/GungsuhChe.ttf`
- Output font file used: `fonts/ttf/hinted/batang-Regular.ttf`

## Confidence
**High**: The repository URL and commit hash are well-documented and verified. The missing config.yaml is expected because this repo uses a custom build pipeline for legacy Korean fonts, not gftools-builder. The status "missing_config" correctly reflects the absence of a config.yaml, but creating one would require converting the build process to gftools-builder, which may not be feasible given the custom TTF-to-TTF processing pipeline.

## Open Questions
- Should the status remain "missing_config" or be changed to something like "no_config_applicable" for repos that fundamentally cannot use gftools-builder?
- The Batang repo also contains Gungsuh and GungsuhChe fonts - are those tracked separately?
