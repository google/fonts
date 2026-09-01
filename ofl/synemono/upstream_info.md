**Model**: Claude Opus 4.6

# Syne Mono — Upstream Source Investigation

## Summary

The canonical upstream repository for Syne Mono was identified at `https://gitlab.com/bonjour-monde/fonderie/syne-typeface`, maintained by Bonjour Monde and Lucas Descroix. The repository contained Glyphs source files for all Syne variants including `sources/SyneMono.glyphs`.

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

**High** — The repository URL was already present in the copyright notice of the font files (`Copyright 2019 The Syne Project Authors (https://gitlab.com/bonjour-monde/fonderie/syne-typeface)`). The METADATA.pb listed the designers as "Bonjour Monde, Lucas Descroix," matching the repository owner and commit author. The Glyphs source file was present.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://gitlab.com/bonjour-monde/fonderie/syne-typeface` at commit `e536e8f1a8724bf282da74bbae410f91231ce94c`.
