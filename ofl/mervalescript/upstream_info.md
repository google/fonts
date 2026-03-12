# Mervale Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Mervale Script is a single-weight handwriting/script typeface designed by Brian J. Bonislawsky and Jim Lyles for Astigmatic (AOETI), released in 2012. No official upstream source repository maintained by Astigmatic could be found. The only GitHub presence is a community mirror under the `librefonts` organization, which is not authoritative.

## Repository

| Field | Value |
|-------|-------|
| Official upstream | Not found |
| Community mirror | https://github.com/librefonts/mervalescript |
| Mirror type | Part of the `librefonts` organization (861 repos; community archive of free fonts, not maintained by Astigmatic) |
| Latest commit (mirror) | `31648e2a8d9b3f059379bb37aebb50f0e0b9d465` (2014-10-17) |
| Designer contact | astigma@astigmatic.com |
| Designer website | www.astigmatic.com (SSL certificate expired — HTTPS unreachable as of investigation date) |

The `librefonts/mervalescript` repo contains TTX-exploded font tables and the original `.vfb` source files, but it is a third-party mirror, not an authoritative Astigmatic repository. No GitHub organization or user account for "Astigmatic" or "Brian J. Bonislawsky" was found that hosts original font sources for this family.

The GitHub user at https://github.com/astigmatic (id 34247703, created 2017-12-04) has only 2 unrelated repositories (an Android test project and a placeholder README) and is not affiliated with the type foundry.

## Source Files

The `.vfb` (FontLab Studio) source files are present in the community mirror's `src/` directory:

| File | Description |
|------|-------------|
| `MervaleScript-Regular.vfb` | Original master source with contour overlaps |
| `MervaleScript-Regular-TTF.vfb` | TrueType variant with hinting adjustments |
| `MervaleScript-Regular-OTF.vfb` | Merged/optimized variant for OTF output |

The `.vfb` format is a proprietary FontLab Studio binary format (FontLab 4/5 era). These files are not readily editable with modern open-source tooling (FontForge, fontmake, etc.) without conversion.

No UFO, Glyphs, or other open-source-friendly source formats were found.

## Build System

The community mirror includes a `.travis.yml` CI configuration using the legacy `fontbakery-build.py` workflow (circa 2014):

- **Tool**: `fontbakery-build.py` (deprecated legacy fontbakery CLI)
- **Dependencies**: FontForge (Python bindings), ttfautohint, fontTools, fontcrunch
- **Build command**: `fontbakery-build.py .`

This build system is entirely obsolete and non-functional with current tooling. There is no `Makefile`, no `fontmake` configuration, and no modern build scripts. The font was likely compiled directly from FontLab by the designer and the binary TTF committed.

## config.yaml Status

No `config.yaml` exists in either:
- `/mnt/shared/google/fonts/ofl/mervalescript/`
- `/mnt/shared/gfonts/ofl/mervalescript/`

The font has never been onboarded with the modern gftools/fontmake build pipeline.

## Notes

- **Font version**: Only one version exists — v1.000 (November 2012). No updates have been made in over 13 years.
- **Glyph coverage**: Latin-1, Latin-2, Turkish, Windows Baltic (per FONTLOG). Supports `latin` and `latin-ext` subsets.
- **Single weight**: Regular (400) only; no variable font or additional weights/styles.
- **Source availability**: The `.vfb` source files are available in the community mirror but are in a proprietary binary format. Recovery/conversion to a modern open format (UFO) would require FontLab or a `.vfb`-capable converter.
- **Upstream activity**: No upstream development activity has been detected. The font appears to be unmaintained.
- **Recommended action**: If modernization is desired, the `.vfb` sources from the community mirror could be opened in FontLab or converted using `vfb2ufo` to produce UFO sources. A `config.yaml` and proper build pipeline would need to be created from scratch. Contacting Astigmatic directly (astigma@astigmatic.com) to confirm source availability and interest in updating would be the appropriate first step.
