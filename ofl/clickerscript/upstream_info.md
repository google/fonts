# Clicker Script

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Clicker Script (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/clickerscript.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  ClickerScript-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/clickerscript at `3a25c83b8d44`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts
2eb0b48d5f76, under tools/table_gate.py and tools/functional_gate.py:
ClickerScript-Regular: 2 blocking rows; functionally equivalent. Those tools, including
this family's plan `plans/clickerscript.json`:
https://github.com/felipesanches/gf-source-modernization at `d6a61f4`.

`3a25c83b8d44` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/clickerscript at
  f8f050697a52a8e2e10009db97c1a18b0099bb6f: src/ClickerScript-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/clickerscript"
      commit: "f8f050697a52a8e2e10009db97c1a18b0099bb6f"
    }

## Previous investigation

## Clicker Script - Investigation Report

### Source Data

| Field | Value |
|-------|-------|
| Family Name | Clicker Script |
| Designer | Astigmatic |
| Repository URL | https://github.com/librefonts/clickerscript |
| Commit Hash | `f8f050697a52a8e2e10009db97c1a18b0099bb6f` |
| Config YAML | None (no buildable sources) |
| Status | Missing Config (no buildable sources) |
| Date Added | 2012-11-11 |

### How URL Found

The repository URL `https://github.com/librefonts/clickerscript` was already documented in the source block of METADATA.pb. The `librefonts` organization on GitHub hosts many Google Fonts families that were originally contributed as part of the open-source font initiative.

### How Commit Determined

The commit `f8f0506` ("update .travis.yml") is the only commit in the repository (single-commit repo). The source block was added as part of a batch commit (`9a14639f3` "Add source blocks to 602 more METADATA.pb files") that documented repository URLs and commit hashes for families without config.yaml.

### Config YAML Status

- **No config.yaml in upstream**: Not applicable -- the repository does not contain any modern buildable source files.
- **No override config.yaml**: There is no override config.yaml in `ofl/clickerscript/` in google/fonts.

Available source files at the recorded commit:
- `src/ClickerScript-Regular.vfb` (FontLab VFB format)
- `src/ClickerScript-Regular-OTF.vfb` (FontLab VFB format)
- `src/ClickerScript-Regular-TTF.vfb` (FontLab VFB format)
- Multiple `.ttx` files (XML font table dumps)

The VFB format is proprietary to FontLab and cannot be used with gftools-builder/fontmake. There are no `.glyphs`, `.ufo`, or `.designspace` files available for modern font building.

### Verification

- Commit hash `f8f0506` verified to exist in upstream repo (it is the only commit)
- Repository contains only legacy FontLab VFB sources and TTX dumps
- No modern buildable sources exist anywhere in the repo
- The font in google/fonts is a static single-weight Regular font

### Confidence Level

**High** - The repository URL and commit hash are verified. The status of "missing_config" is correct because no config.yaml can be created for legacy VFB sources.

### Open Questions

- To rebuild this font with modern tools, the VFB sources would need to be converted to UFO or Glyphs format. This is outside the scope of source documentation.
