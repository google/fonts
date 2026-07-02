# Mervale Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Mervale Script are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/mervalescript/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MervaleScript-Regular.vfb` | FontLab VFB | No (proprietary) |
| `MervaleScript-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MervaleScript-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `MervaleScript-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Three VFB files are present: the main master (`MervaleScript-Regular.vfb`), one with contour overlaps optimized for OTF output (`-OTF.vfb`), and one with hinting adjustments for TTF output (`-TTF.vfb`). No UFO, Glyphs, SFD, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio 4/5) and not editable with modern open-source tooling without conversion.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

## Designer & History

Mervale Script is a single-weight handwriting/script typeface designed by **Brian J. Bonislawsky** and **Jim Lyles** for Astigmatic (AOETI), released in 2012.

- **Contact**: astigma@astigmatic.com
- **Website**: www.astigmatic.com (SSL certificate expired — HTTPS unreachable as of investigation date)
- **Font version**: v1.000 (November 2012). No updates have been made in over 13 years.
- **Glyph coverage**: Latin-1, Latin-2, Turkish, Windows Baltic (per FONTLOG). Supports `latin` and `latin-ext` subsets.
- **Single weight**: Regular (400) only; no variable font or additional weights/styles.

No GitHub organization or user account for "Astigmatic" or "Brian J. Bonislawsky" was found that hosts original font sources. The GitHub user at https://github.com/astigmatic (id 34247703, created 2017-12-04) has only 2 unrelated repositories and is not affiliated with the type foundry.

## Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/mervalescript
- **Type**: Third-party mirror, not an authoritative Astigmatic repository
- **Latest commit**: `31648e2a8d9b3f059379bb37aebb50f0e0b9d465` (2014-10-17)

The mirror contains TTX-exploded font tables and the same VFB source files. It uses an obsolete fontbakery-build pipeline via Travis CI and has been dormant since 2014.

## Notes

- The `.vfb` source files would need conversion via FontLab or `vfb2ufo` to produce UFO sources for modern tooling.
- Contacting Astigmatic directly (astigma@astigmatic.com) to confirm source availability would be the appropriate first step for modernization.
- The `librefonts` organization on GitHub is a community archive of free fonts, not maintained by Astigmatic.
