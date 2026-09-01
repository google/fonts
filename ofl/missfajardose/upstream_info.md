# Miss Fajardose — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Miss Fajardose are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/missfajardose/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MissFajardose-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MissFajardose-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `MissFajardose-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

The VFB file is the OTF production source and the SFD file is the TTF production source. The `.otf` is a compiled binary, not a design source. No UFO, Glyphs, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary and the SFD format is not supported by gftools-builder.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

## Designer & History

- **Designer**: Alejandro Paul / Sudtipos (`sudtipos@sudtipos.com`)
- **Copyright**: "Copyright (c) 2004 Alejandro Paul (sudtipos@sudtipos.com), with Reserved Font Name "MissFajardose""
- **Date added to Google Fonts**: 2011-11-30 (very early era, predates most open source font hosting practices)

Miss Fajardose is a legacy handwriting font from 2004, added to Google Fonts in the very early days (2011).

## Searches Conducted

- A `sudtipos` GitHub user or organization — not found (404)
- `MissFajardose` or `fajardose` repositories on GitHub — no results
- An official Sudtipos repository — Sudtipos does not appear to have a public GitHub presence

## Additional Repository

An unofficial archive mirror exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/missfajardose
- **Created**: 2014-07-16 ("Move missfajardose font files to separate repository") by the LibreFonts archiving project
- **Last pushed**: 2014-10-17. Only 11 commits. No stars, no forks.

This is a third-party archive with no connection to the original author, not suitable as an authoritative upstream.

## Notes

- Sudtipos does not appear to have a public GitHub presence. The designer has not published source files through any discoverable public channel.
- The googlefontdirectory-hg monorepo is the only known location of design source files for this family.
- If source files in modern format are desired, direct outreach to `sudtipos@sudtipos.com` would be necessary.
