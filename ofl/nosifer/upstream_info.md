# Nosifer — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/librefonts/nosifer
- **Status**: Mirror/archive repository; no authoritative upstream from the original designer (Vernon Adams / Typomondo) has been found on GitHub. The designer has no active GitHub presence under known usernames (vernonadams, typomondo).
- **Default branch**: master
- **Latest commit**: `ffe4d8c7fee1470f2e5d2fb5008f00db6bc67ed1` — "update .travis.yml" (2014-10-17)
- **Note on nosifercaps**: Nosifer and Nosifer Caps are separate librefonts repos (`librefonts/nosifer` and `librefonts/nosifercaps`) but share the same designer (Vernon Adams / Typomondo) and the same copyright notice. Both use Version 001.002.

## Source Files

The `src/` directory of `librefonts/nosifer` contains:

- `Nosifer-Regular.sfd` — FontForge source (original outlines)
- `Nosifer-Regular-TTF.sfd` — FontForge source (TrueType-specific outlines)
- `VERSIONS.txt` — records `Nosifer-Regular.ttf: Version 001.002`
- `METADATA_comments.txt` — historical subsetting/build script comments

The root-level TTX files (e.g., `Nosifer-Regular.ttf._g_l_y_f.ttx`) are deconstructed table dumps corresponding to the distributed binary, not a canonical build artifact.

## Build System

No build system is present. The librefonts repo is a 2014-era archive snapshot. The original production workflow used the legacy `googlefontdirectory` toolchain (font-optimizer + subset.py scripts), as evidenced by `METADATA_comments.txt`. No Makefile, Python build scripts, or `gftools` configuration exists.

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/nosifer/`. None is present in the upstream repo either.

## Notes

- Vernon Adams passed away in 2014. His fonts were transferred to the Google Fonts collection but no living maintainer is known to manage the upstream source.
- The font binary in the google/fonts repo (`Nosifer-Regular.ttf`, Version 001.002) matches the version recorded in `librefonts/nosifer/src/VERSIONS.txt`, confirming this is the same release.
- The librefonts organization appears to have been a Google Fonts-affiliated archiving effort (circa 2014) and does not represent active development.
- For future maintenance, the SFD sources in `librefonts/nosifer/src/` are the best available upstream, but they would require significant QA work (FontForge conversion, hinting review) to produce an updated binary.
- A potential canonical source might exist in the old Google Fonts Directory (pre-GitHub migration), but no public access exists to confirm.
