**Model**: Claude Opus 4.6

# Sura — Upstream Source Investigation

## Summary

The canonical upstream repository for Sura was identified at `https://github.com/huertatipografica/sura`, maintained by Huerta Tipográfica (Carolina Giovagnoli's type foundry). The repository contained a Glyphs source file (`Sura.glyphs`).

## Repository Details

- **Repository**: https://github.com/huertatipografica/sura
- **Owner**: huertatipografica (Huerta Tipográfica / Carolina Giovagnoli)
- **License**: OFL
- **Source format**: Glyphs (.glyphs)
- **Latest commit**: `d20d15fe0de4a84a9d3a944f87e9c35d4c9da612`
- **Commit message**: "OT Fixes"
- **Default branch**: master
- **Description**: "Devanagari typeface based on Andada ht"

## Source Files

The repository root contained:
- `Sura.glyphs`
- `fonts/`
- `pdf/`

## Confidence

**High** — The repository was found in the `huertatipografica` GitHub organization. The METADATA.pb designer was listed as "Carolina Giovagnoli," and Huerta Tipográfica is her type foundry. The repository description confirmed the Devanagari nature of the font. The copyright notice in the font confirmed "Carolina Giovagnoli" as author. The Glyphs source file was present.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/huertatipografica/sura` at commit `d20d15fe0de4a84a9d3a944f87e9c35d4c9da612`.
