# Metal Mania — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Metal Mania are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/metalmania/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MetalMania-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Only one design source is present: a FontLab VFB file (300 KB) with TrueType outlines and hinting adjustments. No UFO, Glyphs, SFD, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio 5) and requires conversion before modern tooling can be used.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting the VFB source to a modern format (UFO or Glyphs).

## Designer & History

- **Designer**: Dathan Boardman (Open Window)
- **Contact**: dathanboardman@gmail.com
- **Date added to Google Fonts**: 2012-07-11
- **Font version**: 1.002 (August 2012, unchanged since initial release)
- **FONTLOG reference**: A Google+ profile (`https://profiles.google.com/openwindowfonts/about`) that no longer exists (404).

The designer has a GitHub account at https://github.com/dathanboardman but has 0 public repositories. No upstream source is maintained by the original designer; this family should be considered orphaned.

## Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/metalmania
- **Status**: Dormant — last commit 2014-10-17, no activity since
- **Latest commit**: `7f5e5a82` (2014-10-17) — "update .travis.yml"
- **First commit**: `10c6697f` (2014-07-16) — "Move metalmania font files to separate repository"
- **Total commits**: 11

The repo was created and maintained by Mikhail Kashkin (hash3g) as part of the `librefonts` infrastructure, not by the original designer. The root of the repository contains TTX-format table dumps generated from the binary. It uses an obsolete fontbakery-build pipeline and has no issues, PRs, or forks.

## Notes

- The only authoritative source is the VFB FontLab binary, which would need conversion to UFO or Glyphs for any future rebuild.
- The `librefonts` organization on GitHub was an early Google Fonts infrastructure project that is no longer active.
- Confidence in source identification is high — the VFB filename matches the FONTLOG description exactly ("MetalMania-Regular-TTF.vfb TrueType outlines with hinting adjustments corresponding to the TTF file"), and version 1.002 matches.
