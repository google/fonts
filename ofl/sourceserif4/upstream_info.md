# Source Serif 4 — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Source Serif 4 was identified as
`adobe-fonts/source-serif` on GitHub. The repository contained UFO source files
on the `main` branch and was actively maintained by Adobe.

## Repository

- **URL**: https://github.com/adobe-fonts/source-serif
- **Branch**: `main`
- **Commit**: `b3980ade53bb3d023a0006076d05349236b309b1`
- **Commit message**: "docs: re-shuffle content"

## Source Format

The `main` branch contained UFO sources in the `Roman/Masters/` and
`Italic/Masters/` directory trees. UFO files were located at paths such as
`Roman/Masters/text/master_0/SourceSerif_0.ufo`. Designspace files were also
present (`Roman/SourceSerif4.designspace`). The `release` branch contained
only compiled font binaries.

## Decision

The `source` block was added to `METADATA.pb` pointing to `adobe-fonts/source-serif`
at commit `b3980ade53bb3d023a0006076d05349236b309b1` on the `main` branch.

## Notes

The designer listed in METADATA.pb is Frank Grießhammer. Source Serif 4 is an
open-source serif typeface family created by Adobe, designed as a companion to
Source Sans. It supports Latin, Cyrillic, and Greek scripts and is available
as a variable font with `opsz` and `wght` axes. The typeface is licensed under
the SIL Open Font License.
