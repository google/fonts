# Investigation Report: Fira Sans

## Family Overview
- **Family name**: Fira Sans
- **Designer**: Carrois Apostrophe
- **License**: OFL
- **Category**: Sans Serif
- **Date added to Google Fonts**: 2014-06-18
- **Font files**: 18 static TTFs (9 weights x 2 styles: Thin through Black, each in Roman and Italic)

## Source Information

### Repository URL
- **Current METADATA.pb value**: `https://github.com/googlefonts/FiraGFVersion`
- **Verified**: Yes, repository exists
- **Assessment**: CORRECT but with caveats. The FiraGFVersion repo is a Google Fonts-specific staging repository created by Marc Foley (@m4rc1e) to prepare Fira fonts for onboarding. It contains only pre-built TTF binaries, not source files. The original upstream source is `https://github.com/carrois/Fira` (now redirects to `https://github.com/bBoxType/FiraSans`), and the Mozilla fork is `https://github.com/mozilla/Fira`.

### Commit Hash
- **Current tracking value**: `a7d6892325d5b7382e426bea13bd3ef2c32bd53e` (merge commit)
- **Correct value**: `2f050e7a85240e5c164d1a265a711df012770429`
- **Assessment**: The tracking value `a7d6892` is a merge commit (PR #2) that resolves to the same tree as `2f050e7`. Both reference the same file contents for Fira Sans. However, `2f050e7` is the actual working commit where Marc Foley updated the TTF sources on Dec 2, 2016.

### Commit Verification

Binary file matching was verified by comparing md5 checksums between FiraGFVersion at commit `2f050e7` and google/fonts:

| File | Match? |
|------|--------|
| FiraSans-Regular.ttf | YES (md5: 8a8828468dbb8ca0386ee288e8316257) |
| FiraSans-Bold.ttf | YES (md5: eca2c47a78c324a9245983633733ee6b) |
| FiraSans-Italic.ttf | YES (md5: 45bf96bdc5758e1687bcdad4d34b94f4) |
| FiraSans-Black.ttf | YES (md5: fef3335956713fe239c38dcbc026b869) |
| FiraSans-Thin.ttf | YES (md5: e0d565dd43d6ae00b7a14e8fbfb73f22) |

All tested files are byte-identical between FiraGFVersion@2f050e7 and google/fonts.

Important: The files at FiraGFVersion HEAD (`8d9d02b`) have DIFFERENT checksums due to a later commit (`7b7927f`, Dec 6, 2016) that rebuilt all fonts when adding Fira Code and renaming Compressed to ExtraCondensed. The correct commit for Fira Sans is `2f050e7` (or its merge `a7d6892`), NOT HEAD.

### Build History in google/fonts
1. `90abd17b4` - Initial commit (original Fira Sans files, 2014)
2. `4e1c8e1bb` - "ofl/firasans Update copyright notice"
3. `79d9ee273` - "ofl/firasans Updated to v4.106g"
4. `ed7143b8f` - "firasans: 4.203 added (#483)" -- the current version, merged 2016-12-02

### Config
- **config.yaml**: Does NOT exist in google/fonts or in FiraGFVersion
- **Assessment**: NOT POSSIBLE. The FiraGFVersion repo contains only pre-built TTF binaries. Its `src/` directory contains TTF files (misleadingly named), not .glyphs/.ufo/.designspace source files. There are no buildable sources to reference in a config.yaml.

The original font sources (.glyphs files) exist in:
- `https://github.com/mozilla/Fira` at `source/glyphs/FiraSans.glyphs` and `source/glyphs/FiraSansItalic.glyphs`
- `https://github.com/bBoxType/FiraSans` (formerly carrois/Fira)

However, the fonts in google/fonts were not compiled from .glyphs sources directly. They were compiled by Carrois Apostrophe from those sources, and then the pre-built TTFs were processed through the FiraGFVersion build pipeline (rename, nametable fix, autohint). Creating a gftools-builder config.yaml would require a different approach.

## FiraGFVersion Build Process

The FiraGFVersion `build/build.sh` script:
1. Copies TTFs from `src/` to `fonts/`
2. Removes variants not supported by GF API (Eight, Four, Two, Book, UltraLight)
3. Renames font filenames to fit Thin-Black weight range
4. Applies `fontbakery-nametable-from-filename.py` to fix nametables
5. Runs cleanup scripts

The `src/` TTF files were sourced from `carrois/Fira/tree/master/Fira_Sans_4_2/Fonts/FiraSans_WEB_4203` as documented in commit `2f050e7`.

## Relationship to Fira Superfamily
Fira Sans is the core family of the Fira superfamily, designed by Erik Spiekermann and Carrois Apostrophe for Mozilla/Firefox OS. In google/fonts, it shares the FiraGFVersion upstream repo with Fira Mono, Fira Sans Condensed, and Fira Sans Extra Condensed. Fira Code has a separate upstream (tonsky/FiraCode).

## Status Summary
- **Repository URL**: CORRECT (googlefonts/FiraGFVersion)
- **Commit hash**: CORRECT (`a7d6892` merge = `2f050e7` actual, both valid; binary match confirmed)
- **Config**: missing_config (no buildable sources in repo, TTF-only)
- **Overall status**: missing_config
- **Confidence**: HIGH (for repo URL and commit), N/A (for config)

## Key Evidence
- PR #483 title: "firasans: 4.203 added", author: Marc Foley, merged 2016-12-02
- FiraGFVersion commit `2f050e7` message: "src fonts updated to ttf sources, available here https://github.com/carrois/Fira/tree/master/Fira_Sans_4_2/Fonts/FiraSans_WEB_4203"
- Binary checksums confirm: all Fira Sans files in google/fonts are byte-identical to FiraGFVersion@2f050e7
- FiraGFVersion HEAD (8d9d02b) has different checksums due to the Dec 6 rebuild (commit 7b7927f)
