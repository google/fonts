# Short Stack

**Model**: Claude Opus 5.5
**Date**: 2026-11-20

Sources modernized 2026-11: https://github.com/googlefonts/shortstack held only FontLab
(`.vfb`) and FontForge (`.sfd`) files, and the `.sfd` files are imports of the fonts
Google Fonts ships, so those fonts were converted to Glyphs (`.glyphs`) sources, which
build with gftools-builder and fontc. The repository, commit and config are in the
`source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Short Stack with
https://github.com/googlefonts/googlefontdirectory-hg at `52f780bc9d19` recorded as its
source. That repository and https://github.com/googlefonts/shortstack (at
`2632e2b14af8`) hold the same files: `src/ShortStack-Regular-TTF.sfd`,
`src/ShortStack-Regular.vfb`. The `.sfd` files are imports of the shipped fonts, and the
family could not be built with fontc.

## Actions taken

- The work was done on top of the history of https://github.com/googlefonts/shortstack,
  in a pull request merged into its default branch.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from ShortStack-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/shortstack at `72c526a1a473`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts cc39c4c2c304 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF, hinting), 1 style. Those tools,
including this family's plan `plans/shortstack.json`:
https://github.com/felipesanches/gf-source-modernization at `2648f55`.

`72c526a1a473` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Short Stack -- Upstream Source Investigation

**Model**: Claude Opus 4.6

### Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `shortstack/src/`

### Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 1 SFD file (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

#### Key source files

- `ShortStack-Regular.vfb` (VFB, proprietary)
- `ShortStack-Regular-TTF.sfd` (SFD, FontForge)
- `ShortStack-Regular.otf` (compiled binary)

### Designer

James Grieshaber

### Search Results

- Searched `short stack font sorkin` on GitHub: 0 results
- Searched `shortstack font` on GitHub: 0 results
- Searched `short stack font grieshaber` on GitHub: 0 results
- No Sorkin Type Co or James Grieshaber GitHub presence found with Short Stack sources
