# New Rocker

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped New Rocker (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/newrocker.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from NewRocker-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/newrocker at `17d0c2c70383`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/newrocker.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`17d0c2c70383` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/NewRocker-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## New Rocker — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/newrocker/src/`
- **Buildable**: No — legacy formats only (.vfb)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source Files

| File | Type |
|------|------|
| `NewRocker-Regular-OTF.vfb` | FontLab VFB source, OTF variant (proprietary, not buildable with gftools) |
| `NewRocker-Regular-TTF.vfb` | FontLab VFB source, TTF variant (proprietary, not buildable with gftools) |
| `NewRocker-Regular.vfb` | FontLab VFB source (proprietary, not buildable with gftools) |
| `NewRocker-Regular.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

All three VFB files are FontLab Studio 5 proprietary format sources. No gftools-builder compatible sources (UFO, Glyphs, designspace) are available.

### Designer and Provenance

- **Designer**: Pablo Impallari, Brenda Gallo, and Rodrigo Fuenzalida (Impallari Type), v1.0 released 28 November 2012
- The `impallari` GitHub account has 26 repositories but none named `New-Rocker`, `NewRocker`, or similar
- The designer website `impallari.com` and the project page `impallari.com/projects/overview/newrocker` are currently unreachable (HTTP 523)

### Additional Mirror

A third-party mirror exists at https://github.com/librefonts/newrocker (latest commit `1dae287` on 2014-10-17, "update .travis.yml"). It contains the same VFB sources plus TTX decompilations. The repo includes a legacy fontbakery-era `.travis.yml`, `config.yaml`, and `Makefile`, all using the deprecated `fontbakery-build.py` workflow which is not compatible with modern gftools builds.

### Build System

Not applicable — only VFB sources exist, which require FontLab Studio.

### config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

### Notes

- The Google Fonts binary dates to 2012 (v1.0) and has never been updated.
- The FONTLOG references `http://www.impallari.com/projects/overview/newrocker` as the project page, which is currently unreachable.
- A modern rebuild would require converting the VFB files (e.g., via FontLab or vfb2ufo) to produce gftools-compatible sources.
