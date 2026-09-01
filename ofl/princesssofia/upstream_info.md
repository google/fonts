# Princess Sofia — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/princesssofia/src/` |
| **Buildable** | No — VFB only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

### Source Files

- `PrincessSofia-Regular-TTF.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `METADATA_comments.txt` — metadata comments

Only a single VFB (FontLab, proprietary) source file is present.

## Designer

Crystal Kluge of Tart Workshop (a DBA of Font Diner, Inc). Contact: support@fontdiner.com. The copyright notice in METADATA.pb names "Font Diner, Inc DBA Tart Workshop."

## Repository Investigation

- **Checked cache**: No cached entry in the upstream repo cache.
- **GitHub search**: Searches for "fontdiner", "tart workshop font", and "Princess Sofia font" returned no results pointing to a designer-owned repository.
- **Astigmatic / Font Diner presence**: Font Diner (fontdiner.com) does not appear to maintain a public GitHub organization or user account with font source repositories.
- **FONTLOG evidence**: The FONTLOG lists one source file: `PrincessSofia-Regular-TTF.vfb` — a FontLab VFB file. No open source repository is referenced.

## Verdict

**No canonical upstream repository found; source in googlefontdirectory-hg is not buildable.** Only a VFB (FontLab) source exists. No open-format sources are available. No gftools-builder config is possible.
