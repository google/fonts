# Patrick Hand — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/patrickhand/src/` |
| **Buildable** | No — legacy format only (.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **.sfd** (FontForge): PatrickHand-Regular-TTF.sfd, PatrickHand-Regular_prettfautohint.sfd
- **Compiled binaries** (not design sources): PatrickHand-Regular.otf, PatrickHand-Regular_prettfautohint.ttf
- **Metadata**: METADATA_comments.txt

The only design sources are SFD files (FontForge format), which are not buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

## Investigation

The METADATA.pb listed the designer as Patrick Wagesreiter with copyright dated 2010-2012.

The DESCRIPTION.en_us.html described the font as based on the designer's own handwriting, supporting Latin and Latin extended characters plus Vietnamese. No upstream repository link was present.

Web searches were conducted for Patrick Wagesreiter on GitHub, for a repository named PatrickHand, and for any organization or user matching the designer. The only Patrick Hand-related repository found was `m4rc1e/PatrickHandSC`, attributed to Marc Foley, a Google Fonts developer and font engineer — not the original designer. This covers the SC variant and is an engineering preparation repo, not a canonical designer-owned upstream.

No designer-owned repository was found for either Patrick Hand or Patrick Hand SC.

## Conclusion

No canonical designer-owned upstream repository was found. The `m4rc1e/PatrickHandSC` repo is a Google Fonts engineering repository for the SC variant only. The legacy googlefontdirectory-hg archive contains only SFD sources, which are not buildable with gftools-builder. No METADATA.pb changes were made.
