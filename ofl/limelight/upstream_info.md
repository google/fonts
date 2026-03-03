# Investigation Report: Limelight

**Model**: Claude Opus 4.6

## Summary

Limelight is a display typeface designed by Nicole Fally with spacing and mastering by Eben Sorkin (Sorkin Type). It was added to Google Fonts on 2011-05-25 and has not been updated since the initial google/fonts repository commit on 2015-03-07. The upstream repository is `librefonts/limelight`, which contains only legacy source files (SFD/VFB formats) -- not compatible with gftools-builder. No config.yaml exists or can be created for this font.

## METADATA.pb Analysis

The current METADATA.pb at `ofl/limelight/METADATA.pb` contained no source block. Key fields:
- **Family name**: Limelight
- **Designer**: Nicole Fally, Sorkin Type
- **License**: OFL
- **Category**: DISPLAY
- **Date added**: 2011-05-25
- **Source block**: None

## Upstream Repository

**Repository**: [librefonts/limelight](https://github.com/librefonts/limelight)

The `librefonts` organization was created on 2013-10-20 by Google Fonts team members (davelab6, felipesanches, pathumego) to decompose the monolithic google/fonts repository into individual per-font source repositories. The Limelight repo was created on 2014-07-16 by Mikhail Kashkin (hash3g) with the commit message "Move limelight font files to separate repository."

The repository is not archived and not a fork. It has 12 commits total, all from 2014, primarily updating Travis CI configuration.

### Source Files

The repository contained only legacy format source files:
- `src/Limelight-Regular-TTF.sfd` (FontForge SFD)
- `src/Limelight-Regular-OTF.sfd` (FontForge SFD)
- `src/Limelight-Regular.vfb` (FontLab VFB)

Additionally, the repo contained decomposed TTX table dumps for both TTF and OTF versions.

**No gftools-builder compatible sources** (`.glyphs`, `.ufo`, `.designspace`) were found. No `config.yaml` existed in the repository.

### Commit History

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `f361773` | 2014-10-17 | hash3g | update .travis.yml |
| `36f4764` | 2014-10-06 | hash3g | Rename fontbakery |
| `288a162` | 2014-09-19 | hash3g | Update .travis.yml |
| `886773d` | 2014-09-15 | hash3g | Update .travis.yml |
| `d3ff1ff` | 2014-09-14 | hash3g | Installing ttfautohint from ppa |
| `0d56b89` | 2014-09-12 | hash3g | Added raw=True to VDMX and FFTM |
| `fdcaa8d` | 2014-09-11 | hash3g | update .travis.yml |
| `338c014` | 2014-08-22 | hash3g | Travis.yml update |
| `5599c12` | 2014-08-22 | hash3g | Travis.yml update |
| `50f7dc1` | 2014-08-21 | hash3g | Travis.yml update |
| `3569785` | 2014-08-19 | hash3g | Added .travis.yml |
| `3001376` | 2014-07-16 | Mikhail Kashkin | Move limelight font files to separate repository |

The HEAD commit (`f361773`) was used as the reference commit. Source files were unchanged after the initial commit (`3001376`); all subsequent commits only modified `.travis.yml` configuration.

## Font Binary History in google/fonts

The font binary `Limelight-Regular.ttf` (132,292 bytes, MD5: `665b887accf0b7deeeb087259fe67d59`) was included in the initial monolithic commit (`90abd17b4`) on 2015-03-07 and has never been updated since.

The FONTLOG indicated version 1.002, dated April 2012, with mastering by Eben Sorkin. The font's head table showed a creation date of April 7, 2012 and modification date of August 20, 2012.

## Verification

- **FONTLOG.txt**: Identical between google/fonts and librefonts/limelight.
- **OFL.txt**: Identical between google/fonts and librefonts/limelight.
- **Version**: Both indicated v1.002 (April 2012).
- The upstream repo contained no TTF binary -- only TTX decompositions and SFD/VFB sources.

## PR History in google/fonts

- **PR #6032** (merged 2023-03-16): "Limelight: Added designer (sorkin)" by emmamarichal -- added "Sorkin Type" to the designer field in METADATA.pb.
- **PR #6031** (merged 2023-06-07): Removed a useless line in Sorkin description.
- No PRs existed for source metadata or font binary updates.

## config.yaml Assessment

An override config.yaml **cannot** be created because:
- The upstream sources are in SFD (FontForge) and VFB (FontLab) formats only.
- These formats are not supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources.
- No modern source files exist in any known repository.

## Recommendation

A source block can be added to METADATA.pb pointing to `librefonts/limelight` at commit `f361773`, but without a `config_yaml` field since no gftools-builder compatible sources exist. The source block would document the upstream repository for reference purposes.

```
source {
  repository_url: "https://github.com/librefonts/limelight"
  commit: "f361773b306c507e22a46d18d5e661a6dac84894"
}
```

## Status

- **Status**: no_config (SFD-only sources)
- **Confidence**: HIGH
- **Config**: none (SFD-only sources)
