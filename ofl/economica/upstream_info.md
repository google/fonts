# Investigation Report: Economica

**Date investigated:** 2026-02-27
**Status:** missing_config
**Designer:** Vicente Lamonaca
**METADATA.pb path:** ofl/economica/METADATA.pb

## Source Data

| Field | Value |
|---|---|
| repository_url | https://github.com/librefonts/economica |
| commit_hash | 6bf48e6858755227cdd104ee4b44e9e2e4bb197b |
| config_yaml | N/A (SFD/VFB sources only) |

## How URL Was Found

The METADATA.pb file contains no `source` block, no `repository_url`, and no `config_yaml`. The upstream repository was found in the fontc_crater_cache at `librefonts/economica`. The remote URL is `https://github.com/librefonts/economica`, which returns HTTP 200 and is accessible.

The librefonts GitHub organization is a batch-import project created by Mikhail Kashkin (hash3g) that mirrors fonts from the old Google Font Directory into individual GitHub repositories. This is not the designer's own repository but serves as the only known public upstream source for this font.

## How Commit Hash Was Identified

The upstream repository contains exactly one commit:

- `6bf48e6` (2014-10-17, by hash3g): "update .travis.yml"

This single commit contains all files: the TTX decompositions of the compiled TTF fonts, SFD/VFB source files in `src/`, FONTLOG.txt, METADATA.json, OFL.txt, DESCRIPTION.en_us.html, and a .travis.yml for CI.

Since there is only one commit, the commit hash is trivially `6bf48e6858755227cdd104ee4b44e9e2e4bb197b`.

### Verification of font version match

The font version strings match between google/fonts and the upstream TTX decompositions:

| Font File | google/fonts Version | Upstream TTX Version |
|---|---|---|
| Economica-Regular.ttf | Version 1.101 | Version 1.101 |
| Economica-Bold.ttf | Version 1.100 | Version 1.100 |
| Economica-Italic.ttf | Version 1.100 | Version 1.100 |
| Economica-BoldItalic.ttf | Version 1.100 | Version 1.100 |

The TTX files in the upstream repo are decompositions of the same compiled TTFs that exist in google/fonts. The head table creation date is "Fri Feb 24 21:37:31 2012", consistent with the FONTLOG's initial release date of "24 Feb 2012" and the google/fonts `date_added` of 2012-02-29.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and one cannot be created for gftools-builder because the source files are in legacy formats:

- **SFD files** (FontForge): `src/Economica-Regular-TTF.sfd`, `src/Economica-Bold-TTF.sfd`, `src/Economica-Italic-TTF.sfd`, `src/Economica-BoldItalic-TTF.sfd`
- **VFB files** (FontLab Studio 5): `src/Economica-Regular-OTF.vfb`, `src/Economica-Bold-OTF.vfb`, `src/Economica-Italic-OTF.vfb`, `src/Economica-BoldItalic-OTF.vfb`

There are no `.glyphs`, `.ufo`, or `.designspace` files. The gftools-builder tool does not support SFD or VFB formats, so an override config.yaml cannot be created.

The .travis.yml references the legacy `fontbakery-build.py` tool from 2014, which is no longer maintained.

## Verification

- [x] Repository URL returns HTTP 200
- [x] Repository is clean (no local modifications)
- [x] Only one commit exists; hash is unambiguous
- [x] Font version strings match between google/fonts and upstream TTX decompositions
- [x] Copyright strings match: "Copyright (c) 2012, Vicente Lamonaca"
- [x] Head table creation date (2012-02-24) matches FONTLOG initial release date
- [x] No .glyphs/.ufo/.designspace sources available for gftools-builder

## Confidence

**MEDIUM** -- The repository URL is confirmed (librefonts/economica, accessible on GitHub) and the only commit hash is unambiguous. However, this is a librefonts batch-import repository, not the designer's canonical source. The font predates modern tooling and uses SFD/VFB sources that cannot be built with gftools-builder. Confidence is MEDIUM rather than HIGH because the librefonts repo is a secondary mirror, not the original designer's repository. No config.yaml can be provided.
