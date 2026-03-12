# Nothing You Could Do — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/librefonts/nothingyoucoulddo
- **Status**: Mirror/archive repository. No authoritative upstream repo from Kimberly Geswein has been found on GitHub. The designer has no known GitHub presence. Her official website is https://kimberlygeswein.com (formerly http://kimberlygeswein.com as recorded in the font's name table).
- **Default branch**: master
- **Latest commit**: `545d208b5f9146f60e8b4d0c3b9aaaf94505ed9d` — "update .travis.yml" (2014-10-17)

## Source Files

The `src/` directory of `librefonts/nothingyoucoulddo` contains:

- `NothingYouCouldDo-TTF.sfd` — FontForge source (TrueType-specific outlines)
- `NothingYouCouldDo.vfb` — FontLab Studio source file (original outlines)
- `NothingYouCouldDo.otf.*` — TTX table dumps of an OTF build (C_F_F_ present)
- `VERSIONS.txt` — records `NothingYouCouldDo.ttf: Version 1.005`
- `METADATA_comments.txt` — historical subsetting/build script comments

The presence of both a `.vfb` (FontLab) and a `.sfd` (FontForge TTF) indicates the original design was done in FontLab, with a FontForge conversion for the TrueType production build.

## Build System

No build system is present. The librefonts repo is a 2014-era archive snapshot. The original production workflow used the legacy `googlefontdirectory` toolchain (font-optimizer + subset.py), as evidenced by `METADATA_comments.txt`. No Makefile, Python build scripts, or `gftools` configuration exists.

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/nothingyoucoulddo/`. None is present in the upstream repo either.

## Notes

- The font binary in the google/fonts repo (`NothingYouCouldDo.ttf`, Version 1.005) matches the version in `librefonts/nothingyoucoulddo/src/VERSIONS.txt`.
- The copyright notice references `kimberlygeswein.com` as the designer's URL; as of 2026, this site is still active and lists KG Fonts catalog, but does not include GitHub links or source repositories.
- The librefonts organization appears to have been a Google Fonts-affiliated archiving effort (circa 2014) and does not represent active development.
- The `.vfb` FontLab source is the most authoritative design file available, but FontLab VFB format is proprietary and requires FontLab Studio to open.
- For future maintenance, the VFB source or the SFD conversion in `librefonts/nothingyoucoulddo/src/` are the best available upstream files.
