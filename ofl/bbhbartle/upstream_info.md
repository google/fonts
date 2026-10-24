# BBH Bartle

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Studio DRAMA
**METADATA.pb path**: `ofl/bbhbartle/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Studio-DRAMA/BBH |
| Commit | `b8d40ef62b138be4c7c3dac2de117217f261b24b` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/Studio-DRAMA/BBH` is documented in the METADATA.pb `source {}` block. It is also referenced in the copyright string: "Copyright 2025 The BBH Project Authors (https://github.com/Studio-DRAMA/BBH)".

The font was added to google/fonts in commit `7fd17744c` (2025-11-27, "Add Bartle (new name)") along with the METADATA.pb file that already included the repository_url.

## How the Commit Hash Was Identified

The commit hash `b8d40ef62b138be4c7c3dac2de117217f261b24b` was added to METADATA.pb in a subsequent enrichment commit (`4fd9e2392`, 2026-02-25, "Add source metadata to 125 METADATA.pb files").

This commit was identified by inference: it is the latest commit in the BBH upstream repository dated before the google/fonts onboarding date (2025-11-27). The upstream commit is dated 2025-11-26, just one day before the google/fonts add.

Binary verification confirms the match: the SHA-256 hash of `fonts/ttf/BBHBartle-Regular.ttf` at commit `b8d40ef` in the upstream repo is `f0de1a96b31ed2ce012172dd28d4a5a7c3d4c7fdee84f32f311608ec4eca3431`, which is identical to the font binary added to google/fonts in commit `7fd17744c`.

The upstream commit log around the onboarding period shows `b8d40ef` ("push fonts") was the last commit before the google/fonts add. Subsequent commits (`5d71932`, `3c2301f`, etc.) occurred after the onboarding.

## How Config YAML Was Resolved

The config.yaml is located at `sources/config.yaml` in the upstream repository. This was verified at the recorded commit. The file contains configuration for three BBH font families (Bartle, Bogle, Hegarty):

```yaml
sources:
  - BBH-Bartle.glyphs
  - BBH-Bogle.glyphs
  - BBH-Hegarty.glyphs
familyName: "BBH Display"
buildVariable: false
buildStatic: true
buildTTF: true
buildOTF: true
autohintTTF: false
autohintOTF: false
includeSourceFixes: true
cleanUp: true
```

The `config_yaml` field was added to METADATA.pb in commit `5ddf312e6` (2026-02-20, "Add config_yaml enrichment for 82 font families"). No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2025-11-26 14:40:26 +0100
- Commit message: "push fonts"
- Source files at commit: `sources/BBH-Bartle.glyphs`, `sources/BBH-Bogle.glyphs`, `sources/BBH-Hegarty.glyphs`, `sources/config.yaml`, `.github/workflows/build.yaml`
- Font binary match: Confirmed (SHA-256 identical between upstream and google/fonts)

## Confidence

**High**: The commit hash is verified by binary comparison of the font file between the upstream repo and google/fonts. The commit is dated one day before the google/fonts onboarding, and it is the latest upstream commit before the add date. The repository URL matches the copyright string. The config.yaml exists at the recorded commit and contains gftools-builder configuration.

## Open Questions

- The BBH upstream repository contains three font families (Bartle, Bogle, Hegarty) sharing a single `config.yaml` with `familyName: "BBH Display"`. This multi-family config may need special handling if individual families need to be rebuilt independently.
- The repository has received additional commits after onboarding (latest: `5d71932`, 2025-12-04, "Merge pull request #8 from emmamarichal/main"). Any updates to the fonts would need to go through review.
