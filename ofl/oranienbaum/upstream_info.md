# Oranienbaum — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The `googlefontdirectory-hg` monorepo contains an entry for Oranienbaum, but the only file in the source path (besides metadata) is a compiled OTF binary — no design sources are present. No canonical upstream repository with editable source files was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oranienbaum/src/`
- **Buildable**: No — no design sources present (compiled binary only)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Oranienbaum-Regular.otf` | Compiled binary | Not a design source |

No VFB, SFD, UFO, or Glyphs design sources are present.

## Family Details

- **Designers**: Oleg Pospelov (main type designer), Jovanny Lemonad (art director, technical engineer, publisher)
- **License**: OFL
- **Category**: SERIF
- **Google Fonts date added**: 2012-08-20
- **Copyright**: "Copyright (c) 2012, Oleg Pospelov (oleg@pospelov.com), Jovanny Lemonad (lemonad@jovanny.ru), with Reserved Font Name 'Oranienbaum'"

## Investigation Details

### GitHub Search

GitHub was searched for "Oranienbaum", "Oranienbaum font", and "Oranienbaum Pospelov". Only two repositories were found: `librefonts/oranienbaum` and `google-fonts-bower/oranienbaum-bower`. Neither is a canonical designer-owned repository.

### Designer Profiles

**Oleg Pospelov** (`OlegPospelov` on GitHub): A GitHub account was found but had zero public repositories.

**Jovanny Lemonad** (`jovannylemonad` on GitHub): A GitHub account was found with 9 public repositories, all of which are unrelated single-cut display fonts (Kazmann Sans One, Ardeco One, Matias One, etc.) from a later period. No Oranienbaum repository was present.

### Librefonts Mirror

The `librefonts/oranienbaum` repository contains only TTX (decompiled binary XML) files — there are no original source files (no SFD, VFB, UFO, or Glyphs files). The repository was last updated in October 2014.

## Conclusion

No design sources exist for Oranienbaum in either the `googlefontdirectory-hg` monorepo or any public repository. The original sources (likely FontLab VFB given the 2012 timeframe) were never published. The librefonts mirror contains only decompiled TTX files.
