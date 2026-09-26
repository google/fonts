# Mrs Sheppards — Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/mrssheppards/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (4)

- **.vfb** (FontLab, proprietary format): MrsSheppards-Regular-OTF.vfb
- **.sfd** (FontForge, not supported by gftools-builder): MrsSheppards-Regular-TTF.sfd
- **Compiled binary** (not a design source): MrsSheppards-Regular.otf
- **Metadata**: METADATA_comments.txt

The design sources are a VFB (proprietary) and an SFD (FontForge). Neither format is supported by gftools-builder.

## Build System

Not applicable — no gftools-builder-compatible sources exist.

## Notes

- Font was designed by Sudtipos
- No other public upstream repository has been identified
- Single style: Regular
