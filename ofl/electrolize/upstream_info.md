# Electrolize

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Electrolize (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/electrolize.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Electrolize-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/electrolize at `e647a282361e`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/electrolize.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`e647a282361e` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/electrolize at 2450033307b2d9f771649ae84007e59eb4387d1f:
  src/Electrolize-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/electrolize"
      commit: "2450033307b2d9f771649ae84007e59eb4387d1f"
    }

## Previous investigation

## Electrolize

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Gaslight (designed by Valery Zaveryaev, mastered by Alexei Vanyashin at Cyreal)
**METADATA.pb path**: `ofl/electrolize/METADATA.pb`

### Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/electrolize |
| Commit | `2450033307b2d9f771649ae84007e59eb4387d1f` |
| Config YAML | N/A (no buildable sources) |
| Branch | master |

### How the Repository URL Was Found

The repository URL `https://github.com/librefonts/electrolize` was identified from the `fontc_crater_cache` at `librefonts/electrolize`. The `librefonts` GitHub organization was created by hash3g (Mikhail Sharanda) to host Google Fonts font sources with Travis CI build infrastructure. The repo is publicly accessible (HTTP 200). There is no alternative upstream repository under the `cyrealtype` organization or elsewhere.

The METADATA.pb file does not contain a `source { }` block. The copyright field credits "Cyreal (www.cyreal.org)" and the FONTLOG.txt identifies Valery Zaveryaev as the designer and Alexei Vanyashin (Cyreal) as handling mastering.

### How the Commit Hash Was Identified

The upstream repository contains only a single commit (`2450033307b2d9f771649ae84007e59eb4387d1f`, dated 2014-10-17, by hash3g). This commit is the initial (and only) commit, importing all files including TTX decompositions, VFB source files, and a `.travis.yml` for CI building.

The font binary in google/fonts (`ofl/electrolize/Electrolize-Regular.ttf`, 55712 bytes, SHA256: `aa81ab9015fc0190bb5e68c50290565c7a4a723ddf32b88774aaff05cdd66bca`) has never been modified since the initial commit in google/fonts (`90abd17b4`, 2015-03-07, by Dave Crossland). The current file is byte-identical to the initial import.

Since there is only one commit in the upstream repo, `2450033` is the only possible reference commit.

### Build Configuration

There is no `config.yaml` in the upstream repository and no override `config.yaml` in the google/fonts family directory (`ofl/electrolize/`).

The upstream sources consist of:
- `src/Electrolize-Regular-TTF.vfb` (FontLab VFB format, 104422 bytes)
- `src/Electrolize-Regular-OTF.vfb` (FontLab VFB format, 70166 bytes)
- Multiple TTX decomposition files (both at root level and in `src/`)

**VFB files are not buildable by gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources. An override `config.yaml` cannot be created because there are no compatible source files. The TTX files could theoretically be recompiled with fontTools, but this is not a standard gftools-builder workflow.

### Timeline

- **2011-11-17**: Electrolize v1.000 completed by Valery Zaveryaev
- **2011-11-24**: Electrolize v1.002 mastered by Alexei Vanyashin (minor design and spacing adjustments)
- **2014-10-17**: Upstream repo created by hash3g at `librefonts/electrolize` (single commit `2450033`)
- **2015-03-07**: Font added to google/fonts in the initial bulk commit (`90abd17b4`) by Dave Crossland
- No subsequent font binary updates in google/fonts

### Issues Found

1. **No buildable sources**: The upstream repo only contains VFB (FontLab) format source files, which are not compatible with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` files.
2. **No config.yaml possible**: Since there are no gftools-builder-compatible sources, a config.yaml (either in upstream or as an override) cannot be meaningfully created.
3. **No source block in METADATA.pb**: The METADATA.pb file has no `source { }` block at all.
4. **Designer field discrepancy**: METADATA.pb lists the designer as "Gaslight", but the FONTLOG.txt credits Valery Zaveryaev as designer and Alexei Vanyashin / Cyreal as mastering. "Gaslight" may be an alias or studio name associated with the project.

### Confidence

**MEDIUM** -- The repository URL and commit hash are definitive (single-commit repo, only known upstream). However, the font cannot be rebuilt from sources using gftools-builder due to VFB-only sources. The status remains `missing_config` with no path to resolution without source format conversion.
