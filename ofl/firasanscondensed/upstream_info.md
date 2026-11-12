# Investigation Report: Fira Sans Condensed

## Family Overview
- **Family name**: Fira Sans Condensed
- **Designer**: Carrois Apostrophe
- **License**: OFL
- **Category**: Sans Serif
- **Date added to Google Fonts**: 2016-12-02
- **Font files**: 18 static TTFs (9 weights x 2 styles: Thin through Black, each in Roman and Italic)

## Source Information

### Repository URL
- **Current METADATA.pb value**: `https://github.com/googlefonts/FiraGFVersion`
- **Verified**: Yes, repository exists
- **Assessment**: CORRECT but with caveats. The FiraGFVersion repo is a Google Fonts-specific staging repository created by Marc Foley (@m4rc1e). It contains only pre-built TTF binaries, not source files. The original upstream is `https://github.com/carrois/Fira` (now redirects to `https://github.com/bBoxType/FiraSans`).

### Commit Hash
- **Current tracking value**: `a7d6892325d5b7382e426bea13bd3ef2c32bd53e` (merge commit)
- **Correct value**: `2f050e7a85240e5c164d1a265a711df012770429`
- **Assessment**: The tracking value `a7d6892` is a merge commit (PR #2) that resolves to the same tree as `2f050e7`. Both reference the same file contents for Fira Sans Condensed. `2f050e7` is the actual working commit (Dec 2, 2016).

### Commit Verification

Binary file matching was verified by comparing md5 checksums.

The Condensed files at FiraGFVersion commit `2f050e7` match the google/fonts versions:
- FiraSansCondensed-Regular.ttf: google/fonts md5 = `13826286e7c6673a8a7e16233aba99e5`, matches `2f050e7`

Important: At FiraGFVersion HEAD (`8d9d02b`), the Condensed files have DIFFERENT checksums (same file sizes but different md5). This is because commit `7b7927f` (Dec 6, 2016, "added Fira Code, Renamed Compressed to ExtraCondensed") rebuilt ALL fonts including the Condensed ones. The files in google/fonts match the `2f050e7` versions, NOT the HEAD versions.

Timeline:
- Dec 2, 2016: Commit `2f050e7` updated TTF sources in FiraGFVersion
- Dec 2, 2016: PR #486 merged the Condensed files into google/fonts (using fonts from `2f050e7`)
- Dec 6, 2016: Commit `7b7927f` rebuilt all fonts (including Condensed) when adding Fira Code
- Dec 7, 2016: Merge commit `8d9d02b` (HEAD) contains the rebuilt Dec 6 versions

The google/fonts Condensed files match the Dec 2 commit, not the Dec 6 rebuild.

### Build History in google/fonts
1. `a3d70f5d8` - "firasanscondensed: v4.203 added (#486)" -- the only commit that modified font binaries, merged 2016-12-02

This was a new addition to Google Fonts (date_added: 2016-12-02), unlike Fira Sans and Fira Mono which were present since 2014.

### Config
- **config.yaml**: Does NOT exist in google/fonts or in FiraGFVersion
- **Assessment**: NOT POSSIBLE. The FiraGFVersion repo contains only pre-built TTF binaries. There are no .glyphs/.ufo/.designspace source files to reference in a config.yaml.

The original source (.glyphs) for the condensed variants may exist in mozilla/Fira or bBoxType/FiraSans, but the fonts in google/fonts were built from pre-compiled TTFs through the FiraGFVersion pipeline (rename, nametable fix), not compiled from source.

## FiraGFVersion Repository Context

At the time Fira Sans Condensed was added (Dec 2, 2016), the FiraGFVersion repo's `fonts/` directory contained Condensed files originally named with the "Condensed" prefix. The build script (`build/build.sh`) processed them through renaming and nametable fixes.

The Condensed files were present in FiraGFVersion from the very first content commit (`85db9d5`, Nov 29, 2016), updated in `2f050e7` (Dec 2) to use TTF sources instead of OTF, and then rebuilt again in `7b7927f` (Dec 6) alongside the Compressed->ExtraCondensed rename.

## Relationship to Fira Superfamily
Fira Sans Condensed is a width variant of Fira Sans, part of the Fira superfamily designed by Erik Spiekermann and Carrois Apostrophe for Mozilla/Firefox OS. In google/fonts, it shares the FiraGFVersion upstream repo with Fira Sans, Fira Mono, and Fira Sans Extra Condensed. It was onboarded at the same time as Fira Sans and Fira Mono (Dec 2, 2016), all via PRs by Marc Foley.

## Status Summary
- **Repository URL**: CORRECT (googlefonts/FiraGFVersion)
- **Commit hash**: CORRECT (`a7d6892` merge = `2f050e7` actual, both valid; binary match confirmed)
- **Config**: missing_config (no buildable sources in repo, TTF-only)
- **Overall status**: missing_config
- **Confidence**: HIGH (for repo URL and commit), N/A (for config)

## Key Evidence
- PR #486 title: "firasanscondensed: v4.203 added", author: Marc Foley, merged 2016-12-02
- FiraGFVersion commit `2f050e7`: "src fonts updated to ttf sources" (from carrois/Fira v4.2)
- Binary checksums confirm: Condensed files at `2f050e7` match google/fonts; HEAD versions differ
- No .glyphs/.ufo/.designspace sources in FiraGFVersion -- only pre-built TTFs
