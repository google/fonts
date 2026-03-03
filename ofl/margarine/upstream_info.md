# Margarine — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only basic metadata (name, designer, license, category, fonts, subsets, stroke, classifications).

## Repository Analysis

**Repository**: https://github.com/librefonts/margarine
**Owner**: librefonts (a third-party organization, not the original designer)
**Created**: 2014-07-16
**Default branch**: master
**Total commits**: 12 (all from 2014, by Mikhail Kashkin aka hash3g)

The `librefonts` organization (861 public repos) was a third-party effort by Mikhail Kashkin that extracted font files from the old Google Font Directory into individual GitHub repositories. This is not an original upstream source maintained by the designer.

### Commit History

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `56637ab` | 2014-07-16 | Mikhail Kashkin | Move margarine font files to separate repository |
| `645187d` | 2014-07-18 | Mikhail Kashkin | cleanup |
| `70e841c` - `c612652` | 2014-08-19 to 2014-10-17 | hash3g | Various .travis.yml updates |

### Repository Contents

The repo contains only:
- **TTX files**: Decomposed TrueType tables (`Margarine-Regular.ttf.*.ttx`) at root level
- **VFB files**: FontLab Studio binaries in `src/` directory:
  - `Margarine-Regular.vfb` (original source)
  - `Margarine-Regular-TTF.vfb` (TrueType outlines with hinting)
  - `Margarine-Regular-OTF.vfb` (merged contours, optimized)
- **OTF TTX**: Decomposed OTF tables in `src/`
- **No config.yaml**
- **No modern source files** (.glyphs, .ufo, .designspace, .sfd)

The VFB (FontLab Studio) format is a proprietary binary format that is not compatible with gftools-builder. The TTX files are decompositions of the compiled fonts, not editable design sources.

## Onboarding History

The font was added to google/fonts in the initial commit (`90abd17b4`, 2015-03-07, by Dave Crossland). This was the massive initial import of the entire Google Fonts library into the current GitHub repository structure. No PR or specific onboarding process was associated with this font -- it was part of the bulk migration.

The font was originally designed by Brian J. Bonislawsky (Astigmatic/AOETI) and released in November 2012 (Version 1.000). The font has never been updated in google/fonts since the initial commit (aside from metadata changes to METADATA.pb).

### Original Designer

- **Designer**: Brian J. Bonislawsky
- **Foundry**: Astigmatic (AOETI)
- **Email**: astigma@astigmatic.com
- **Website**: www.astigmatic.com
- **GitHub**: https://github.com/astigmatic (exists but has no font repos)

The designer has a GitHub account but does not host font sources there. No alternative upstream repository with modern source files was found.

## Build Configuration

**No config.yaml exists** in the upstream repo, and **no override config.yaml** can be created because there are no gftools-builder compatible source files. The only source files are VFB (FontLab) binaries, which cannot be processed by gftools-builder.

An override config.yaml is not feasible because:
1. VFB files require FontLab Studio (proprietary) to open
2. There are no .glyphs, .ufo, or .designspace files that gftools-builder could use
3. The TTX files are decompositions of already-compiled binaries, not true design sources

## Findings

1. **No source block** exists in METADATA.pb.
2. **The librefonts/margarine repo** is a third-party extraction of files from the old Google Font Directory, not an original upstream maintained by the designer. All commits were from Mikhail Kashkin in 2014, and the repo has been dormant since.
3. **No modern source files** exist anywhere -- the only sources are VFB (FontLab) binaries, which are not compatible with gftools-builder.
4. **The original designer** (Brian J. Bonislawsky / Astigmatic) has a GitHub account but no font source repositories.
5. **No config.yaml** can be created (neither upstream nor override) due to lack of compatible source files.
6. **The font has never been updated** since the initial bulk import in 2015.

## Recommended Source Block

A source block can be added pointing to the librefonts repo as the best available reference, but it should be noted that this is a third-party mirror with VFB-only sources:

```
source {
  repository_url: "https://github.com/librefonts/margarine"
  commit: "c6126521f50b0be64bbc44cd287f71eb706127a1"
  branch: "master"
}
```

**Notes**:
- The `config_yaml` field is omitted because no config.yaml exists and none can be created (VFB-only sources).
- The commit `c612652` is the latest (and only meaningful) commit in the repo. Since the librefonts repo was created after the font was already in Google Fonts, this commit does not represent an original onboarding commit -- it represents the state of a third-party extraction.
- This source block is of limited value since the font cannot be rebuilt from these sources using modern tooling.
- Status should be recorded as `missing_config` with a note about VFB-only sources.
