# Cedarville Cursive

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Kimberly Geswein
**METADATA.pb path**: `ofl/cedarvillecursive/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/cedarvillecursive |
| Commit | `cd212b0e2dc2364a3012ef43a3b9155c7ed0d352` |
| Config YAML | -- |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/cedarvillecursive` was identified from the existing tracking data in `data/gfonts_library_sources.json`. The URL was verified to be accessible (HTTP 200). The repository belongs to the `librefonts` GitHub organization, which was a project that created archive repositories for Google Fonts families by extracting TTX data from the binary fonts and preserving original source files (when available).

The repo was created on 2014-07-16 and contains a single commit from 2014-10-17 by user `hash3g`. There are no other known upstream repositories for this font by the designer (Kimberly Geswein). No repositories were found under other owners on GitHub.

The METADATA.pb file in google/fonts currently has no `source` block.

## How the Commit Hash Was Identified

The repository contains only a single commit:

- **Hash**: `cd212b0e2dc2364a3012ef43a3b9155c7ed0d352`
- **Date**: 2014-10-17 13:32:23 +0300
- **Author**: hash3g
- **Message**: "update .travis.yml"

Since this is the only commit, it is necessarily the one that represents the full state of the repository. The commit message ("update .travis.yml") is misleading -- it appears to be the initial import of all files into the librefonts archive, committed as a single squashed commit.

The font was added to google/fonts in the initial commit (`90abd17b4`, 2015-03-07 by Dave Crossland). The binary was later modified in commit `8ccda7bf7` (2015-08-05, "Fix fsType for 40 font files") which patched the fsType flag without rebuilding from source.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The only source file is `src/Cedarville-Cursive.vfb`, which is a FontLab Studio binary format (`.vfb`). This format is **not supported** by gftools-builder or fontc.

The repository also contains TTX (XML) decompositions of the compiled font binary (split across multiple `.ttx` files), but these are not editable design sources -- they are a representation of the compiled binary itself.

An override `config.yaml` **cannot** be created because:
1. The `.vfb` format is not supported by any current open-source font build toolchain
2. The TTX files are decomposed binaries, not design sources
3. There are no `.glyphs`, `.ufo`, or `.designspace` files available

No override `config.yaml` exists in the google/fonts family directory either.

## Verification

- Commit exists in upstream repo: **Yes** (only commit)
- Commit date: 2014-10-17 13:32:23 +0300
- Commit message: "update .travis.yml"
- Source files at commit:
  - `src/Cedarville-Cursive.vfb` (FontLab binary, 91125 bytes)
  - `src/VERSIONS.txt` ("Cedarville-Cursive.ttf: Version 1.001 2010")
  - `src/METADATA_comments.txt` (font-optimizer subsetting commands)
  - `Cedarville-Cursive.ttf.ttx` (master TTX referencing 17 split TTX table files)
  - `.travis.yml` (fontbakery CI configuration)
  - `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`

## Confidence

**HIGH**: The repository URL is confirmed accessible, the commit hash is the only commit in the repo, and the source format limitation (VFB-only) is definitively verified. The font cannot be rebuilt from open-source tooling without source conversion work. The librefonts archive is the only known upstream for this font.
