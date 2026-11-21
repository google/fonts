# Quintessential

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Quintessential (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/quintessential.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Quintessential-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/quintessential at `32ac87daac4b`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts
2eb0b48d5f76, under tools/table_gate.py and tools/functional_gate.py:
Quintessential-Regular: 2 blocking rows; functionally equivalent. Those tools, including
this family's plan `plans/quintessential.json`:
https://github.com/felipesanches/gf-source-modernization at `d6a61f4`.

`32ac87daac4b` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The build's GSUB numbers or packs some lookups differently from the release's (fontc
  places a lookup that only a contextual lookup calls, and packs chained contextual
  rules, its own way: gfonts-ai-usage-report 22-fontc-problems, problems 12 and 13);
  every rule is the same and the text shapes identically (tools/functional_gate.py).
  Decided 2026-10-02: problems that need fontc are disclosed and fixed in fontc later.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/quintessential at
  a3d26ff9183382b8379f368b41b07eb52f1bd193: src/Quintessential-Regular-TTF.vfb, a
  FontLab import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/quintessential"
      commit: "a3d26ff9183382b8379f368b41b07eb52f1bd193"
    }

## Previous investigation

## Quintessential - Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [librefonts/quintessential](https://github.com/librefonts/quintessential) |
| **Commit** | `a3d26ff9183382b8379f368b41b07eb52f1bd193` |
| **Confidence** | medium |
| **Source Types** | ttx |
| **Has config.yaml** | No |

### Investigation Summary

METADATA.pb for Quintessential had no source block. A source block was added pointing to the librefonts mirror repository.

### Source Analysis

The repository at https://github.com/librefonts/quintessential is a **librefonts mirror**. These repositories contain TTX (XML) files that were mechanically decompiled from the binary TTF fonts, not original design sources. They do not contain the original .glyphs, .ufo, .sfd, or other editable source files that the designer used to create the font.

**Available source types**: ttx (decompiled from binaries)

### Build Status

This family is **not buildable** with gftools-builder from these sources. The TTX files in librefonts mirrors are binary round-trips, not design sources. No config.yaml was created because there are no compatible sources to build from.

### Notes

librefonts mirror with TTX sources. No Astigmatic repo found.

### Binary History in google/fonts

```
2015-03-07 05:14:52 +0530 90abd17b4f97671435798b6147b698aa9087612f Initial commit
```

### Actions Taken

1. A `source { }` block was added to METADATA.pb with the librefonts mirror repository URL and commit hash.
2. No config.yaml was created because the repository contains only TTX decompiled binary dumps, not original design sources suitable for gftools-builder.
