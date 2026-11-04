# Hermeneus One

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Hermeneus One (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/hermeneusone.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  HermeneusOne-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/hermeneusone at `622d1cf409f1`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/hermeneusone.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`622d1cf409f1` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/HermeneusOne-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Hermeneus One -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

### Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `hermeneusone/src/`

#### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `HermeneusOne-Regular.vfb` | FontLab binary | No |
| `HermeneusOne-Regular-OTF.vfb` | FontLab binary | No |
| `HermeneusOne-Regular-TTF.vfb` | FontLab binary | No |
| `HermeneusOne-Regular.otf` | Compiled binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata | N/A |

The source directory contains three VFB files (FontLab proprietary binary format) and a compiled OTF binary. VFB files cannot be processed by gftools-builder, fontmake, or fontc. No `.glyphs`, `.ufo`, or `.designspace` files exist.

### Designer

Pablo Impallari and Rodrigo Fuenzalida. Hinting by Igino Marini (v1.2, November 2011). Copyright: "(c) 2012, Pablo Impallari (www.impallari.com|impallari@gmail.com) and Rodrigo Fuenzalida (www.rfuenzalida.com), with Reserved Font Name Hermeneus."

Hermeneus One is a Grecian-style serif display font. The FONTLOG.txt references the project page at `http://www.impallari.com/projects/overview/hermeneus`.

### librefonts Mirror

A mirror exists at `https://github.com/librefonts/hermeneusone` with a single commit:
- `20a3262` (2014-10-17) by hash3g: "update .travis.yml"

The repo contains the same VFB sources, TTX table dumps, and metadata files. It adds no additional design sources beyond what is in googlefontdirectory-hg.

### google/fonts History

The font binary was added in the initial commit `90abd17b4` (2015-03-07, author: Dave Crossland). The font file (`HermeneusOne-Regular.ttf`, 132940 bytes) has never been modified since.

### Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- All source files are VFB format (FontLab proprietary binary), not supported by gftools-builder
- To build from these sources, VFB would need conversion to UFO or .glyphs format first
- A config.yaml cannot be created for this family with the current source formats
