# Caesar Dressing

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Caesar Dressing (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/caesardressing.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  CaesarDressing-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/caesardressing at `ead46ca1c29d`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/caesardressing.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`ead46ca1c29d` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/caesardressing at
  fb212a606bc3f65a2b3d210c88e938f6090cff15: src/CaesarDressing-Regular-TTF.vfb, a
  FontLab import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/caesardressing"
      commit: "fb212a606bc3f65a2b3d210c88e938f6090cff15"
    }

## Previous investigation

## Caesar Dressing - Investigation Report

### Source Data

| Field | Value |
|---|---|
| Family Name | Caesar Dressing |
| Designer | Open Window |
| License | OFL |
| Date Added | 2011-12-19 |
| Repository URL | https://github.com/librefonts/caesardressing |
| Commit Hash | fb212a606bc3f65a2b3d210c88e938f6090cff15 |
| Config YAML | None |
| Status | missing_config |

### How URL Was Found

The repository URL `https://github.com/librefonts/caesardressing` was added as part of the bulk source block addition in commit `9a14639f3` (2026-02-25). The librefonts GitHub organization hosts archived copies of many early Google Fonts projects. This is a standard librefonts archive repository containing TTX decompositions and metadata.

### How Commit Was Determined

The commit hash `fb212a606bc3f65a2b3d210c88e938f6090cff15` is the only commit in the repository (and therefore HEAD). It was made on 2014-10-17 with the message "update .travis.yml". This is a single-commit archive repository.

Caesar Dressing was part of the initial commit (`90abd17b4`) in the google/fonts repository, meaning it was one of the earliest families added to Google Fonts. The librefonts repository is an archive of the original source material, not an active development repository.

### Config YAML Status

**No config.yaml exists** in the upstream repository and none is expected. The repository contains only:
- `src/CaesarDressing-Regular-TTF.vfb` (FontLab format) - This is a legacy format not supported by gftools-builder.
- TTX decompositions of the font in the root directory.
- Standard metadata files (DESCRIPTION, FONTLOG, OFL, METADATA.json).

There is no override `config.yaml` in the google/fonts family directory either.

This family cannot be built with gftools-builder because the only source is in VFB (FontLab) format, which is not a supported input format. The font would need to be converted to Glyphs, UFO, or Designspace format before a config.yaml could be useful.

### Verification

- **Repository URL**: Valid. The librefonts/caesardressing repository exists and is accessible.
- **Commit Hash**: Verified. The hash `fb212a606bc3f65a2b3d210c88e938f6090cff15` is the sole commit in the repository.
- **Source Files**: VFB format only (legacy, not gftools-buildable).
- **Font Origin**: This is a very early Google Fonts family (initial commit). The librefonts repo is an archive, not the original development repository.

### Confidence Level

**HIGH** for the repository URL and commit hash. The librefonts repo is a well-known archive of early Google Fonts sources. Since there is only one commit, there is no ambiguity about the commit hash.

**Note**: This family is effectively "complete" in terms of source documentation, but cannot be made gftools-buildable without converting the VFB sources to a modern format.

### Open Questions

1. Is there any plan to convert the VFB sources to a modern format (Glyphs/UFO) for this family?
2. The designer "Open Window" (Dathan Boardman, dathanboardman@gmail.com per the copyright string) may have the original editable sources in a different format.
