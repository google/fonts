# Prosto One

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Prosto One (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/prostoone.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from ProstoOne-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/prostoone at `3791f69d7f70`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/prostoone.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`3791f69d7f70` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/ProstoOne-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Prosto One — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/prostoone/src/` |
| **Buildable** | No — VFB only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

#### Source Files

- `ProstoOne-Regular-OTF.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `ProstoOne-Regular-TTF.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `ProstoOne-Regular-kern_classes.flc` — FontLab kerning classes file
- `ProstoOne-Regular-Sketches.ai` — Adobe Illustrator sketch file
- `ProstoOne-Regular.otf` — compiled binary, not a design source
- `METADATA_comments.txt` — metadata comments

Design sources are VFB files (FontLab, proprietary), accompanied by supporting FontLab kerning data and Illustrator sketches.

### Designers

- Jovanny Lemonad (lemonad@jovanny.ru, http://www.jovanny.ru) — original type designer
- Pavel Emelyanov (zakachka2006@mail.ru) — original type designer

### Repository Investigation

- **Checked cache**: No cached entry in the upstream repo cache.
- **GitHub search**: Searches for "Prosto One font", "jovanny lemonad font", and "ProstoOne" returned no relevant results. A GitHub user `jovanny` exists but has only one unrelated repo (`jovanny/repositorio`).
- **jovanny.ru**: The website was unreachable (connection refused) at time of previous investigation.
- **Google Fonts history**: The git log for `ofl/prostoone` in google/fonts showed no upstream commit references.
- **FONTLOG evidence**: The FONTLOG does not reference any source repository.

### Verdict

**No canonical upstream repository found; sources in googlefontdirectory-hg are not buildable.** Only VFB (FontLab) sources exist. No open-format sources are available. No gftools-builder config is possible.
