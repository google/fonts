# Abril Fatface

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: TypeTogether
**METADATA.pb path**: `ofl/abrilfatface/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/abrilfatface |
| Commit | `5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f` |
| Config YAML | -- |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/abrilfatface` was identified from the upstream repo cache at `upstream_repos/fontc_crater_cache/librefonts/abrilfatface`. There is no `source { }` block in METADATA.pb at all. The `librefonts` organization on GitHub hosts TTX-decomposed mirrors of many early Google Fonts families, created by Dave Crossland.

Note: TypeTogether (the credited designer) does not appear to have a public GitHub repository for Abril Fatface. The `librefonts/abrilfatface` repo is a legacy TTX mirror, not the original design source.

## How the Commit Hash Was Identified

The upstream repo has only a single commit: `5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f` (dated 2014-10-17, message: "update .travis.yml"). This is the HEAD and only commit of the repository. The commit hash was selected as it represents the complete state of this single-commit repo.

The last font-modifying commit in google/fonts is `90abd17b4f97` from 2015-03-07, with message "Initial commit" (part of the initial google/fonts repository setup). The font was added to Google Fonts on 2011-08-31 according to METADATA.pb, predating this repository's creation.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in the google/fonts family directory (`ofl/abrilfatface/`).

The upstream repo contains only legacy source formats:
- `src/AbrilFatface-Regular-TTF.sfd` (FontForge SFD format)
- `src/AbrilFatface-Regular.vfb` (FontLab VFB format)
- Various `.ttx` decomposed table files
- OTF-related TTX source files

These source formats are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. A config.yaml cannot be meaningfully created without converting the sources to a modern format first.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:27:35 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/AbrilFatface-Regular-TTF.sfd`, `src/AbrilFatface-Regular.vfb`, various `.ttx` files

## Confidence

**Medium**: The repository URL is confirmed and the commit is verified in the upstream repo. However, `librefonts/abrilfatface` is a legacy TTX mirror, not a true design source repository. TypeTogether (the credited designer) may have the original design sources in a different format or location. The font binary in google/fonts predates the librefonts repo (2011 vs 2014). The relationship between this repo and the original font production is indirect -- the repo was created as an archival/reproducibility effort, not as the original design source.

## Open Questions

- Does TypeTogether maintain an original source repository for Abril Fatface with `.glyphs` or `.ufo` sources?
- Since the source formats (SFD/VFB) are not gftools-builder compatible, is there a plan to convert the sources to a modern format?
- Should METADATA.pb be updated to include a `source { }` block pointing to this repo, even though it cannot be built with gftools-builder?
- The font has been in Google Fonts since 2011 and has not been updated since the initial commit. Is an update planned?
