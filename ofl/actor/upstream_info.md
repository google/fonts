# Actor

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Thomas Junold
**METADATA.pb path**: `ofl/actor/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/actor |
| Commit | `b1617e5929c9a78c56bbbe056b471cfdbdc13c50` |
| Config YAML | -- |
| Branch | `master` |

## How the Repository URL Was Found

The METADATA.pb file contains **no source block** at all -- it only has the font name, designer, license, category, date_added (2011-08-03), font definition, and subsets. The repository URL `https://github.com/librefonts/actor` was discovered through research of the `librefonts` GitHub organization, which hosts mirrors/archives of many early Google Fonts projects. The URL has been verified as accessible (HTTP 200).

The copyright notice in METADATA.pb credits Thomas Junold (`hallo@buerofueraufmerksamkeit.de`), and the librefonts/actor repository contains TTX decompositions and VFB source files matching this font.

## How the Commit Hash Was Identified

The upstream repo contains only **one commit**:

- `b1617e5929c9a78c56bbbe056b471cfdbdc13c50` (2014-10-17): "update .travis.yml"

Since this is the sole commit in the repository, it is the only possible reference point. The font in google/fonts was last modified in the initial mass migration commit (`90abd17b4f97`, 2015-03-07: "Initial commit"), predating any structured onboarding process. There is no PR reference or packager commit to trace.

The google/fonts directory has had 5 subsequent commits, but all were metadata-only changes (language support, METADATA.pb cleanup, METADATA.json removal) -- none modified the actual .ttf file.

## How Config YAML Was Resolved

**No config.yaml exists or can be created** with the current source files:

- The upstream repo contains only **VFB** (FontLab 5 proprietary binary) source files:
  - `src/Actor-Regular-TTF.vfb`
  - `src/Actor-Regular.vfb`
- There are **no modern buildable sources** (`.glyphs`, `.ufo`, `.designspace`)
- No override `config.yaml` exists in `ofl/actor/` in google/fonts
- The remaining repo contents are TTX table dumps (decomposed binary representations) and metadata files

The font would need to be converted from VFB to a modern format (e.g., `.glyphs` or `.ufo`) before any gftools-builder configuration could be created.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:27:40 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Actor-Regular-TTF.vfb`, `src/Actor-Regular.vfb` (VFB binary format only -- not buildable with gftools)

## Confidence

**High**: The repository URL is confirmed valid, and with only one commit in the repo, there is no ambiguity about the commit reference. However, the practical usefulness is limited because VFB files cannot be built with gftools-builder, and the font has not been updated since its initial import into google/fonts in 2015.

## Open Questions

1. Should the METADATA.pb be updated to include a `source { repository_url }` block pointing to `https://github.com/librefonts/actor`?
2. Is there a plan to convert the VFB sources to `.glyphs` or `.ufo` format to enable modern builds?
3. Does Thomas Junold have the original editable sources in a more modern format?
