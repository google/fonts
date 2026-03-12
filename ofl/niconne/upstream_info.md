# Niconne — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The best available upstream source for Niconne is the **librefonts** organization mirror on GitHub:

- **Repository**: https://github.com/librefonts/niconne
- **Designer**: Vernon Adams (vern@newtypography.co.uk)
- **Default branch**: master
- **Latest commit**: `80a93c0d8fd4a56727ce0dada12b2d6accf7e2bc` (2014-10-17), message: "update .travis.yml"
- **Last pushed**: 2014-10-17

No official upstream repository maintained by Vernon Adams himself was found on GitHub. Vernon Adams was active in the Google Fonts ecosystem (email: vern@newtypography.co.uk, website: newtypography.co.uk) but does not appear to have a personal GitHub account with public repositories. The `librefonts` organization on GitHub hosted a collection of Google Fonts source files around 2014, and this appears to be the closest thing to a canonical source repo for Niconne.

## Source Files

The `librefonts/niconne` repository contains the following source files under `src/`:

| File | Type |
|------|------|
| `src/Niconne-Regular-OTF.vfb` | FontLab Studio source (OTF workflow) |
| `src/Niconne-Regular-TTF.sfd` | FontForge source (TTF workflow, ~825 KB) |
| `src/Niconne-Regular.otf.*` + `.ttx` | TTX table dumps |
| `src/VERSIONS.txt` | Records version 1.002 |

The font in Google Fonts is Version 1.002 (confirmed from binary name table), which matches the version recorded in `src/VERSIONS.txt`.

The root of the repository also contains the full TTX decomposition of the TTF (`Niconne-Regular.ttf.*.ttx`) in addition to the OTF TTX dumps in `src/`.

## Build System

No Makefile, build script, or automated build system is present in the repository. The `.travis.yml` file exists (last touched in the final commit) but its content was not retrieved. Given the era (2014) and that the source is a single-weight `.vfb`/`.sfd`, the build process was almost certainly a manual FontLab/FontForge export workflow.

## config.yaml Status

No `config.yaml` exists. One could be written targeting the `librefonts/niconne` repository, but given the repository has been unmaintained since 2014 and Vernon Adams is deceased (passed away ~2014), the font is unlikely to receive upstream updates.

## Notes

- Vernon Adams passed away in 2014; no active maintainer exists for his font projects.
- The `librefonts` organization appears to be a semi-official archive of Google Fonts sources from that era, possibly maintained by the Google Fonts team at the time.
- The SFD source (`Niconne-Regular-TTF.sfd`) is the most practical source file for rebuilding the TTF.
- The version in Google Fonts (1.002) matches the librefonts mirror — the repo reflects exactly what is shipped.
- **Confidence**: Medium-High. The librefonts mirror is the best available source and matches the shipped version; however, it is not an "official" designer-maintained repo.
