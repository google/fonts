# Maiden Orange — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in METADATA.pb. The current file contains only basic font metadata:

```
name: "Maiden Orange"
designer: "Astigmatic"
license: "APACHE2"
category: "SERIF"
date_added: "2010-12-20"
```

Located at `apache/maidenorange/METADATA.pb` (Apache license, not OFL).

## Repository Analysis

**Repository**: https://github.com/librefonts/maidenorange

This is a "librefonts" mirror-style repository created on 2014-07-16 by Mikhail Kashkin (xen/hash3g). The librefonts organization systematically split out font families from the old google/fonts monorepo into individual repositories. This is not an original designer repository.

**Contributors**: vitalyvolkov, xen (Mikhail Kashkin)

**Repository contents**:
- TTX dump files (`.ttx`) of the original `MaidenOrange.ttf` (version 1.000)
- `src/MaidenOrange.vfb` — FontLab binary source file
- `src/VERSIONS.txt` — records "MaidenOrange.ttf: Version 1.000"
- `METADATA.json` — legacy metadata
- `.travis.yml` — old fontbakery CI build pipeline (from 2014)
- No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` sources
- No `config.yaml`

**Commit history** (12 commits, all from 2014):
- `7024a60` (2014-07-16) — "Move maidenorange font files to separate repository" (initial commit by Mikhail Kashkin)
- `a957774` through `20a4f8d` (2014-08-19 to 2014-10-17) — Travis CI configuration updates by hash3g

The repository has been dormant since October 2014 and is not archived.

## Onboarding History

**Initial addition**: Maiden Orange was part of the initial commit (`90abd17`) to the google/fonts repository on 2015-03-07 by Dave Crossland. The font file was named `MaidenOrange.ttf` (version 1.000) and was added under the `apache/` license directory. The `date_added` field in METADATA.pb is "2010-12-20", indicating the font was part of Google Fonts well before the current repository structure.

**Hotfix update (PR #781)**: On 2017-08-07, Marc Foley submitted PR #781 ("hotfix-maidenorange: v1.001 added") which:
- Renamed the font file from `MaidenOrange.ttf` to `MaidenOrange-Regular.ttf`
- Updated the font binary to version 1.001 (from 1.000)
- Updated DESCRIPTION.en_us.html formatting
- Updated METADATA.pb (filename, full_name, copyright, subsets order)

The PR body was empty, providing no information about where the v1.001 binary came from. This was a common pattern for Marc Foley's hotfix PRs at the time, where the font engineer would fix issues (like missing `-Regular` suffix) and regenerate the font.

**Key observation**: The v1.001 font currently in google/fonts does NOT exist in the upstream `librefonts/maidenorange` repository, which only contains version 1.000 sources and TTX dumps.

## Build Configuration

**No config.yaml exists** in either the upstream repository or the google/fonts family directory.

The upstream repository contains only:
- `src/MaidenOrange.vfb` — a FontLab 5 binary source file
- `.travis.yml` — old fontbakery-build pipeline (not gftools-builder compatible)

The `.vfb` format is a proprietary FontLab binary format that cannot be processed by gftools-builder or fontc. To create a gftools-builder compatible build pipeline, the `.vfb` would need to be converted to `.glyphs`, `.ufo`, or `.designspace` format first.

**Build pipeline assessment**: Not feasible with current sources. The font would need source conversion before a `config.yaml` could be created.

## Findings

1. **No source block in METADATA.pb** — needs to be added.

2. **Repository is a librefonts mirror, not an original source** — The `librefonts/maidenorange` repository was created by the librefonts organization as part of a systematic split of fonts from the google/fonts monorepo. The original designer (Brian J. Bonislawsky / Astigmatic / AOETI) does not appear to have a GitHub repository for this font.

3. **Version mismatch** — The font in google/fonts is version 1.001, while the upstream repository only contains version 1.000 sources and data. The v1.001 update was done by Marc Foley in PR #781 as a hotfix and the updated sources were never pushed to the librefonts repository.

4. **VFB-only sources** — The only source file is `MaidenOrange.vfb` (FontLab 5 binary), which is not compatible with gftools-builder or fontc. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist.

5. **No config.yaml possible** — Without gftools-builder compatible source files, a `config.yaml` cannot be meaningfully created. The font cannot be rebuilt from sources using the current toolchain.

6. **Legacy font** — Added to Google Fonts in 2010, this is a legacy font with proprietary-format sources and no active upstream development.

## Recommended Source Block

Given the limitations (VFB-only sources, version mismatch, mirror repo), a minimal source block documenting what is known:

```
source {
  repository_url: "https://github.com/librefonts/maidenorange"
}
```

**Notes on the recommendation**:
- The `repository_url` points to the only known public repository containing source files for this font.
- No `commit` hash is included because the font currently in google/fonts (v1.001) does not correspond to any commit in the upstream repository (which only has v1.000 sources).
- No `config_yaml` is included because the repository has no gftools-builder compatible configuration and the VFB source format is not supported by the current build toolchain.
- This source block has **LOW confidence** due to the repository being a third-party mirror rather than an original designer repo, and the version mismatch between the repo contents and the font in google/fonts.
