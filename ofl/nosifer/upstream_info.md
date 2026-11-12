# Nosifer — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/nosifer/src/`
- **Buildable**: No — legacy formats only (.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `Nosifer-Regular.sfd` | FontForge SFD source, original outlines (not buildable with gftools-builder) |
| `Nosifer-Regular-TTF.sfd` | FontForge SFD source, TrueType-specific outlines (not buildable with gftools-builder) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

Two SFD files are present — one with original outlines and one with TrueType-specific outlines. Both are FontForge format, not compatible with gftools-builder.

## Designer and Provenance

- **Designer**: Vernon Adams (Typomondo)
- Vernon Adams passed away in 2014. His fonts were transferred to the Google Fonts collection but no living maintainer is known.
- No authoritative upstream from the original designer has been found on GitHub (no active presence under usernames vernonadams, typomondo).
- **Relationship to Nosifer Caps**: Nosifer and Nosifer Caps are separate families sharing the same designer, copyright notice (`Copyright (c) 2011, Typomondo`), and version (001.002).

## Additional Mirror

A third-party mirror exists at https://github.com/librefonts/nosifer (latest commit `ffe4d8c` on 2014-10-17, "update .travis.yml"). It contains the same SFD sources plus TTX table dumps. The `src/VERSIONS.txt` records version 001.002, matching the Google Fonts binary.

## Build System

Not applicable — the SFD sources require FontForge. The original production workflow used the legacy `googlefontdirectory` toolchain (font-optimizer + subset.py scripts).

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- The font binary in google/fonts (`Nosifer-Regular.ttf`, Version 001.002) matches the version in the librefonts mirror's `VERSIONS.txt`.
- The `librefonts` organization appears to have been a Google Fonts-affiliated archiving effort circa 2014 and does not represent active development.
- For future maintenance, the SFD sources are the best available upstream, but would require FontForge conversion and significant QA work to produce updated binaries.
