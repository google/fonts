# Butterfly Kids

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Butterfly Kids (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/butterflykids.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  ButterflyKids-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/butterflykids at `ba6a0c6241f0`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/butterflykids.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`ba6a0c6241f0` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/butterflykids at
  0c553b23416ad40db0b241d1d0b9165d890933b7: src/ButterflyKids-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/butterflykids"
      commit: "0c553b23416ad40db0b241d1d0b9165d890933b7"
    }

## Previous investigation

## Butterfly Kids - Investigation Report

### Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Butterfly Kids |
| **Designer** | Tart Workshop |
| **License** | OFL |
| **Date Added** | 2012-02-15 |
| **Repository URL** | https://github.com/librefonts/butterflykids |
| **Commit Hash** | `0c553b23416ad40db0b241d1d0b9165d890933b7` |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config |

### How URL Was Found

The repository URL `https://github.com/librefonts/butterflykids` was added as part of a batch source block addition in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). The librefonts GitHub organization hosts mirrors/archives of many Google Fonts source repos.

### How Commit Was Determined

The recorded commit `0c553b23416ad40db0b241d1d0b9165d890933b7` is the **only commit** in the entire repository. The repo was initialized by hash3g on 2014-10-17 with the message "update .travis.yml". Since there is only one commit, it is trivially the correct reference -- there is no other state the repo has ever been in.

The font binaries in google/fonts were last updated via PR #871 ("hotfix-butterflykids: v1.001 added"), authored by m4rc1e and merged on 2017-08-07. This was a hotfix to the font file.

### Config YAML Status

**No config.yaml exists** in the upstream repository and no override config.yaml exists in the google/fonts family directory.

The repository contains only a VFB (FontLab 5) source file at `src/ButterflyKids-Regular-TTF.vfb`. VFB is a proprietary binary format from FontLab 5 that is **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources.

No config.yaml can be created for this family without first converting the sources to a gftools-compatible format.

### Verification

- **Repository URL**: Confirmed valid; repo is cloned at `upstream_repos/fontc_crater_cache/librefonts/butterflykids/`
- **Commit hash**: Verified -- it is the only commit in the repo (HEAD of master)
- **Source files**: Only VFB file present (`src/ButterflyKids-Regular-TTF.vfb`)
- **Font binary history**: Last updated in google/fonts via PR #871 (m4rc1e, 2017-08-07)

### Confidence Level

**HIGH** -- The repository URL is correct and the commit hash is trivially verified as the sole commit. The missing_config status is accurate because only a VFB source file exists, which cannot be built with gftools-builder.

### Open Questions

None. The data is complete and verified. The family will remain in `missing_config` status unless the sources are converted to a gftools-compatible format (e.g., .glyphs or .ufo).
