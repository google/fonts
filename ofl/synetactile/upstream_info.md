**Model**: Claude Opus 4.6

# Syne Tactile — Upstream Source Investigation

## Summary

The canonical upstream repository for Syne Tactile was identified at `https://gitlab.com/bonjour-monde/fonderie/syne-typeface`, the same repository as Syne and Syne Mono, maintained by Bonjour Monde and Lucas Descroix. The repository contained a dedicated Glyphs source file `sources/SyneTactile.glyphs`.

## Repository Details

- **Repository**: https://gitlab.com/bonjour-monde/fonderie/syne-typeface
- **Platform**: GitLab
- **Owner**: bonjour-monde / fonderie
- **License**: OFL
- **Source format**: Glyphs (.glyphs)
- **Latest commit**: `e536e8f1a8724bf282da74bbae410f91231ce94c`
- **Commit message**: "Update README.md"
- **Commit author**: Lucas Descroix
- **Commit date**: 2022-03-03
- **Description**: "Type family originally designed for Synesthésie art center (Saint-Denis, Fr)"

## Source Files

The `sources/` directory contained:
- `Syne.glyphs`
- `SyneMono.glyphs`
- `SyneTactile.glyphs`
- `build.sh`
- `v-1.200/` (historical subdirectory)

## Confidence

**High** — The repository URL was already present in the copyright notice of the font files (`Copyright 2019 The Syne Project Authors (https://gitlab.com/bonjour-monde/fonderie/syne-typeface)`). The METADATA.pb listed the designers as "Bonjour Monde, Lucas Descroix," matching the repository owner and commit author. A dedicated Glyphs source file for Syne Tactile was present.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://gitlab.com/bonjour-monde/fonderie/syne-typeface` at commit `e536e8f1a8724bf282da74bbae410f91231ce94c`.
