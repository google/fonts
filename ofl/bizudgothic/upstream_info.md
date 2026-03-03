# BIZ UDGothic

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Type Bank Co., Morisawa Inc.
**METADATA.pb path**: `ofl/bizudgothic/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/morisawa-biz-ud-gothic |
| Commit | `38953aa0afd6937b9caa899e18f4550db7298d69` |
| Config YAML | Override in google/fonts (`ofl/bizudgothic/config.yaml`) |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/morisawa-biz-ud-gothic` is recorded in the METADATA.pb `source` block and confirmed by the gftools-packager commit messages in google/fonts. The upstream repo is under the googlefonts GitHub org and is publicly accessible.

## How the Commit Hash Was Identified

The commit `38953aa0afd6937b9caa899e18f4550db7298d69` is recorded in the METADATA.pb `source` block and cross-verified against multiple sources:

1. **gftools-packager message**: The google/fonts commit `01ac47e0b` (PR #4579, merged 2022-05-11) explicitly states: "BIZ UDGothic Version 1.05 taken from the upstream repo https://github.com/googlefonts/morisawa-biz-ud-gothic at commit 38953aa0afd6937b9caa899e18f4550db7298d69."
2. **PR timeline**: PR #4579 was created by aaronbell on 2022-05-03 and merged on 2022-05-11. The upstream commit `38953aa` is dated 2022-05-02 (one day before the PR).
3. **Upstream history**: Commit `38953aa` is a merge commit ("Merge pull request #9 from aaronbell/main -- Extended character set and Unicode updates") and was the HEAD of the upstream repo at the time of onboarding.
4. **Post-onboarding commits**: The upstream repo has newer commits (up to `18934af` from Sep 2023), but those were used for the separate BIZ UDPGothic v1.051 update. The BIZ UDGothic binaries were NOT updated after v1.05.

The BIZ UDGothic binaries in google/fonts were last modified in PR #4579 (v1.05) and have not been updated since, confirming `38953aa` as the correct and current onboarding commit.

## How Config YAML Was Resolved

The upstream repo does **not** have a `config.yaml` file. It uses a custom `sources/build.py` script for font compilation. An override `config.yaml` was created in the google/fonts family directory at `ofl/bizudgothic/config.yaml`:

```yaml
sources:
  - sources/extensions/BIZ-UDGothicExt.glyphs
familyName: BIZ UDGothic
buildStatic: true
buildOTF: false
```

This override was added in commit `f6c68379a` ("Add override config.yaml for 50 font families"). Because the override exists in the google/fonts directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## Verification

- Commit exists in upstream repo: Yes (`38953aa0afd6937b9caa899e18f4550db7298d69`)
- Commit date: 2022-05-02 13:38:49 -0700
- Commit message: "Merge pull request #9 from aaronbell/main -- Extended character set and Unicode updates"
- Commit author: Aaron (aaronbell)
- Source files at commit: `sources/build.py`, `sources/extensions/BIZ-UDGothicExt.glyphs`, `sources/extensions/BIZ-UDGothic-BoldExt.glyphs`, `sources/extensions/BIZ-UDPGothicExt.glyphs`, `sources/extensions/BIZ-UDPGothic-BoldExt.glyphs`, plus OTF/TTF reference files
- Repository accessible: Yes
- Is HEAD of upstream: No (latest is `18934af` from Sep 2023, used for BIZ UDPGothic update)

## Confidence

**High**: The commit hash is explicitly recorded in both the METADATA.pb and the gftools-packager message. The PR timeline (upstream commit May 2, google/fonts PR created May 3) is fully consistent. Aaron Bell authored both the upstream commit and the google/fonts PR.

## Open Questions

None. All data is consistent and well-documented.
