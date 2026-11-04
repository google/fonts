# Miltonian

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Miltonian (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/miltonian.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Miltonian-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/miltonian at `3e30828a0c79`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/miltonian.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`3e30828a0c79` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/impallari/Miltonian at 95d180e8744380f93a8437226e58032d484882c7:
  source/Miltonian-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/impallari/Miltonian"
      commit: "95d180e8744380f93a8437226e58032d484882c7"
    }

## Previous investigation

## Miltonian — Source Repository Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| Repository | [impallari/Miltonian](https://github.com/impallari/Miltonian) |
| Commit | `95d180e8744380f93a8437226e58032d484882c7` |
| Date | 2016-01-15 |
| Confidence | High |

### Investigation

The METADATA.pb for Miltonian had no source block. The upstream repository was identified as impallari/Miltonian, by designer Pablo Impallari. The repository contains sources for both Miltonian and Miltonian Tattoo.

#### Source Types Available

- **VFB** (FontLab): `source/Miltonian-Regular.vfb`, `source/Miltonian-Regular-OTF.vfb`, `source/Miltonian-Regular-TTF.vfb`
- **SFD**: Referenced in earlier investigations but VFB is the canonical format
- **Binary fonts**: `fonts/TTF/Miltonian-Regular-TTF.ttf`, `fonts/OTF/Miltonian-Regular.otf`
- **Documentation**: `FONTLOG.txt`, `README.md`

#### Buildability

VFB-only editable sources (FontLab Studio proprietary format). No `.glyphs`, `.ufo`, or `.designspace` files are present. Not directly buildable with gftools-builder.

#### Notes

- The repository covers both Miltonian and Miltonian Tattoo families
- Co-designer credit: Igino Marini (ikern.com) for kerning
- The designer Pablo Impallari passed away in 2021; the repo is unlikely to receive further updates
- Commit `95d180e` (2016-01-15, "v1.7") is the latest content commit, matching the google/fonts update (2016-01-25)
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

#### Actions Taken

A source block was added to METADATA.pb pointing to commit `95d180e` at impallari/Miltonian.
