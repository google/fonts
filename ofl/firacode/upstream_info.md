# Investigation Report: Fira Code

## Family Overview
- **Family name**: Fira Code
- **Designer**: The Mozilla Foundation, Telefonica S.A., Nikita Prokopov
- **License**: OFL
- **Category**: Monospace
- **Date added to Google Fonts**: 2019-03-25
- **Font files**: 1 variable font (FiraCode[wght].ttf, wght 300-700)

## Source Information

### Repository URL
- **Current METADATA.pb value**: `https://github.com/tonsky/FiraCode`
- **Verified**: Yes, repository exists and is active
- **Assessment**: CORRECT. tonsky/FiraCode is the primary upstream for Fira Code. It contains `FiraCode.glyphs` as the source file.

### Commit Hash
- **Current tracking value**: `8da49d55f8b5978c5f888dd85452b79aad16cca2`
- **Assessment**: CORRECT. This is the commit for tag `5.2` (dated 2020-06-12), which matches the version referenced in google/fonts PR #3786 ("Updating to Fira Code 5.2").

### Commit Verification

The current font binary in google/fonts (`FiraCode[wght].ttf`, 260,364 bytes) was added via PR #3786, merged 2021-09-08 by Aaron Bell (@aaronbell).

The pre-built variable font at the 5.2 tag (`distr/variable_ttf/FiraCode-VF.ttf`) is 259,912 bytes, slightly different from the google/fonts version. This is expected: the PR body states "Additionally, the STAT table is now working as required," indicating Aaron built from the `FiraCode.glyphs` source at the 5.2 tag and applied additional post-processing (STAT table fixes, gftools fixes).

Note: There have been many commits to `FiraCode.glyphs` after the 5.2 tag (including additions up through commit `fd5acad` on 2021-08-09, before the PR was created on 2021-09-01). However, the PR explicitly references version 5.2 and the comparison link `https://github.com/tonsky/FiraCode/compare/1.207...5.2`. The 5.2 tag commit is the correct reference.

### Build History in google/fonts
1. `cf61567f7` - "fira code: v1.207 added" (original addition)
2. `a5b584e16` - "firacode: v3.206 added (#516)" (Dec 6, 2016, from FiraGFVersion)
3. `01f775560` - "Revert 'firacode: v3.206 added' (#520)" (immediately reverted by Dave Crossland)
4. `f7877b1dd` - "firacode: v1.208 added" (hotfix to remove MVAR table)
5. `70b0fc8a8` - "Remove static fonts for unhinted variable font families (#3695)"
6. `30485dad1` - "Updating to Fira Code 5.2 (#3786)" -- the current version, merged 2021-09-08

### Config
- **config.yaml location**: Override config.yaml exists in google/fonts (`ofl/firacode/config.yaml`)
- **Config contents**: `sources: ["FiraCode.glyphs"]`
- **config_yaml in METADATA.pb**: Not set (correctly omitted since override exists)
- **Assessment**: COMPLETE. The override config.yaml correctly references `FiraCode.glyphs` which exists at the repo root in tonsky/FiraCode.

## Relationship to Fira Superfamily
Fira Code is a separate project by Nikita Prokopov (tonsky), built as an extension of Fira Mono with programming ligatures. It has its own independent upstream repo (tonsky/FiraCode) and its own .glyphs source file. It is NOT part of the googlefonts/FiraGFVersion repo which hosts the other Fira families (Fira Sans, Fira Mono, Fira Sans Condensed, Fira Sans Extra Condensed).

The copyright in the font file references "The Fira Code Project Authors (https://github.com/tonsky/FiraCode)".

## Status Summary
- **Repository URL**: CORRECT (tonsky/FiraCode)
- **Commit hash**: CORRECT (8da49d5, tag 5.2)
- **Config**: COMPLETE (override config.yaml in google/fonts)
- **Overall status**: complete
- **Confidence**: HIGH

## Key Evidence
- PR #3786 title: "Fira Code: Version 5.2 added"
- PR #3786 body: references `https://github.com/tonsky/FiraCode/compare/1.207...5.2`
- PR #3786 author: Aaron Bell (@aaronbell), merged 2021-09-08
- Tag 5.2 resolves to commit `8da49d5` dated 2020-06-12
- Override config.yaml already present in google/fonts directory
