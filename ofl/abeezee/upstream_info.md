# ABeeZee

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Anja Meiners
**METADATA.pb path**: `ofl/abeezee/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/abeezee |
| Commit | `b9bd3f3522d91aca81eb668f56d40c2c62a90125` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/abeezee`. This matches the copyright string in the font files ("Copyright 2011 The ABeeZee Project Authors (https://github.com/googlefonts/abeezee)"). The gftools-packager commit `a8bc01c6` in google/fonts also references this URL in its body.

## How the Commit Hash Was Identified

The current METADATA.pb commit hash is `b9bd3f3522d91aca81eb668f56d40c2c62a90125`. However, this does **not** match the original onboarding commit referenced by gftools-packager.

The original font onboarding in google/fonts was done via PR #4265, with the gftools-packager commit `a8bc01c6` (2022-02-04) stating: "ABeeZee Version 1.003; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/abeezee at commit https://github.com/googlefonts/abeezee/commit/a84aead1554a7adc09c6dd01161ac4a5a9f2c001."

The original onboarding commit `a84aead1554a7adc09c6dd01161ac4a5a9f2c001` is **no longer present** in the upstream repository -- it appears the repository was force-pushed to a single commit. The current commit `b9bd3f35` (2022-02-04 16:00:44 +0100, message: "Merge pull request #4 from emmamarichal/main") is the only commit remaining in the repo. This commit was from the same day as the onboarding.

The METADATA.pb source block was added by the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported information from fontc_crater's target.json. The `b9bd3f35` commit hash was likely used as the latest available commit in the force-pushed repo.

## How Config YAML Was Resolved

The config file `sources/config.yaml` exists in the upstream repository at the recorded commit hash `b9bd3f35`. It contains gftools-builder configuration referencing two source files (`ABeeZee.glyphs` and `ABeeZee-Italic.glyphs`) with `buildVariable: false`. No override config.yaml exists in the google/fonts family directory (`ofl/abeezee/`).

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-02-04 16:00:44 +0100
- Commit message: "Merge pull request #4 from emmamarichal/main"
- Source files at commit: `sources/ABeeZee-Italic.glyphs`, `sources/ABeeZee.glyphs`, `sources/config.yaml`

## Confidence

**Medium**: The repository URL is well-established and confirmed by multiple sources. However, the commit hash in METADATA.pb (`b9bd3f35`) does not match the original onboarding commit (`a84aead1`) cited by gftools-packager in PR #4265. The upstream repo appears to have been force-pushed, losing the original onboarding commit. The current commit `b9bd3f35` is the only commit remaining and is from the same day as the onboarding, so the source files are likely functionally equivalent. The config.yaml is present and valid. The discrepancy between the recorded and original onboarding commits is a known consequence of the repo being force-pushed.

## Open Questions

1. The original onboarding commit `a84aead1554a7adc09c6dd01161ac4a5a9f2c001` is no longer present in the upstream repo. Were source files modified between that commit and the current one (`b9bd3f35`)? Since both are from the same day (2022-02-04), the difference is likely minimal, but it cannot be verified.
