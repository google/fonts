# Lobster Two — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only font metadata (name, designer, license, category, fonts, subsets, stroke, classifications) with no `source { }` block.

## Repository Analysis

The upstream repository is **librefonts/lobstertwo** at https://github.com/librefonts/lobstertwo.

- **Not archived**, not a fork
- **Created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Single commit**: `0f38cf2` (2014-10-17) — "update .travis.yml"
- **Single branch**: `master`

### Repository Structure

The repo contains:
- Root level: `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `METADATA.json`, `OFL.txt`, `.travis.yml`
- Root level: TTX table dumps of the TTF files (e.g., `LobsterTwo-Regular.ttf._g_l_y_f.ttx`, etc.)
- `src/` directory: VFB source files and OTF TTX dumps

### Source Files

The `src/` directory contains only **VFB (FontLab)** source files:
- `LobsterTwo-Regular.vfb` and `LobsterTwo-Regular-TTF.vfb`
- `LobsterTwo-Italic.vfb` and `LobsterTwo-Italic-TTF.vfb`
- `LobsterTwo-Bold.vfb` and `LobsterTwo-Bold-TTF.vfb`
- `LobsterTwo-BoldItalic.vfb` and `LobsterTwo-BoldItalic-TTF.vfb`

There are **no** `.glyphs`, `.ufo`, or `.designspace` source files anywhere in the repository. There is **no** `config.yaml` file.

The `.travis.yml` references an old build pipeline using `fontbakery-build.py` (circa 2014), not gftools-builder.

### Font Versions

All four TTF files are version 1.006.

### Related Repository

A related but distinct repository exists: **impallari/The-Lobster-Font** (https://github.com/impallari/The-Lobster-Font). This repo contains a `Lobster.glyphs` source file but is for the original single-weight "Lobster" font (Regular only), not "Lobster Two" (Regular, Italic, Bold, BoldItalic). The two are related families but separate projects.

## Onboarding History

Lobster Two was added to google/fonts in the **initial commit** (`90abd17b`) on 2015-03-07 by Dave Crossland. This was a bulk import that added many font families at once. There were no PRs associated with the onboarding of this specific font.

Subsequent commits in google/fonts that touched the lobstertwo directory were all metadata-only changes:
- METADATA.pb textproto conversion
- Copyright field updates
- METADATA.json removal
- Designer key updates
- Language metadata additions/rollbacks
- Stroke and classification metadata updates

The TTF binary files have **never been updated** since the initial commit.

## Build Configuration

**No config.yaml exists** in the upstream repository, and none can be created because the source files are VFB-only. VFB is a proprietary FontLab format that is **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` source files.

An override config.yaml in the google/fonts directory is also not feasible because there are no gftools-builder compatible sources to point to.

## Findings

1. **No source block** in METADATA.pb — needs to be added.
2. **VFB-only sources**: The upstream repo at `librefonts/lobstertwo` contains only FontLab VFB files, which are not compatible with modern gftools-builder tooling. No `.glyphs`, `.ufo`, or `.designspace` files exist.
3. **Single commit repo**: The repo has only one commit from 2014, predating the google/fonts initial commit (2015).
4. **Font never updated**: The TTF binaries have remained unchanged since the 2015 initial commit to google/fonts.
5. **Designer**: Pablo Impallari (impallari@gmail.com), with kerning by Igino Marini.
6. **No config.yaml possible**: Since the sources are VFB-only, no gftools-builder config can be provided. The fonts were likely compiled directly from FontLab, not through an automated build pipeline.
7. **Related "Lobster" repo**: The `impallari/The-Lobster-Font` repo has a `.glyphs` source but only for the original single-weight "Lobster" font, not "Lobster Two".

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lobstertwo"
  commit: "0f38cf2a6f0ffd8e8334fa15ad761cedf78136cc"
}
```

Notes on the recommended block:
- The `repository_url` points to the only known upstream repo for Lobster Two.
- The `commit` is `0f38cf2` — the single and only commit in the repo, which predates the google/fonts initial import.
- The `config_yaml` field is **omitted** because no gftools-builder compatible config exists (VFB-only sources).
- **Status**: This source block is incomplete from a build reproducibility standpoint. The fonts cannot be rebuilt from source using modern tooling without first converting the VFB sources to a supported format.
