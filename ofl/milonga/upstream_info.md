# Milonga — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The upstream source repository is hosted on GitHub by the librefonts organization:

- **URL**: https://github.com/librefonts/milonga
- **Type**: Non-fork repository
- **Last commit**: `5cbad6e6871080ea3507db062760135a22522a5e` (2014-10-17, "update .travis.yml")

No dedicated repository under the `impallari` GitHub account was found for Milonga (unlike Miltonian, which has `impallari/Miltonian`). A search for `impallari/Milonga` returns a 404. The `librefonts/milonga` repository is the best-known upstream source.

The designer is **Pablo Impallari** (Impallari Type), with co-designers Brenda Gallo and Rodrigo Fuenzalida per the copyright notice.

## Source Files

In the `librefonts/milonga` repository, source files are under `src/`:

- `src/Milonga-Regular.vfb` — FontLab Studio source file (285 KB, main master)
- `src/Milonga-Regular-OTF.vfb` — FontLab source optimized for OTF output (192 KB)
- `src/Milonga-Regular-TTF.vfb` — FontLab source optimized for TTF output (259 KB)
- `src/Milonga-Regular.otf.*.ttx` — ttx table dumps of the OTF build
- `src/VERSIONS.txt` — notes version as `Milonga-Regular.ttf: Version 1.000; ttfautohint (v0.93)`
- `src/METADATA_comments.txt` — metadata notes

The `.vfb` files (FontLab Studio native format) are the canonical source. The repo root also contains a full set of `.ttx` table dumps and the compiled `Milonga-Regular.ttf`.

## Build System

The `librefonts/milonga` repo uses a legacy `fontbakery-build.py` CI pipeline via `.travis.yml`, driven by FontForge + ttfautohint. This build system is obsolete (Travis CI is no longer free; fontbakery-cli as used here is a very old version).

No modern build system (e.g., gftools builder, fontmake) is present.

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/milonga/`. None exists in the upstream repository.

## Notes

- The `librefonts/milonga` repo has not been updated since October 2014 and predates the current Google Fonts source workflow.
- The `.vfb` source format requires FontLab Studio (proprietary) to edit. No open-source-friendly alternative source (e.g., UFO, Glyphs, `.sfd`) is available.
- Milonga is version 1.000 — appears to be an initial release with no subsequent updates in the known repos.
- The font was designed as a tribute to Rioplatense culture, inspired by the Argentine/Uruguayan "fileteado porteño" painting tradition. It is useful for display/headline use.
- A config.yaml would need to be authored from scratch for any future Google Fonts rebuild.
- Consider reaching out via the Impallari Type GitHub account or the contact listed in the copyright string (`impallari@gmail.com`) to determine if updated sources exist.
