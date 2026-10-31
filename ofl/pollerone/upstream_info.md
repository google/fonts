# Poller One — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/pollerone/src/` |
| **Buildable** | No — VFB and SFD only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

### Source Files

- `PollerOne.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `PollerOne-TTF.sfd` — FontForge SFD (open format, not supported by gftools-builder)
- `PollerOne.otf` — compiled binary, not a design source
- `METADATA_comments.txt` — metadata comments

Design sources include a VFB (proprietary) and an SFD (open but not supported by gftools-builder).

## Notes

Designer: Yvonne Schuttler. Script: Latin. Category: DISPLAY (sans serif stroke). Published by Sorkin Type Co.

## Verdict

**Sources found in googlefontdirectory-hg but not buildable.** Neither VFB nor SFD formats are supported by gftools-builder. No config is possible.
