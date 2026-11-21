# Averia Serif Libre

**Model**: Claude Opus 5.5
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Averia Serif Libre as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/averiaseriflibre.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  AveriaSerifLibre-{Bold,BoldItalic,Italic,Light,LightItalic,Regular}.ttf, the fonts
  Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/averiaseriflibre at `473558d24c41`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts
2eb0b48d5f76, under tools/table_gate.py and tools/functional_gate.py:
AveriaSerifLibre-Bold: 3 blocking rows; functionally equivalent
AveriaSerifLibre-BoldItalic: 3 blocking rows; functionally equivalent
AveriaSerifLibre-Italic: 3 blocking rows; functionally equivalent
AveriaSerifLibre-Light: 3 blocking rows; functionally equivalent
AveriaSerifLibre-LightItalic: 3 blocking rows; functionally equivalent
AveriaSerifLibre-Regular: 3 blocking rows; functionally equivalent. Those tools,
including this family's plan `plans/averiaseriflibre.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`473558d24c41` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts kern with a legacy `kern` table; these sources kern through a GPOS
  kern feature, which is how fontc builds kerning. HarfBuzz shapes every kerned pair
  alike in both, except pairs with the soft hyphen (U+00AD), which it hides: there the
  release leaves half the pair's value on the following glyph and the build none (42 to
  102 pairs per style, tools/probes/binary_to_source/results/legacy-kern-pairs.txt in
  the evidence repository). Decided 2026-10-01: releases with an old kern table are
  accepted and disclosed.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/averiaseriflibre"
      commit: "d1b2ab3fcea4e6a77af02a5e7861ed7753793dfd"
    }

## Previous investigation

## Averia Serif Libre - Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [librefonts/averiaseriflibre](https://github.com/librefonts/averiaseriflibre) |
| **Commit** | `d1b2ab3fcea4e6a77af02a5e7861ed7753793dfd` |
| **Confidence** | medium |
| **Source Types** | ttx |
| **Has config.yaml** | No |

### Investigation Summary

METADATA.pb for Averia Serif Libre had no source block. A source block was added pointing to the librefonts mirror repository.

### Source Analysis

The repository at https://github.com/librefonts/averiaseriflibre is a **librefonts mirror**. These repositories contain TTX (XML) files that were mechanically decompiled from the binary TTF fonts, not original design sources. They do not contain the original .glyphs, .ufo, .sfd, or other editable source files that the designer used to create the font.

**Available source types**: ttx (decompiled from binaries)

### Build Status

This family is **not buildable** with gftools-builder from these sources. The TTX files in librefonts mirrors are binary round-trips, not design sources. No config.yaml was created because there are no compatible sources to build from.

### Notes

librefonts mirror with TTX sources.

### Binary History in google/fonts

```
2017-08-07 15:56:50 -0400 463ce0ab22efecdd01ac957ae91e5dcac810fef2 hotfix-averiaseriflibre: v1.002 added (#839)
```

### Actions Taken

1. A `source { }` block was added to METADATA.pb with the librefonts mirror repository URL and commit hash.
2. No config.yaml was created because the repository contains only TTX decompiled binary dumps, not original design sources suitable for gftools-builder.
