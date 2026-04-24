**Model**: Claude Opus 4.6

# Sulphur Point — Upstream Source Investigation

## Summary

The canonical upstream repository for Sulphur Point was identified at `https://github.com/noponies/sulphur-point`, maintained by Dale Sattler. The repository contained a Glyphs source file (`sources/sulphur-point.glyphs`) along with documentation, fonts, and assets directories.

## Repository Details

- **Repository**: https://github.com/noponies/sulphur-point
- **Owner**: noponies (Dale Sattler)
- **License**: OFL
- **Source format**: Glyphs (.glyphs)
- **Latest commit**: `2c1a600846ca8b7890a89076aeeb2d43cdaeac23`
- **Commit message**: "S character adjustments — Minor fixes to the lower case s"
- **Commit date**: 2019-11-17

## Source Files

The `sources/` directory contained:
- `sulphur-point.glyphs`

## Confidence

**High** — The repository URL matched the copyright notice in the font files (`Copyright 2019 The Sulphur Point Project Authors (https://github.com/noponies)`). The designer name (Dale Sattler) matched the METADATA.pb. The Glyphs source file was present and the repository was not a librefonts mirror.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/noponies/sulphur-point` at commit `2c1a600846ca8b7890a89076aeeb2d43cdaeac23`.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sulphurpoint/` referencing the upstream gftools-builder-compatible source at the pinned commit `2c1a600` (`sources/sulphur-point.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
