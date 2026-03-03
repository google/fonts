# Investigation Report: Expletus Sans

## Family Details

- **Family name**: Expletus Sans
- **Designer**: Designtown (Jasper de Waard)
- **License**: OFL
- **Category**: DISPLAY
- **Date added to Google Fonts**: 2011-05-04
- **Path in google/fonts**: `ofl/expletussans/`

## Source Repository

- **Repository URL**: https://github.com/googlefonts/Expletus-Sans
- **Repository accessible**: Yes (HTTP 200)
- **Branch**: master
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/Expletus-Sans/`

## Source Files

- `sources/ExpletusSans.glyphs` (Glyphs format, 268 KB)
- `sources/ExpletusSans-Italic.glyphs` (Glyphs format, 264 KB)

## Config

- **config.yaml location**: `sources/config.yaml` (in upstream repo)
- **Override config in google/fonts**: No
- **config_yaml in METADATA.pb**: `sources/config.yaml`

The config.yaml defines:
- Two sources: `ExpletusSans.glyphs` and `ExpletusSans-Italic.glyphs`
- Axis order: wght, ital
- Family name: "Expletus Sans"
- STAT table entries for weight (400-700) and italic axes

## Font Files in google/fonts

- `ExpletusSans[wght].ttf` (variable, wght 400-700)
- `ExpletusSans-Italic[wght].ttf` (variable, wght 400-700)

## Commit Verification

### METADATA.pb commit hash
- **Commit in METADATA.pb**: `b64823a38d36cb09ec9ffce05f079585a4811217`
- **Commit message**: "renamed old directory without special characters"
- **Author**: Rosalie Wagner (mail@rosaliewagner.com)
- **Date**: 2021-11-25

### Upstream repo state
The upstream repo has only a single commit (`b64823a`), which is the one referenced in METADATA.pb. This is the HEAD and only commit on master. The repo appears to have been force-pushed/squashed to a single commit at some point, erasing the earlier history.

### Binary file verification
The font files in google/fonts are **byte-identical** to those in the upstream repo at commit `b64823a`:
- `ExpletusSans[wght].ttf`: MD5 `6e285f8a36f1effe8e843184c0245990` (matches)
- `ExpletusSans-Italic[wght].ttf`: MD5 `471950f08e1fa040940f73232dda6ead` (matches)

### google/fonts onboarding history
The variable font version was added in google/fonts commit `37c8dee94` (PR #4032) on 2021-11-25:
- **PR title**: "Expletus Sans: Version 7.500 added"
- **PR author**: Emma Marichal (@emmamarichal)
- **Merged by**: Rosalie Wagner (@RosaWagner)
- **Created**: 2021-11-04
- **Merged**: 2021-11-25

### Commit hash discrepancy (resolved)
The PR body and the merged commit message reference two different upstream commit hashes:
1. PR body: `33f622f8385bb879f9daa3f851901aabe7ac7da4`
2. Merged commit body: `b9dffadf9e98e7d1786699b93f39a6a8fc15ed67`

Neither of these hashes exists in the current upstream repo, which only has commit `b64823a` (dated 2021-11-25, same day as PR merge). This strongly indicates the upstream repo was force-pushed/squashed to a single commit on the day the PR was merged. Since the binary files match exactly, commit `b64823a` is the correct reference - it contains the same content that was onboarded, just with a cleaned-up git history.

## Source Block History in METADATA.pb

1. **2024-04-03**: Simon Cozens added the source block (repository_url, files, branch) via "Merge upstream.yaml into METADATA.pb" commit `66f91f10f`
2. **2025-03-31**: Felipe Sanches added commit hash and config_yaml via "[Batch 1/4] port info from fontc_crater targets list" commit `19cdcec59`

## Status

- **Status**: complete
- **Confidence**: HIGH
- **Repository URL**: Verified (accessible, binary files match)
- **Commit hash**: Verified (only commit in repo, binaries match exactly)
- **config.yaml**: Present in upstream repo at `sources/config.yaml`
- **Source types**: Glyphs (.glyphs)

## Notes

The upstream repo was clearly reorganized (force-pushed to a single squashed commit) around the time the font was onboarded to Google Fonts (2021-11-25). The original commit hashes referenced in the google/fonts PR (#4032) no longer exist in the upstream repo. However, this is not a concern because: (1) the repo has only one commit, so there is no ambiguity about which commit to reference, and (2) the binary files are byte-identical, confirming the content matches perfectly.

The font was originally added to Google Fonts in 2011 as static fonts. The variable font upgrade (Version 7.500) was done in November 2021 by Emma Marichal and Rosalie Wagner.
