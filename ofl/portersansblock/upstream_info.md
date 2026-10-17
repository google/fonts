# Porter Sans Block — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/portersansblock/src/` |
| **Buildable** | No — no design sources present |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

### Source Files

- `PorterSansBlock-Regular.otf` — compiled binary, not a design source
- `METADATA_comments.txt` — metadata comments

No design source files were found — only a compiled OTF binary and metadata comments.

## Notes

Designer: Tyler Finck. Script: Latin. Category: DISPLAY (sans serif stroke).

## Verdict

**No usable source files in googlefontdirectory-hg.** Only a compiled OTF binary is present; no design sources (VFB, SFD, UFO, .glyphs) were included. No gftools-builder config is possible.
