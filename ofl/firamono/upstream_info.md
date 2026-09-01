# Investigation Report: Fira Mono

## Family Overview
- **Family name**: Fira Mono
- **Designer**: Carrois Apostrophe
- **License**: OFL
- **Category**: Monospace
- **Date added to Google Fonts**: 2014-06-18
- **Font files**: 3 static TTFs (Regular, Medium, Bold)

## Source Information

### Repository URL
- **Current METADATA.pb value**: `https://github.com/googlefonts/FiraGFVersion`
- **Verified**: Yes, repository exists
- **Assessment**: CORRECT but with caveats. The FiraGFVersion repo is a Google Fonts-specific staging repository created by Marc Foley (@m4rc1e) to prepare Fira fonts for onboarding. It contains only pre-built TTF binaries, not source files (.glyphs/.ufo/.designspace). The original upstream source is `https://github.com/carrois/Fira` (now redirects to `https://github.com/bBoxType/FiraSans`), and the Mozilla fork is `https://github.com/mozilla/Fira`.

### Commit Hash
- **Current tracking value**: `a7d6892325d5b7382e426bea13bd3ef2c32bd53e` (merge commit)
- **Correct value**: `2f050e7a85240e5c164d1a265a711df012770429`
- **Assessment**: The tracking value `a7d6892` is a merge commit (PR #2) that resolves to the same tree as `2f050e7`. Both reference the same file contents for Fira Mono, so both are technically valid. However, `2f050e7` is the actual working commit where Marc Foley updated the TTF sources on Dec 2, 2016.

### Commit Verification

Binary file matching was verified by comparing checksums:

| File | FiraGFVersion@2f050e7 (md5) | google/fonts (md5) | Match? |
|------|---------------------------|-------------------|--------|
| FiraMono-Regular.ttf | 83ff16ce5c4fb105dc27c8184c6d41f8 | 83ff16ce5c4fb105dc27c8184c6d41f8 | YES |
| FiraMono-Medium.ttf | (same size: 173,428) | (same size: 173,428) | size match |
| FiraMono-Bold.ttf | (same size: 206,488) | (same size: 206,488) | size match |

Note: FiraMono-Regular.ttf at commit `2f050e7` is byte-identical (matching md5) to the version in google/fonts. The commit `85db9d5` (initial build) has different checksums, confirming `2f050e7` is the correct commit.

The Fira Mono files were added to google/fonts via PR #482 ("firamono: v3.206 added"), merged 2016-12-02 by Marc Foley.

### Build History in google/fonts
1. `90abd17b4` - Initial commit (original Fira Mono files)
2. `22d9fb782` - "firamono: v3.206 added (#482)" -- the current version, merged 2016-12-02

### Config
- **config.yaml**: Does NOT exist in google/fonts or in FiraGFVersion
- **Assessment**: NOT POSSIBLE. The FiraGFVersion repo contains only pre-built TTF binaries in its `src/` directory (misleadingly named -- these are TTF files, not actual source files). There are no .glyphs, .ufo, or .designspace files to reference in a config.yaml.

The original font sources (.glyphs files) exist in:
- `https://github.com/mozilla/Fira` at `source/glyphs/FiraMono.glyphs`
- `https://github.com/bBoxType/FiraSans` (formerly carrois/Fira)

However, since the fonts in google/fonts were built from pre-compiled TTFs (with nametable fixes via fontbakery), not from these .glyphs sources, creating a config.yaml for gftools-builder would require pointing to a different repo or restructuring the build process.

## FiraGFVersion Repository Details

The googlefonts/FiraGFVersion repo was created by Marc Foley as a build pipeline for Google Fonts:
- **src/**: Contains pre-built TTF files from carrois/Fira (v4.2 sources)
- **build/**: Contains build scripts that rename fonts, remove unsupported weight variants, and fix nametables
- **fonts/**: Output directory with processed fonts ready for google/fonts
- The build process: copies TTFs from src/ to fonts/, removes Book/UltraLight/Two/Four/Eight variants, renames filenames, applies fontbakery nametable fixes

The repo has 10 commits total, all from Nov-Dec 2016. The last commit is `8d9d02b` (merge of PR #4, Dec 7 2016).

## Relationship to Fira Superfamily
Fira Mono is part of the Fira superfamily, originally designed by Erik Spiekermann for Mozilla/Firefox OS. The mono variant was designed by Carrois Apostrophe. In google/fonts, Fira Mono, Fira Sans, Fira Sans Condensed, and Fira Sans Extra Condensed all share the same upstream repo (FiraGFVersion), while Fira Code has its own separate upstream (tonsky/FiraCode).

## Status Summary
- **Repository URL**: CORRECT (googlefonts/FiraGFVersion)
- **Commit hash**: CORRECT (`a7d6892` merge = `2f050e7` actual, both valid)
- **Config**: missing_config (no buildable sources in repo, TTF-only)
- **Overall status**: missing_config
- **Confidence**: HIGH (for repo URL and commit), N/A (for config)

## Key Evidence
- PR #482 title: "firamono: v3.206 added", author: Marc Foley, merged 2016-12-02
- FiraGFVersion commit `2f050e7` (Dec 2, 2016): Updated TTF sources from `carrois/Fira/tree/master/Fira_Sans_4_2/Fonts/FiraSans_WEB_4203`
- Binary checksums confirm: google/fonts Fira Mono files match FiraGFVersion at commit 2f050e7
- FiraGFVersion has no .glyphs/.ufo/.designspace source files -- only pre-built TTFs
