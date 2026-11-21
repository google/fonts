# Spicy Rice

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Spicy Rice (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/spicyrice.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from SpicyRice-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/spicyrice at `5f2a867790a4`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: SpicyRice-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/spicyrice.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`5f2a867790a4` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The build's GSUB numbers or packs some lookups differently from the release's (fontc
  places a lookup that only a contextual lookup calls, and packs chained contextual
  rules, its own way: gfonts-ai-usage-report 22-fontc-problems, problems 12 and 13);
  every rule is the same and the text shapes identically (tools/functional_gate.py).
  Decided 2026-10-02: problems that need fontc are disclosed and fixed in fontc later.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/SpicyRice-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Spicy Rice -- Upstream Source Investigation

**Model**: Claude Opus 4.6

### Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `spicyrice/src/`

### Source Files

The source directory contains: 3 VFB files (FontLab, proprietary format); 1 compiled binary (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

#### Key source files

- `SpicyRice-Regular-OTF.vfb` (VFB, proprietary)
- `SpicyRice-Regular-TTF.vfb` (VFB, proprietary)
- `SpicyRice-Regular.vfb` (VFB, proprietary)
- `SpicyRice-Regular.otf` (compiled binary)

### Research

Spicy Rice was designed by Brian J. Bonislawsky for Astigmatic (AOETI)
(astigma@astigmatic.com) and released in 2011. Searches on GitHub for
Astigmatic-related repositories and for the Spicy Rice font source files
returned no relevant results. The Astigmatic GitHub organization did not
exist, and no personal GitHub account for Brian Bonislawsky was found with
font source repositories.


### Notes

The designer listed in METADATA.pb is Astigmatic. Spicy Rice is described as
a casual display font with festive flair. It supports Latin and Latin Extended
character sets and is licensed under the SIL Open Font License.
