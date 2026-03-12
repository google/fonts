# Source Sans 3 — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Source Sans 3 was identified as
`adobe-fonts/source-sans` on GitHub. The repository contains UFO source files
on the `main` branch and is actively maintained by Adobe.

## Repository

- **URL**: https://github.com/adobe-fonts/source-sans
- **Branch**: `main`
- **Commit**: `272b22b02e097e8eff1372111f88b5ab6063499f`
- **Commit message**: "Update index.html"

## Source Format

The `main` branch contained UFO sources in the `Upright/Poles/` and
`Italic/Poles/` directories. The upright UFOs were located at paths such as
`Upright/Poles/pole_0/SourceSans3-ExtraLight.ufo`. Designspace files were also
present (`Upright/SourceSans3-Upright.designspace`). The `release` branch
contained only compiled font binaries.

## Decision

The `source` block was added to `METADATA.pb` pointing to `adobe-fonts/source-sans`
at commit `272b22b02e097e8eff1372111f88b5ab6063499f` on the `main` branch.

## Notes

The designer listed in METADATA.pb is Paul D. Hunt. Source Sans 3 (formerly
Source Sans Pro) is an open-source sans-serif typeface family created by Adobe.
It was the first open-source typeface family published by Adobe and is licensed
under the SIL Open Font License.
