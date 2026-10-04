# Investigation Report: Emilys Candy

- **Date investigated**: 2026-02-27
- **Status**: missing_config (VFB-only sources, not gftools-buildable)
- **Designer**: Neapolitan (Crystal Kluge, Font Diner, Inc)

## METADATA.pb Path

`ofl/emilyscandy/METADATA.pb`

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/librefonts/emilyscandy |
| commit           | 6c0f2ad7e9b0bcc6d69bbd5896b980bf1e208074 |
| config_yaml      | N/A (VFB-only sources) |

## How URL Was Found

The upstream repository URL `https://github.com/librefonts/emilyscandy` was already documented in the project tracking data (`data/gfonts_library_sources.json`). The repository is part of the `librefonts` GitHub organization, which hosts many early Google Fonts families that were migrated from the legacy `googlefontdirectory` structure. The URL was verified to return HTTP 200.

## How Commit Hash Was Identified

The upstream repository at `librefonts/emilyscandy` contains exactly **one commit**:

- `6c0f2ad` (2014-10-17) by hash3g - "update .travis.yml"

Despite the commit message saying "update .travis.yml", this is actually the sole commit in the repository, containing all files (the repo was likely created via a batch process that squashed history). Since there is only one commit in the entire repository, there is no ambiguity about the commit hash.

The font was added to Google Fonts on 2012-02-29 (per `date_added` in METADATA.pb), which predates the upstream repo's creation. This is consistent with the librefonts organization pattern: these repos were created after the fonts were already in Google Fonts, as a way to provide source repositories for existing catalog entries.

In `google/fonts`, the font binary (`EmilysCandy-Regular.ttf`) was present in the initial commit (`90abd17b4`, 2015-03-07 by Dave Crossland) and has not been modified since. The FONTLOG.txt in google/fonts is identical to the one in the upstream repo.

## How Config YAML Was Resolved

**No config.yaml exists** in the upstream repository, and no override config.yaml exists in the `google/fonts` family directory.

The upstream repository contains:
- `src/EmilysCandy-Regular-TTF.vfb` - FontLab Studio binary format (proprietary)
- Decomposed TTX files (XML representation of the compiled TTF)
- `.travis.yml` with a fontbakery-build pipeline
- `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`

The VFB format is a proprietary FontLab Studio format that is **not supported by gftools-builder**. The TTX files are decomposed representations of the already-compiled binary, not true editable sources. Therefore, no config.yaml can be created for this family -- it cannot be rebuilt from source using the current gftools toolchain.

## Verification

- **Repository URL**: Verified accessible (HTTP 200)
- **Repository is clean**: `git status` shows clean working tree, up to date with `origin/master`
- **Commit exists**: Only one commit in the repo; hash `6c0f2ad7e9b0bcc6d69bbd5896b980bf1e208074` is the HEAD of master
- **FONTLOG match**: The FONTLOG.txt in google/fonts matches the upstream repo exactly
- **DESCRIPTION match**: Content matches between google/fonts and upstream (minor HTML formatting differences from a 2024 reformatting commit in google/fonts)
- **Source block status**: No source block in METADATA.pb on the main branch of google/fonts (one was proposed in an unmerged branch `sources_info_2026-02-25`)

## Confidence

**HIGH** -- The repository URL is confirmed valid, and there is only one commit in the repository, making the commit hash unambiguous. The font sources are VFB-only, which is a known limitation for many early Google Fonts families.

## Notes

- Designer is Crystal Kluge of Neapolitan (a DBA of Font Diner, Inc)
- The font copyright contains a typo: "Reseved" instead of "Reserved"
- The repo was created as part of the librefonts batch migration of early Google Fonts families
- The `.travis.yml` references legacy tooling (fontbakery-build.py, fontcrunch, python 2.7)
- This family cannot be rebuilt from source without the original FontLab Studio project or conversion of the VFB to a modern format (.glyphs, .ufo)
