# Phetsarath — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/phetsarath/src/` |
| **Buildable** | No — no design sources present (compiled TTF binaries only) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source files

- **Compiled binaries** (not design sources): Phetsarath-Regular_hinted.ttf, Phetsarath-Bold-unhinted.ttf

The googlefontdirectory-hg archive contains only compiled TTF binaries for this family. No design sources (VFB, SFD, .glyphs, .ufo, or .designspace) are present. These files cannot be used for reproducible builds.

## Investigation

Designer: Danh Hong. Script: Lao (Laoo). Category: SANS_SERIF. Published by the Ministry of Posts and Telecommunications, Laos. Includes Regular and Bold weights.

No source block was found in METADATA.pb. No canonical upstream GitHub repository was identified.

## Conclusion

No canonical upstream repository was found beyond the legacy googlefontdirectory-hg archive. The archive contains only compiled TTF binaries, with no design sources available. No METADATA.pb changes were made.
