# Old Standard TT — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at `akryukov/oldstand` on GitHub, owned by the designer Alexey Kryukov. However, the repository contains only SFD (FontForge) sources — no UFO or Glyphs format sources. Per policy, METADATA.pb was not updated because UFO/Glyphs sources are required for a source block addition.

## Family Details

- **Designer**: Alexey Kryukov
- **License**: OFL
- **Category**: SERIF
- **Google Fonts date added**: 2010-05-18
- **Copyright**: "Copyright 2011 The Old Standard Project Authors (amkryukov@gmail.com)"

## Upstream Repository

- **URL**: https://github.com/akryukov/oldstand
- **Owner**: `akryukov` — Alexey Kryukov (confirmed via profile showing affiliation with Moscow State University and other font projects including Theano Classical Fonts)
- **Description**: "Old Standard font family"
- **Last pushed**: 2017-03-31

The repository contains FontForge SFD sources:
- `OldStandard-Regular.sfd`
- `OldStandard-Italic.sfd`
- `OldStandard-Bold.sfd`
- `OldStandard.cfg` — a CacheTT configuration file
- `genfonts.sh` — build script
- `ost-generate.py` — Python generation script
- GDL (Graphite Description Language) files for each weight
- A `manual/` directory with source documentation

## Commits

The repository was last updated in August 2013. Three commits were found:
- `f379c2c4` (2013-08-12): "A cfg filr for cachett"
- `80f7b552` (2013-08-12): "Old Standard manual sources"
- `6ab74e04` (2013-08-12): "pushing main font files"

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Conclusion

A canonical designer-owned repository exists at `akryukov/oldstand`. The sources are in FontForge SFD format only — no UFO or Glyphs sources are available. No METADATA.pb changes were made, as the policy requires UFO or Glyphs sources to justify a source block addition.

## Confidence

**High** — The repository is owned by Alexey Kryukov (`akryukov`), whose email `amkryukov@gmail.com` matches the copyright string exactly. The font files in the repository match the names used in the Google Fonts release.
