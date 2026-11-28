# Magra

**Model**: Claude Opus 5.5
**Date**: 2026-10-22

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Magra built from FontForge `.sfd` sources in the family's directory
in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/magra` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. All 2 shipped binaries carry FontForge's `FFTM` table,
so FontForge generated them. The directory also holds FontLab `.vfb` files; the `.sfd`
is taken as the master because FontForge generated the shipped fonts and the build from
the `.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/magra.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last change to the font.

## Final state

The source is https://github.com/googlefonts/magra at `f884305229b5`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 2 styles. Those tools,
including this family's plan `plans/magra.json`:
https://github.com/felipesanches/gf-source-modernization at `488fa72`.

`f884305229b5` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Where the shipped
binaries differ from the source, the difference is reproduced by a documented commit
before the conversion, never silently corrected. Any improvement is a later commit that
needs its own QA, and is left as future work for an onboarder to review in a font-update
PR.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Magra — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

### Source Repository

The source files for Magra are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `magra/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Magra-Regular.vfb` | FontLab VFB | Original source with contour overlaps (proprietary, not buildable) |
| `Magra-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Magra-Bold-OTF.vfb` | FontLab VFB | Merged contours for Bold OTF output |
| `Magra-Regular-TTF.sfd` | FontForge SFD | TrueType outlines with hinting (not gftools-builder compatible) |
| `Magra-Bold-TTF.sfd` | FontForge SFD | TrueType outlines with hinting |
| `Magra-Regular.otf` | Compiled OTF binary | Not a design source |
| `Magra-Bold.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The sources are exclusively VFB (FontLab, proprietary binary format) and SFD (FontForge format).

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/magra, created on 2014-07-16 under the `librefonts` GitHub organization. The repo has 12 commits total, all from 2014. The initial commit (`905fba1`, 2014-07-16) moved the font files from a prior location, and all 11 subsequent commits only modified Travis CI configuration — no source file changes were ever made.

The designer's GitHub account (`fontfuror`) only has one repository: `fontfuror/Enriqueta`. No `googlefonts/magra` repository exists.

#### Commit History Highlights

| Commit | Date | Message |
|--------|------|---------|
| `905fba1` | 2014-07-16 | Move magra font files to separate repository |
| `dc47090` | 2014-10-17 | update .travis.yml (HEAD) |

### Onboarding History

Magra was added to Google Fonts on 2012-01-11 (per `date_added` in METADATA.pb). The font files were included in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland). The font binary files have never been updated since that initial commit.

**Designer**: Viviana Monsalve / FontFuror (www.fontfuror.com)
**Copyright**: Copyright (c) 2011, FontFuror (info@fontfuror.com)
**Version**: 1.001
**Weights**: Regular (400) and Bold (700)
**File sizes**: Regular: 45,536 bytes, Bold: 44,500 bytes

No pull requests were associated with the addition of Magra to Google Fonts — it predated the current PR-based workflow.

### Build Configuration

No `config.yaml` exists and none can be created. The sources are in VFB (proprietary FontLab format) and SFD (FontForge format), which are not compatible with gftools-builder. The FONTLOG.txt indicates the font was originally built from FontLab VFB files. The `.travis.yml` used the legacy `fontbakery-build.py` pipeline.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/magra"
  commit: "dc47090320b21439c1a97594548890ccd86a42e3"
  branch: "master"
}
```

No `config_yaml` field is included because the sources are SFD/VFB-only and not compatible with gftools-builder. The latest commit `dc47090` is appropriate for referencing, as no source files were modified after the initial commit.
