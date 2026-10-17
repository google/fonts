# Poetsen One — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/poetsenone/src/` |
| **Buildable** | No — VFB only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

### Source Files

- `PoetsenOne-Regular.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `PoetsenOne-Regular-OTF.vfb` — FontLab VFB (OTF generation variant)
- `PoetsenOne-Regular-TTF.vfb` — FontLab VFB (TTF generation variant)
- `PoetsenOne-Regular.otf` — compiled binary, not a design source
- `METADATA_comments.txt` — metadata comments

All design sources are in VFB format (FontLab proprietary). No open-format sources (UFO, .glyphs, .sfd) are available.

## Notes

Designer: Rodrigo Fuenzalida, Pablo Impallari. Script: Latin. Category: DISPLAY (sans serif stroke).

## Verdict

**Sources found in googlefontdirectory-hg but not buildable.** Only VFB (FontLab) sources exist. No gftools-builder config is possible.
