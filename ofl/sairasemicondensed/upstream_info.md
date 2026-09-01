# Saira Semi Condensed — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Saira Semi Condensed was identified at `Omnibus-Type/Saira` on GitHub. The Saira Semi Condensed family is generated from the same source repository as the main Saira family and other condensed variants, using a variable font source with a `wdth` axis. A source block was added to METADATA.pb.

## Upstream Repository

- **URL**: https://github.com/Omnibus-Type/Saira
- **Owner**: Omnibus-Type
- **Branch**: master
- **Commit**: `1916f2a575479b626238d9842126e63aa208eebf`
- **Commit message**: "generated fonts 1.101"

## Source Files Found

| File | Type |
|------|------|
| `Saira/sources/Saira.glyphs` | Glyphs source (upright, all widths) |
| `Saira/sources/Saira-Italic.glyphs` | Glyphs source (italic, all widths) |
| `Saira/sources/config.yaml` | Build configuration |

## Designer

Saira was designed by Omnibus-Type (omnibus.type@gmail.com). The repository is hosted under the `Omnibus-Type` GitHub user account.

## Investigation Notes

The Saira Semi Condensed family shares its source with Saira, Saira Condensed, and Saira Extra Condensed. The `wdth` axis in the Glyphs source files generates all condensed variants. The `SairaSemiCondensed-*.ttf` output files were confirmed in the repository's `Saira/fonts/ttf/` directory.

## Result

A source block was added to METADATA.pb referencing the repository URL, the latest commit hash, and the `config.yaml` path.
