# Poor Story

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Poor Story as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/poorstory.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from PoorStory-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/poorstory at `b2d4c0cc67e5`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/poorstory.json`:
https://github.com/felipesanches/gf-source-modernization at `1dddab8`.

`b2d4c0cc67e5` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/yoondesign/Yoonfont-PoorStory at
  ba19825551ed130aa7c3f035992eac63dacc477e, the designers' repository: the fonts as
  built (TTF, OTF), their license and READMEs; no source. google/fonts has no source
  block for this family (added as built in google/fonts#1459, 2018).

## Previous investigation

## Poor Story — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository
- **URL**: No source block present
- **Designers' repository** (not in METADATA.pb): https://github.com/yoondesign/Yoonfont-PoorStory
  at `ba19825551ed130aa7c3f035992eac63dacc477e` holds the fonts as built (`Poorstory.ttf`,
  `Poorstory.otf`), their license and READMEs; no source, at that commit or in its history.
- **Commit**: N/A
- **Status**: absent

### What Was Done
The existing source metadata was reviewed. No source block was found in METADATA.pb.

### Notes
Designer: Yoon Design. Script: Korean (Kore). Category: DISPLAY. Copyright: YoonDesign Inc.
