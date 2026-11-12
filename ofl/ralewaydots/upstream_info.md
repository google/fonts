# Raleway Dots

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Raleway Dots (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/ralewaydots.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  RalewayDots-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/ralewaydots at `ce7463426672`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/ralewaydots.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`ce7463426672` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/ralewaydots at c845d1a8e75014ad17dbbf2633119226bed462d8:
  src/RalewayDots-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/ralewaydots"
      commit: "c845d1a8e75014ad17dbbf2633119226bed462d8"
    }

## Previous investigation

## Raleway Dots - Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [librefonts/ralewaydots](https://github.com/librefonts/ralewaydots) |
| **Commit** | `c845d1a8e75014ad17dbbf2633119226bed462d8` |
| **Confidence** | medium |
| **Source Types** | ttx |
| **Has config.yaml** | No |

### Investigation Summary

METADATA.pb for Raleway Dots had no source block. A source block was added pointing to the librefonts mirror repository.

### Source Analysis

The repository at https://github.com/librefonts/ralewaydots is a **librefonts mirror**. These repositories contain TTX (XML) files that were mechanically decompiled from the binary TTF fonts, not original design sources. They do not contain the original .glyphs, .ufo, .sfd, or other editable source files that the designer used to create the font.

**Available source types**: ttx (decompiled from binaries)

### Build Status

This family is **not buildable** with gftools-builder from these sources. The TTX files in librefonts mirrors are binary round-trips, not design sources. No config.yaml was created because there are no compatible sources to build from.

### Notes

librefonts mirror with TTX sources. Note: impallari/Raleway exists but covers main Raleway, not Dots variant.

### Binary History in google/fonts

```
2019-07-10 10:45:16 +0100 023aa4b2855c95413d1b1c510ad812beb345df75 Remove trailing whitespace from font family names
```

### Actions Taken

1. A `source { }` block was added to METADATA.pb with the librefonts mirror repository URL and commit hash.
2. No config.yaml was created because the repository contains only TTX decompiled binary dumps, not original design sources suitable for gftools-builder.
