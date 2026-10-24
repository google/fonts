# Niconne — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/niconne/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `Niconne-Regular-OTF.vfb` | FontLab VFB source, OTF variant (proprietary, not buildable with gftools) |
| `Niconne-Regular-TTF.sfd` | FontForge SFD source, TTF variant (not buildable with gftools-builder) |
| `Niconne-Regular.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The VFB file is the original design source (FontLab proprietary format). The SFD is a FontForge conversion used for TrueType production. Neither format is compatible with gftools-builder.

## Designer and Provenance

- **Designer**: Vernon Adams (vern@newtypography.co.uk, newtypography.co.uk)
- Vernon Adams passed away in 2014; no active maintainer exists for his font projects.
- No official upstream repository maintained by Vernon Adams was found on GitHub. He does not appear to have had a personal GitHub account with public repositories.

## Additional Mirror

A third-party mirror exists at https://github.com/librefonts/niconne (latest commit `80a93c0` on 2014-10-17, "update .travis.yml"). It contains the same VFB and SFD sources plus TTX decompilations. The `src/VERSIONS.txt` records version 1.002, matching the Google Fonts binary.

The `librefonts` organization on GitHub hosted a collection of Google Fonts source files around 2014 and appears to be the closest thing to a canonical source archive for this family.

## Build System

Not applicable — the VFB source requires FontLab Studio and the SFD source requires FontForge. Neither is compatible with the modern gftools-builder pipeline.

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- The font in Google Fonts is Version 1.002, matching `VERSIONS.txt` in the librefonts mirror.
- The SFD source (`Niconne-Regular-TTF.sfd`) is the most practical source file for rebuilding the TTF, though not via gftools-builder.
- **Confidence**: Medium-High. The librefonts mirror is the best available source and matches the shipped version; however, it is not a designer-maintained repository.
