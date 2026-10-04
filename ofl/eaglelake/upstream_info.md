# Eagle Lake - Investigation Report

**Date investigated:** 2026-02-27
**Status:** missing_config (VFB-only sources, no gftools-builder compatible files)
**Designer:** Brian J. Bonislawsky (Astigmatic / AOETI)

## METADATA.pb path

`ofl/eaglelake/METADATA.pb`

## Source Data

| Field           | Value |
|-----------------|-------|
| repository_url  | https://github.com/librefonts/eaglelake |
| commit          | 4e2b26479cf425b115731aa69e380fd2f5fd88e5 |
| branch          | master |
| config_yaml     | (none) |

## How URL Was Found

The repository URL `https://github.com/librefonts/eaglelake` was already recorded in the tracking file (`data/gfonts_library_sources.json`). The `librefonts` GitHub organization was created by Mikhail Kashkin (hash3g) as an infrastructure project to mirror Google Fonts font sources along with TTX dumps and Travis CI configurations. This is not the original designer's repository -- it is a community mirror that stores the sources in decomposed TTX format plus the original FontLab `.vfb` binaries.

The repository is accessible (HTTP 200) and verified at `https://github.com/librefonts/eaglelake`.

No original Astigmatic/Brian Bonislawsky repository was found for this font on GitHub.

## How Commit Hash Was Identified

The upstream repository contains only a single commit:

- **4e2b264** (2014-10-17): "update .travis.yml" by hash3g

This is a shallow clone, so the commit is the only one available. It is the sole commit in the repository and represents the initial import of all files (TTX dumps, VFB sources, metadata, license, etc.) into the librefonts mirror.

The font binary in google/fonts (`ofl/eaglelake/EagleLake-Regular.ttf`, 78,000 bytes, SHA-256: `53a4e929c9ea3584f2432157fd549c7604e6be7e6c4b39873f34fae7f6823928`) has not changed since the initial bulk commit in google/fonts (`90abd17b4`, 2015-03-07, "Initial commit"). The only subsequent modification was a `chmod -x` permission change (`49fbebd3d`, 2016-09-26) which did not alter the file contents.

The font was created in May 2012 (per the `head` table `created` date and FONTLOG), added to Google Fonts on 2012-07-11 (per `date_added` in METADATA.pb), and the librefonts mirror was created in October 2014.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The repository contains only:

- **VFB source files** (FontLab binary format, not compatible with gftools-builder):
  - `src/EagleLake-Regular.vfb` -- original source with contour overlaps
  - `src/EagleLake-Regular-OTF.vfb` -- merged contours for OTF
  - `src/EagleLake-Regular-TTF.vfb` -- TrueType outlines with hinting
- **TTX dumps** of the compiled TTF and OTF fonts (both at repo root and in `src/`)
- Standard metadata files (FONTLOG.txt, OFL.txt, METADATA.json, DESCRIPTION.en_us.html)
- A `.travis.yml` for CI testing using the legacy fontbakery-build.py pipeline

Since the source files are `.vfb` (FontLab proprietary binary format), they cannot be used with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No override `config.yaml` can be meaningfully created.

No override `config.yaml` exists in the google/fonts family directory either.

## Verification

- [x] Repository URL is accessible (HTTP 200)
- [x] Repository is clean (no local modifications)
- [x] Single commit in repository: `4e2b264` (2014-10-17)
- [x] Font binary in google/fonts has not changed since initial commit (SHA-256 verified)
- [x] Font version: 1.000 (per name table and head.fontRevision)
- [x] Font created: May 2012 by Brian J. Bonislawsky (Astigmatic)
- [x] Source files are VFB-only -- not compatible with gftools-builder
- [ ] No config.yaml possible (VFB sources only)

## Confidence

**MEDIUM** -- The librefonts mirror is the only known public repository for this font. It contains the original VFB sources but is a community mirror, not the designer's own repository. The commit hash is trivially identified as it is the only commit. However, no gftools-builder configuration can be created because the sources are in FontLab's proprietary VFB format, which is not supported by modern open-source font build tools.

## Notes

- This font was designed by Brian J. Bonislawsky of Astigmatic (AOETI) in 2012.
- The librefonts organization mirrors were created by Mikhail Kashkin (hash3g) circa 2014, decomposing compiled fonts into TTX and storing the original VFB sources.
- The font has never been updated in google/fonts since its initial inclusion.
- To make this font buildable from source, the VFB files would need to be converted to a modern format (e.g., `.glyphs` or `.ufo`), which would require manual intervention or access to FontLab.
- The designer's website (http://www.astigmatic.com/) is referenced in the font's name table.
