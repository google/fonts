# Akronim

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Akronim as binaries only (google/fonts at commit `2eb0b48d5f76`).
No source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/akronim.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Akronim-Regular.ttf,
  the font Google Fonts ships, with babelfont 58eedc8 (felipesanches/babelfont-rs branch
  2026-10-22: simoncozens/babelfont-rs main plus the TTF reader changes proposed to it):
  its TTF reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/akronim at `8ad7073228a0`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/akronim.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`8ad7073228a0` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release kerns with a legacy `kern` table (1051 pairs) and has no GPOS; these
  sources kern through a GPOS kern feature, which is how fontc builds kerning. HarfBuzz
  shapes every kerned pair alike in both (the functional gate). Decided 2026-10-01:
  releases with an old kern table are accepted and disclosed.
- The released font is partly hinted (TrueType instructions in 16 of its 254 glyphs).
  These sources carry no TrueType instructions, so the build is hinted by ttfautohint:
  the outlines, spacing and layout are the release's, its rendering at small sizes under
  a TrueType interpreter is not. Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/librefonts/akronim at 9288ae0636d38a5b42002d6df8b5906c49fe9b1a: a
  build of the font dumped to TTX, and its metadata; no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/akronim"
      commit: "9288ae0636d38a5b42002d6df8b5906c49fe9b1a"
    }

## Previous investigation

## Akronim - Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [librefonts/akronim](https://github.com/librefonts/akronim) |
| **Commit** | `9288ae0636d38a5b42002d6df8b5906c49fe9b1a` |
| **Confidence** | medium |
| **Source Types** | ttx |
| **Has config.yaml** | No |

### Investigation Summary

METADATA.pb for Akronim had no source block. A source block was added pointing to the librefonts mirror repository.

### Source Analysis

The repository at https://github.com/librefonts/akronim is a **librefonts mirror**. These repositories contain TTX (XML) files that were mechanically decompiled from the binary TTF fonts, not original design sources. They do not contain the original .glyphs, .ufo, .sfd, or other editable source files that the designer used to create the font.

**Available source types**: ttx (decompiled from binaries)

### Build Status

This family is **not buildable** with gftools-builder from these sources. The TTX files in librefonts mirrors are binary round-trips, not design sources. No config.yaml was created because there are no compatible sources to build from.

### Notes

librefonts mirror with TTX sources. src/ has only METADATA_comments.txt and VERSIONS.txt.

### Binary History in google/fonts

```
2017-05-01 13:20:28 -0400 347b8a4d15b618e787fc726898c66bb1dd6c0b02 hotfix-akronim: v1.002 added (#746)
```

### Actions Taken

1. A `source { }` block was added to METADATA.pb with the librefonts mirror repository URL and commit hash.
2. No config.yaml was created because the repository contains only TTX decompiled binary dumps, not original design sources suitable for gftools-builder.
