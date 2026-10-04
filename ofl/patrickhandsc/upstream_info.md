# Patrick Hand SC — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/patrickhandsc/src/` |
| **Buildable** | No — legacy format only (.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **.sfd** (FontForge): PatrickHandSC-Regular_prettfautohint.sfd
- **Compiled binaries** (not design sources): PatrickHandSC-Regular.otf, PatrickHandSC-Regular_prettfautohint.ttf
- **Metadata**: METADATA_comments.txt

The only design source is an SFD file (FontForge format), which is not buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

## Investigation

The METADATA.pb listed the designer as Patrick Wagesreiter with copyright dated 2012 ("The Patrick Hand Authors").

The DESCRIPTION.en_us.html described Patrick Hand SC as the Small Caps sister family to Patrick Hand, with a 2019-03 update reference noting "Updated to latest upstream release, fixing 'fi' ligature."

The only GitHub repository found for Patrick Hand SC is `github.com/m4rc1e/PatrickHandSC`, maintained by Marc Foley (a Google Fonts engineer), not the original designer Patrick Wagesreiter. This repository is an engineering preparation repo for Google Fonts, not a canonical designer-owned upstream. Its latest commit was dated 2019-02-11 (SHA `9b973bc50d7ad26fd2d2b26725a457fdeef11d3e`), consistent with the 2019-03 update mentioned in the DESCRIPTION.

The Patrick Hand investigation (conducted in parallel) also found no designer-owned repository for either family variant.

## Conclusion

No canonical designer-owned upstream repository was found. The `m4rc1e/PatrickHandSC` repo is a Google Fonts engineering repository, not the original designer's upstream. The legacy googlefontdirectory-hg archive contains only SFD sources, which are not buildable with gftools-builder. No METADATA.pb changes were made.
