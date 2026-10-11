# B612

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Nicolas Chauveau, Thomas Paillot, Jonathan Favre-Lamarine, Jean-Luc Vinot
**METADATA.pb path**: `ofl/b612/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/polarsys/b612 |
| Commit | `48ac6ba67ecab8123e8e36d6aa05367db0c7b638` |
| Config YAML | override in google/fonts |
| Branch | -- |

## How the Repository URL Was Found

The repository URL `https://github.com/polarsys/b612` is documented in the METADATA.pb `source {}` block. It is also referenced in the copyright string of the font files: "Copyright 2012 The B612 Project Authors (https://github.com/polarsys/b612)".

The onboarding PR #1877 (commit `2e8cd558a`, 2019-03-18) explicitly states: "Taken from the upstream repo https://github.com/polarsys/b612 at commit https://github.com/polarsys/b612/commit/7b5a653a6ae2bb05479297fed05ddf8c212d5477".

## How the Commit Hash Was Identified

The METADATA.pb currently records commit `48ac6ba67ecab8123e8e36d6aa05367db0c7b638`, which was the latest commit on the B612 repo at the time of onboarding (2019-03-18). However, the onboarding PR #1877 body explicitly references commit `7b5a653a6ae2bb05479297fed05ddf8c212d5477` as the source.

The difference between these commits is 2 intermediate commits:
1. `697af2c` - "Update EPL from 1.0 to 2.0" (license text change)
2. `ab82be3` - "Update links from http:// to https://" (README change)
3. `48ac6ba` - "Merge pull request #17 from sunpoet/master" (merges the above)

These 3 commits only modified `README.md` -- no font source files or binaries were changed. Therefore, both commits point to identical font source content. The commit `48ac6ba` was recorded in METADATA.pb because it was the HEAD of the repo at the time of onboarding, even though the actual font-producing commit was `7b5a653`.

The commit hash `48ac6ba` was added to METADATA.pb by a previous enrichment pass (commit `6a8253c9a`, 2025-11-19, "sources info for b612: v1.008 (PR #1877)").

## How Config YAML Was Resolved

The upstream repository does not contain a `config.yaml` file at either commit. An override config.yaml exists at `google/fonts/ofl/b612/config.yaml` with the following content:

```yaml
buildVariable: false
sources:
  - sources/ufo/B612-Bold.ufo
  - sources/ufo/B612-BoldItalic.ufo
  - sources/ufo/B612-Italic.ufo
  - sources/ufo/B612-Regular.ufo
```

Since the override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2019-03-18 14:24:05 +0100
- Commit message: "Merge pull request #17 from sunpoet/master"
- Source files at commit: UFO sources for B612-Bold, B612-BoldItalic, B612-Italic, B612-Regular, B612Mono-Bold, B612Mono-BoldItalic, B612Mono-Italic, B612Mono-Regular (all under `sources/ufo/`)

Note: The PR-referenced commit `7b5a653` also exists:
- Commit date: 2019-03-12 18:10:12 +0100
- Commit message: "Merge pull request #15 from intactile/master"

## Confidence

**High**: The repository URL is confirmed by both the METADATA.pb and the PR body. The commit hash in METADATA.pb (`48ac6ba`) was HEAD at onboarding time and contains identical source files to the PR-referenced commit (`7b5a653`). While the PR body technically references a different (earlier) commit, the source content is identical between them. The override config.yaml correctly handles the absence of config.yaml in the upstream repo.

## Open Questions

- The METADATA.pb commit `48ac6ba` differs from the PR-referenced commit `7b5a653`. While the source files are identical, it may be more accurate to use `7b5a653` since that is the commit explicitly referenced in the onboarding PR. However, `48ac6ba` as HEAD at onboarding time is also defensible. This is a minor discrepancy with no practical impact.
- The B612 upstream repository (`polarsys/b612`) has not been updated since commit `48ac6ba` (2019-03-18), which is 7 years ago. The repo appears to be inactive.
