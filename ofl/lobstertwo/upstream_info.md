# Lobster Two - Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Confidence**: HIGH

## Source Repository

The original design sources for Lobster Two are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `lobstertwo/src/`.

### Source Files in googlefontdirectory-hg

- `LobsterTwo-Regular.vfb` / `LobsterTwo-Regular-TTF.vfb` -- FontLab binary sources (proprietary, not buildable with gftools-builder)
- `LobsterTwo-Bold.vfb` / `LobsterTwo-Bold-TTF.vfb` -- FontLab binary sources
- `LobsterTwo-Italic.vfb` / `LobsterTwo-Italic-TTF.vfb` -- FontLab binary sources
- `LobsterTwo-BoldItalic.vfb` / `LobsterTwo-BoldItalic-TTF.vfb` -- FontLab binary sources
- `LobsterTwo-Regular.otf`, `LobsterTwo-Bold.otf`, `LobsterTwo-Italic.otf`, `LobsterTwo-BoldItalic.otf` -- compiled OTF binaries, not design sources
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are exclusively VFB (FontLab binary) format. No `.glyphs`, `.ufo`, or `.designspace` files are present. VFB files are not compatible with gftools-builder.

## METADATA.pb Analysis

No source block exists in the current METADATA.pb. The file contains only font metadata (name, designer, license, category, fonts, subsets, stroke, classifications) with no `source { }` block.

## Upstream Repository (librefonts archive)

The upstream repository is **librefonts/lobstertwo** at https://github.com/librefonts/lobstertwo.

- **Not archived**, not a fork
- **Created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Single commit**: `0f38cf2` (2014-10-17) -- "update .travis.yml"
- **Single branch**: `master`

The repository contains the same VFB source files as the googlefontdirectory-hg monorepo, plus TTX table dumps of the TTF files. There are **no** `.glyphs`, `.ufo`, `.designspace`, or `config.yaml` files.

The `.travis.yml` references an old build pipeline using `fontbakery-build.py` (circa 2014), not gftools-builder.

### Related Repository

A related but distinct repository exists: **impallari/The-Lobster-Font** (https://github.com/impallari/The-Lobster-Font). This repo contains a `Lobster.glyphs` source file but is for the original single-weight "Lobster" font (Regular only), not "Lobster Two" (Regular, Italic, Bold, BoldItalic). The two are related families but separate projects.

## Onboarding History

Lobster Two was added to google/fonts in the **initial commit** (`90abd17b`) on 2015-03-07 by Dave Crossland. This was a bulk import that added many font families at once. There were no PRs associated with the onboarding of this specific font.

Subsequent commits in google/fonts that touched the lobstertwo directory were all metadata-only changes (METADATA.pb textproto conversion, copyright field updates, METADATA.json removal, designer key updates, language metadata, stroke and classification metadata).

The TTF binary files have **never been updated** since the initial commit. All four TTF files are version 1.006.

## Designer Information

Designer: Pablo Impallari (impallari@gmail.com), with kerning by Igino Marini.

## Build Configuration

**No config.yaml exists** in the upstream repository, and none can be created because the source files are VFB-only. VFB is a proprietary FontLab format that is **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` source files.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lobstertwo"
  commit: "0f38cf2a6f0ffd8e8334fa15ad761cedf78136cc"
}
```

The `config_yaml` field is **omitted** because no gftools-builder compatible config exists (VFB-only sources).

## Conclusion

The source block documents the only known upstream repository. The fonts cannot be rebuilt from source using modern tooling without first converting the VFB sources to a supported format.
