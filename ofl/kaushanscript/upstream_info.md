# Kaushan Script

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Kaushan Script (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/kaushanscript.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  KaushanScript-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/kaushanscript at `403737c6ee2e`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/kaushanscript.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`403737c6ee2e` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/kaushanscript at
  b1b7451878d44084faa32e3bcc5ce043f4d1acf4: src/KaushanScript-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/kaushanscript"
      commit: "b1b7451878d44084faa32e3bcc5ce043f4d1acf4"
    }

## Previous investigation

## Kaushan Script — Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/librefonts/kaushanscript |
| Commit | `b1b7451878d44084faa32e3bcc5ce043f4d1acf4` |
| Confidence | Medium |

### Source Types

The repository contains TTX-decompiled sources only, in the `src/` directory.

### Build Compatibility

Not buildable with gftools-builder. The TTX files are decompiled binary font dumps, not original editable design sources. No Impallari/Kaushan repository was found on GitHub (Pablo Impallari's repos for this font appear to be unavailable).

### Investigation Notes

This is a librefonts mirror repository containing TTX-decompiled binary dumps. Kaushan Script was designed by Pablo Impallari, but no original repository with editable design sources was found on GitHub.

**Note on librefonts TTX mirrors**: These repositories contain TTX (XML) representations of the compiled font binaries. They are mechanically decompiled from the .ttf files and do not represent original design sources. They cannot be used for font development or rebuilding with gftools-builder.

The binary in google/fonts dates from the initial commit (2015-03-07).

A source block was added to METADATA.pb pointing to this repository and commit.

### Confidence: Medium

Librefonts TTX mirror; original design sources are not available.
