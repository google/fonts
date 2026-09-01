# Peralta — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/peralta/src/` |
| **Buildable** | No — legacy format only (.vfb) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **.vfb** (FontLab, proprietary): Peralta-Regular-OTF.vfb, Peralta-Regular-TTF.vfb, Peralta-Regular.vfb
- **Compiled binary** (not a design source): Peralta-Regular.otf

All design sources are VFB (FontLab, proprietary) format files, which are not buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

## Investigation

Designer: Astigmatic (Brian J. Bonislawsky). Script: Latin. Category: SERIF / DISPLAY (slab serif).

No source block was found in METADATA.pb. No canonical upstream GitHub repository was identified.

## Conclusion

No canonical upstream repository was found beyond the legacy googlefontdirectory-hg archive. Sources exist only as VFB files, which are proprietary and not buildable with gftools-builder. No METADATA.pb changes were made.
