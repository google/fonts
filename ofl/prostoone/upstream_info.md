# Prosto One — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/prostoone/src/` |
| **Buildable** | No — VFB only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

### Source Files

- `ProstoOne-Regular-OTF.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `ProstoOne-Regular-TTF.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `ProstoOne-Regular-kern_classes.flc` — FontLab kerning classes file
- `ProstoOne-Regular-Sketches.ai` — Adobe Illustrator sketch file
- `ProstoOne-Regular.otf` — compiled binary, not a design source
- `METADATA_comments.txt` — metadata comments

Design sources are VFB files (FontLab, proprietary), accompanied by supporting FontLab kerning data and Illustrator sketches.

## Designers

- Jovanny Lemonad (lemonad@jovanny.ru, http://www.jovanny.ru) — original type designer
- Pavel Emelyanov (zakachka2006@mail.ru) — original type designer

## Repository Investigation

- **Checked cache**: No cached entry in the upstream repo cache.
- **GitHub search**: Searches for "Prosto One font", "jovanny lemonad font", and "ProstoOne" returned no relevant results. A GitHub user `jovanny` exists but has only one unrelated repo (`jovanny/repositorio`).
- **jovanny.ru**: The website was unreachable (connection refused) at time of previous investigation.
- **Google Fonts history**: The git log for `ofl/prostoone` in google/fonts showed no upstream commit references.
- **FONTLOG evidence**: The FONTLOG does not reference any source repository.

## Verdict

**No canonical upstream repository found; sources in googlefontdirectory-hg are not buildable.** Only VFB (FontLab) sources exist. No open-format sources are available. No gftools-builder config is possible.
