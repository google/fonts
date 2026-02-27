# Investigation Report: Esteban

- **Date investigated**: 2026-02-27
- **Status**: SFD-only sources (not gftools-builder compatible)
- **Designer**: Angelica Diaz
- **METADATA.pb path**: `ofl/esteban/METADATA.pb`

## Source Data

| Field            | Value                                                |
|------------------|------------------------------------------------------|
| Repository URL   | https://github.com/librefonts/esteban                |
| Commit hash      | 35e274d49210b9c8a7864689b48d6156e6be6bbf             |
| Branch           | master                                               |
| Config YAML      | None (SFD-only sources)                              |
| Source format(s) | .vfb (FontLab), .sfd (FontForge)                     |

## Current METADATA.pb State

The METADATA.pb has no `source { }` block. It contains only basic font metadata:
- `name`: "Esteban"
- `designer`: "Angelica Diaz"
- `license`: "OFL"
- `category`: "SERIF"
- `date_added`: "2012-01-11"
- Single font: Esteban-Regular.ttf (weight 400, normal style)

## How URL Was Found

The repository URL `https://github.com/librefonts/esteban` was identified from the `fontc_crater_cache` directory structure. The `librefonts` GitHub organization was created as part of the fontbakery project to host decomposed font sources (TTX tables) alongside original source files. This repo is a fontbakery-era mirror, not an original designer repository.

The URL was verified accessible (HTTP 200).

## How Commit Hash Was Identified

The upstream repository contains only a single commit:

- **35e274d** (2014-10-17): "update .travis.yml" by hash3g <hash.3g@gmail.com>

This is the only commit in the repository, so it is trivially the correct reference. The commit created all files in the repo as a single initial import, including:
- TTX decomposed tables of the TTF and OTF binaries
- Source files: `src/Esteban-Regular.vfb`, `src/Esteban-Regular-OTF.vfb`, `src/Esteban-Regular-TTF.sfd`
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`
- `.travis.yml` for fontbakery CI

The font binary in google/fonts (`ofl/esteban/Esteban-Regular.ttf`) was added in the initial google/fonts commit `90abd17b4` (2015-03-07, Dave Crossland "Initial commit") and has never been updated since. The font reports Version 1.002.

The upstream repo's `src/VERSIONS.txt` confirms: "Esteban-Regular.ttf: Version 1.002", matching the binary in google/fonts.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files are in legacy formats:
- `src/Esteban-Regular.vfb` - FontLab VFB format (proprietary binary)
- `src/Esteban-Regular-OTF.vfb` - FontLab VFB format (for OTF output)
- `src/Esteban-Regular-TTF.sfd` - FontForge SFD format

None of these formats (.vfb, .sfd) are compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. An override `config.yaml` cannot be created because there are no compatible source files to reference.

The `.travis.yml` in the repo shows it used `fontbakery-build.py` for CI builds, which is a legacy build system that predates gftools-builder.

## Verification

- **Repository accessible**: Yes (HTTP 200)
- **Repository clean**: Yes (`nothing to commit, working tree clean`)
- **Branch**: master (single branch, up to date with origin)
- **Binary match**: The font in google/fonts is Version 1.002, matching the upstream's `src/VERSIONS.txt`
- **No updates since onboarding**: The font binary has only been touched once in google/fonts (initial commit 90abd17b4)
- **No config.yaml possible**: Source formats (.vfb, .sfd) are incompatible with gftools-builder

## Confidence

**HIGH** -- The upstream repository has a single commit, making identification trivial. The version numbers match. However, this is a `librefonts` mirror repository, not the original designer's source repository. The original sources may have been in the old Google Font Directory (`googlefontdirectory/esteban/` as referenced in `src/METADATA_comments.txt`).

## Notes

- This font was added to Google Fonts on 2012-01-11 (per `date_added` in METADATA.pb), predating the librefonts mirror (2014-10-17) and the google/fonts initial commit (2015-03-07).
- The designer is Angelica Diaz Rivera, contactable at angiecina@gmail.com per the copyright notice and FONTLOG.
- The font is named after Jorge Alfredo Diaz Esteban, a writer whose manuscript style inspired the typeface's modulated strokes.
- The `librefonts` repository is essentially an archival mirror with TTX-decomposed tables and legacy source files. It does not represent an active upstream development repository.
- Building from source would require converting the .sfd or .vfb files to a modern format (.glyphs or .ufo) first.
- A source block could be added to METADATA.pb pointing to this repo, but with status "missing_config" since no gftools-builder config is possible with the current source formats.
