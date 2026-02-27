# Ewert - Investigation Report

## Family Details
- **Family name**: Ewert
- **Designer**: Johan Kallas, Mihkel Virkus
- **License**: OFL
- **Category**: DISPLAY
- **Date added**: 2012-02-08
- **Path in google/fonts**: `ofl/ewert`

## Source Repository
- **Repository URL**: https://github.com/librefonts/ewert
- **Status**: Accessible (HTTP 200)
- **Branch**: master

## Repository Analysis

### Commit History
The repository contains a single commit:

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `21fa9ed` | 2014-10-17 | hash3g | update .travis.yml |

This is a single-commit repository created by the `librefonts` GitHub organization (maintained by hash3g). The librefonts org migrated individual font families from the monolithic Google Font Directory into separate per-family repositories, each with CI via Travis CI and fontbakery.

### Source Files
The repository contains:
- `src/Ewert-Regular-TTF.sfd` -- FontForge SFD source (558,360 bytes)
- `src/Ewert-Regular-OTF.vfb` -- FontLab VFB binary source (119,693 bytes)
- Various TTX dumps of the compiled TTF and OTF files
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`
- `.travis.yml` for CI with fontbakery

The primary source format is **SFD (FontForge)**, which is not compatible with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` files.

### Config File
- **No config.yaml** in the upstream repository
- **No config.yaml** in the google/fonts family directory
- Not applicable: SFD sources are not compatible with gftools-builder

## Google Fonts History

### Binary File History
The TTF file (`Ewert-Regular.ttf`, 70,752 bytes) was added in the initial commit of the google/fonts repository:
- Commit `90abd17b` (2015-03-07) by Dave Crossland -- "Initial commit"
- The font has never been updated since being added to the repository.

### Font Metadata (from binary)
- **Version**: 1.001
- **Copyright**: Copyright (c) 2011, Johan Kallas, Copyright (c) 2011 Mihkel Virkus
- **Unique ID**: JohanKallas,MihkelVirkus: Ewert: 2012
- **Created/Modified**: Fri Feb 3 21:13:17 2012

The font was originally created in February 2012 and released as version 1.001.

### METADATA.pb Changes
1. `90abd17b` (2015-03-07) -- Initial commit (added with the entire google/fonts repo)
2. `480630de` -- Tentative update to METADATA.pb textprotos
3. `27f377ab` -- Update copyright field
4. `883939708` -- Remove METADATA.json files
5. `06331b24` (2021-03-22) -- Ewert: Multiple designers fixed (#3228) by Rosalie Wagner
6. Various language support and classification batch updates
7. `df925b959` (2026-02-27) -- Ewert: add source block to METADATA.pb (also added upstream_info.md)

## Commit Hash Verification

Since the librefonts/ewert repository has only a single commit (`21fa9ed`), and the TTX dumps in the repository match the font metadata in the google/fonts binary (Version 1.001, same copyright, same name table entries), the commit hash `21fa9ed2031b8f7f1bec75cb3f91ad495e3b2370` is the correct reference.

The upstream repo was created on 2014-10-17, while the font was added to Google Fonts on 2012-02-08 (pre-dating the librefonts repo). This confirms the librefonts repo is a migration of the original sources, not the original development repository. The original sources from the designers (Johan Kallas and Mihkel Virkus) are not available in a separate public repository.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/ewert"
  commit: "21fa9ed2031b8f7f1bec75cb3f91ad495e3b2370"
}
```

No `config_yaml` field is needed because the sources are SFD-only (FontForge format), which is not compatible with gftools-builder.

## Status
- **Status**: complete (SFD-only sources)
- **Confidence**: HIGH
- **Config**: none (SFD-only sources)

## Notes
- The librefonts organization was a community effort by hash3g to split the monolithic Google Font Directory into individual per-family repositories with CI integration.
- The SFD and VFB sources are legacy formats. If this font were to be rebuilt, the sources would need to be converted to a gftools-compatible format (.glyphs, .ufo, or .designspace).
- The font has not been updated since its original onboarding in 2012.
