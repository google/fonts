# Play — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/play/src/` |
| **Buildable** | No — legacy format only (.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **.sfd** (FontForge): Play-Regular-TTF.sfd, Play-Bold-TTF.sfd
- **Metadata**: METADATA_comments.txt

The only design sources are SFD files (FontForge format), which are not buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

## Investigation

Designer: Jonas Hecksher (e-types / Playtypes). Script: Latin, Cyrillic, Greek, Vietnamese. Category: SANS_SERIF / DISPLAY. Includes Regular and Bold weights.

No source block was found in METADATA.pb. No canonical upstream GitHub repository was identified.

## Conclusion

No canonical upstream repository was found beyond the legacy googlefontdirectory-hg archive. Sources exist only as SFD files, which are not buildable with gftools-builder. No METADATA.pb changes were made.
