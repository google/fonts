**Model**: Claude Opus 4.6

# Sumana — Upstream Source Investigation

## Summary

The canonical upstream repository for Sumana was identified at `https://github.com/cyrealtype/Sumana`, maintained by Cyreal. The repository contained both UFO source directories and a Glyphs source file.

## Repository Details

- **Repository**: https://github.com/cyrealtype/Sumana
- **Owner**: cyrealtype (Cyreal)
- **License**: OFL
- **Source format**: Glyphs (.glyphs) and UFO
- **Latest commit**: `68c5ce43ae96268ac93ee3b79c720c7f479c5ee1`
- **Commit message**: "fixes #5"
- **Default branch**: main

## Source Files

The `sources/` directory contained:
- `Sumana.glyphs`
- `Sumana-Regular.ufo/`
- `Sumana-Bold.ufo/`
- `FontLab/` (legacy)
- `OTF/`

## Confidence

**High** — The repository was found in the `cyrealtype` GitHub organization, which is the official Cyreal account. The designer name matched the METADATA.pb (Cyreal). Both UFO and Glyphs sources were present.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/cyrealtype/Sumana` at commit `68c5ce43ae96268ac93ee3b79c720c7f479c5ee1`.
