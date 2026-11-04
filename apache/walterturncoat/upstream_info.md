# Walter Turncoat

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Walter Turncoat as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/walterturncoat.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  WalterTurncoat-Regular.ttf, the font Google Fonts ships, with babelfont 58eedc8
  (felipesanches/babelfont-rs branch 2026-10-22: simoncozens/babelfont-rs main plus the
  TTF reader changes proposed to it): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/walterturncoat at `62e29daafc55`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/walterturncoat.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`62e29daafc55` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release kerns with a legacy `kern` table (1114 pairs) and has no GPOS; these
  sources kern through a GPOS kern feature, which is how fontc builds kerning. HarfBuzz
  shapes every kerned pair alike in both (the functional gate). Decided 2026-10-01:
  releases with an old kern table are accepted and disclosed.
- The release has no glyph instructions: its font program defines functions that no
  glyph calls, and its control value program only turns on dropout control (SCANCTRL
  511, SCANTYPE 4). These sources carry no TrueType instructions, and the build is
  hinted by ttfautohint, as for every release that has a font program: the outlines,
  spacing and layout are the release's, its rendering at small sizes under a TrueType
  interpreter is not. Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6, apache/walterturncoat/: the font as built
  and its metadata; src/ holds METADATA_comments.txt, WalterTurncoat-VTT.ttf, no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## walterturncoat

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `apache/walterturncoat/src/` |
| **Buildable** | No — no source files: only the font as built and its metadata |

The family is in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013. No source file of
this family is in it, at this commit or in any other.

#### Files in `src/` (2)

- Other: METADATA_comments.txt, WalterTurncoat-VTT.ttf
