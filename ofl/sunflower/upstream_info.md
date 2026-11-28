# Sunflower

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Sunflower as binaries only (google/fonts at commit `2eb0b48d5f76`).
No source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/sunflower.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Sunflower-{Bold,Light,Medium}.ttf, the fonts Google Fonts ships, with babelfont
  26fdcfa (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main
  plus the name changes proposed to it (#117, typographic-family-names)): its TTF
  reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/sunflower at `ee6d06ce4876`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 3 styles. Those tools,
including this family's plan `plans/sunflower.json`:
https://github.com/felipesanches/gf-source-modernization at `1dddab8`.

`ee6d06ce4876` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the releases', its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- None known: google/fonts has no source block for this family; the fonts were added as
  built in google/fonts#1459 (2018, "korean families r01"), and JIKJISOFT's one public
  repository, jikjisoft/jikjifont, is empty.

## Previous investigation

**Model**: Claude Opus 4.6

## Sunflower — Upstream Source Investigation

### Summary

No canonical upstream repository with UFO or Glyphs sources was found for Sunflower. The font is a Korean (Hangul) typeface by JIKJISOFT.

### Designer

JIKJISOFT

### Search Results

- The `jikjisoft` GitHub user was found but had only one repository (`jikjifont`), which was empty (no commits or files).
- No other repositories for Sunflower were found via searches for "Sunflower Korean font", "JIKJISOFT", or similar queries.
- The font's copyright notice dates to 2008 ("Copyright 2008 The Sunflower Project Authors"), suggesting it originated well before common use of GitHub for font hosting.

### Conclusion

No source block was added. No canonical repository with UFO or Glyphs sources was found.
