# Press Start 2P — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/pressstart2p/src/` |
| **Buildable** | No — BDF bitmap source only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

### Source Files

- `PressStart2P-8.bdf` — BDF bitmap font source (not buildable with gftools-builder)
- `METADATA_comments.txt` — metadata comments

The only source is a BDF (Bitmap Distribution Format) file. BDF is a bitmap font format and is not buildable with gftools-builder, which expects outline font sources.

## Notes

Designer: CodeMan38 (Cody Boisclair, cody@zone38.net). Script: Latin, Cyrillic, Greek. Category: DISPLAY. Pixel/retro gaming aesthetic.

## Verdict

**Source found in googlefontdirectory-hg but not buildable.** Only a BDF bitmap source exists; no outline-based design sources are available. No gftools-builder config is possible.
