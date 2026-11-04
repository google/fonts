# Song Myung

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Song Myung as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/songmyung.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from SongMyung-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/songmyung at `34d21808ddde`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/songmyung.json`:
https://github.com/felipesanches/gf-source-modernization at `1dddab8`.

`34d21808ddde` is the equivalence commit: its build is functionally equivalent to the
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
  built in google/fonts#1459 (2018, "korean families r01"), and JIKJISOFT's one public
  repository, jikjisoft/jikjifont, is empty.

## Previous investigation

## Song Myung — Upstream Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

### Summary

No canonical upstream repository with UFO or Glyphs source files was found for
the Song Myung font.

### Research

Song Myung was created by JIKJI (JIKJISOFT), a Korean type foundry established
in 2004. The font is a contemporary take on a traditional Hangul serif design.
Searches on GitHub for JIKJI-related repositories returned a result at
`webfontworld/jikji` but this repository did not exist (returned 404). Other
searches for JIKJI's GitHub presence and for the Song Myung source files
returned only font distribution sites, not a source repository.

### Decision

No `source` block was added to `METADATA.pb`. No publicly accessible source
repository in UFO, Glyphs, or other editable format was found.

### Notes

The designer listed in METADATA.pb is JIKJI. Song Myung is a Korean and Latin
typeface that supports the Korean (Hangul) script. The Latin portion is a
version of Source Serif Pro adjusted to fit the Korean design. The font is
licensed under the SIL Open Font License.
