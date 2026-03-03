# MedievalSharp — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists. The current METADATA.pb contains only basic font metadata (name, designer, license, category, fonts, subsets, classifications) with no `source { }` block.

## Repository Analysis

### librefonts/medievalsharp (primary upstream candidate)

- **URL**: https://github.com/librefonts/medievalsharp
- **Default branch**: master
- **Single commit**: `0bf7f34` (2014-10-17) by hash3g — "update .travis.yml"
- **Organization**: librefonts (created 2013-10-20), a GitHub organization that hosts TTX-decomposed archives of Google Fonts families
- **Contents**: TTX decomposition of the binary font, plus source files in `src/` directory
- **Source files**:
  - `src/MedievalSharp.sfd` — FontForge source (793 KB)
  - `src/MedievalSharp-TTF.vfb` — FontLab Studio source (222 KB)
  - `src/MedievalSharp.png` — demo image
- **Build system**: Old fontbakery-build pipeline via `.travis.yml` (pre-gftools era)
- **No config.yaml**: No gftools-builder configuration exists
- **No gftools-compatible sources**: No `.glyphs`, `.ufo`, or `.designspace` files

### wmk69/Medieval-Sharp (designer's repo)

- **URL**: https://github.com/wmk69/Medieval-Sharp
- **Default branch**: main
- **Created**: 2022-03-13 (much later than Google Fonts onboarding)
- **Single commit**: `ee7510b` (2022-03-13) — "Add files via upload"
- **Contents**: An expanded 4-style family (Book, BookOblique, Bold, BoldOblique) with SFD sources and TTF binaries
- **Not the onboarding source**: This repo was created 7+ years after the font was added to Google Fonts and contains a different (expanded) version of the family

### Source Format

Both repositories contain only FontForge SFD sources. The gftools-builder toolchain does not support SFD as an input format — it requires `.glyphs`, `.ufo`, or `.designspace` files. Therefore, no config.yaml can be meaningfully created for this font without a source format conversion.

## Onboarding History

- **Added to Google Fonts**: 2011-03-02 (per `date_added` in METADATA.pb)
- **Initial commit in google/fonts repo**: `90abd17b4` (2015-03-07) by Dave Crossland — "Initial commit" (this was the bulk import of the entire google/fonts repository; the font predated this commit)
- **Font binary has not been updated** since the initial commit — the only subsequent commits touched METADATA files (METADATA.json, METADATA.pb), not the font binary
- **Font metadata from binary**: Created with FontForge on 2011-02-27, Version 1.0, copyright by wmk69 (Wojciech Kalinowski)
- **Original source**: The font was originally published on Open Font Library (http://openfontlibrary.org) per the FONTLOG.txt

The librefonts/medievalsharp repository was created in 2014 as a TTX-decomposed archive of the font, predating the google/fonts initial commit (2015). The single commit (`0bf7f34`) represents the state of the sources at that time.

## Build Configuration

**No config.yaml exists or can be created.** The font sources are exclusively in FontForge SFD format, which is not supported by gftools-builder. Building from these sources would require:

1. Converting the SFD to a gftools-compatible format (UFO or .glyphs)
2. Creating a config.yaml referencing the converted sources
3. Verifying the build output matches the existing binary

This is outside the scope of metadata enrichment and would constitute a font engineering task.

## Findings

1. **No source block in METADATA.pb** — needs to be added
2. **librefonts/medievalsharp is the appropriate upstream repo** — it contains the SFD source and VFB source files for the single-style font that matches what is in Google Fonts
3. **The only commit is `0bf7f34`** — this is the sole commit in the repository and represents the archived state of the sources
4. **SFD-only sources** — gftools-builder cannot build from SFD files, so no config.yaml can be provided
5. **wmk69/Medieval-Sharp is NOT the onboarding repo** — it was created in 2022, contains an expanded 4-style family, and represents newer work by the designer
6. **The font has not been updated since initial onboarding** — the binary in google/fonts dates to 2011 and has never been rebuilt

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/medievalsharp"
  commit: "0bf7f34428dfca63c645b586572e85af77095d08"
  branch: "master"
}
```

**Notes**:
- No `config_yaml` field is included because the sources are SFD-only and no gftools-builder configuration exists or can be created without source format conversion
- The commit hash `0bf7f34428dfca63c645b586572e85af77095d08` is the only commit in the repository
- Status is "incomplete" because while the repository URL and commit are known, there is no gftools-builder compatible build configuration
