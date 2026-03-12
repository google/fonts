# Oranienbaum — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with Glyphs or UFO sources was found. The only GitHub repository identified was `librefonts/oranienbaum`, which is a librefonts mirror containing only TTX (decompiled binary) files — no original source files. No designer-owned GitHub repository was found for either Oleg Pospelov or Jovanny Lemonad under the Oranienbaum project. No METADATA.pb changes were made.

## Family Details

- **Designers**: Oleg Pospelov (main type designer), Jovanny Lemonad (art director, technical engineer, publisher)
- **License**: OFL
- **Category**: SERIF
- **Google Fonts date added**: 2012-08-20
- **Copyright**: "Copyright (c) 2012, Oleg Pospelov (oleg@pospelov.com), Jovanny Lemonad (lemonad@jovanny.ru), with Reserved Font Name 'Oranienbaum'"

## Search Results

### GitHub Search

GitHub was searched for "Oranienbaum", "Oranienbaum font", and "Oranienbaum Pospelov". Only two repositories were found: `librefonts/oranienbaum` and `google-fonts-bower/oranienbaum-bower`. Neither is a canonical designer-owned repository.

### Designer Profiles

**Oleg Pospelov** (`OlegPospelov` on GitHub): A GitHub account was found but had zero public repositories.

**Jovanny Lemonad** (`jovannylemonad` on GitHub): A GitHub account was found with 9 public repositories, all of which are unrelated single-cut display fonts (Kazmann Sans One, Ardeco One, Matias One, etc.) from a later period. No Oranienbaum repository was present.

### Librefonts Mirror

The `librefonts/oranienbaum` repository contains only TTX (decompiled binary XML) files — there are no original source files (no SFD, VFB, UFO, or Glyphs files). The `src/` directory contains only TTX decompilations of OTF and TTF binaries, plus a `VERSIONS.txt` and metadata comments file. The repository was last updated in October 2014.

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Conclusion

No canonical upstream repository exists for Oranienbaum. The original sources (likely FontLab VFB given the 2012 timeframe) were never published to a public repository. The librefonts mirror contains only decompiled TTX files, not usable design sources. No METADATA.pb changes were made.
