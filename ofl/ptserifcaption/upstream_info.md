# PT Serif Caption

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped PT Serif Caption as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/ptserifcaption.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  PT_Serif-Caption-Web-{Italic,Regular}.ttf, the fonts Google Fonts ships, with
  babelfont 58eedc8 (felipesanches/babelfont-rs branch 2026-10-22:
  simoncozens/babelfont-rs main plus the TTF reader changes proposed to it): its TTF
  reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/ptserifcaption at `95cb161f0ed9`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 2 styles. Those tools,
including this family's plan `plans/ptserifcaption.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`95cb161f0ed9` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The releases kern through a GPOS kern feature and also carry a legacy `kern` table
  (20694 to 20882 pairs per style). Shapers read the GPOS feature, which these sources
  keep; the legacy table, read only by software without GPOS support, is not carried.
- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the releases', its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6, ofl/ptserif/src/: ParaType's own builds of
  PT Serif Caption (PTZ55F.ttf, PTZ56F.ttf and their web formats) beside PT Serif's; no
  source. google/fonts has no source block for this family.

## Previous investigation

## PT Serif Caption — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Summary

No canonical upstream GitHub repository was found for PT Serif Caption. PT Serif Caption is an optical size variant of PT Serif by ParaType, sharing the same provenance and lack of public repository. No METADATA.pb changes were made.

### Designer

ParaType (yakupov@paratype.com). Copyright 2010 ParaType Ltd.

### Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry.
- **GitHub organization**: The `paratype` GitHub organization exists but contains no font source repositories.
- **GitHub search**: No canonical designer-owned repository was found for PT Serif Caption or the PT font family as a whole.
- **Third-party mirrors**: No packaging mirrors were found for PT Serif Caption specifically.

### Context

PT Serif Caption is the small-text optical size variant of PT Serif, designed for use at small point sizes. It shares the same design heritage as PT Serif — part of the PT (Public Type) family commissioned by the Federal Agency on Press and Mass Communications of the Russian Federation, released in 2010 by Paratype. The Google Fonts version includes Regular and Italic variants.

### Verdict

**No canonical upstream repository found.** PT Serif Caption is distributed by ParaType but no public source repository exists. No METADATA.pb changes were made.
