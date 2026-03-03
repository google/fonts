# Lusitana — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only basic font metadata (name, designer, license, category, date_added, fonts, subsets) with no `source { }` block.

## Repository Analysis

### googlefonts/lusitana (https://github.com/googlefonts/lusitana)

This repository is **archived and empty** (size 0). It was created on 2015-04-17 but never received any content — no commits, no branches. It cannot serve as an upstream source.

### librefonts/lusitana (https://github.com/librefonts/lusitana)

This is the only repository containing source files for Lusitana. It belongs to the `librefonts` organization, which appears to be an automated archival/mirror project that hosts many Google Fonts families (aclonica, arimo, calligraffitti, etc.). The repository was created on 2014-07-16 and has a single commit (`8fa070c`) dated 2014-10-17, authored by "hash3g" (hash.3g@gmail.com).

**Source files found** in the `src/` directory:
- `Lusitana-Regular-TTF.sfd` — FontForge Spline Font Database v3.0
- `Lusitana-Bold-TTF.sfd` — FontForge Spline Font Database v3.0
- `Lusitana-Regular-OTF.vfb` — FontLab binary source
- `Lusitana-Bold-OTF.vfb` — FontLab binary source
- Various `.ttx` decomposed font table dumps (TTX XML format)

The repository also contains TTX dumps of the compiled TTF files at the top level, a `.travis.yml` for fontbakery CI, `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`, and `OFL.txt`.

**No config.yaml** exists in this repository. The sources are SFD (FontForge) and VFB (FontLab) format files, which are not compatible with gftools-builder. An override config.yaml cannot be created for these source types.

### Designer Information

The original type designer is **Ana Paula Megda** (anapbm@gmail.com, www.anamegda.com). The font copyright dates to 2011. No personal GitHub repository for this font was found.

## Onboarding History

Lusitana was added to Google Fonts as part of the **initial commit** (`90abd17b4`) on 2015-03-07 by Dave Crossland. This massive initial commit imported the entire existing Google Fonts library into the current repository structure. The font binary files (Lusitana-Regular.ttf, Lusitana-Bold.ttf) have **never been updated** since that initial commit.

Subsequent commits only modified metadata files:
- 2015-12-08: METADATA.pb textproto conversion (Rod Sheeter)
- 2016-01-11: Copyright field update and METADATA.json removal (Rod Sheeter)
- 2021-12-12: Language support metadata added (Nathan Williams, PR #4160)
- 2022-04-15 to 2022-05-23: Language metadata rollback and redo (PRs #4677, #4706)

### Related Issues

- **Issue #2647** (opened 2020-08-26 by Marc Foley): Reports a problem with caret (^) sidebearings in Lusitana. This is a font quality issue, not related to onboarding.

## Build Configuration

No `config.yaml` exists in the upstream repository. The source files are in SFD (FontForge) and VFB (FontLab) formats, which are **not compatible with gftools-builder**. The font predates the modern gftools-builder workflow — it was compiled using older tooling (FontForge/FontLab) circa 2011.

An override config.yaml **cannot** be meaningfully created because:
1. gftools-builder does not support SFD or VFB source formats
2. The sources would need to be converted to .glyphs, .ufo, or .designspace format first
3. Such a conversion would constitute a new build, not a reproduction of the original

## Findings

1. **No source block** exists in METADATA.pb — one needs to be added.
2. The `googlefonts/lusitana` repository is **archived and empty** — it should not be used as repository_url.
3. The `librefonts/lusitana` repository contains the only known sources (SFD + VFB files) but is not the original designer's repository — it is a third-party archive maintained by the `librefonts` organization.
4. The source files are in **legacy formats** (SFD, VFB) that are not compatible with gftools-builder.
5. The font has **never been updated** since the initial Google Fonts import in March 2015.
6. The font was originally released in December 2011 (version 1.001) by Ana Paula Megda.
7. Since the librefonts repo has only one commit, the commit hash `8fa070c` is the only option for referencing the source state.
8. There is no config.yaml and none can be created for SFD-only sources.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lusitana"
  commit: "8fa070c2ac2963f13feee142e2001777ac48e774"
}
```

**Notes on this recommendation**:
- The `librefonts/lusitana` repository is used as it is the only repository with source files. It is a third-party archive, not the original designer's repository.
- The `config_yaml` field is omitted because the sources are SFD/VFB format files that are incompatible with gftools-builder. No override config.yaml can be created.
- The commit hash `8fa070c` is the only commit in the repository.
- Confidence: **MEDIUM** — The librefonts repo is a legitimate archive of the sources, but it is not maintained by the original designer. The SFD/VFB sources cannot be used with modern build tooling.
