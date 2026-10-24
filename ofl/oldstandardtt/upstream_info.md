# Old Standard TT — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-19 (updated)

## Summary

The upstream repository was updated to point to the actively maintained SourceHut fork at `https://git.sr.ht/~ralessi/oldstandard`, maintained by Robert Alessi. This replaces the dormant GitHub repository `akryukov/oldstand` (last updated 2017). The SourceHut fork has continued development through v2.7a with additional weights (Bold Italic) and a Math font variant. Sources remain SFD-only (no gftools-builder pipeline possible).

## Family Details

- **Designer**: Alexey Kryukov (original), Robert Alessi & Antonis Tsolomitis (current maintainers)
- **License**: OFL
- **Category**: SERIF
- **Google Fonts date added**: 2010-05-18
- **Copyright**: "Copyright 2011 The Old Standard Project Authors (amkryukov@gmail.com)"

## Upstream Repository

- **Active URL**: https://git.sr.ht/~ralessi/oldstandard (SourceHut)
- **Maintainer**: Robert Alessi (alessi@robertalessi.net)
- **Co-maintainer**: Antonis Tsolomitis (atsol@aegean.gr)
- **Latest release**: v2.7a
- **Bug tracker**: https://todo.sr.ht/~ralessi/oldstandard

### Original Repository (dormant)

- **URL**: https://github.com/akryukov/oldstand
- **Owner**: Alexey Kryukov (original designer, `amkryukov@gmail.com`)
- **Description**: "Old Standard font family"
- **Last pushed**: 2017-03-31
- **Status**: Dormant since 2013; the SourceHut fork continues active development

The original repository contains FontForge SFD sources:
- `OldStandard-Regular.sfd`
- `OldStandard-Italic.sfd`
- `OldStandard-Bold.sfd`
- `OldStandard.cfg` — a CacheTT configuration file
- `genfonts.sh` — build script
- `ost-generate.py` — Python generation script
- GDL (Graphite Description Language) files for each weight
- A `manual/` directory with source documentation

Notable commits:
- `f379c2c4` (2013-08-12): "A cfg filr for cachett"
- `80f7b552` (2013-08-12): "Old Standard manual sources"
- `6ab74e04` (2013-08-12): "pushing main font files"

## Source Files (SourceHut repo)

The `src/` directory contains FontForge SFD sources:
- `OldStandard-Regular.sfd` (2.0 MiB)
- `OldStandard-Italic.sfd` (1.8 MiB)
- `OldStandard-Bold.sfd` (1.7 MiB)
- `OldStandard-BoldItalic.sfd` (2.2 MiB) — not in Google Fonts
- `OldStandard-Math.sfd` (7.6 MiB) — not in Google Fonts

Build is driven by a `makefile` at the repo root.

## Actions Taken

- METADATA.pb `source.repository_url` was set to the SourceHut repo URL
- No commit hash was recorded (SFD sources cannot go through gftools-builder)
- No config.yaml was created (no modern build pipeline possible)

## Conclusion

The SourceHut fork is the actively maintained upstream. It contains expanded glyph coverage and additional weights beyond what Google Fonts currently ships. Sources are SFD-only, so reproducible builds via gftools-builder are not possible.

## Confidence

**High** — Robert Alessi's fork is clearly a continuation of the original project, with proper attribution and OFL licensing. The SourceHut bug tracker is active.

## Commit Added (LOW confidence)

Commit `b8feb6753e80522bfec434da05a5d31b6b3ff094` was determined by **head**. Used the current HEAD of the repository. No date correlation was possible. This is a best guess.
