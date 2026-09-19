# Afacad

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Kristian Moller, Dicotype
**METADATA.pb path**: `ofl/afacad/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Dicotype/Afacad |
| Commit | `b294b1f8610ff16a3846a255b1a6a2e6788a056e` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in METADATA.pb in the `source { repository_url }` field: `https://github.com/Dicotype/Afacad`. This is consistent with the copyright notice in the font files: "Copyright 2023 The Afacad Project Authors (https://github.com/Dicotype/Afacad)".

The `Dicotype` GitHub organization is the official home of typefaces designed by Kristian Moller / Dicotype.

## How the Commit Hash Was Identified

The commit hash situation is complex, involving **three different referenced commits**:

1. **METADATA.pb current commit**: `b294b1f8610ff16a3846a255b1a6a2e6788a056e` -- This was added in commit `19cdcec59` (2025-03-31) as part of "[Batch 1/4] port info from fontc_crater targets list" by Felipe Sanches. This commit is from the fontc_crater targets.json data.

2. **gftools-packager merge commit message** (`aa30c14f9`, 2023-10-20): References commit `d7e973f5d3f17f54662ed9a18b130dcbf7a0e709` with the message "Afacad Version 1.000 taken from the upstream repo https://github.com/Dicotype/Afacad at commit https://github.com/Dicotype/Afacad/commit/d7e973f5d3f17f54662ed9a18b130dcbf7a0e709."

3. **PR #6881 initial body**: References yet another commit `39d4a8f1e6c5a64d4c31a639c251800ee4b65fa7`.

**Critical finding**: The Dicotype/Afacad repository has been **force-pushed** and now contains only a **single commit** (`b294b1f8`, 2024-10-03: "Update README.md"). Both the original packager commit (`d7e973f5`) and the initial PR commit (`39d4a8f1`) no longer exist in the repository. The repository history has been completely rewritten.

The commit `b294b1f8` currently in METADATA.pb is the only commit that exists in the repo, but it dates to **2024-10-03** -- nearly a year after the font was added to google/fonts (2023-10-20). This commit cannot be the one used for the original onboarding.

## How Config YAML Was Resolved

The `sources/config.yaml` file exists in the upstream repository at the current commit (`b294b1f8`). Its contents include:

```yaml
sources:
  - Afacad.glyphs
  - Afacad-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Afacad
outputDir: "../fonts/Afacad"
```

The repo also contains `sources/config_flux.yaml` for the related Afacad Flux family, and `sources/AfacadFlux.glyphs`.

Note: Since the repo was force-pushed, we cannot verify that this config.yaml existed at the time of the original onboarding. However, the fontc_crater targets list references this path, and the config is valid for gftools-builder.

## Verification

- Commit exists in upstream repo: Yes (but it is the ONLY commit -- repo was force-pushed)
- Commit date: 2024-10-03 10:40:24 +0200
- Commit message: "Update README.md"
- Source files at commit: `sources/Afacad.glyphs`, `sources/Afacad-Italic.glyphs`, `sources/config.yaml`, `sources/AfacadFlux.glyphs`, `sources/config_flux.yaml`, plus instance UFO JSON files

## Confidence

**Medium**: The repository URL is confirmed correct (matches copyright notice and PR references). The config.yaml path is valid and the file exists. However, the commit hash situation is problematic:

- The original onboarding commit (`d7e973f5`) no longer exists in the repo due to force-pushing
- The current METADATA.pb commit (`b294b1f8`) post-dates the font's addition to google/fonts by nearly a year
- The repo has been completely rewritten to a single commit, destroying the original history

The practical impact is limited since the config.yaml and source files are present at the current (and only) commit, but the commit hash does not represent the original onboarding state.

## Open Questions

1. The original onboarding commit `d7e973f5d3f17f54662ed9a18b130dcbf7a0e709` was lost due to a force-push of the Dicotype/Afacad repository. Should the commit field be updated to the current HEAD, or should this be flagged as needing investigation with the designer?
2. Has the source content changed materially between the original onboarding and the current single commit? Without the original history, this cannot be verified from git alone.
3. Should the METADATA.pb `source { commit }` field note that this is a post-force-push reference rather than the original onboarding commit?
