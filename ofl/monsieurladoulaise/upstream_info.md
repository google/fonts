# Monsieur La Doulaise — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Monsieur La Doulaise are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/monsieurladoulaise/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MonsieurLaDoulaise-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MonsieurLaDoulaise-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `MonsieurLaDoulaise-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

The VFB file is the OTF production source and the SFD file is the TTF production source. The `.otf` is a compiled binary, not a design source. No UFO, Glyphs, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary and the SFD format is not supported by gftools-builder.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

## Designer & History

- **Designer**: Alejandro Paul / Sudtipos (`sudtipos@sudtipos.com`)
- **Original design**: 2006
- **Date added to Google Fonts**: 2011

The font was added to Google Fonts in the early era. Sudtipos does not appear to have a public GitHub presence for font sources.

## Notes

- The googlefontdirectory-hg monorepo is the only known location of design source files for this family.
- If modernized sources are desired, direct outreach to `sudtipos@sudtipos.com` would be necessary.
