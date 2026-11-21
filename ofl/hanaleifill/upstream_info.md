# Hanalei Fill

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Hanalei Fill (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/hanaleifill.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  HanaleiFill-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/hanaleifill at `ddf4f849d6ed`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: HanaleiFill-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/hanaleifill.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`ddf4f849d6ed` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/hanaleifill at 1df8f49232e80f4f17d8a5eb9fc55c90a3214f61:
  src/HanaleiFill-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/hanaleifill"
      commit: "1df8f49232e80f4f17d8a5eb9fc55c90a3214f61"
    }

## Previous investigation

## Investigation Report: Hanalei Fill

### Summary

Hanalei Fill is a display font designed by Brian J. Bonislawsky (Astigmatic), added to Google Fonts on 2012-11-26. The font was included in the initial commit of the google/fonts repository and has never been updated since. The upstream repository is `librefonts/hanaleifill` on GitHub, which contains only VFB source files (FontLab format) and TTX decompositions. No gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist in the upstream repo, making it impossible to create a config.yaml for building with gftools-builder.

### Key Findings

| Field | Value |
|---|---|
| **Family Name** | Hanalei Fill |
| **Designer** | Brian J. Bonislawsky (Astigmatic) |
| **Date Added** | 2012-11-26 |
| **Repository URL** | https://github.com/librefonts/hanaleifill |
| **Commit Hash** | 1df8f49232e80f4f17d8a5eb9fc55c90a3214f61 |
| **Config YAML** | None (VFB-only sources) |
| **Status** | no_config_possible |
| **Confidence** | HIGH |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb has no `source { }` block. The font has a single weight (Regular) with filename `HanaleiFill-Regular.ttf`.

#### Git History in google/fonts

The font binary was added in the initial commit of the google/fonts repository:
- `90abd17b4` (2015-03-07) - "Initial commit" by Dave Crossland

The font file has only been touched once more:
- `76adaf1d2` (2021-11-01) - "deploy: c7e2740188205a85323c7385547f6f59b4f2245a" - This is a gh-pages deployment, not a font update.

The binary has never been updated since the initial commit.

#### Upstream Repository

The upstream repository is at `https://github.com/librefonts/hanaleifill`. This is a `librefonts` organization mirror-style repository. It has only a single commit:
- `1df8f49232e80f4f17d8a5eb9fc55c90a3214f61` (2014-10-17) - "update .travis.yml"

The repository contains:
- **Font files**: TTX decompositions of the TTF file
- **Source files** in `src/`:
  - `HanaleiFill-Regular.vfb` - Original VFB source
  - `HanaleiFill-Regular-TTF.vfb` - TTF variant
  - `HanaleiFill-Regular-OTF.vfb` - OTF variant
  - Various OTF TTX decompositions
- **No gftools-builder compatible sources**: No `.glyphs`, `.ufo`, or `.designspace` files exist

#### Source Compatibility

The only source files are VFB (FontLab format), which cannot be used with gftools-builder. There is no config.yaml in the upstream repo, and creating an override config.yaml would not be possible without compatible source files.

#### Commit Hash Rationale

Since the upstream repository has only one commit (`1df8f49`), this is the only possible commit to reference. The font was onboarded from this repository's content (or an equivalent state), and the single commit predates the google/fonts initial commit.

### Conclusion

Hanalei Fill has an identifiable upstream repository at `librefonts/hanaleifill`, but it only contains VFB sources, making gftools-builder incompatible. The source block should reference the repository and the single available commit, but no config.yaml is possible.

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/hanaleifill"
  commit: "1df8f49232e80f4f17d8a5eb9fc55c90a3214f61"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "HanaleiFill-Regular.ttf._g_l_y_f.ttx"
    dest_file: "HanaleiFill-Regular.ttf"
  }
}
```

Note: The files mapping above is approximate. The google/fonts binary was likely compiled from the VFB sources rather than extracted from the TTX files. Since the sources are VFB-only and no config.yaml is feasible, the `config_yaml` field should be omitted.

**Status**: no_config_possible (VFB-only sources, no gftools-builder compatible files)
