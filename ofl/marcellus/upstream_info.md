# Marcellus — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (VFB-only sources, no gftools-builder compatible sources)

## METADATA.pb Source Block (current)

No source block exists. The current METADATA.pb contains only basic metadata:

```
name: "Marcellus"
designer: "Astigmatic"
license: "OFL"
category: "SERIF"
date_added: "2012-05-09"
fonts {
  name: "Marcellus"
  style: "normal"
  weight: 400
  filename: "Marcellus-Regular.ttf"
  post_script_name: "Marcellus-Regular"
  full_name: "Marcellus"
  copyright: "Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name \"Marcellus\""
}
subsets: "menu"
subsets: "latin"
subsets: "latin-ext"
```

## Repository Analysis

### librefonts/marcellus (https://github.com/librefonts/marcellus)

This repository was created on 2014-07-16 by Mikhail Kashkin (hash3g / m@xen.ru) as part of the fontbakery-dashboard project, which split fonts from the legacy Google Font Directory into individual repositories under the `librefonts` GitHub organization. It is **not** the original designer's source repository.

The repo contains:
- **TTX decompositions** of the compiled TTF and OTF binaries (split into per-table `.ttx` files)
- **VFB source files** (FontLab Studio proprietary format):
  - `src/Marcellus-Regular.vfb` — original source with contour overlaps
  - `src/Marcellus-Regular-OTF.vfb` — merged contours, optimized for OTF
  - `src/Marcellus-Regular-TTF.vfb` — TrueType outlines with hinting adjustments
- `src/VERSIONS.txt` — records "Marcellus-Regular.ttf: Version 1.000"
- `src/METADATA_comments.txt` — legacy subsetting commands from the Google Font Directory era
- `.travis.yml` — fontbakery CI configuration (obsolete)

**No gftools-builder compatible source files exist** (.glyphs, .glyphx, .ufo, .designspace, .sfd). The only sources are VFB files, which are proprietary FontLab Studio format and cannot be used with gftools-builder or fontc.

**Commit history** (11 commits total, all by hash3g):
- `ae5b2de` (2014-07-16) — "Move marcellus font files to separate repository" (initial commit)
- `cc26bb6` through `93dc35b` (2014-08-19 to 2014-10-17) — Various `.travis.yml` updates for fontbakery CI

The repo was last updated on 2014-10-17 and has seen no activity since.

### Original Designer

The font was designed by **Brian J. Bonislawsky** of Astigmatic (AOETI). The designer's website was `www.astigmatic.com` and contact email was `astigma@astigmatic.com`. A GitHub account `astigmatic` exists but was created in 2017 and contains only two unrelated Java repositories — it does not appear to be the font designer's account.

**No original source repository** from the designer was found. The font was likely delivered directly to Google as compiled binaries, which was common practice for fonts onboarded in 2012.

## Onboarding History

Marcellus was added to the Google Fonts catalog on **2012-05-09** (per the `date_added` field). The font binary in google/fonts was included in the initial repository commit (`90abd17b4`, 2015-03-07, by Dave Crossland), which migrated all existing Google Fonts to the current repository structure. The TTF file has **never been modified** since that initial commit.

The font version embedded in the binary is **Version 1.000**, and the FONTLOG records the initial release as "7 April 2012 (Brian J. Bonislawsky) Marcellus v1.001".

Subsequent commits to the `ofl/marcellus/` directory were all metadata-only changes:
- `480630de3` — METADATA.pb textproto conversion
- `883939708` — Remove METADATA.json files
- `633ebadbf` / `c6307ba83` / `701bd391b` — Language support metadata updates

## Build Configuration

**No config.yaml exists**, either in the upstream repo or in the google/fonts family directory.

**Creating an override config.yaml is not feasible** because:
1. The upstream repo contains only VFB (FontLab Studio) files, which are proprietary binary format
2. gftools-builder cannot process VFB files
3. There are no .glyphs, .ufo, .designspace, or .sfd source files that could be referenced in a config
4. The TTX decompositions in the repo are for analysis/archival purposes, not for building

## Findings

1. **No source block** currently exists in METADATA.pb.
2. The **librefonts/marcellus** repo is a TTX decomposition archive, not a genuine source repository. It was created by Mikhail Kashkin as part of the fontbakery-dashboard infrastructure, not by the font designer.
3. The font's only sources are **VFB files** (FontLab Studio proprietary format), which cannot be used with modern font build tooling (gftools-builder, fontc, fontmake).
4. The original designer (Brian J. Bonislawsky / Astigmatic) does not appear to have a public source repository for this font.
5. The font binary has been **unchanged since its original onboarding** in 2012 and remains at Version 1.000.
6. This is a companion to **Marcellus SC** (small caps variant), which is in a similar situation with VFB-only sources at `librefonts/marcellussc`.

## Recommended Source Block

A source block can be added pointing to the librefonts repository, but it must be acknowledged that the sources are VFB-only and not buildable with gftools-builder:

```
source {
  repository_url: "https://github.com/librefonts/marcellus"
  commit: "93dc35b5b10ccae45266e0661ae357d84dc0ec5d"
  branch: "master"
}
```

**Note**: The `config_yaml` field is intentionally omitted because no gftools-builder compatible configuration exists or can be created for VFB-only sources. The commit `93dc35b` is the latest (and most complete) commit in the repository, representing the state that includes all source files and TTX decompositions.

**Status**: incomplete — The source block can reference the repo, but the font cannot be rebuilt from source using modern tooling without converting the VFB files to an open format (e.g., UFO or .glyphs).
