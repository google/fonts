# Sansita — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Sansita was identified at `Omnibus-Type/Sansita` on GitHub. The repository contained Glyphs source files in the `sources/Backup/` directory. The main `sources/` folder contained no primary Glyphs source at the root level, only the Backup subfolder, post-processing scripts, and images. A source block was added to METADATA.pb referencing the most recent Glyphs backup file.

## Upstream Repository

- **URL**: https://github.com/Omnibus-Type/Sansita
- **Owner**: Omnibus-Type
- **Branch**: master
- **Commit**: `168abd68a378c93d6febb46b453efd67e9ed86f2`
- **Commit message**: "Merge pull request #7 from Omnibus-Type/pr/5 — v1.007 update"

## Source Files Found

| File | Type | Notes |
|------|------|-------|
| `sources/Backup/1216_Sansita.glyphs` | Glyphs source | Most recent version |
| `sources/Backup/1216_Sansita Italic.glyphs` | Glyphs source | Most recent version |
| `sources/Backup/1176_Sansita.glyphs` | Glyphs source | Older version |
| `sources/Backup/1176_Sansita Italic.glyphs` | Glyphs source | Older version |

## Designer

Sansita was designed by Omnibus-Type (omnibus.type@gmail.com). The repository is hosted under the `Omnibus-Type` GitHub user account.

## Investigation Notes

The repository was found by checking the `Omnibus-Type` user repositories list. The `sources/` directory did not contain active working Glyphs files at root level; sources were only present in the `Backup/` subdirectory. The `1216_Sansita.glyphs` file represents the most recent version based on the version number in the filename. The `fonts/` directory contained the compiled TTF, OTF, and webfont outputs.

## Result

A source block was added to METADATA.pb referencing the repository URL, the latest commit hash, and the most recent Glyphs backup source file.
