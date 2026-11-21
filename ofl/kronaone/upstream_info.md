# Krona One

**Model**: Claude Opus 5.5
**Date**: 2026-11-20

Sources modernized 2026-11: https://github.com/googlefonts/kronaone held only FontLab
(`.vfb`) and FontForge (`.sfd`) files, and the `.sfd` files are imports of the fonts
Google Fonts ships, so those fonts were converted to Glyphs (`.glyphs`) sources, which
build with gftools-builder and fontc. The repository, commit and config are in the
`source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Krona One with
https://github.com/googlefonts/googlefontdirectory-hg at `52f780bc9d19` recorded as its
source. That repository and https://github.com/googlefonts/kronaone (at `72c7f1c10ccf`)
hold the same files: `src/KronaOne-Regular-OTF.sfd`, `src/KronaOne-Regular-TTF.sfd`,
`src/KronaOne-Regular.vfb`. The `.sfd` files are imports of the shipped fonts, and the
family could not be built with fontc.

## Actions taken

- The work was done on top of the history of https://github.com/googlefonts/kronaone, in
  a pull request merged into its default branch.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from KronaOne-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/kronaone at `a7b07801999d`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts cc39c4c2c304 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF, hinting), 1 style. Those tools,
including this family's plan `plans/kronaone.json`:
https://github.com/felipesanches/gf-source-modernization at `2648f55`.

`a7b07801999d` is the equivalence commit: its build is functionally equivalent to the
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

## Investigation: Krona One

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/kronaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files (5)

| File | Format | Notes |
|------|--------|-------|
| `KronaOne-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KronaOne-Regular-OTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KronaOne-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KronaOne-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline.

### Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com eben@eyebytes.com) with Reserved Font Name 'Krona'."

The DESCRIPTION.en_us.html credits "Sorkin Type Co" and mentions the source files were available from "Google Code" (http://code.google.com/p/googlefontdirectory/), which is no longer available. The FONTLOG.txt confirms the Sorkin Type Co origin with contact email `sorkineben@gmail.com`.

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/kronaone` containing only TTX dumps. The googlefontdirectory-hg monorepo preserves the more complete VFB and SFD design sources that the librefonts mirror did not retain. The original Google Code hosting is defunct.

### Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. The original Google Code hosting is defunct, and no upstream GitHub repository is known for this family.
