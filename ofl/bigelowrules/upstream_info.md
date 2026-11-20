# Bigelow Rules

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Bigelow Rules (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/bigelowrules.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  BigelowRules-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/bigelowrules at `d153e877f651`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: BigelowRules-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/bigelowrules.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`d153e877f651` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/bigelowrules at
  f3ba7414e96d1a940b935d4fa4d2bab47150c7fc: src/BigelowRules-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/bigelowrules"
      commit: "f3ba7414e96d1a940b935d4fa4d2bab47150c7fc"
    }

## Previous investigation

## Investigation Report: Bigelow Rules

### Source Data

| Field | Value |
|-------|-------|
| Family Name | Bigelow Rules |
| Designer | Astigmatic (Brian J. Bonislawsky) |
| License | OFL |
| Date Added | 2012-11-02 |
| Repository URL | https://github.com/librefonts/bigelowrules |
| Commit Hash | `f3ba7414e96d1a940b935d4fa4d2bab47150c7fc` |
| Branch | master |
| Config YAML | N/A (no buildable sources) |
| Status | **Missing config** (unbuildable - VFB only) |

### How URL Found

The repository URL `https://github.com/librefonts/bigelowrules` was identified from the librefonts organization on GitHub, which hosts archived copies of many Google Fonts. This is a standard librefonts mirror repository.

### How Commit Determined

The upstream repository has only **one commit** (`f3ba741 update .travis.yml`), making the commit hash trivially the only option. Since the font was last updated in google/fonts via PR #856 ("hotfix-bigelowrules: v1.001 added") by Marc Foley on 2017-08-07, and the librefonts repo contains the corresponding TTX decomposition of the font files, the single commit represents the full state of the repository.

### Config YAML Status

**No config.yaml exists**, and none can be created because the upstream repository contains no gftools-buildable source files. The available source files are:

- `src/BigelowRules-Regular.vfb` - FontLab VFB (proprietary format)
- `src/BigelowRules-Regular-OTF.vfb` - FontLab VFB
- `src/BigelowRules-Regular-TTF.vfb` - FontLab VFB
- `*.ttx` files - TTX decompositions of the binary font

VFB files cannot be processed by gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` source files.

### Verification

- **Commit exists in upstream repo**: Yes (it is the only commit)
- **Config YAML exists at commit**: No
- **Buildable sources available**: No (VFB only)
- **Source block in METADATA.pb**: Not yet in the upstream google/fonts (pending PR)
- **Override config.yaml in google/fonts**: No

### Google Fonts History

1. `90abd17b4` - Initial commit (part of the original google/fonts repo)
2. `4a101fcb7` - PR #856: "hotfix-bigelowrules: v1.001 added" by m4rc1e (2017-08-07) - last font binary update
3. Various metadata updates (stroke, classifications, languages)

### Confidence Level

**High** for URL and commit hash (single-commit repo, standard librefonts mirror). **N/A** for config.yaml since the font has no buildable sources.

### Open Questions

- This font cannot be rebuilt from source using gftools-builder due to VFB-only sources. The original designer (Astigmatic/Brian Bonislawsky) would need to provide sources in a buildable format (.glyphs, .ufo, or .designspace) for this to change.
