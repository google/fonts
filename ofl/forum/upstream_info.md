# Forum

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Forum (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/forum.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Forum-Regular.ttf, the
  font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/forum at `af5cedec1cf3`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/forum.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`af5cedec1cf3` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/forum at e8efc0bceef3b98cf32f722bf637f3c110f68a37:
  src/Forum-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/forum"
      commit: "e8efc0bceef3b98cf32f722bf637f3c110f68a37"
    }

## Previous investigation

## Investigation: Forum

### Summary

- **Family name**: Forum
- **Designer**: Denis Masharov
- **Date added to Google Fonts**: 2011-07-06
- **Repository URL**: https://github.com/librefonts/forum
- **Commit**: e8efc0bceef3b98cf32f722bf637f3c110f68a37
- **Config**: none (VFB-only sources)
- **Status**: complete (no buildable sources)
- **Confidence**: HIGH

### METADATA.pb (current)

The current METADATA.pb has no `source` block. The font is categorized as DISPLAY/SERIF with subsets: menu, cyrillic, cyrillic-ext, latin, latin-ext.

### Upstream Repository

- **URL**: https://github.com/librefonts/forum (verified accessible, HTTP 200)
- **Type**: librefonts archive repo (TTX decomposition + VFB sources)
- **Single commit**: `e8efc0b` by hash3g (2014-10-17) -- "update .travis.yml"
- **Remote**: `origin` at `https://github.com/librefonts/forum`
- **Status**: clean, up to date with origin/master

#### Repository Contents

The repo contains:
- **Root**: TTX decomposition files of `Forum-Regular.ttf` (split by table), plus DESCRIPTION.en_us.html, METADATA.json, OFL.txt, menusubset-forum.ff, .travis.yml
- **src/**: `Forum-Regular.vfb` (258,436 bytes), `Forum-Regular-TTF.vfb` (268,592 bytes), OTF TTX decomposition files, METADATA_comments.txt, VERSIONS.txt

#### Source File Analysis

- **VFB files** (FontLab Studio binary format): These are the original design sources but are not buildable with gftools-builder or fontc.
- **No .glyphs, .ufo, .designspace, or .sfd files** exist in the repo.
- **No config.yaml** exists in the repo.
- The TTX files are decompositions of the compiled binary, not editable design sources.
- VERSIONS.txt confirms: "Forum-Regular.ttf: Version 1.000"

### google/fonts History

The font binary (`Forum-Regular.ttf`, 303,316 bytes) has been unchanged since the initial commit in google/fonts:
- **Initial commit**: `90abd17b` (2015-03-07) by Dave Crossland -- "Initial commit" -- blob hash `961dffbb`
- **Current HEAD**: Same blob hash `961dffbb` -- the binary has never been modified
- The font was originally part of the Google Web Fonts directory (dateAdded: 2011-07-06) and was migrated to the google/fonts repo in the 2015 initial import.

#### Font Metadata (from TTX name table)

- Copyright: "Copyright (c) 2011, Denis Masharov"
- Version: 1.000
- Created: Thu Jun 30 08:26:00 2011
- Modified: Thu Jun 30 08:28:24 2011
- Unique ID: "DenisMasharov: Forum: 2011"

### Commit Hash Verification

The upstream repo has only a single commit (`e8efc0b`), so this is trivially the correct reference. The repo was created on 2014-10-17 as a librefonts archive containing the TTX decomposition and VFB sources of the original font. Since the google/fonts binary has never been updated, this single commit encompasses all the source material that corresponds to the font in the catalog.

### Build Configuration

No config.yaml is needed. The upstream repo contains only VFB sources (FontLab binary format), which are not compatible with gftools-builder or fontc. There are no .glyphs, .ufo, .designspace, or .sfd source files that could be used for rebuilding.

### Proposed Source Block

```
source {
  repository_url: "https://github.com/librefonts/forum"
  commit: "e8efc0bceef3b98cf32f722bf637f3c110f68a37"
}
```

No `config_yaml` field is needed since there are no buildable sources.
