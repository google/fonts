# Investigation Report: Elms Sans

## Family Overview
- **Family Name**: Elms Sans
- **Designer**: Amarachi Nwauwa, Gida Type Studio
- **License**: OFL
- **Date Added**: 2025-10-17
- **Category**: Sans Serif
- **Axes**: wght (100-900)
- **Files**: ElmsSans[wght].ttf, ElmsSans-Italic[wght].ttf (variable fonts)

## Source Repository
- **Repository URL**: https://github.com/mara-aa/elms-sans
- **Commit**: `bc5a52f3499f1a9858e56430da9e955c15366b3e`
- **Branch**: main
- **Config YAML**: `sources/config.yaml`

## METADATA.pb Status
The METADATA.pb already has a complete `source { }` block with:
- `repository_url`: https://github.com/mara-aa/elms-sans
- `commit`: bc5a52f3499f1a9858e56430da9e955c15366b3e
- `branch`: main
- `config_yaml`: sources/config.yaml
- `files` mappings for OFL.txt, ElmsSans[wght].ttf, and ElmsSans-Italic[wght].ttf

## Investigation Details

### Onboarding History in google/fonts
The font was onboarded via PR #9925, with the following commits in google/fonts:

1. **a6d580b2** (2025-10-17) by Emma Marichal -- "Elms Sans: Version 1.061 added"
   - Commit message explicitly states: "Taken from the upstream repo https://github.com/mara-aa/elms-sans at commit bc5a52f3499f1a9858e56430da9e955c15366b3e"
   - Added font binaries, METADATA.pb, OFL.txt, and article
2. **d3599724** (2025-10-17) -- "add article" (article images/videos)
3. **c323e702** (2025-10-22) by Felipe Sanches -- "sources info for Elms Sans: Version 1.061 (PR #9925)" (added config_yaml to METADATA.pb)
4. **b5a3b571** (2025-11-07) -- "add Gida Type Studio in designers"

### Upstream Repository Analysis
- The upstream repo at `mara-aa/elms-sans` has only a single commit: `bc5a52f` (a merge commit from PR #6 by emmamarichal, dated 2025-10-16)
- This merge commit is titled "Update to QA, Fixes & Font Build" and contains the entire repository content (initial setup using the Google Fonts template)
- The repo is clean and up-to-date with origin

### Commit Hash Verification
- **Binary file comparison**: SHA256 hashes of both `ElmsSans[wght].ttf` and `ElmsSans-Italic[wght].ttf` match exactly between the upstream repo at commit `bc5a52f` and google/fonts
  - ElmsSans[wght].ttf: `5a5c6aca186c65ad8323212c4e336507e68f4ee09d75ae0366607b5eb1a4498f`
  - ElmsSans-Italic[wght].ttf: `bc485f45f3090748e540223fe29f44bed69b67c7311a3f984dffa5295713a017`
- The commit hash is confirmed correct

### Source Files
- **Source format**: Glyphs 3 (.glyphs file) -- `sources/ElmsSans.glyphs` (appVersion 3428, formatVersion 3)
- **Config YAML**: `sources/config.yaml` exists in the upstream repo at the referenced commit
  - Sources: ElmsSans.glyphs
  - familyName: Elms Sans
  - cleanUp: true
  - splitItalic: true (Roman and Italic variable fonts are split from a single source)
  - Full STAT table configuration for wght (100-900) and ital axes
- **Additional source files**: `sources/CustomFilter_GF_Latin_All.plist`
- **No override config.yaml** in the google/fonts family directory

## Status
- **Status**: Complete
- **Confidence**: HIGH
- **All source metadata is present and verified**

No action needed. The METADATA.pb source block is complete with verified repository URL, commit hash, branch, config_yaml path, and file mappings. Binary files match the referenced commit exactly.
