# Investigation Report: Fira Sans Extra Condensed

## Family Overview
- **Family name**: Fira Sans Extra Condensed
- **Designer**: Carrois Apostrophe
- **License**: OFL
- **Category**: Sans Serif
- **Date added to Google Fonts**: 2016-12-06
- **Font files**: 18 static TTFs (9 weights x 2 styles: Thin through Black, each in Roman and Italic)

## Source Information

### Repository URL
- **Current METADATA.pb value**: `https://github.com/googlefonts/FiraGFVersion`
- **Verified**: Yes, repository exists
- **Assessment**: CORRECT but with caveats. The FiraGFVersion repo is a Google Fonts-specific staging repository created by Marc Foley (@m4rc1e). It contains only pre-built TTF binaries, not source files. The original upstream is `https://github.com/carrois/Fira` (now redirects to `https://github.com/bBoxType/FiraSans`).

### Commit Hash
- **Current tracking value**: `7b7927fac6d4651685e201081b31193852a7a94f`
- **Assessment**: CORRECT. This is the commit where Marc Foley renamed the "Compressed" fonts to "ExtraCondensed" and added Fira Code (Dec 6, 2016). The merge commit `8d9d02b` resolves to the same tree.

### Commit Verification

Binary file matching was verified by comparing md5 checksums between FiraGFVersion at commit `7b7927f` (or equivalently `8d9d02b`) and google/fonts:

| File | FiraGFVersion (md5) | google/fonts (md5) | Match? |
|------|-------------------|-------------------|--------|
| FiraSansExtraCondensed-Regular.ttf | e11706e5d7fd76fc3cf5221f7f470489 | e11706e5d7fd76fc3cf5221f7f470489 | YES |
| FiraSansExtraCondensed-Black.ttf | b6c74f973b91106a64e0a77ca6b0b76d | b6c74f973b91106a64e0a77ca6b0b76d | YES |
| FiraSansExtraCondensed-Bold.ttf | cbeaf842332fd9fdf5ba42fc367a0bd8 | cbeaf842332fd9fdf5ba42fc367a0bd8 | YES |
| FiraSansExtraCondensed-Thin.ttf | 2708434b9a4cc19aa3b11486082bb874 | 2708434b9a4cc19aa3b11486082bb874 | YES |
| FiraSansExtraCondensed-ExtraBold.ttf | b88a4bcfcf10582abc2a5d6659c43cb0 | b88a4bcfcf10582abc2a5d6659c43cb0 | YES |
| FiraSansExtraCondensed-BlackItalic.ttf | 3592f2c070b1ea98d13941991ee3cdbc | 3592f2c070b1ea98d13941991ee3cdbc | YES |
| FiraSansExtraCondensed-BoldItalic.ttf | c076c1f0f23ccbb61b1a8db0b4cba370 | c076c1f0f23ccbb61b1a8db0b4cba370 | YES |
| FiraSansExtraCondensed-SemiBold.ttf | 3f7401345f9095df4387b7a767e72c9a | 3f7401345f9095df4387b7a767e72c9a | YES |
| FiraSansExtraCondensed-Light.ttf | 37bd5b4a3063cefad8294966554603c4 | 37bd5b4a3063cefad8294966554603c4 | YES |

ALL tested files are byte-identical. This is the most definitive match of any Fira family -- every checked file has identical md5 checksums.

### How ExtraCondensed Was Created

The Fira Sans Extra Condensed files did not exist in the FiraGFVersion repo before commit `7b7927f`. They were created in that commit by renaming the "FiraSansCompressed" fonts to "FiraSansExtraCondensed" and applying nametable fixes. The original "Compressed" variant TTFs were sourced from `carrois/Fira`.

PR #518 in google/fonts ("firasansextracondensed: v4.203 added") was opened by Marc Foley on Dec 6, 2016, with the comment: "I haven't uploaded the ridiculous hairline sub family :-)" This refers to the FiraSansExtraCondensedHairline variant which exists in FiraGFVersion but was NOT added to google/fonts.

### Build History in google/fonts
1. `a8eaa3ebf` - "firasansextracondensed: v4.203 added (#518)" -- the only commit, merged 2016-12-06

This family was added 4 days after Fira Sans, Fira Mono, and Fira Sans Condensed (which were all merged Dec 2).

### Config
- **config.yaml**: Does NOT exist in google/fonts or in FiraGFVersion
- **Assessment**: NOT POSSIBLE. The FiraGFVersion repo contains only pre-built TTF binaries (renamed from "Compressed" to "ExtraCondensed"). There are no .glyphs/.ufo/.designspace source files.

## FiraGFVersion Repository Context

The ExtraCondensed files were originally "Compressed" variants from the carrois/Fira repo. In commit `7b7927f`:
- Compressed fonts were renamed to ExtraCondensed
- All existing fonts (Sans, Condensed, Mono) were also rebuilt
- Fira Code was added

The commit message is: "src | fonts | build: added Fira Code. Renamed 'Compressed' fonts to 'ExtraCondensed'"

## Relationship to Fira Superfamily
Fira Sans Extra Condensed is the narrowest width variant of Fira Sans (originally called "Compressed"). It is part of the Fira superfamily designed by Erik Spiekermann and Carrois Apostrophe for Mozilla/Firefox OS. In google/fonts, it shares the FiraGFVersion upstream repo with Fira Sans, Fira Mono, and Fira Sans Condensed.

Note: The FiraGFVersion repo also contains FiraSansExtraCondensedHairline variants (Regular and Italic) which were NOT uploaded to google/fonts, as noted by Marc Foley in PR #518.

## Status Summary
- **Repository URL**: CORRECT (googlefonts/FiraGFVersion)
- **Commit hash**: CORRECT (`7b7927f`, verified with byte-identical checksums)
- **Config**: missing_config (no buildable sources in repo, TTF-only)
- **Overall status**: missing_config
- **Confidence**: HIGH (for repo URL and commit), N/A (for config)

## Key Evidence
- PR #518 title: "firasansextracondensed: v4.203 added", author: Marc Foley, merged 2016-12-06
- PR #518 body: "I haven't uploaded the ridiculous hairline sub family :-)"
- FiraGFVersion commit `7b7927f` (Dec 6, 2016): renamed Compressed to ExtraCondensed
- Binary checksums confirm: ALL tested ExtraCondensed files are byte-identical between FiraGFVersion@7b7927f and google/fonts
- Merge commit `8d9d02b` resolves to same tree (no diff)
