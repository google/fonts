# Candal - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Candal |
| Designer | Vernon Adams |
| License | OFL |
| Date Added | 2011-03-09 |
| Repository URL | https://github.com/librefonts/candal |
| Commit Hash | 64c937069fed67f562829846315a0e2e7789e6a6 |
| Branch | master |
| Config YAML | N/A |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/candal` was added as part of the batch source blocks commit (9a14639f3, "Add source blocks to 602 more METADATA.pb files"). The librefonts organization hosts mirrors of many Google Fonts projects. The METADATA.pb in google/fonts previously had no source block.

Vernon Adams, the original designer, passed away in 2014. His fonts were preserved in the librefonts mirrors.

## How Commit Determined

The commit `64c937069fed67f562829846315a0e2e7789e6a6` is the HEAD (and only commit) of the librefonts/candal repository, dated 2014-10-17. The commit message is "update .travis.yml". This is a single-commit repo.

The font binary in google/fonts was last updated in commit cfa69ab46 (2015-04-27, "Updating ofl/candal/*ttf with nbspace and fsType fixes" by Dave Crossland), which was a metadata-only fix (file size unchanged), not a rebuild from sources. The initial font was added in 90abd17b4 ("Initial commit").

Since the librefonts repo has only one commit, the recorded hash is the only valid option.

## Config YAML Status

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in google/fonts either.

The upstream repo contains only FontForge SFD sources (`src/Candal.sfd`, `src/Candal-TTF.sfd`) and VFB files (`src/Candal-TTF.vfb`, `src/Candal.vfb`). These are not gftools-builder compatible formats.

## Verification

- **Commit hash verified**: The hash `64c9370` exists in the librefonts/candal repository and is HEAD of master. CONFIRMED.
- **Repository accessible**: librefonts/candal is a valid GitHub repository. CONFIRMED.
- **Source files**: Only SFD and VFB formats available, no .glyphs/.ufo/.designspace sources.
- **Single-commit repo**: Only one commit in the entire history (2014-10-17).

## Confidence Level

**HIGH** - The repository URL and commit hash are correct. The librefonts mirror is the only known upstream, and Vernon Adams (the designer) is deceased, so no additional source repo is expected.

## Open Questions

- No path to gftools-builder compatibility without source conversion from SFD/VFB format.
- The font has not been updated since the initial onboarding (only metadata fixes).
