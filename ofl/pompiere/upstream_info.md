# Pompiere

**Model**: Claude Opus 5.5
**Date**: 2026-11-20

Sources modernized 2026-11: https://github.com/googlefonts/pompiere held only FontLab
(`.vfb`) and FontForge (`.sfd`) files, and the `.sfd` files are imports of the fonts
Google Fonts ships, so those fonts were converted to Glyphs (`.glyphs`) sources, which
build with gftools-builder and fontc. The repository, commit and config are in the
`source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Pompiere with https://github.com/googlefonts/googlefontdirectory-hg
at `52f780bc9d19` recorded as its source. That repository and
https://github.com/googlefonts/pompiere (at `ba67f8d068ad`) hold the same files:
`src/Pompiere-Regular-TTF.sfd`, `src/Pompiere-Regular.vfb`. The `.sfd` files are imports
of the shipped fonts, and the family could not be built with fontc.

## Actions taken

- The work was done on top of the history of https://github.com/googlefonts/pompiere, in
  a pull request merged into its default branch.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from Pompiere-Regular.ttf, the font Google
  Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/pompiere at `5fd68f82e69f`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts cc39c4c2c304,
under tools/table_gate.py and tools/functional_gate.py: Pompiere-Regular: 0 blocking
rows; functionally different in shaping. Those tools, including this family's plan
`plans/pompiere.json`: https://github.com/felipesanches/gf-source-modernization at
`b963246`.

`5fd68f82e69f` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- Combining marks are placed by the shaper from glyph bounding boxes (the font has no
  GPOS). 174 of the released font's glyf bounding boxes are stale, while a compiled
  font's are exact, so 25596 of 26656 base+mark pairs place the mark differently, by up
  to 35 units (of 2048) (tools/probes/hg_forks_from_binary).

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Pompiere — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-25

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/pompiere/src/` |
| **Buildable** | No — VFB and SFD only |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository that was the canonical host for Google Fonts
from 2010 to 2013.

#### Source Files

- `Pompiere-Regular.vfb` — FontLab VFB (proprietary, not buildable with gftools)
- `Pompiere-Regular-TTF.sfd` — FontForge SFD (open format, not supported by gftools-builder)
- `Pompiere-Regular.otf` — compiled binary, not a design source
- `METADATA_comments.txt` — metadata comments

Design sources include a VFB (proprietary) and an SFD (open but not supported by gftools-builder).

### Notes

Designer: Karolina Lach. Script: Latin. Category: DISPLAY (sans serif stroke). Published by Sorkin Type Co.

### Verdict

**Sources found in googlefontdirectory-hg but not buildable.** Neither VFB nor SFD formats are supported by gftools-builder. No config is possible.
