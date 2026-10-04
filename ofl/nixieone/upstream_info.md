# Nixie One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/nixieone/src/`
- **Buildable**: No — legacy formats only (.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `NixieOne-Regular-TTF.sfd` | FontForge SFD source (not buildable with gftools-builder) |
| `NixieOne-Regular.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The SFD file is the only editable source. It is a FontForge format file, not compatible with gftools-builder.

## Designer and Provenance

- **Designer**: Jovanny Lemonad (`lemonad@jovanny.ru`, jovanny.ru)
- The designer's website `jovanny.ru` is currently unreachable (ECONNREFUSED).
- No official repository maintained by the designer was found on GitHub. Jovanny Lemonad designed several other Google Fonts (e.g., Philosopher, Yeseva One); some have GitHub repos under `alexeiva/` but no Nixie One repo was found.

## Additional Mirror

A third-party mirror exists at https://github.com/librefonts/nixieone (latest commit `14c80bd` on 2014-10-17, "update .travis.yml"). It contains the same SFD source plus TTX decompilations. The `src/VERSIONS.txt` records version 1.004, matching the Google Fonts binary.

## Build System

Not applicable — the SFD source requires FontForge and is not compatible with the modern gftools-builder pipeline.

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- The font in Google Fonts is Version 1.004, matching `VERSIONS.txt` in the librefonts mirror.
- Nixie One is a single-weight family (Regular only); no italic or bold sources exist.
- **Confidence**: Medium-High. The librefonts mirror matches the shipped version exactly; however, it is not a designer-maintained repository.
