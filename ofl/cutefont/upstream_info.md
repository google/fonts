# Cute Font

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Cute Font as binaries only (google/fonts at commit `2eb0b48d5f76`).
No source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/cutefont.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from CuteFont-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/cutefont at `759c5c5d251f`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/cutefont.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`759c5c5d251f` is the equivalence commit: its build is functionally equivalent to the
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

- None known: google/fonts has no source block for this family; the fonts were added as
  built in google/fonts#1459 (2018, "korean families r01"), and TypoDesign Lab.
  publishes no source repository.

## Previous investigation

## Cute Font

**Date investigated**: 2026-02-26
**Status**: no_upstream_repo
**Designer**: TypoDesign Lab. Inc
**METADATA.pb path**: `ofl/cutefont/METADATA.pb`

### Source Data

| Field | Value |
|-------|-------|
| Repository URL | None |
| Commit | None |
| Config YAML | None |
| Branch | None |

### How the Repository URL Was Found

No repository URL exists in METADATA.pb. There is no `source { }` block at all. The font was added to Google Fonts as part of a batch of Korean fonts in PR #1459 ("korean families r01: added"), authored by Marc Foley (m4rc1e) on 2018-03-13. The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com".

No upstream GitHub repository has been found for this font. Searches on GitHub for "CuteFont" and "TypoDesign Lab" did not reveal a source repository. The font appears to have been delivered as pre-compiled binary files by TypoDesign Lab. Inc, a Korean foundry, and mastered by Aaron Bell.

The copyright string in the font reads: "COPYRIGHT 2004-2017 by TypoDesign Lab. Inc. All rights reserved. Font designed by TypoDesign Lab. Inc." This does not reference any repository URL.

### How the Commit Hash Was Identified

No commit hash exists because there is no known upstream repository. The binary font file was directly submitted in PR #1459 without reference to a source repository.

### How Config YAML Was Resolved

Not applicable. Without an upstream repository, there is no config.yaml. No override config.yaml exists in the google/fonts family directory (`ofl/cutefont/`).

### Verification

- The font directory contains only: `CuteFont-Regular.ttf`, `DESCRIPTION.en_us.html`, `METADATA.pb`, `OFL.txt`
- No source block in METADATA.pb
- Font was added 2018-02-23 (date_added in METADATA.pb)
- PR #1459 was a batch PR adding multiple Korean fonts (Black And White Picture, Black Han Sans, Cute Font, Do Hyeon, Dokdo, East Sea Dokdo, Gaegu, Gamja Flower, and others)
- All Korean fonts in this batch were mastered by Aaron Bell from pre-existing font files

### Confidence

**High**: The font clearly has no known upstream repository. The onboarding was done from pre-compiled binaries provided by TypoDesign Lab. Inc, mastered by Aaron Bell. The `no_upstream_repo` status is correct.

### Open Questions

1. Does TypoDesign Lab. Inc maintain source files anywhere (even privately) that could be made available as an open-source upstream repo? This would require contacting the foundry.
