# Oranienbaum

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Oranienbaum as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/oranienbaum.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Oranienbaum-Regular.ttf, the font Google Fonts ships, with babelfont 58eedc8
  (felipesanches/babelfont-rs branch 2026-10-22: simoncozens/babelfont-rs main plus the
  TTF reader changes proposed to it): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/oranienbaum at `8e89dc77fa0d`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/oranienbaum.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`8e89dc77fa0d` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release kerns through a GPOS kern feature and also carries a legacy `kern` table
  (5243 pairs). Shapers read the GPOS feature, which these sources keep; the legacy
  table, read only by software without GPOS support, is not carried.
- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6, ofl/oranienbaum/: the font as built and its
  metadata; src/ holds METADATA_comments.txt, Oranienbaum-Regular.otf, no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Oranienbaum — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Summary

The `googlefontdirectory-hg` monorepo contains an entry for Oranienbaum, but the only file in the source path (besides metadata) is a compiled OTF binary — no design sources are present. No canonical upstream repository with editable source files was found.

### Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oranienbaum/src/`
- **Buildable**: No — no design sources present (compiled binary only)

#### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Oranienbaum-Regular.otf` | Compiled binary | Not a design source |

No VFB, SFD, UFO, or Glyphs design sources are present.

### Family Details

- **Designers**: Oleg Pospelov (main type designer), Jovanny Lemonad (art director, technical engineer, publisher)
- **License**: OFL
- **Category**: SERIF
- **Google Fonts date added**: 2012-08-20
- **Copyright**: "Copyright (c) 2012, Oleg Pospelov (oleg@pospelov.com), Jovanny Lemonad (lemonad@jovanny.ru), with Reserved Font Name 'Oranienbaum'"

### Investigation Details

#### GitHub Search

GitHub was searched for "Oranienbaum", "Oranienbaum font", and "Oranienbaum Pospelov". Only two repositories were found: `librefonts/oranienbaum` and `google-fonts-bower/oranienbaum-bower`. Neither is a canonical designer-owned repository.

#### Designer Profiles

**Oleg Pospelov** (`OlegPospelov` on GitHub): A GitHub account was found but had zero public repositories.

**Jovanny Lemonad** (`jovannylemonad` on GitHub): A GitHub account was found with 9 public repositories, all of which are unrelated single-cut display fonts (Kazmann Sans One, Ardeco One, Matias One, etc.) from a later period. No Oranienbaum repository was present.

#### Librefonts Mirror

The `librefonts/oranienbaum` repository contains only TTX (decompiled binary XML) files — there are no original source files (no SFD, VFB, UFO, or Glyphs files). The repository was last updated in October 2014.

### Conclusion

No design sources exist for Oranienbaum in either the `googlefontdirectory-hg` monorepo or any public repository. The original sources (likely FontLab VFB given the 2012 timeframe) were never published. The librefonts mirror contains only decompiled TTX files.
