# Sansation

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Sansation as binaries only (google/fonts at commit `2eb0b48d5f76`).
No source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/sansation.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from
  Sansation-{Bold,BoldItalic,Italic,Light,LightItalic,Regular}.ttf, the fonts Google
  Fonts ships, with babelfont ed59a63 (felipesanches/babelfont-rs branch 2026-10-22:
  simoncozens/babelfont-rs main plus the TTF reader changes proposed to it): its TTF
  reader, no filters. sources/config.yaml: productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/sansation at `074dd0f8c369`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Sansation-Bold: 3 blocking rows;
functionally equivalent Sansation-BoldItalic: 3 blocking rows; functionally equivalent
Sansation-Italic: 3 blocking rows; functionally equivalent Sansation-Light: 3 blocking
rows; functionally equivalent Sansation-LightItalic: 4 blocking rows; functionally
different in line_spacing Sansation-Regular: 3 blocking rows; functionally equivalent.
Those tools, including this family's plan `plans/sansation.json`:
https://github.com/felipesanches/gf-source-modernization at `99dd9c3`.

`074dd0f8c369` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts kern with a legacy `kern` table (their GPOS has no kern feature);
  these sources kern through a GPOS kern feature, which is how fontc builds kerning.
  HarfBuzz shapes all 1097 kerned pairs of every style alike in both
  (tools/probes/binary_to_source/results/legacy-kern-pairs.txt in the evidence
  repository). Decided 2026-10-01: releases with an old kern table are accepted and
  disclosed.
- Sansation Light Italic is flagged italic in the release (fsSelection ITALIC, macStyle
  italic) with an italic angle of 0, as all of the family's italics are. A Glyphs source
  cannot state that to fontc 1.0.0, which flags a static font italic only for a nonzero
  italic angle or a master named Italic or Bold Italic, so the build is flagged regular.
  Decided 2026-10-02: problems that need fontc are disclosed, and fixed later.
- The release's post table names two glyphs of Sansation Light Italic `ffi`; the second,
  which the f f j ligature substitutes, is `ffi.1` in the source, as fontTools reads it.
  The table gate, which pairs glyphs by name, therefore compares the release's first
  `ffi` with the source's and reports its advance (1618 against 1628) as an hmtx
  difference; the glyph the release draws under that name is unchanged.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Sansation — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sansation/src/`

### Source Files

The `sansation/src/` directory contains only non-source files (menu subsets, metadata). No design source files are present.

- **Other**: menusubset-sansation.ff

### Buildability

No design source files are available in this directory. The font cannot be rebuilt from the files present here.

### Designer

- **Designer**: Bernd Montag (berndmontag@gmx.de)

### Investigation Details

The following searches and checks were performed:

- Searched GitHub for `Sansation font` — no relevant results (returned unrelated sans-serif fonts)
- Searched GitHub for `Sansation font Bernd Montag` — no results
- Checked `repos/googlefonts/SansationFont` — not found
- Checked `repos/berndmontag/Sansation` — not found
