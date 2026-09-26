# Investigation Report: Fredoka

## Family Details
- **Family name**: Fredoka
- **Path in google/fonts**: `ofl/fredoka/`
- **Designer**: Milena Brandao, Hafontia
- **License**: OFL
- **Date added**: 2021-12-15 (variable version; original "Fredoka One" was added 2012-03-14)
- **Font files**: `Fredoka[wdth,wght].ttf` (variable, width 75-125, weight 300-700)

## Source Block in METADATA.pb (current)
```
source {
  repository_url: "https://github.com/hafontia-zz/Fredoka-One"
  commit: "35c584ff23450c9bcdf8819706e12fcdeefe1712"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Fredoka[wdth,wght].ttf"
    dest_file: "Fredoka[wdth,wght].ttf"
  }
  branch: "gh-pages"
  config_yaml: "sources/config.yml"
}
```

## Upstream Repository
- **URL**: https://github.com/hafontia-zz/Fredoka-One
- **Status**: Accessible (HTTP 200)
- **Default branch**: `gh-pages`
- **Repository owner**: hafontia-zz (original); hafontia is a fork
- **Last pushed**: 2022-03-03
- **Local cache**: `upstream_repos/fontc_crater_cache/hafontia-zz/Fredoka-One/`
- **Cache status**: Clean, up to date with remote

### Repository Structure (at commit 35c584f)
The repo has a single commit on the `gh-pages` branch (it was force-pushed at some point, replacing history):
```
35c584f  2022-03-03  Added semibold instance + changed font origin so the default is also a fvar instance
```
Key directories:
- `sources/Fredoka.glyphs` -- Glyphs source file
- `sources/config.yml` -- gftools-builder configuration
- `fonts/variable/Fredoka[wdth,wght].ttf` -- compiled variable font
- `fonts/ttf/` -- static TTF instances (Light, Regular, Medium, SemiBold, Bold)
- `fonts/otf/` -- static OTF instances
- `documentation/` -- specimen images and PDFs

### config.yml Contents
```yaml
sources:
  - Fredoka.glyphs
includeSourceFixes: false
autohintTTF: false
buildStatic: true
outputDir: "../fonts"
```
Located at `sources/config.yml` relative to repo root.

## Commit Hash Verification

### Commit referenced in METADATA.pb
- **Hash**: `35c584ff23450c9bcdf8819706e12fcdeefe1712`
- **Date**: 2022-03-03T14:22:47+01:00
- **Message**: "Added semibold instance + changed font origin so the default is also a fvar instance"

### Verification
This is the only commit in the `gh-pages` branch of the upstream repo (the branch was force-pushed at some point). The binary font file in google/fonts is **identical** to the file at this commit:
- google/fonts: `ofl/fredoka/Fredoka[wdth,wght].ttf` -- 159,184 bytes
- upstream: `fonts/variable/Fredoka[wdth,wght].ttf` -- 159,184 bytes
- Binary diff: **files are identical**

### google/fonts Commit History
1. **bbd715dfa** (2021-12-15) -- PR #4170 by Marc Foley (m4rc1e): "Fredoka: Version 2.000 added"
   - Referenced upstream commit `04d5e5545f807f1c4e80404e29e0b38d6775a996` (no longer exists in repo due to force-push)
   - Initial onboarding of the variable Fredoka (replacing the old single-weight "Fredoka One")
   - Font file was 157,564 bytes at this point
   - Fixes issue #1677 ("Upgrade Fredoka One")
2. **852e3979d** (2022) -- PR #4243 by Rosalie Wagner: "Fredoka: updated metadata and description"
3. **eda3fe521** (2022-03-03) -- PR #4345 by Rosalie Wagner: "Fredoka: Version 2.001 added"
   - gftools-packager automated update
   - Referenced upstream commit `35c584ff23450c9bcdf8819706e12fcdeefe1712` (current METADATA.pb hash)
   - Font file updated to 159,184 bytes (current version)
4. **11c7c02a2** (2023-02-28) -- PR #5942 by Rosalie Wagner: "Fredoka: added missing designer"
   - Added back "Milena Brandao" to designer field
5. **66f91f10f** -- Merge upstream.yaml into METADATA.pb (batch operation)
6. **19cdcec59** -- Batch port from fontc_crater targets list (added `config_yaml: "sources/config.yml"`)

## Historical Context

Fredoka has an interesting lineage:
- **Fredoka One** (originally added 2012-03-14): A single-weight display font by Milena Brandao. It was later delisted from Google Fonts (commit e49bba379, PR #6041).
- **Fredoka** (added 2021-12-15): A variable font with width and weight axes, developed by Ben Nathan (Hafontia) who added Hebrew support and created the variable version. This replaced Fredoka One in the catalog.
- The copyright notice references `https://github.com/hafontia/Fredoka-One`, but the actual upstream is `hafontia-zz/Fredoka-One`. The `hafontia/Fredoka-One` repo (ID 436663115) is a **fork** of `hafontia-zz/Fredoka-One` (ID 42506586), last pushed in 2021-11-11 and behind the original.
- Issue #1677 was filed by Ben Nathan requesting the upgrade from Fredoka One to the new variable Fredoka with Hebrew support.

## Assessment

| Field | Value | Status |
|-------|-------|--------|
| repository_url | `https://github.com/hafontia-zz/Fredoka-One` | Correct |
| commit | `35c584ff23450c9bcdf8819706e12fcdeefe1712` | Correct (verified: binary identical) |
| branch | `gh-pages` | Correct |
| config_yaml | `sources/config.yml` | Correct (exists at referenced commit) |

## Status: COMPLETE
- **Confidence**: HIGH
- All source metadata fields are present and verified.
- The repository URL points to the correct upstream (hafontia-zz, not the fork hafontia).
- The commit hash is verified by binary comparison of the font file.
- The config.yml exists in the upstream repo at the correct path and contains valid gftools-builder configuration with Glyphs source.
- No action required.
