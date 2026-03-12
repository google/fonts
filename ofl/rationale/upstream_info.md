# Rationale — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **URL**: https://github.com/cyrealtype/Rationale
- **Owner**: cyrealtype (Cyreal)
- **Branch**: master
- **Latest commit**: `b12941da538d15c94bc04f60926288a791d5a81c` (2023-05-11)
- **Source format**: Glyphs (`Rationale.glyphs`)

## What Was Done

The canonical upstream repository at `cyrealtype/Rationale` was located by searching GitHub for the designer name (Cyreal) and font name. The repository was confirmed to contain a Glyphs source file (`Rationale.glyphs`) in its `sources/` directory. The latest commit hash was verified via the GitHub API. A `source` block was added to `METADATA.pb` referencing the repository and commit.

## Notes

The repository also contains VFB files (legacy FontLab format), but the primary source is `Rationale.glyphs`. The copyright statement in METADATA.pb references `www.cyreal.org`, consistent with the `cyrealtype` GitHub organization.
