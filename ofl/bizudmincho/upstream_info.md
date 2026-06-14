# BIZ UDMincho

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Type Bank Co., Morisawa Inc.
**METADATA.pb path**: `ofl/bizudmincho/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/morisawa-biz-ud-mincho |
| Commit | `c30a6221b1f3d09afae9137ffe73c7cbec649947` |
| Config YAML | Override in google/fonts (`ofl/bizudmincho/config.yaml`) |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/morisawa-biz-ud-mincho` is recorded in the METADATA.pb `source` block and confirmed by the gftools-packager commit messages in google/fonts. The upstream repo is under the googlefonts GitHub org and is publicly accessible. Note: the copyright string and METADATA.pb both use this URL.

## How the Commit Hash Was Identified

The commit `c30a6221b1f3d09afae9137ffe73c7cbec649947` is recorded in the METADATA.pb `source` block and cross-verified:

1. **gftools-packager message**: The google/fonts commit `63833b7d1` (PR #5697, merged 2022-12-15) explicitly states: "BIZ UDMincho Version 1.06 taken from the upstream repo https://github.com/googlefonts/morisawa-biz-ud-mincho.git at commit c30a6221b1f3d09afae9137ffe73c7cbec649947."
2. **PR timeline**: PR #5697 was created by aaronbell on 2022-12-09 and merged on 2022-12-15. The upstream commit `c30a622` is dated 2022-12-06 (3 days before the PR).
3. **Upstream history**: Commit `c30a622` is a merge commit ("Merge pull request #17 from aaronbell/main -- Updating requirements document") and is the **HEAD** of the upstream repo -- no further commits have been made since.
4. **Same PR for two families**: PR #5697 also updated BIZ UDPMincho, both using the same upstream commit `c30a622` from the shared morisawa-biz-ud-mincho repository.

## How Config YAML Was Resolved

The upstream repo does **not** have a `config.yaml` file. It uses a custom `sources/build.py` script for font compilation. An override `config.yaml` was created in the google/fonts family directory at `ofl/bizudmincho/config.yaml`:

```yaml
sources:
  - sources/extensions/BIZ-UDMinchoExt.glyphs
familyName: BIZ UDMincho
buildStatic: true
buildOTF: false
```

This override was added in commit `f6c68379a` ("Add override config.yaml for 50 font families"). Because the override exists in the google/fonts directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes (`c30a6221b1f3d09afae9137ffe73c7cbec649947`)
- Commit date: 2022-12-06 20:17:38 -0800
- Commit message: "Merge pull request #17 from aaronbell/main -- Updating requirements document"
- Commit author: Aaron (aaronbell)
- Source files at commit: `sources/build.py`, `sources/extensions/BIZ-UDMinchoExt.glyphs`, `sources/extensions/BIZ-UDMincho-HeavyExt.glyphs`, `sources/extensions/BIZ-UDPMinchoExt.glyphs`, `sources/extensions/BIZ-UDPMincho-HeavyExt.glyphs`, plus OTF/TTF reference files
- Repository accessible: Yes
- Is HEAD of upstream: Yes (no commits since Dec 2022)

## Confidence

**High**: The commit hash is explicitly recorded in both the METADATA.pb and the gftools-packager message. The PR timeline is fully consistent (upstream commit Dec 6, google/fonts PR created Dec 9). Aaron Bell authored both the upstream work and the google/fonts PR. The commit is the HEAD of the upstream repo, meaning no additional upstream work has occurred since onboarding.

## Open Questions

None. All data is consistent and well-documented.
