# Marck Script — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in `ofl/marckscript/METADATA.pb`. The file contains only basic metadata (name, designer, license, category, fonts, subsets, classifications) with no `source { }` block.

## Repository Analysis

### Repository: librefonts/marckscript

- **URL**: https://github.com/librefonts/marckscript
- **Default branch**: master
- **Created**: 2014-07-16
- **Last updated**: 2014-10-17

This repository belongs to the `librefonts` organization, which was created as part of an effort to split individual font families out of the old `googlefontdirectory` monorepo into separate repositories. The initial commit message ("Move marckscript font files to separate repository") confirms this origin.

The repository contains:
- **Root level**: TTX decompositions of the compiled TTF binary, plus `METADATA.json`, `DESCRIPTION.en_us.html`, `OFL.txt`, and a FontForge menu subsetting script
- **`src/` directory**:
  - `MarckScript-Regular.vfb` (5.4 MB) — FontLab Studio binary source
  - `MarckScript-Regular-TTF.sfd` (851 KB) — FontForge SFD source
  - TTX decompositions of an OTF version
  - `VERSIONS.txt` — records "MarckScript-Regular.ttf: Version 1.002"
  - `METADATA_comments.txt` — subsetting commands referencing the old googlefontdirectory structure

**No config.yaml** exists in the repository. There are **no gftools-builder compatible source files** (no `.glyphs`, `.ufo`, or `.designspace` files).

### Commit History (12 commits total)

| Commit | Date | Description |
|--------|------|-------------|
| 699f314 | 2014-10-17 | update .travis.yml |
| 21bcf62 | 2014-10-06 | Rename fontbakery |
| b88137c | 2014-09-19 | Update .travis.yml |
| 32cd1ad | 2014-09-15 | Update .travis.yml |
| 6381a2c | 2014-09-14 | Installing ttfautohint from ppa |
| 0db17e7 | 2014-09-12 | Added raw=True to VDMX and FFTM |
| 139a2c3 | 2014-09-11 | update .travis.yml |
| a275516 | 2014-08-22 | Travis.yml update |
| 77aa975 | 2014-08-22 | Travis.yml update |
| 622fe3f | 2014-08-21 | Travis.yml update |
| 835d406 | 2014-08-19 | Added .travis.yml |
| 211ebe3 | 2014-07-16 | Move marckscript font files to separate repository |

After the initial commit that moved the files, all subsequent commits were CI/Travis configuration changes — no source file modifications occurred.

### Other Repositories Checked

- **googlefonts/marckscript** — Does not exist
- **googlefonts/marck-script** — Does not exist
- **acidwave/typeface-marck-script** — An npm/CSS package wrapping the font for web use (created 2020), not original sources
- **google-fonts-bower/marckscript-bower** — A Bower package, not original sources
- No GitHub account found for designer Denis Masharov

## Onboarding History

The font was added to Google Fonts on **2011-10-12** (per `date_added` in METADATA.pb). The binary file `MarckScript-Regular.ttf` has only ever been present in one commit in the `google/fonts` repository: the initial repository restructuring commit `90abd17b` (2015-03-07), which was the "Initial commit" that established the current repository structure by importing content from the older `googlefontdirectory` repo.

No pull requests related to Marck Script were found in `google/fonts`. The font has never been updated since its original onboarding.

### Font Binary Details

- **File**: `MarckScript-Regular.ttf` (83,664 bytes)
- **Version**: 1.002
- **Copyright**: "Copyright (c) 2011, Denis Masharov & Marck Fogel, with Reserved Font Names 'Marck Script'"
- **Designer**: Denis Masharov (denis.masharov@gmail.com), Marck Fogel

## Build Configuration

**No config.yaml exists** — neither in the upstream repository nor as an override in the google/fonts family directory.

The upstream sources are in legacy formats only:
- `.vfb` (FontLab Studio binary) — proprietary format, not directly usable by gftools-builder
- `.sfd` (FontForge) — while open source, not a format supported by gftools-builder

Creating an override `config.yaml` is **not feasible** because there are no gftools-builder compatible source files (`.glyphs`, `.ufo`, `.designspace`) in the repository. The font would need to be converted from VFB/SFD to a modern format before a build configuration could be created.

## Findings

1. **No source block** exists in METADATA.pb.
2. The only known repository is `librefonts/marckscript`, which is a `librefonts` organization mirror containing TTX decompositions and legacy source files (VFB + SFD), not a designer-maintained upstream repository.
3. The original designer (Denis Masharov) does not appear to have a GitHub account or any publicly accessible source repository for this font.
4. The font sources are exclusively in legacy formats (FontLab Studio `.vfb` and FontForge `.sfd`), making it **impossible to create a gftools-builder config.yaml** without first converting the sources to a modern format.
5. The font has never been updated since its initial onboarding in 2011 and the binary in google/fonts has remained unchanged since the repository restructuring in 2015.
6. The latest commit in the librefonts repo (`699f314`, 2014-10-17) is only a Travis CI configuration update; the actual source files were introduced in commit `211ebe3` (2014-07-16).

## Recommended Source Block

A source block can be added, but it will be limited due to the lack of gftools-builder compatible sources:

```
source {
  repository_url: "https://github.com/librefonts/marckscript"
  commit: "211ebe3a510e950f242bb7be29f1ed245ef71540"
  branch: "master"
}
```

**Notes on the recommended block**:
- The `repository_url` points to the librefonts mirror, which is the only known public repository containing source files for this font. It is not a designer-maintained upstream repo.
- The `commit` references `211ebe3`, the initial commit that introduced the font files, since all subsequent commits were Travis CI changes only.
- No `config_yaml` field is included because there are no gftools-builder compatible sources — the font was built from VFB/SFD sources using legacy tooling.
- **Status**: incomplete — SFD-only sources, no gftools-builder compatible configuration possible without source format conversion.
- **Confidence**: MEDIUM — The librefonts repo is verified to contain the original sources (VFB/SFD), but it is a mirror organization, not the original designer's repository.
