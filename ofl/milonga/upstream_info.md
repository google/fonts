# Milonga — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Milonga are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/milonga/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `Milonga-Regular.vfb` | FontLab VFB | No (proprietary) |
| `Milonga-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `Milonga-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `Milonga-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Three VFB files are present: the main master (`Milonga-Regular.vfb`, 285 KB), one optimized for OTF output (`-OTF.vfb`, 192 KB), and one optimized for TTF output (`-TTF.vfb`, 259 KB). The `.otf` is a compiled binary, not a design source. No UFO, Glyphs, SFD, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio) and requires conversion before modern tooling can be used.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

## Designer & History

- **Designer**: Pablo Impallari (Impallari Type), with co-designers Brenda Gallo and Rodrigo Fuenzalida
- **Contact**: impallari@gmail.com
- **Font version**: 1.000 — initial release with no subsequent updates
- **Design notes**: A tribute to Rioplatense culture, inspired by the Argentine/Uruguayan "fileteado porteno" painting tradition. Designed for display/headline use.

No dedicated repository under the `impallari` GitHub account was found for Milonga (unlike Miltonian, which has `impallari/Miltonian`). A search for `impallari/Milonga` returns a 404.

## Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/milonga
- **Last commit**: `5cbad6e6871080ea3507db062760135a22522a5e` (2014-10-17, "update .travis.yml")

This is a legacy mirror from 2014 with an obsolete fontbakery-build pipeline. It has not been updated since October 2014.

## Notes

- The VFB source format requires FontLab Studio (proprietary) to edit. No open-source-friendly alternative source (UFO, Glyphs, SFD) is available.
- Consider reaching out via the Impallari Type GitHub account or `impallari@gmail.com` to determine if updated sources exist.
- The `librefonts` organization on GitHub was an early Google Fonts infrastructure project that is no longer active.
