# Nosifer Caps — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/nosifercaps/src/`
- **Buildable**: No — legacy formats only (.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `NosiferCaps-Regular.sfd` | FontForge SFD source, original outlines (not buildable with gftools-builder) |
| `NosiferCaps-Regular-TTF.sfd` | FontForge SFD source, TrueType-specific outlines (not buildable with gftools-builder) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

Two SFD files are present — one with original outlines and one with TrueType-specific outlines. Both are FontForge format, not compatible with gftools-builder.

## Designer and Provenance

- **Designer**: Vernon Adams (Typomondo)
- Vernon Adams passed away in 2014; no living maintainer is known for these fonts.
- No authoritative upstream from the original designer has been found on GitHub.
- **Relationship to Nosifer**: Nosifer Caps shares the same designer, copyright notice (`Copyright (c) 2011, Typomondo`), and version (001.002) as Nosifer. They are distinct typefaces (caps-only design vs. full display) but share the same origin.

## Additional Mirror

A third-party mirror exists at https://github.com/librefonts/nosifercaps (latest commit `4d06a56` on 2014-10-17, "update .travis.yml"). It contains the same SFD sources plus TTX table dumps. The `src/VERSIONS.txt` records version 001.002, matching the Google Fonts binary. The repo also includes DSIG, GDEF, GPOS, and GSUB table dumps, indicating the caps variant has OpenType feature tables absent from the base Nosifer.

## Build System

Not applicable — the SFD sources require FontForge. The original production workflow used the legacy `googlefontdirectory` toolchain (font-optimizer + subset.py scripts).

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- The font binary in google/fonts (`NosiferCaps-Regular.ttf`, Version 001.002) matches the version in the librefonts mirror's `VERSIONS.txt`.
- The `librefonts` organization appears to have been a Google Fonts-affiliated archiving effort circa 2014 and does not represent active development.
- See also: Nosifer investigation for additional context on the designer and provenance.
