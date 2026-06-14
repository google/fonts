# Poly — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/poly/src/` |
| **Buildable** | No — VFB and SFD only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

### Source Files

- `Poly-Regular.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `Poly-Italic.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `Poly-Regular-TTF.sfd` — FontForge SFD (open format, not supported by gftools-builder)
- `Poly-Italic-TTF.sfd` — FontForge SFD (open format, not supported by gftools-builder)
- `Poly-Regular.otf` — compiled binary, not a design source
- `Poly-Italic.otf` — compiled binary, not a design source
- `METADATA_comments.txt` — metadata comments

Design sources include VFB and SFD files for both Regular and Italic styles. Neither format is supported by gftools-builder.

## Notes

Designer: Nicolas Silva (Schwarzenberg). Script: Latin. Category: SERIF. Includes Regular and Italic styles.

## Verdict

**Sources found in googlefontdirectory-hg but not buildable.** Neither VFB nor SFD formats are supported by gftools-builder. No config is possible.
