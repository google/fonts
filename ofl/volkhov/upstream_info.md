# Volkhov

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Volkhov (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/volkhov.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Volkhov-{Bold,BoldItalic,Italic,Regular}.ttf, the fonts Google Fonts ships, with
  babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/volkhov at `d1b0e055d066`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools,
including this family's plan `plans/volkhov.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`d1b0e055d066` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Volkhov-Bold-TTF.vfb,
  src/Volkhov-BoldItalic-TTF.vfb, src/Volkhov-Italic-TTF.vfb,
  src/Volkhov-Regular-TTF.vfb, a FontLab import of the shipped fonts, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Volkhov — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Cyreal

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `volkhov/src/`.

#### Source Files

- **VFB (FontLab)**: Volkhov-Bold-OTF.vfb, Volkhov-Bold-TTF.vfb, Volkhov-Bold.vfb, Volkhov-BoldItalic-OTF.vfb, Volkhov-BoldItalic-TTF.vfb, Volkhov-BoldItalic.vfb, Volkhov-Italic-OTF.vfb, Volkhov-Italic-TTF.vfb, Volkhov-Italic.vfb, Volkhov-Regular-OTF.vfb, Volkhov-Regular-TTF.vfb, Volkhov-Regular.vfb
- **SFD (FontForge)**: Volkhov-BoldItalic-TTF.sfd, Volkhov-Italic-TTF.sfd
- **OTF (compiled)**: Volkhov-Bold-OTF.otf, Volkhov-BoldItalic-OTF.otf, Volkhov-Italic-OTF.otf, Volkhov-Regular-OTF.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

### Investigation Details

The [cyrealtype GitHub organization](https://github.com/cyrealtype) was identified as the correct maintainer (linked from `www.cyreal.org`). A `cyrealtype/Volkhov` repository exists on GitHub but contains only a single `README.md` file with no font source files. The repository appears to be a placeholder that was never populated with source files. The older `cyrealtype/Cyrealfonts` archive also did not contain Volkhov source files. No UFO, Glyphs, or other open-format source files were found in any publicly accessible repository.
