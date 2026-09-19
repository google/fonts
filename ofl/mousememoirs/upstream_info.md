# Mouse Memoirs — Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/mousememoirs/src/` |
| **Buildable** | No — VFB only (proprietary format) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (5)

- **.vfb** (FontLab, proprietary format): MouseMemoirs-Regular.vfb, MouseMemoirs-Regular-OTF.vfb, MouseMemoirs-Regular-TTF.vfb
- **Compiled binary** (not a design source): MouseMemoirs-Regular.otf
- **Metadata**: METADATA_comments.txt

The only design sources are VFB files, which require FontLab (proprietary) to open and cannot be built with gftools-builder.

## Build System

Not applicable — no gftools-builder-compatible sources exist.

## Notes

- Font was designed by Brian J. Bonislawsky (Astigmatic)
- The family was added to Google Fonts in 2012
- Single style: Regular
- No other public upstream repository has been identified
