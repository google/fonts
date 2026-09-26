# Mystery Quest — Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/mysteryquest/src/` |
| **Buildable** | No — VFB only (proprietary format) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (2)

- **.vfb** (FontLab, proprietary format): MysteryQuest-Regular-TTF.vfb
- **Metadata**: METADATA_comments.txt

The only design source is a VFB file, which requires FontLab (proprietary) to open and cannot be built with gftools-builder.

## Build System

Not applicable — no gftools-builder-compatible sources exist.

## Notes

- Font was designed by Sideshow (Font Diner)
- No other public upstream repository has been identified
- Single style: Regular
