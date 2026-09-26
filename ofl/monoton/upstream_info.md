# Monoton — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Monoton are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/monoton/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `Monoton-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Only one design source is present: a FontForge SFD file for TTF production. The SFD format is not supported by gftools-builder. No UFO, Glyphs, VFB, or other sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The SFD format is not compatible with gftools-builder.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting the SFD source to a modern format (UFO or Glyphs).

## Designer & History

- **Designer**: Vernon Adams
- **Date added to Google Fonts**: 2011

The font was added to Google Fonts in the early era before open source font hosting on GitHub was common practice.

## Notes

- The googlefontdirectory-hg monorepo is the only known location of design source files for this family.
- The SFD source could potentially be converted to UFO using FontForge for future modernization.
