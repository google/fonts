# Sriracha — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

A repository for Sriracha was found at `cadsondemak/sriracha` on GitHub, but
the sources were in FontLab VFB format only. No UFO or Glyphs source files
were present.

## Repository

- **URL**: https://github.com/cadsondemak/sriracha
- **Branch**: `master`

## Source Format

The `sources/` directory of the repository contained only VFB (FontLab
proprietary) files: `Sriracha-Regular.vfb`, `Sriracha-Regular_SS01.vfb`,
and `Sriracha-Regular_SS02.vfb`. No UFO or Glyphs source files were present.

## Decision

No `source` block was added to `METADATA.pb`. Per the investigation policy,
VFB/SFD-only repositories are excluded from consideration.

## Notes

The designer listed in METADATA.pb is Cadson Demak. Sriracha is a Thai and
Latin handwriting font designed by Cadson Demak with additional Latin design
contributions by Pablo Impallari. Cadson Demak is a Thai type foundry with
multiple font families on Google Fonts. The font supports Thai, Latin,
Latin Extended, and Vietnamese character sets.
