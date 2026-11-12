# Changa

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Eduardo Tunni
**METADATA.pb path**: `ofl/changa/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/changa-vf |
| Commit | `fb3207d4fe7234f610d0d4ef77dce01cfda57027` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/changa-vf` was already present in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font files ("Copyright 2018 The Changa Project Authors (https://github.com/eliheuer/changa-vf)") -- note the repo was later transferred from `eliheuer` to `googlefonts`. The gftools-packager commit `5b61d6b49` in google/fonts (PR #3873) also references this URL explicitly.

## How the Commit Hash Was Identified

The commit `fb3207d4fe7234f610d0d4ef77dce01cfda57027` was ported from the fontc_crater targets list in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31).

However, there is a **discrepancy** with the original onboarding record. The gftools-packager commit `5b61d6b49` (PR #3873, "Changa: Version 3.003 added", 2021-09-29) explicitly states: "Changa Version 3.003 taken from the upstream repo https://github.com/googlefonts/changa-vf at commit https://github.com/googlefonts/changa-vf/commit/6b01b524a87bded805a3de339d087da6e9fc310a."

The referenced onboarding commit `6b01b524` (2021-09-22, "Merge pull request #5 from aaronbell/master - Adding in ExtraLight master") is an **earlier commit** than the one in METADATA.pb. The METADATA.pb commit `fb3207d4` (2021-09-29, "Update OFL.txt") came one week later and only changed `OFL.txt`. No font source files were modified between these two commits.

The fontc_crater targets list likely recorded the latest commit (`fb3207d4`) rather than the exact onboarding commit (`6b01b524`). Since the only difference is an OFL.txt text change, the source files used for building are identical in both commits.

## How Config YAML Was Resolved

The `config.yaml` file exists in the upstream repository at `sources/config.yaml`. It contains gftools-builder configuration:

```yaml
sources:
  - Changa.glyphs
axisOrder:
  - wght
familyName: "Changa"
stat:
  Changa[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: ExtraLight
      value: 200
    ...
```

This is a variable font build configuration for the `wght` axis (200-800). No override config.yaml exists in the google/fonts family directory.

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes
- Commit date: 2021-09-29 10:02:04 +0000
- Commit message: "Update OFL.txt"
- Source files at commit: `sources/Changa.glyphs`, `sources/config.yaml`
- Variable font axes: `wght` (200-800)
- METADATA.pb has complete source block with files mapping and branch

## Confidence

**High**: The repository URL is well-established and confirmed by multiple sources. The commit hash `fb3207d4` is functionally equivalent to the original onboarding commit `6b01b524` -- the only difference is an OFL.txt text update. The config.yaml is present and valid. The METADATA.pb source block is fully populated with repository_url, commit, files mapping, branch, and config_yaml.

## Open Questions

1. The METADATA.pb commit `fb3207d4` does not exactly match the original onboarding commit `6b01b524` cited in PR #3873. While the source files are identical between these commits (only OFL.txt was changed), it would be more precise to use `6b01b524` as the commit hash. However, since the fontc_crater targets list uses `fb3207d4`, changing it could cause inconsistencies with that system.
