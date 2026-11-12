# Cantora One

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Cantora One (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/cantoraone.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from CantoraOne-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/cantoraone at `60930f3a7873`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/cantoraone.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`60930f3a7873` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/cantoraone at 45d202afe1668a05e0afd870e124d72c2b82143c:
  src/CantoraOne-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/cantoraone"
      commit: "45d202afe1668a05e0afd870e124d72c2b82143c"
    }

## Previous investigation

## Cantora One

**Date investigated**: 2026-02-27
**Status**: missing_config
**Designer**: Impallari Type (Pablo Impallari, Rodrigo Fuenzalida)
**METADATA.pb path**: `ofl/cantoraone/METADATA.pb`

### Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/cantoraone |
| Commit | `45d202afe1668a05e0afd870e124d72c2b82143c` |
| Config YAML | -- |
| Branch | master |

### How the Repository URL Was Found

The METADATA.pb file for Cantora One has no `source` block and no `repository_url` field. The upstream repo was found at `librefonts/cantoraone` in the fontc_crater_cache. A GitHub search for "cantoraone" confirmed that `https://github.com/librefonts/cantoraone` is the only upstream repository for this font. It was created on 2014-07-16 by the librefonts community effort (contributors: vitalyvolkov, xen) to preserve font sources from the Google Fonts library. The repo contains TTX decomposed font files and original VFB (FontLab) source files.

### How the Commit Hash Was Identified

The upstream repository contains only a single commit:

- `45d202a` (2014-10-17, by hash3g): "update .travis.yml"

This sole commit added all files to the repo in one go -- the TTX files, VFB sources, DESCRIPTION.en_us.html, METADATA.json, OFL.txt, and a .travis.yml. The font version in the upstream repo is **1.001** (seen in the `_name` TTX: "Version 1.001; ttfautohint (v0.8) -G 200 -r 50" and in `_head` TTX: fontRevision 1.00100708008).

**Important note**: The current font in google/fonts is **version 1.002**, updated by PR #5355 (merged 2022-10-07 by Rosalie Wagner). This HOTFIX was created directly in the google/fonts repo to fix a ligature bug (issue #3089: `ffu` ligature in words like "diffusion" incorrectly rendered as `ffh`). The HOTFIX also corrected naming inconsistencies between the font file (CantoraOne) and the API name (Cantora One). The upstream librefonts repo was **never updated** with the v1.002 HOTFIX.

Therefore, the commit `45d202a` represents the original v1.001 sources, not the current v1.002 binary in google/fonts. The v1.002 changes were made directly in google/fonts PR #5355 without corresponding upstream changes.

### How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository and none can be created. The source files are:

- `src/CantoraOne-Regular.vfb` -- FontLab 5 binary source
- `src/CantoraOne-Regular-TTF.vfb` -- FontLab 5 binary (TTF version)
- `src/CantoraOne-Regular-OTF.vfb` -- FontLab 5 binary (OTF version)
- `src/CantoraOne-Regular.otf.*.ttx` -- TTX decomposed OTF tables
- `CantoraOne-Regular.ttf.*.ttx` -- TTX decomposed TTF tables (at repo root)

VFB is the proprietary FontLab 5 binary format. It is **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources. There are no open-format editable sources available for this font. An override config.yaml cannot be created because there are no compatible source files to reference.

### Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17
- Commit message: "update .travis.yml"
- Source files at commit: `src/CantoraOne-Regular.vfb`, `src/CantoraOne-Regular-TTF.vfb`, `src/CantoraOne-Regular-OTF.vfb`, plus TTX files and `src/FONTLOG.txt`

### Additional Context

- **Font added to Google Fonts**: 2012-07-30 (per METADATA.pb `date_added`)
- **Initial google/fonts commit**: 90abd17b (2015-03-07, by Dave Crossland) -- "Initial commit" that created the entire google/fonts repo
- **HOTFIX PR #5355**: Merged 2022-10-07 by Rosalie Wagner. Fixed ligature bug from issue #3089 and corrected metadata. The font binary was updated from v1.001 to v1.002 directly in google/fonts.
- **librefonts repo**: Created 2014-07-16, last pushed 2014-10-17. This is a community archive, not an active development repo. It was never updated with the v1.002 fix.
- **Original designer**: Pablo Impallari (impallari@gmail.com) and Rodrigo Fuenzalida (hello@rfuenzalida.com), with spacing/kerning by Igino Marini

### Confidence

**MEDIUM**: The repository URL is confirmed as the only known upstream source for Cantora One. However, the upstream repo only contains v1.001 sources while google/fonts has v1.002 (from a direct HOTFIX). The source files are in VFB format, which is incompatible with gftools-builder, so no config.yaml can be created. The commit hash is the only commit in the repo and represents the pre-HOTFIX state. A complete rebuild from source would require converting the VFB files to an open format first.
