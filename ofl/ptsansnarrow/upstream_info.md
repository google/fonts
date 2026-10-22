# PT Sans Narrow

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped PT Sans Narrow as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/ptsansnarrow.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  PT_Sans-Narrow-Web-{Bold,Regular}.ttf, the fonts Google Fonts ships, with babelfont
  58eedc8 (felipesanches/babelfont-rs branch 2026-10-22: simoncozens/babelfont-rs main
  plus the TTF reader changes proposed to it): its TTF reader, no filters.
  sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/ptsansnarrow at `ff02de9bb277`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 2 styles. Those tools,
including this family's plan `plans/ptsansnarrow.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`ff02de9bb277` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The releases kern through a GPOS kern feature and also carry a legacy `kern` table
  (23449 to 25231 pairs per style). Shapers read the GPOS feature, which these sources
  keep; the legacy table, read only by software without GPOS support, is not carried.
- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## PT Sans Narrow — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ptsansnarrow/src/`

### Source Files

The `ptsansnarrow/src/` directory contains only non-source files (menu subsets, metadata). No design source files are present.

- **Menu subset**: PT_Sans-Narrow.menu

### Buildability

No design source files are available in this directory. The font cannot be rebuilt from the files present here.

### Designer

ParaType (yakupov@paratype.com). Copyright 2009 ParaType Ltd.

### Investigation Details

- **Checked cache**: the upstream repo cache — no cached entry.
- **GitHub organization**: The `paratype` GitHub organization exists but contains no font source repositories.
- **GitHub search**: No canonical designer-owned repository was found for PT Sans Narrow or the PT font family.
- **Third-party mirrors**: Only Linux distribution packaging mirrors were found, which are not canonical.

### Notes

PT Sans Narrow is the condensed width variant of PT Sans, designed for use in space-constrained layouts such as tables and narrow columns. It shares the same design heritage as PT Sans — commissioned by the Federal Agency on Press and Mass Communications of the Russian Federation, released in 2009 by Paratype.
