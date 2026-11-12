# Crafty Girls

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Crafty Girls as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/craftygirls.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  CraftyGirls-Regular.ttf, the font Google Fonts ships, with babelfont 58eedc8
  (felipesanches/babelfont-rs branch 2026-10-22: simoncozens/babelfont-rs main plus the
  TTF reader changes proposed to it): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/craftygirls at `79274ee13dfb`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/craftygirls.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`79274ee13dfb` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release kerns with a legacy `kern` table (375 pairs) and has no GPOS; these
  sources kern through a GPOS kern feature, which is how fontc builds kerning. HarfBuzz
  shapes every kerned pair alike in both (the functional gate). Decided 2026-10-01:
  releases with an old kern table are accepted and disclosed.
- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6, apache/craftygirls/: the font as built and
  its metadata; src/ holds CraftyGirls-TTX.ttf (the font round-tripped through TTX) and
  METADATA_comments.txt, no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Investigation Report: Crafty Girls

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `apache/craftygirls/src/` |
| **Buildable** | No — no original design sources available |

The font is referenced in the **googlefontdirectory-hg** monorepo (the git mirror of the original Google Code Mercurial repository that hosted Google Fonts from 2010–2013). However, the `src/` directory contains only a TTX-processed TTF and metadata comments — not original design sources. The original .vfb design files were never published.

#### Files in googlefontdirectory-hg `src/`

- `CraftyGirls-TTX.ttf` — TTX round-tripped binary (not a design source)
- `METADATA_comments.txt`

### Summary

Crafty Girls is a handwriting font designed by Crystal Kluge for Font Diner, Inc (DBA Tart Workshop). It was added to Google Fonts on 2011-01-06 and last updated via PR #770 in August 2017. The font was produced by a commercial foundry and delivered as a compiled binary. No original design sources (.glyphs, .ufo, .vfb) are known to exist in any public repository.

### Key Facts

| Field | Value |
|-------|-------|
| Designer | Tart Workshop (Crystal Kluge) |
| License | Apache 2.0 |
| Date Added | 2011-01-06 |
| Font Version | 1.001 |
| Source Types | TTX only (no design sources) |
| Confidence | HIGH |

### Investigation Details

#### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 98e7670 | 2017-08-07 | Marc Foley | hotfix-craftygirls: v1.001 added (#770) |
| 64d3e3a | earlier | (batch) | Remove duplicate files |
| 90abd17 | 2015-03-07 | Dave Crossland | Initial commit |

PR #770 (merged 2017-08-07) renamed the font file from CraftyGirls.ttf to CraftyGirls-Regular.ttf and updated metadata. The PR body was empty.

#### librefonts/craftygirls Mirror

The `librefonts/craftygirls` GitHub repo is an automated TTX dump, not an upstream source. It contains decompiled table dumps (`CraftyGirls-TTX.ttf.*.ttx`) which cannot be used to rebuild the font. Single commit by hash3g: "update .travis.yml".

#### Search for Original Sources

- **fontdiner/fonts** on GitHub exists but is empty (LICENSE + README only)
- No `googlefonts/craftygirls` repository exists
- Font Diner / Tart Workshop is a commercial foundry; the original design sources (.vfb) were never published
