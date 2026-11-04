# Yeon Sung

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Yeon Sung as binaries only (google/fonts at commit `2eb0b48d5f76`).
No source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/yeonsung.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from YeonSung-Regular.ttf,
  the font Google Fonts ships, with babelfont 58eedc8 (felipesanches/babelfont-rs branch
  2026-10-22: simoncozens/babelfont-rs main plus the TTF reader changes proposed to it):
  its TTF reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/yeonsung at `8979fd9bff99`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/yeonsung.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`8979fd9bff99` is the equivalence commit: its build is functionally equivalent to the
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

Other copies of this family, kept on record; none of them is a source:

- https://github.com/woowabros/Yeonsung at 599fc1b88ba87312e69b3ad9085158542fbcccc1: the
  fonts as built (2 font files); no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/woowabros/Yeonsung"
      commit: "599fc1b88ba87312e69b3ad9085158542fbcccc1"
    }

## Previous investigation

## Yeon Sung — Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/woowabros/Yeonsung |
| Commit | `599fc1b88ba87312e69b3ad9085158542fbcccc1` |
| Confidence | High |

### Source Types

The repository contains compiled font files only:
- `FONT/YEONSUNG.otf and YEONSUNG.ttf` — OTF and TTF binaries

No editable design sources (Glyphs, UFO, etc.) are available.

### Build Compatibility

Not buildable with gftools-builder. The repository contains only compiled OTF/TTF binaries, not editable source files. This is typical of Korean font releases from Woowahan Brothers (Baemin/Baedal Minjok).

### Investigation Notes

Woowahan Brothers (the company behind Baemin/Baedal Minjok food delivery service) released several Korean display fonts as open source. The Yeon Sung repository contains only the final compiled fonts without design sources. The binary in google/fonts was last updated on 2024-01-19 (hotfix for space & nbspace characters).

A source block was added to METADATA.pb pointing to this repository and commit.

### Confidence: High

Woowahan Brothers (woowabros) is the original publisher and this is their official repository.
