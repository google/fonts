# Babylonica

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/babylonica/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/babylonica |
| Commit | `7b1c733f74a11604a711e87f840010e0746cfcd1` |
| Config YAML | `sources/config.yml` |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/babylonica` is documented in the METADATA.pb `source` block and in the font copyright string. The google/fonts commit body (PR #4324) also explicitly references this repo. This is a googlefonts organization repo, consistent with the TypeSetIT onboarding batch.

## How the Commit Hash Was Identified

The commit hash in METADATA.pb is `7b1c733f74a11604a711e87f840010e0746cfcd1`. Importantly, this differs from the hash originally referenced in the PR #4324 body.

**PR timeline analysis:**
- The PR body initially referenced commit `39b985f83f2186579d4f78e21205b1b379015b80` (dated 2022-02-16, message: "sample image updated").
- Between that commit and the final hash, there is exactly one additional commit: `7b1c733` (dated 2022-02-23, by Viviana Monsalve, message: "apple glyph using Robbie shape").
- This upstream fix (adding/fixing the apple glyph) was made during the PR review period, and the onboarder updated the gftools-packager commit to reference the newer hash before merging.
- The merged commit in google/fonts (2022-02-24) references the updated hash `7b1c733f`, confirming the final version used.

Cross-verification:
- Upstream commit `7b1c733` date: 2022-02-23 (one day before the google/fonts merge on 2022-02-24).
- This commit is the HEAD of the upstream repo -- no subsequent changes exist.
- The font was onboarded by Viviana Monsalve as part of "Batch 5 of TypeSetIT fonts" (per PR comments).

This is a textbook example of the hash hint in PR bodies being stale -- the onboarder made an additional upstream fix before merging, updating the hash in the process.

## How Config YAML Was Resolved

The upstream repo contains `sources/config.yml` at the referenced commit. This file is present and contains a valid gftools-builder configuration:

```yaml
sources:
  - Babylonica.glyphs
familyName: "Babylonica"
buildVariable: false
```

Note the file uses the `.yml` extension rather than `.yaml`. The METADATA.pb correctly records the path as `sources/config.yml`. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-02-23 21:48:21 -0500
- Commit message: "apple glyph using Robbie shape"
- Commit author: Viviana Monsalve
- Source files at commit: `sources/Babylonica.glyphs`, `sources/config.yml`, `fonts/ttf/Babylonica-Regular.ttf`
- Commit is HEAD of upstream main branch: Yes (no newer commits)

## Confidence

**High**: The merged commit body in google/fonts references the exact hash now in METADATA.pb. The hash was updated from the original PR body to reflect an upstream fix made during the review period. The config.yml path is verified. The commit is the latest in the upstream repo.

## Open Questions

None. The discrepancy between the PR body hash and the METADATA.pb hash is fully explained by the upstream fix made during the review period.
