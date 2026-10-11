# Blinker

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Juergen Huber
**METADATA.pb path**: `ofl/blinker/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/supertype-de/Blinker |
| Commit | `35cee57f389012c6a213acab504efb82f81c3b8f` |
| Config YAML | Override config.yaml in google/fonts |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL `https://github.com/supertype-de/Blinker` was already present in the METADATA.pb `source { repository_url }` field. It is confirmed by the copyright string in all 8 font files ("Copyright 2019 the Blinker project authors (https://github.com/supertype-de/Blinker)") and by the initial onboarding commit `9d2830d30` (2019-06-24, by Marc Foley) and PR #2045, both of which state: "Taken from the upstream repo https://github.com/supertype-de/Blinker at commit 35cee57f..."

## How the Commit Hash Was Identified

The commit hash `35cee57f389012c6a213acab504efb82f81c3b8f` is recorded in METADATA.pb. It matches the initial onboarding commit `9d2830d30` in google/fonts (2019-06-24, by Marc Foley) and PR #2045, which explicitly state: "Taken from the upstream repo https://github.com/supertype-de/Blinker at commit https://github.com/supertype-de/Blinker/commit/35cee57f389012c6a213acab504efb82f81c3b8f."

The commit exists in the upstream repo with date 2019-06-19 and message "fixup.sh: added." This was the initial onboarding of all 8 weights (Thin, ExtraLight, Light, Regular, SemiBold, Bold, ExtraBold, Black) at v1.015.

A subsequent update (`ff8e6172b`, 2019-09-11, by Micah Stupak) replaced only `Blinker-Light.ttf` to v1.016 to fix incorrect post_script_name metadata, but this was a targeted single-file fix and did not change the recorded upstream commit. The upstream repo shows later commits (e.g., `1db9bbd` "changed Light.ttf names from ExtraLight to Light" on 2019-09-11, likely related to the same fix), but these were not formally recorded in METADATA.pb.

## How Config YAML Was Resolved

There is no `config.yaml` in the upstream repository at any commit. An override `config.yaml` exists in the google/fonts family directory (`ofl/blinker/config.yaml`), added by commit `6f92eb5d7` (2025-12-11, by Felipe Sanches). It contains:

```yaml
buildVariable: false
sources:
  - sources_ps/Blinker.designspace
```

The `Blinker.designspace` file exists in the upstream repo at the recorded commit under `sources_ps/`. Since the override config.yaml is in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2019-06-19 13:29:23 +0200
- Commit message: "fixup.sh: added."
- Source files at commit: `sources_ps/Blinker.designspace` and 5 UFO directories (Black, Bold, Headline, Regular, Thin)
- Override config.yaml in google/fonts: Yes
- Font family: 8 weights (Thin through Black), static only
- Later upstream commits exist (up to 2022-04-24) but were not used for google/fonts updates

## Confidence

**High**: The repository URL and commit hash are consistently referenced across METADATA.pb, the initial onboarding commit, and PR #2045. The commit exists in the upstream repo. The override config.yaml in google/fonts correctly references the designspace file present at that commit. The only minor nuance is the Blinker-Light v1.016 fix, which was a targeted metadata fix that did not update the recorded upstream commit.

## Open Questions

1. The upstream repo has newer commits (up to `b917479`, 2022-04-24, "Adding vulgar fractions, adding wght mapping in designspace, regenerating static and variable fonts") that were never incorporated into google/fonts. These may contain improvements worth reviewing in a future update cycle.
2. The Blinker-Light v1.016 fix (`ff8e6172b`) was likely derived from upstream commit `1db9bbd` (which fixed Light/ExtraLight naming), but this is not explicitly documented.
