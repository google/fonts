# Reenie Beanie

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Reenie Beanie as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/reeniebeanie.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from ReenieBeanie.ttf, the
  font Google Fonts ships, with babelfont 58eedc8 (felipesanches/babelfont-rs branch
  2026-10-22: simoncozens/babelfont-rs main plus the TTF reader changes proposed to it):
  its TTF reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/reeniebeanie at `ffb157a38ce6`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/reeniebeanie.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`ffb157a38ce6` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released font is hinted by hand in VTT (googlefontdirectory-hg kept the VTT
  project, ofl/reeniebeanie/src/ReenieBeanie-VTT.ttf at 52f780bc9d19). These sources
  carry no TrueType instructions, so the build is hinted by ttfautohint: the outlines,
  spacing and layout are the release's, its rendering at small sizes under a TrueType
  interpreter is not. Hinting is not compared by the gates.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Reenie Beanie — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `reeniebeanie/src/`

### Source Files

The `reeniebeanie/src/` directory contains compiled binaries and web font formats, but no editable design sources.

- **TTF** (compiled binaries, not design sources): ReenieBeanie-VTT.ttf

### Buildability

No design source files are available in this directory. The font cannot be rebuilt from the files present here.

### Investigation Details

GitHub was searched for "Reenie Beanie" and "James Grieshaber Typeco". The font was created by James Grieshaber of Typeco (`james@typeco.com`). No GitHub account for "typeco" or "james grieshaber" was found. No repository was identified for this font on GitHub or any other public code hosting platform.

### Notes

The font was released in 2010 and is a handwriting-style typeface. At the time of its creation, it was common for font designers to distribute fonts without publishing the source files publicly. No public source repository was found.
