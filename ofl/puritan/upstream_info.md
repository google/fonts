# Puritan — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `puritan/src/`

## Source Files

The `puritan/src/` directory contains design sources in SFD (FontForge) format only, which cannot be built with gftools-builder:

- **SFD** (FontForge, not buildable with gftools-builder): Puritan-Bold.sfd, Puritan-BoldItalic.sfd, Puritan-Italic.sfd, Puritan-Regular.sfd
- **OTF** (compiled binaries, not design sources): Puritan-Bold.otf, Puritan-BoldItalic.otf, Puritan-Italic.otf, Puritan-Regular.otf
- **Other**: ben_weiner.jpg, ben_weiner.tif, generate.py

## Buildability

Not buildable with gftools-builder. The SFD sources are in FontForge format, which is not supported by the gftools-builder pipeline. Conversion to UFO or Glyphs format would be required.

## Designer

Ben Weiner (ben@readingtype.org.uk, http://www.readingtype.org.uk). The font was originally drawn as a student project at the University of Reading, UK, first released in 2001.

## Investigation Details

- **Checked cache**: the upstream repo cache — no cached entry.
- **GitHub search**: Searches for "Puritan font OFL", "Ben Weiner font", and "puritan font readingtype" returned no relevant results.
- **readingtype.org.uk**: The website was checked but contained no GitHub or repository links for the Puritan font.
- **Dave Crossland**: The FONTLOG notes that Dave Crossland made minor contributions in November 2010 (adding yacute, build script, metadata cleanup), but no repository link was provided.
- **FONTLOG evidence**: The FONTLOG describes conversion of source files from Macromedia Fontographer format to FontForge SFD ASCII text files (version 2.0a, March 2007). No repository URL is mentioned.
