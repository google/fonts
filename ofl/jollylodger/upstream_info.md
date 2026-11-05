# Jolly Lodger

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Jolly Lodger (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/jollylodger.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  JollyLodger-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/jollylodger at `e6b36c6ce4e0`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/jollylodger.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`e6b36c6ce4e0` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/jollylodger at 06a3c7f44fc01a8d09ed73ea8c180a11018bdac8:
  src/JollyLodger-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/jollylodger"
      commit: "06a3c7f44fc01a8d09ed73ea8c180a11018bdac8"
    }

## Previous investigation

## Investigation: Jolly Lodger

### Summary

| Field | Value |
|-------|-------|
| Family Name | Jolly Lodger |
| Slug | jolly-lodger |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/jollylodger |
| Commit Hash | 06a3c7f44fc01a8d09ed73ea8c180a11018bdac8 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

### Source Data (METADATA.pb)

No source block

### Investigation

The `ofl/jollylodger/` directory in google/fonts contains `DESCRIPTION.en_us.html`, `JollyLodger-Regular.ttf`, `METADATA.pb`, and `OFL.txt`. The METADATA.pb has only basic metadata — no `source { }` block.

The git log shows the font has been in google/fonts since the initial commit (`90abd17b4`, 2015-03-07). No font file updates have been pushed since then.

The copyright reads: "Copyright (c) 2012 by Font Diner, Inc (diner@fontdiner.com) with Reserved Font Name 'Jolly Lodger'." Created by Font Diner (Stuart Sandler).

The tracking JSON (`data/gfonts_library_sources.json`) records the upstream repository as `https://github.com/librefonts/jollylodger` at commit `06a3c7f44fc01a8d09ed73ea8c180a11018bdac8` (subject: "update .travis.yml"). This is the librefonts GitHub organization's mirror repository.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/librefonts/jollylodger`. The local clone has only one commit (shallow clone). The repository contains:
- `JollyLodger-Regular.ttf` (binary font)
- `src/JollyLodger-Regular-TTF.vfb` (FontLab Studio source, TTF variant)
- `src/VERSIONS.txt`: "JollyLodger-Regular.ttf: Version 1.000"
- TTX decompositions of the fonts

The source format is `.vfb` (FontLab Studio), which is NOT compatible with gftools-builder. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist.

### Conclusion

The upstream repository is `https://github.com/librefonts/jollylodger` at commit `06a3c7f44fc01a8d09ed73ea8c180a11018bdac8`. However, the only sources available are `.vfb` (FontLab Studio) files, which are not gftools-builder compatible. No config.yaml is possible with these sources. A source block needs to be added to METADATA.pb but the status will remain `missing_config` until buildable sources become available.
