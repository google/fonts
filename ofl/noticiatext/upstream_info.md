# Noticia Text — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/jmsole/noticiatext
- **Status**: Authoritative upstream repository, maintained by the original designer José Miguel Solé (JM Solé).
- **Default branch**: master
- **Latest commit**: `bcc80c5a33855419251ac3b9d1fa08d42d52f3ef` — "Initial commit and repository setup." (2016-09-28)
- **Repository description**: "Main repository for Noticia Text font by JM Solé"

## Source Files

The `source/` directory contains Glyphs source files for all four styles:

- `NoticiaText-Regular.glyphs`
- `NoticiaText-Italic.glyphs`
- `NoticiaText-Bold.glyphs`
- `NoticiaText-BoldItalic.glyphs`

The `source/vfb/` subdirectory also contains the original FontLab VFB sources:

- `NoticiaText-Regular.vfb`
- `NoticiaText-Italic.vfb`
- `NoticiaText-Bold.vfb`
- `NoticiaText-BoldItalic.vfb`

The `extras/` directory at the repo root contains additional assets (exact contents not fully enumerated).

The FONTLOG documents three source file types per style: the original contour-overlap VFB, a merged/OTF-optimized VFB, and a TrueType-hinted VFB. The Glyphs files in `source/` are likely converted from the VFB originals for the 2016 repository setup.

## Build System

No automated build system (Makefile, build scripts, or `gftools` configuration) is present in the repository. The repo contains only source files and a README. The existing production binaries were built using FontLab and manually hinted for Windows rasterization (as described in the FONTLOG).

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/noticiatext/`. None is present in the upstream repo either.

## Notes

- The font binaries in the google/fonts repo (Version 1.003) match the changelog entry "16 December 2011 (v.1.003)" in the FONTLOG, confirming these are the final released versions.
- The jmsole/noticiatext repository was set up in 2016 with only a single commit; there has been no subsequent upstream development.
- The designer's contact: info@jmsole.cl, website: http://jmsole.cl (Chilean type designer).
- The FONTLOG describes an ambitious 18-style family vision (text, condensed, display, sans variants), but only the 4 text styles have been released.
- The Glyphs source format (`.glyphs`) is the most practical entry point for any future maintenance work using modern tooling (`fontmake` + `gftools`).
- A `config.yaml` could be authored to enable a `fontmake`-based build pipeline from the `.glyphs` sources, but this would require QA comparison against the manually hinted existing binaries.
