# BIZ UDPMincho

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Type Bank Co., Morisawa Inc.
**METADATA.pb path**: `ofl/bizudpmincho/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/morisawa-biz-ud-mincho |
| Commit | `c30a6221b1f3d09afae9137ffe73c7cbec649947` |
| Config YAML | Override in google/fonts (`ofl/bizudpmincho/config.yaml`) |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/morisawa-biz-ud-mincho` is documented in the METADATA.pb `source` block and is also referenced in the copyright field of the font entries. The google/fonts commit body (PR #5697) explicitly states the font was taken from this upstream repo. The same URL appears in the copyright strings in METADATA.pb.

## How the Commit Hash Was Identified

The commit `c30a6221b1f3d09afae9137ffe73c7cbec649947` was referenced in google/fonts PR #5697, merged on 2022-12-15. The PR body states: "BIZ UDPMincho Version 1.06 taken from the upstream repo [...] at commit c30a6221b1f3d09afae9137ffe73c7cbec649947."

Cross-verification:
- The upstream commit is dated 2022-12-06 (a merge of PR #17 from aaronbell/main).
- The google/fonts merge happened on 2022-12-15, 9 days later -- reasonable for review and onboarding.
- This commit is the HEAD of the upstream repo -- no subsequent commits exist, which means no work has happened upstream since onboarding.
- The gftools-packager message in both the PR body and the merged commit body reference the same hash, providing strong consistency.

## How Config YAML Was Resolved

The upstream repository does **not** have a `config.yaml` file at any commit (including HEAD). Instead, this font uses a custom `sources/build.py` script and a `Makefile` for building. The build process merges extension glyphs into base TTFs provided directly by Morisawa.

Because there is no `config.yaml` in the upstream repo, an override `config.yaml` was added in the google/fonts family directory at `ofl/bizudpmincho/config.yaml` (commit `f6c68379a`). This override config references `sources/extensions/BIZ-UDPMinchoExt.glyphs` as the source. With the override in place, the `config_yaml` field is correctly omitted from the METADATA.pb `source` block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-12-06 20:17:38 -0800
- Commit message: "Merge pull request #17 from aaronbell/main"
- Source files at commit: `sources/extensions/BIZ-UDPMinchoExt.glyphs`, `sources/extensions/BIZ-UDPMincho-HeavyExt.glyphs`, `sources/build.py`, `fonts/ttf/BIZUDPMincho-Regular.ttf`, `fonts/ttf/BIZUDPMincho-Bold.ttf`
- Commit is HEAD of upstream main branch: Yes (no newer commits)
- Font files are pre-built TTFs copied directly from upstream `fonts/ttf/` directory

## Confidence

**High**: The commit hash is consistently referenced in the PR body, the merged commit message, and the METADATA.pb. The commit is the latest in the upstream repo. The override config.yaml in google/fonts correctly addresses the absence of a config.yaml in the upstream repo.

## Open Questions

None. This family uses a non-standard build process (custom Python script merging extension glyphs into base TTFs), which is why the source block references pre-built TTFs rather than source files compiled via gftools-builder. The override config.yaml provides a standard gftools-builder configuration for fontc_crater compatibility.
