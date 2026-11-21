# Tienne — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Tienne was found at https://github.com/googlefonts/Tienne2Font, hosted under the googlefonts organization. The repository contained UFO source files for two weights (Regular and Heavy), as well as legacy SFD and OTF files. Tienne is a serif display typeface designed by Vernon Adams.

## Repository

- **URL**: https://github.com/googlefonts/Tienne2Font
- **Owner**: googlefonts
- **Default branch**: master
- **Commit used**: `e49a4151f9be25337e3873c71b2430f18113fdfc`
- **Source format**: UFO (and legacy SFD/OTF)

## Source Files

The repository root contained:
- `Tienne-Regular.ufo` — UFO source for Regular weight
- `Tienne-Heavy.ufo` — UFO source for Heavy weight
- `Tienne-Regular.sfd` — Legacy FontForge source
- `Tienne-Heavy.sfd` — Legacy FontForge source
- `Tienne-Regular.otf` — Built OTF
- `Tienne-Heavy.otf` — Built OTF
- `Tienne-Regular-kern.fea` — OpenType feature file

## Confidence

High — the repository was hosted under the googlefonts organization and clearly associated with the Tienne family (the designer Vernon Adams passed away; the googlefonts organization was a known archive of his work).
