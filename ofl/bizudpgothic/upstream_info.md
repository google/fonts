# BIZ UDPGothic

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Type Bank Co., Morisawa Inc.
**METADATA.pb path**: `ofl/bizudpgothic/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/morisawa-biz-ud-gothic |
| Commit | `18934af56b9c003ca58c54bffbf226848cb11032` |
| Config YAML | Override in google/fonts (`ofl/bizudpgothic/config.yaml`) |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/morisawa-biz-ud-gothic` is recorded in the METADATA.pb `source` block. Note that BIZ UDPGothic shares the same upstream repository as BIZ UDGothic -- both are proportional and fixed-width variants built from sources in the same repo. The copyright string also references this URL.

## How the Commit Hash Was Identified

The commit `18934af56b9c003ca58c54bffbf226848cb11032` is recorded in the METADATA.pb `source` block and cross-verified:

1. **gftools-packager message**: The google/fonts commit `7da950f21` (PR #6664, merged 2023-09-07) explicitly states: "BIZ UDPGothic Version 1.051 taken from the upstream repo https://github.com/googlefonts/morisawa-biz-ud-gothic at commit 18934af56b9c003ca58c54bffbf226848cb11032."
2. **PR timeline**: PR #6664 was created by aaronbell on 2023-09-06 and merged on 2023-09-07. The upstream commit `18934af` is dated 2023-09-06 (same day as the PR).
3. **Upstream history**: Commit `18934af` is a merge commit ("Merge pull request #23 from aaronbell/main -- Update to the UDPGothic Regular / Bold") and is the **HEAD** of the upstream repo -- no further commits have been made since.
4. **Relationship to BIZ UDGothic**: BIZ UDGothic uses an earlier commit (`38953aa`) from the same repo. The `18934af` commit updated the UDPGothic font files but the UDGothic binaries were NOT re-onboarded at that time. This is why the two families reference different commits from the same repo.
5. **Separate update**: This was a standalone update (v1.051) separate from the initial v1.05 onboarding in PR #4579, which had both families at commit `38953aa`.

## How Config YAML Was Resolved

The upstream repo does **not** have a `config.yaml` file at either commit. It uses a custom `sources/build.py` script for font compilation. An override `config.yaml` was created in the google/fonts family directory at `ofl/bizudpgothic/config.yaml`:

```yaml
sources:
  - sources/extensions/BIZ-UDPGothicExt.glyphs
familyName: BIZ UDPGothic
buildStatic: true
buildOTF: false
```

This override was added in commit `f6c68379a` ("Add override config.yaml for 50 font families"). Because the override exists in the google/fonts directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes (`18934af56b9c003ca58c54bffbf226848cb11032`)
- Commit date: 2023-09-06 14:08:09 -0700
- Commit message: "Merge pull request #23 from aaronbell/main -- Update to the UDPGothic Regular / Bold"
- Commit author: Aaron (aaronbell)
- Source files at commit: `sources/build.py`, `sources/extensions/BIZ-UDPGothicExt.glyphs`, `sources/extensions/BIZ-UDPGothic-BoldExt.glyphs`, `sources/extensions/BIZ-UDGothicExt.glyphs`, `sources/extensions/BIZ-UDGothic-BoldExt.glyphs`, plus OTF/TTF reference files
- Repository accessible: Yes
- Is HEAD of upstream: Yes (no commits since Sep 2023)

## Confidence

**High**: The commit hash is explicitly recorded in both the METADATA.pb and the gftools-packager message. The PR was created on the same day as the upstream commit, both by Aaron Bell. The commit is the HEAD of the upstream repo, confirming no additional upstream work has occurred.

## Open Questions

None. All data is consistent and well-documented.
