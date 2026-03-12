# Metamorphous — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The best available upstream repository is:

- **URL**: https://github.com/librefonts/metamorphous
- **Owner**: librefonts (a GitHub organization that mirrors libre font projects)
- **Status**: Archived / unmaintained — last push was 2014-10-17
- **Latest relevant commit**: `a66876f61b0cbdc917da33bd844a71f9fa94c561` (2014-10-17, "update .travis.yml")
- **First meaningful commit**: `1ae01ae80d66` (2014-07-16, "Move metamorphous font files to separate repository")

No canonical upstream repository under SorkinType or the original designer (James Grieshaber / typeco.com) was found. The SorkinType GitHub organization (https://github.com/SorkinType) has 60+ font repositories but does not include Metamorphous. No repository was found under a `grieshaber` or `typeco` GitHub account either.

The `librefonts/metamorphous` repository appears to be a third-party mirror/archive, not the authoritative source. It was created in July 2014, more than two years after the font's last release (April 2012, v1.002).

## Source Files

The repository contains the following source files under `src/`:

- `Metamorphous-Regular-TTF.sfd` — FontForge SFD source (TTF-flavored), ~730 KB
- `Metamorphous-Regular-OTF.sfd` — FontForge SFD source (OTF-flavored)
- `Metamorphous-Regular.vfb` — original FontLab VFB file
- `Metamorphous-Regular.otf.*` — decomposed TTX files for the OTF
- `VERSIONS.txt` — records version 1.001 for the TTF
- `METADATA_comments.txt`

At the root level, there are also decomposed TTX files for the TTF (`.ttx` per-table files), `FONTLOG.txt`, `OFL.txt`, and `DESCRIPTION.en_us.html`.

The original design was created in FontLab (`.vfb`) and mastered to TTF/OTF by Eben Sorkin. The SFD files in the repository appear to be FontForge conversions of those originals.

## Build System

The repository uses a legacy `fontbakery-build.py` / Travis CI pipeline (circa 2014):

- Build tool: `fontbakery-cli` (old Python 2 era, no longer maintained)
- Additional tools: `fontforge` (Python bindings), `ttfautohint`, `fontTools`, `fontcrunch`
- The `.travis.yml` drives `fontbakery-build.py .` which reads `METADATA.json` and rebuilds from SFD sources

This build system is completely obsolete. There is no `Makefile`, `build.sh`, or other modern build script. The repository has not been updated since 2014 and the toolchain it depends on no longer exists in its original form.

## config.yaml Status

No `config.yaml` exists in this repository or in the Google Fonts directory at `/mnt/shared/google/fonts/ofl/metamorphous/`. A `config.yaml` would need to be created from scratch if this family were to be rebuilt using modern gftools.

## Notes

- The font has only a single weight (Regular 400) and no variable font version.
- The FONTLOG records three release events: v1.000 (Nov 2010, James Grieshaber, FontLab VFB), v1.001 (Dec 2011, Eben Sorkin, mastered to TTF), v1.002 (Apr 2012, Eben Sorkin, added TTFAutohint hinting). No updates have been released since April 2012.
- The current binary in Google Fonts (`Metamorphous-Regular.ttf`) matches v1.002 as described in the FONTLOG.
- There is no evidence of an active maintainer. James Grieshaber's website (typeco.com) is still listed in the FONTLOG but no GitHub presence was found.
- If a rebuild or update is desired, the FontForge SFD sources in `librefonts/metamorphous` are the best available starting point, but they would need significant modernization work (OFL name table cleanup, hinting review, OpenType feature review).
- The `librefonts` organization also hosts mirrors for other libre fonts and appears to have been set up as a CI experiment around 2014.
