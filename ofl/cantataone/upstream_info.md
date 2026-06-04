# Cantata One

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Joana Correia (design), Eben Sorkin (mastering)
**METADATA.pb path**: `ofl/cantataone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/cantataone |
| Commit | `947c3dd6e969867a02166335a27c48c0a7f9123d` |
| Config YAML | -- |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/cantataone` was already recorded in the tracking file. Verification confirms:

- The GitHub repo returns HTTP 200 and is accessible.
- The repo was created on 2014-07-16 and last pushed on 2014-10-17.
- The repo contains matching source files (SFD, VFB) and the same FONTLOG.txt, DESCRIPTION.en_us.html, and OFL.txt files found in `ofl/cantataone/` in google/fonts.
- The librefonts organization hosts many Google Fonts family repos in a decomposed TTX format used by the fontc_crater_cache system.

The font was originally hosted on Google Code (referenced in the DESCRIPTION.en_us.html: "Source files are available from Google Code") before being migrated to the librefonts GitHub organization.

## How the Commit Hash Was Identified

The upstream repository contains exactly **one commit**: `947c3dd6e969867a02166335a27c48c0a7f9123d`.

- **Commit date**: 2014-10-17 13:32:04 +0300
- **Author**: hash3g <hash.3g@gmail.com>
- **Message**: "update .travis.yml"
- Despite the commit message referencing only `.travis.yml`, this is the initial (and only) commit that created the entire repository with all files.

Since there is only a single commit, it is unambiguously the correct reference point. The font binary in google/fonts was part of the initial google/fonts repository commit (`90abd17b4`, dated 2015-03-07) and has never been updated since. The font was added to Google Fonts on 2012-02-29 (per METADATA.pb `date_added`), predating the GitHub repo creation (2014-07-16), indicating the original source was on Google Code.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory (`ofl/cantataone/`).

The upstream repo contains only legacy source formats:
- `src/CantataOne-Regular.vfb` -- FontLab VFB (original source with contour overlaps)
- `src/CantataOne-Regular-OTF.sfd` -- FontForge SFD (merged contours, OTF-targeted)
- `src/CantataOne-Regular-TTF.sfd` -- FontForge SFD (TrueType outlines with hinting)

These formats are **not compatible with gftools-builder**. A config.yaml cannot be meaningfully created because gftools-builder requires `.glyphs`, `.ufo`, or `.designspace` source files. The sources would need to be converted to a modern format before a config.yaml could be useful.

## Verification

- Commit exists in upstream repo: **Yes**
- Commit date: 2014-10-17 13:32:04 +0300
- Commit message: "update .travis.yml"
- Source files at commit:
  - `src/CantataOne-Regular.vfb` (FontLab binary)
  - `src/CantataOne-Regular-OTF.sfd` (FontForge Spline Font Database)
  - `src/CantataOne-Regular-TTF.sfd` (FontForge Spline Font Database)
  - `src/CantataOne-Regular.otf.*` (decomposed OTF TTX tables)
  - `CantataOne-Regular.ttf.*` (decomposed TTF TTX tables)
  - `.travis.yml` (fontbakery CI config)
  - `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `OFL.txt`, `METADATA.json`

## Additional Notes

- The font was designed by Joana Maria Correia da Silva and mastered by Eben Sorkin (Sorkin Type Co).
- Version 1.002 is the latest, with hinting added via TTFAutohint v0.8 (per FONTLOG.txt).
- The `.travis.yml` references fontbakery-build.py and fontbakery-report.py, vintage CI tooling from 2014.
- The METADATA.pb in google/fonts has no `source { }` block.
- The font has never been updated in google/fonts since the initial repository commit.

## Confidence

**HIGH**: The upstream repository has a single commit, making identification unambiguous. The repository URL is confirmed accessible and contains matching source files. The status is "missing_config" because the sources are in legacy formats (SFD/VFB) that are not compatible with gftools-builder, so no config.yaml can be created without first converting the sources to a modern format.
