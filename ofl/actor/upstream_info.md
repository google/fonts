# Actor

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Actor (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/actor.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Actor-Regular.ttf, the
  font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/actor at `ddd45a44c902`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/actor.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`ddd45a44c902` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/actor at b1617e5929c9a78c56bbbe056b471cfdbdc13c50:
  src/Actor-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/actor"
      commit: "b1617e5929c9a78c56bbbe056b471cfdbdc13c50"
    }

## Previous investigation

## Actor

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Thomas Junold
**METADATA.pb path**: `ofl/actor/METADATA.pb`

### Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/actor |
| Commit | `b1617e5929c9a78c56bbbe056b471cfdbdc13c50` |
| Config YAML | -- |
| Branch | `master` |

### How the Repository URL Was Found

The METADATA.pb file contains **no source block** at all -- it only has the font name, designer, license, category, date_added (2011-08-03), font definition, and subsets. The repository URL `https://github.com/librefonts/actor` was discovered through research of the `librefonts` GitHub organization, which hosts mirrors/archives of many early Google Fonts projects. The URL has been verified as accessible (HTTP 200).

The copyright notice in METADATA.pb credits Thomas Junold (`hallo@buerofueraufmerksamkeit.de`), and the librefonts/actor repository contains TTX decompositions and VFB source files matching this font.

### How the Commit Hash Was Identified

The upstream repo contains only **one commit**:

- `b1617e5929c9a78c56bbbe056b471cfdbdc13c50` (2014-10-17): "update .travis.yml"

Since this is the sole commit in the repository, it is the only possible reference point. The font in google/fonts was last modified in the initial mass migration commit (`90abd17b4f97`, 2015-03-07: "Initial commit"), predating any structured onboarding process. There is no PR reference or packager commit to trace.

The google/fonts directory has had 5 subsequent commits, but all were metadata-only changes (language support, METADATA.pb cleanup, METADATA.json removal) -- none modified the actual .ttf file.

### How Config YAML Was Resolved

**No config.yaml exists or can be created** with the current source files:

- The upstream repo contains only **VFB** (FontLab 5 proprietary binary) source files:
  - `src/Actor-Regular-TTF.vfb`
  - `src/Actor-Regular.vfb`
- There are **no modern buildable sources** (`.glyphs`, `.ufo`, `.designspace`)
- No override `config.yaml` exists in `ofl/actor/` in google/fonts
- The remaining repo contents are TTX table dumps (decomposed binary representations) and metadata files

The font would need to be converted from VFB to a modern format (e.g., `.glyphs` or `.ufo`) before any gftools-builder configuration could be created.

### Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:27:40 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Actor-Regular-TTF.vfb`, `src/Actor-Regular.vfb` (VFB binary format only -- not buildable with gftools)

### Confidence

**High**: The repository URL is confirmed valid, and with only one commit in the repo, there is no ambiguity about the commit reference. However, the practical usefulness is limited because VFB files cannot be built with gftools-builder, and the font has not been updated since its initial import into google/fonts in 2015.

### Open Questions

1. Should the METADATA.pb be updated to include a `source { repository_url }` block pointing to `https://github.com/librefonts/actor`?
2. Is there a plan to convert the VFB sources to `.glyphs` or `.ufo` format to enable modern builds?
3. Does Thomas Junold have the original editable sources in a more modern format?
