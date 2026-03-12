# Sacramento — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Sacramento was identified at `googlefonts/SacramentoFont` on GitHub. The repository contained a Glyphs source file at `sources/Sacramento.glyphs`. A source block was added to METADATA.pb.

## Upstream Repository

- **URL**: https://github.com/googlefonts/SacramentoFont
- **Owner**: googlefonts (Google Fonts organization)
- **Branch**: main
- **Commit**: `86d34cf5a57af8dfa41c01e32a9529ed6aa499b6`
- **Commit message**: "v1.100 generated"

## Source Files Found

| File | Type |
|------|------|
| `sources/Sacramento.glyphs` | Glyphs source |

## Designer

Sacramento was designed by Brian J. Bonislawsky (DBA Astigmatic / AOETI). The repository is hosted under the Google Fonts GitHub organization.

## Investigation Notes

The repository was located by searching GitHub for `sacramento font astigmatic`. The repository name `SacramentoFont` was confirmed to exist at `googlefonts/SacramentoFont`. The `sources/` directory contained a single Glyphs file, `Sacramento.glyphs`, confirming active source availability. Old VFB sources from version 1.000 were also present in an `old/` directory but are superseded by the Glyphs file.

## Result

A source block was added to METADATA.pb referencing the repository URL, the latest commit hash, and the `sources/Sacramento.glyphs` file.
