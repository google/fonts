# Nosifer Caps — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/librefonts/nosifercaps
- **Status**: Mirror/archive repository; no authoritative upstream from the original designer (Vernon Adams / Typomondo) has been found on GitHub.
- **Default branch**: master
- **Latest commit**: `4d06a566155423ccc76fa04f2929cb17bead6050` — "update .travis.yml" (2014-10-17)
- **Relationship to Nosifer**: Nosifer Caps shares the same designer, copyright notice (`Copyright (c) 2011, Typomondo`), and version (001.002) as Nosifer. Both reside in the `librefonts` GitHub organization as parallel archive repos. They are distinct typefaces (caps-only design vs. full display) but share the same origin.

## Source Files

The `src/` directory of `librefonts/nosifercaps` contains:

- `NosiferCaps-Regular.sfd` — FontForge source (original outlines)
- `NosiferCaps-Regular-TTF.sfd` — FontForge source (TrueType-specific outlines)
- `VERSIONS.txt` — records `NosiferCaps-Regular.ttf: Version 001.002`
- `METADATA_comments.txt` — historical subsetting/build script comments

Root-level TTX files are deconstructed table dumps of the distributed binary, not canonical build artifacts. The repo also includes DSIG, GDEF, GPOS, and GSUB table dumps, indicating the caps variant has OpenType feature tables absent from the base Nosifer.

## Build System

No build system is present. The librefonts repo is a 2014-era archive snapshot. The original production workflow used the legacy `googlefontdirectory` toolchain (font-optimizer + subset.py scripts). No Makefile, Python build scripts, or `gftools` configuration exists.

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/nosifercaps/`. None is present in the upstream repo either.

## Notes

- Vernon Adams passed away in 2014. No living maintainer is known for these fonts.
- The font binary in the google/fonts repo (`NosiferCaps-Regular.ttf`, Version 001.002) matches the version in `librefonts/nosifercaps/src/VERSIONS.txt`.
- The librefonts organization appears to have been a Google Fonts-affiliated archiving effort (circa 2014) and does not represent active development.
- For future maintenance, the SFD sources in `librefonts/nosifercaps/src/` are the best available upstream.
- See also: Nosifer investigation at `/mnt/shared/google/fonts/ofl/nosifer/upstream_info.md` for additional context on the designer and provenance.
