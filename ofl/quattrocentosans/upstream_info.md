# Quattrocento Sans

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Quattrocento Sans (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/quattrocentosans.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  QuattrocentoSans-{Bold,BoldItalic,Italic,Regular}.ttf, the fonts Google Fonts ships,
  with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/quattrocentosans at `7fb6e41bc0fa`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools,
including this family's plan `plans/quattrocentosans.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`7fb6e41bc0fa` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/QuattrocentoSans-Bold-TTF.vfb,
  src/QuattrocentoSans-BoldItalic-TTF.vfb, src/QuattrocentoSans-Italic-TTF.vfb,
  src/QuattrocentoSans-Regular-TTF.vfb, a FontLab import of the shipped fonts, not a
  source: Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Quattrocento Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `quattrocentosans/src/`

### Source Files

The `quattrocentosans/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): QuattrocentoSans-Bold-OTF.vfb, QuattrocentoSans-Bold-TTF.vfb, QuattrocentoSans-Bold.vfb, QuattrocentoSans-BoldItalic-OTF.vfb, QuattrocentoSans-BoldItalic-TTF.vfb, QuattrocentoSans-BoldItalic.vfb, QuattrocentoSans-Italic-OTF.vfb, QuattrocentoSans-Italic-TTF.vfb, QuattrocentoSans-Italic.vfb, QuattrocentoSans-Regular-OTF.vfb, QuattrocentoSans-Regular-TTF.vfb, QuattrocentoSans-Regular.vfb
- **OTF** (compiled binaries, not design sources): QuattrocentoSans-Bold.otf, QuattrocentoSans-BoldItalic.otf, QuattrocentoSans-Italic.otf, QuattrocentoSans-Regular.otf

### Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

### Investigation Details

The following searches were performed:

- Searched GitHub for "quattrocento sans font" and "QuattrocentoSans" repositories.
- Checked the `impallari` GitHub account — Pablo Impallari has 26 public repositories, but none for Quattrocento Sans. (Same investigation as Quattrocento above.)
- Searched for repos with "QuattrocentoSans" in the name — found only `librefonts/quattrocentosans` (a librefonts mirror — skipped per policy) and `google-fonts-bower/quattrocentosans-bower` (a Bower packaging mirror).
- Checked the `OpenMandrivaAssociation/texlive-quattrocento` repo found in search — this is a LaTeX package, not a font source repository.

No canonical upstream repository with font source files was found.

### Notes

- Designer: Pablo Impallari (Impallari Type), with contributions from Brenda Gallo, Rodrigo Fuenzalida, and kerning by Igino Marini
- Quattrocento Sans is the companion sans-serif to Quattrocento
- Same situation as Quattrocento: Impallari's GitHub account does not include a source repository for this family
