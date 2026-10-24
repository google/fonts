# New Rocker — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/newrocker/src/`
- **Buildable**: No — legacy formats only (.vfb)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `NewRocker-Regular-OTF.vfb` | FontLab VFB source, OTF variant (proprietary, not buildable with gftools) |
| `NewRocker-Regular-TTF.vfb` | FontLab VFB source, TTF variant (proprietary, not buildable with gftools) |
| `NewRocker-Regular.vfb` | FontLab VFB source (proprietary, not buildable with gftools) |
| `NewRocker-Regular.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

All three VFB files are FontLab Studio 5 proprietary format sources. No gftools-builder compatible sources (UFO, Glyphs, designspace) are available.

## Designer and Provenance

- **Designer**: Pablo Impallari, Brenda Gallo, and Rodrigo Fuenzalida (Impallari Type), v1.0 released 28 November 2012
- The `impallari` GitHub account has 26 repositories but none named `New-Rocker`, `NewRocker`, or similar
- The designer website `impallari.com` and the project page `impallari.com/projects/overview/newrocker` are currently unreachable (HTTP 523)

## Additional Mirror

A third-party mirror exists at https://github.com/librefonts/newrocker (latest commit `1dae287` on 2014-10-17, "update .travis.yml"). It contains the same VFB sources plus TTX decompilations. The repo includes a legacy fontbakery-era `.travis.yml`, `config.yaml`, and `Makefile`, all using the deprecated `fontbakery-build.py` workflow which is not compatible with modern gftools builds.

## Build System

Not applicable — only VFB sources exist, which require FontLab Studio.

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- The Google Fonts binary dates to 2012 (v1.0) and has never been updated.
- The FONTLOG references `http://www.impallari.com/projects/overview/newrocker` as the project page, which is currently unreachable.
- A modern rebuild would require converting the VFB files (e.g., via FontLab or vfb2ufo) to produce gftools-compatible sources.
