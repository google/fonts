# Tillana — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Tillana was found at https://github.com/itfoundry/tillana, hosted under the itfoundry GitHub organization (Indian Type Foundry). The repository contained both a Glyphs source file and UFO masters. Tillana is a Devanagari display typeface designed by Indian Type Foundry.

## Repository

- **URL**: https://github.com/itfoundry/tillana
- **Owner**: itfoundry (Indian Type Foundry)
- **Default branch**: master
- **Commit used**: `7fccbe20b93ad8bcb3c7d7bee3afec03799bf5f6`
- **Source format**: Glyphs + UFO

## Source Files

The `masters/` directory contained:
- `Tillana.glyphs` — Glyphs source file
- `Tillana_0.ufo` — UFO master (light end)
- `Tillana_1.ufo` — UFO master (heavy end)
- `instances` — Instances configuration

Additional files in the repository root included build scripts (build.py), OpenType feature files, and configuration files typical of ITF's build process.

## Confidence

High — the repository was hosted under the official Indian Type Foundry GitHub organization, matching the designer credited in METADATA.pb.
