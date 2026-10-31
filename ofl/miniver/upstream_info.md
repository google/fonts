# Miniver — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Miniver are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/miniver/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `Miniver-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Only one design source is present: a FontLab VFB file (63 KB) optimized for TTF output. No UFO, Glyphs, SFD, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio) and requires conversion before modern tooling can be used.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting the VFB source to a modern format (UFO or Glyphs).

## Designer & History

- **Designer**: Dathan Boardman (Open Window)
- **Contact**: dathanboardman@gmail.com
- **FONTLOG**: Confirms "Designed by Dathan Boardman of Open Window", matching the copyright in METADATA.pb exactly.

No canonical repository by the designer was found on GitHub.

## Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/miniver
- **Latest commit**: `b301973d6822dc2661ce510355b4d7f9ed573926` (2014-10-17, "update .travis.yml")
- **Default branch**: `master`

The repo has been dormant since October 2014. It contains TTX decompositions of the built font in the root directory and uses an obsolete Travis CI configuration.

## Notes

- The VFB source format is proprietary and requires FontLab Studio or conversion to UFO for modern tooling.
- No evidence of an authoritative repository from the original designer (Open Window / Dathan Boardman) was found on GitHub.
- The `librefonts` organization archived this font as-is; it is unlikely to receive further upstream development.
- Confidence in source identification: High — FONTLOG text, designer name, email, and font name all match the METADATA.pb.
