# Buenard

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Gustavo Ibarra
**METADATA.pb path**: `ofl/buenard/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/buenard |
| Commit | `cf400a29bbb4c8d850c221aa5b9835e8783648fb` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/buenard` is documented in the METADATA.pb `source { repository_url }` field. It was also referenced in the google/fonts commit `7217e59b6` ("Buenard: Version 2.000 added"), which explicitly states: "Taken from the upstream repo https://www.github.com/googlefonts/buenard". The copyright string in the font files also references this URL.

## How the Commit Hash Was Identified

The current METADATA.pb records commit `cf400a29bbb4c8d850c221aa5b9835e8783648fb`. However, the Version 2.000 onboarding commit in google/fonts (`7217e59b6`, 2025-01-16) originally referenced a different commit: `4e9ae114c1180a9093d310e7985aa4e024e4901e`.

The upstream repository appears to have been force-pushed/squashed to a single commit. The repository now contains only one commit (`cf400a2`, dated 2025-01-16 11:34:34 +0000, message: "Let skia-python float"). The original onboarding commit `4e9ae114` no longer exists in the repository.

The current commit `cf400a29` was set in the METADATA.pb as part of the batch port commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list"), which ported data from fontc_crater's target.json.

Critically, both the upstream commit (`cf400a2`, 2025-01-16 11:34:34) and the last google/fonts binary update (`851184c61` "Cedilla, brackets, lcaron", 2025-01-16 11:48:34) are from the same day, within 14 minutes of each other. This strongly suggests the font was built from this single remaining commit.

## How Config YAML Was Resolved

The file `sources/config.yaml` exists in the upstream repository at the recorded commit. Its contents are:

```yaml
sources:
  - Buenard.glyphs
axisOrder:
  - wght
familyName: Buenard
```

This is a valid gftools-builder configuration referencing a Glyphs source file. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2025-01-16 11:34:34 +0000
- Commit message: "Let skia-python float"
- Source files at commit: `sources/Buenard.glyphs`, `sources/config.yaml`
- Font binary in google/fonts: Variable font `Buenard[wght].ttf` (wght 400-700)
- Last binary update in google/fonts: 2025-01-16 (commit `851184c61`)
- Font added to Google Fonts: 2011-12-19 (original static version)
- Version 2.000 (variable) update: 2025-01-16

## Confidence

**Medium-High**: The repository URL is well-established and confirmed by multiple sources. The commit hash `cf400a29` is the only commit remaining in the force-pushed repo, making it the only viable reference. The timestamps confirm it is contemporary with the font binary update. The original onboarding commit `4e9ae114` is lost, but since the repo was squashed on the same day as the binary update, the source files should be functionally equivalent.

## Open Questions

1. The original onboarding commit `4e9ae114c1180a9093d310e7985aa4e024e4901e` referenced in the v2.000 google/fonts commit is no longer present in the upstream repository. The repo was force-pushed to a single commit on the same day. Were there meaningful source differences between that commit and the current one? Given the same-day timing, any differences are likely negligible.
