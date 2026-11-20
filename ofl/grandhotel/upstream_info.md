# Grand Hotel

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Grand Hotel (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/grandhotel.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from GrandHotel-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/grandhotel at `506942160990`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: GrandHotel-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/grandhotel.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`506942160990` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/grandhotel at b0716771fb1056ca9db1d65d94e62ecf9dbedefa:
  src/GrandHotel-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/grandhotel"
      commit: "b0716771fb1056ca9db1d65d94e62ecf9dbedefa"
    }

## Previous investigation

## Grand Hotel — Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/librefonts/grandhotel |
| Commit | `b0716771fb1056ca9db1d65d94e62ecf9dbedefa` |
| Confidence | Medium |

### Source Types

The repository contains:
- `src/GrandHotel-Regular.vfb` — FontLab VFB source
- TTX-decompiled files

### Build Compatibility

Not buildable with gftools-builder. The VFB (FontLab Studio) format is a proprietary binary format that requires FontLab to open. No modern Glyphs, UFO, or Designspace sources are available. No native Astigmatic (Brian J. Bonislawsky) repository was found on GitHub.

### Investigation Notes

This is a librefonts mirror repository. The `src/` directory contains a FontLab VFB file, which represents the original design source but in a proprietary format. The TTX files are decompiled binary dumps.

**Note on librefonts mirrors**: This repository is a community archive. The VFB source is closer to the original design than TTX dumps, but still requires proprietary software (FontLab Studio) to edit.

The binary in google/fonts dates from the initial commit (2015-03-07).

A source block was added to METADATA.pb pointing to this repository and commit.

### Confidence: Medium

Librefonts mirror with VFB source; not buildable with modern open-source tooling.
