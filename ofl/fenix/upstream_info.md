# Investigation Report: Fenix

## Family Details
- **Family name**: Fenix
- **Designer**: Fernando Diaz
- **License**: OFL
- **Category**: Serif
- **Date added to Google Fonts**: 2012-09-24
- **Fonts**: Fenix-Regular.ttf (400 normal)

## Upstream Repository
- **URL**: https://github.com/librefonts/fenix
- **Status**: Accessible (HTTP 200)
- **Owner**: librefonts (organization)
- **Default branch**: master
- **Created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Contributors**: vitalyvolkov, xen

## Commit Analysis
- **Total commits**: 1
- **Only commit**: `b5107c124ba8762eeaccd00b73a7302897d4367e` (2014-10-17, by hash3g)
- **Commit message**: "update .travis.yml"
- **Confidence**: HIGH -- there is only one commit in the entire repository, so this is unambiguously the correct reference.

## Source Files in Upstream Repository

### Root directory (TTX decomposed from TTF binary):
- `Fenix-Regular.ttf.*.ttx` (multiple table-split TTX files, ttLibVersion 2.4)
- `DESCRIPTION.en_us.html`
- `FONTLOG.txt`
- `METADATA.json`
- `OFL.txt`
- `.travis.yml` (legacy Travis CI config using fontbakery-build.py)

### src/ directory (original design sources):
- `Fenix-Regular-TTF.sfd` (FontForge SFD format, 282 KB)
- `Fenix-Regular-OTF.vfb` (FontLab VFB format, 120 KB)
- `Fenix-Regular.vfb` (FontLab VFB format, 178 KB)
- `Fenix-Regular.otf.*.ttx` (OTF table-split TTX files)
- `METADATA_comments.txt` (contains build/subset commands)
- `VERSIONS.txt` (contents: "Fenix-Regular.ttf: 004.301")

### Source type assessment:
- **SFD-only sources** (FontForge format) plus VBF (FontLab format)
- No `.glyphs`, `.ufo`, or `.designspace` files
- Not compatible with gftools-builder
- No `config.yaml` present or possible

## Binary Verification

The font binary in google/fonts (`ofl/fenix/Fenix-Regular.ttf`, 45,144 bytes) matches the upstream TTX decomposition:
- **Version string** (nameID 5): "004.301" -- matches both the binary and the upstream TTX
- **Font creation date** (head table): Mon Oct 1 14:45:46 2012
- **Font modification date** (head table): Mon Oct 1 14:45:46 2012
- **checkSumAdjustment**: 0xd9d8ad71 (from upstream TTX)
- **fontRevision**: 1.0

The SFD file header confirms the same version: "Version: 004.301".

## Google Fonts Repository History

The font file history in google/fonts shows only two commits touching `ofl/fenix/`:
1. `90abd17b4f` (2015-03-07) -- "Initial commit" by Dave Crossland. This was the bulk import of the entire Google Fonts library into the git repository. The font itself was added to Google Fonts on 2012-09-24, predating the git repo.
2. `76adaf1d29` (2021-11-01) -- "deploy: c7e2740188205a85..." -- A deploy commit that deleted files (part of a repo restructure). The files were restored/maintained through the branch structure.

No PRs or commits indicate any updates to the Fenix binary since original onboarding.

## Repository Context

The `librefonts` organization on GitHub appears to be a community archival effort to host libre/open-source font projects with their sources and TTX decompositions. The single commit was authored by "hash3g" (hash.3g@gmail.com), and the listed contributors are vitalyvolkov and xen. The repo was created on 2014-07-16, nearly two years after the font was added to Google Fonts.

The METADATA_comments.txt file in `src/` contains the original subsetting and font-optimizer commands used during Google Fonts onboarding, confirming this is the authoritative source archive for this font.

## Designer Information

- **Designer**: Fernando Diaz (Fernando Diaz)
- **Website**: www.ferfolio.com (currently suspended/inactive)
- **Email**: fer@ferfolio.com (from METADATA.pb copyright), fenix@ferfolio.com (from FONTLOG)
- **Copyright**: "Copyright (c) 2012, Fernando Diaz (www.ferfolio.com fer@ferfolio.com) with Reserved Font Name 'Fenix'"

## Existing Source Block

A source block was added to METADATA.pb in commit `9a14639f3c` (2026-02-25) as part of a batch addition of 602 source blocks:

```
source {
  repository_url: "https://github.com/librefonts/fenix"
  commit: "b5107c124ba8762eeaccd00b73a7302897d4367e"
}
```

This source block is correct. The commit hash references the only commit in the repository.

Note: This source block has not yet been merged into google/fonts main -- it was added in a local working branch.

## Status and Recommendation

- **Repository URL**: Confirmed correct (`https://github.com/librefonts/fenix`)
- **Commit hash**: Confirmed correct (`b5107c124ba8762eeaccd00b73a7302897d4367e`, the only commit)
- **Config**: None possible -- sources are SFD/VBF only, not compatible with gftools-builder
- **Status**: `complete` (for source metadata purposes; no config.yaml needed or possible)
- **Confidence**: HIGH

No override `config.yaml` is needed or possible since the sources are in legacy formats (FontForge SFD and FontLab VBF) that are not supported by gftools-builder. The source block with repository_url and commit hash is sufficient.
