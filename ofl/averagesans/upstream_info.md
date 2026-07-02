# Average Sans

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Eduardo Tunni
**METADATA.pb path**: `ofl/averagesans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | -- |
| Commit | -- |
| Config YAML | -- |
| Branch | -- |

## How the Repository URL Was Found

No repository URL is documented in the METADATA.pb (there is no `source { }` block at all). The designer Eduardo Tunni does not have an "averagesans" or "average-sans" repository on his GitHub account (etunni). His GitHub profile lists many font repos (including `average` for the serif sister family), but no Average Sans repo.

A legacy `librefonts/averagesans` repository exists at https://github.com/librefonts/averagesans, created in July 2014. However, this is a legacy mirror containing only TTX (decompiled font) files and old binary sources (.vfb, .sfd). It has no `.glyphs`, `.designspace`, or `config.yaml` files, making it unsuitable as a build source for gftools-builder. The repo has not been updated since 2014.

No other upstream repository with proper sources was found.

## How the Commit Hash Was Identified

N/A -- No proper upstream repository with build-compatible sources exists.

The last TTF-modifying commit in google/fonts is `76f813683` ("hotfix-averagesans: v1.002 added", PR #835, by m4rc1e). This was a hotfix merged on 2017-08-07, with an empty PR body and no reference to an upstream commit.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repo (librefonts/averagesans) or in the google/fonts family directory (`ofl/averagesans/`). The librefonts repo contains only legacy source files:
- `src/AverageSans-Regular-OTF.vfb` (FontLab binary)
- `src/AverageSans-Regular-TTF.sfd` (FontForge source)
- TTX (decompiled font) files

These formats are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources with a `config.yaml`.

## Verification

- Commit exists in upstream repo: N/A
- Commit date: N/A
- Commit message: N/A
- Source files at commit: Only legacy .vfb/.sfd in librefonts/averagesans

## Confidence

**High**: There is high confidence that no proper upstream repository with gftools-builder-compatible sources exists. Eduardo Tunni's GitHub has a repo for the serif "Average" family but not for "Average Sans". The only available repo (librefonts/averagesans) is a legacy mirror with no modern build sources.

## Open Questions

1. Does Eduardo Tunni have the Average Sans .glyphs source file? His "average" repo has `sources/Average.glyphs` for the serif family -- he may have a similar .glyphs file for Average Sans that was never published to GitHub.
2. Should a new upstream repo be created (or the existing one updated) with modern source files to enable rebuilding?
