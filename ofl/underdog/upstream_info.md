# Underdog

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Underdog (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/underdog.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Underdog-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/underdog at `7fd152d75041`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/underdog.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`7fd152d75041` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Underdog-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Underdog — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Sergey Steblina, Jovanny Lemonad

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `underdog/src/`.

#### Source Files

- **VFB (FontLab)**: Underdog-Regular-OTF.vfb, Underdog-Regular-TTF.vfb
- **OTF (compiled)**: Underdog-Regular.otf
- **Adobe Illustrator**: ai_files/underdog_f.ai, ai_files/underdog_f2_extra.ai, ai_files/underdog_letters_correction.ai
- **Other**: test_files/cyr.jpg, test_files/cyr_caps.jpg, test_files/latin.jpg, test_files/latin_caps.jpg

Sources are in VFB format (FontLab, proprietary), which is not buildable with gftools-builder.

### Investigation Details

Underdog was designed by Sergey Steblina and technically engineered and published by Jovanny Lemonad (lemonad@jovanny.ru). It is an informal display typeface with Cyrillic and Latin support.

The following searches were conducted:

1. **steblina GitHub**: A GitHub account `steblina` was found but contained only two personal/unrelated repositories (miniature-tribble, theme-binary).
2. **lemonad GitHub**: The GitHub account `lemonad` (Jovanny Lemonad) was found but its repositories were all unrelated to font design (coding exercises, course projects, moodle plugins, web apps, etc.).
3. **jovanny GitHub**: A GitHub user `jovanny` was found but had only one repository (`repositorio`) unrelated to fonts.
4. **alexeiva GitHub**: Examined as a related Russian type designer with Cyrillic fonts on Google Fonts, but no Underdog repository was found.
5. **Repository name search**: Searches for "underdog font", "underdog cyrillic", and related terms returned no font source repositories.

Underdog was published to Google Fonts in 2012 but the source files have not been made publicly available on GitHub or any other discoverable platform. Neither of the two credited designers has published font source repositories under their GitHub accounts.
