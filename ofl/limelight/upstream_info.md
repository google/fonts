# Investigation Report: Limelight

**Model**: Claude Opus 4.6

## Source Repository

The original design sources for Limelight are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `limelight/src/`.

### Source Files in googlefontdirectory-hg

- `Limelight-Regular.vfb` -- FontLab binary source (proprietary, not buildable with gftools-builder)
- `Limelight-Regular-OTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Limelight-Regular-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Limelight-Regular.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are in VFB and SFD legacy formats only. No `.glyphs`, `.ufo`, or `.designspace` files are present. These formats are not compatible with gftools-builder.

## Summary

Limelight is a display typeface designed by Nicole Fally with spacing and mastering by Eben Sorkin (Sorkin Type). It was added to Google Fonts on 2011-05-25 and has not been updated since the initial google/fonts repository commit on 2015-03-07.

## METADATA.pb Analysis

The current METADATA.pb at `ofl/limelight/METADATA.pb` contained no source block. Key fields:
- **Family name**: Limelight
- **Designer**: Nicole Fally, Sorkin Type
- **License**: OFL
- **Category**: DISPLAY
- **Date added**: 2011-05-25
- **Source block**: None

## Upstream Repository (librefonts archive)

**Repository**: [librefonts/limelight](https://github.com/librefonts/limelight)

The `librefonts` organization was created on 2013-10-20 by Google Fonts team members (davelab6, felipesanches, pathumego) to decompose the monolithic google/fonts repository into individual per-font source repositories. The Limelight repo was created on 2014-07-16 by Mikhail Kashkin (hash3g) with the commit message "Move limelight font files to separate repository."

The repository is not archived and not a fork. It has 12 commits total, all from 2014, primarily updating Travis CI configuration.

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

## Build Configuration

An override config.yaml **cannot** be created because:
- The upstream sources are in SFD (FontForge) and VFB (FontLab) formats only.
- These formats are not supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources.
- No modern source files exist in any known repository.

## Conclusion

- **Repository URL**: `https://github.com/librefonts/limelight`
- **Commit**: `f361773b306c507e22a46d18d5e661a6dac84894`
- **Config**: None (SFD/VFB-only sources, not gftools-builder compatible)
- **Confidence**: HIGH
