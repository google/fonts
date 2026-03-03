# La Belle Aurore - Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete (VFB-only sources)
**Confidence**: HIGH

## Summary

La Belle Aurore is a handwriting font designed by Kimberly Geswein, added to Google Fonts on 2011-06-08. The upstream repository at `librefonts/labelleaurore` contains only VFB (FontLab binary) sources, which are not compatible with gftools-builder. No config.yaml is applicable.

## METADATA.pb Analysis

The current METADATA.pb on the main branch of google/fonts has no source block. A source block was previously prepared on the `sources_info_2026-02-25` branch (commit 9a14639f3) but has not been merged to main.

Current METADATA.pb fields:
- **name**: "La Belle Aurore"
- **designer**: "Kimberly Geswein"
- **license**: OFL
- **category**: HANDWRITING
- **date_added**: 2011-06-08
- **classifications**: DISPLAY, HANDWRITING

## Upstream Repository

- **URL**: https://github.com/librefonts/labelleaurore
- **Accessible**: Yes (HTTP 200)
- **Local cache**: `upstream_repos/fontc_crater_cache/librefonts/labelleaurore/`
- **Clean**: Yes (no local modifications, up to date with origin/master)

### Repository Contents

The repository has a single commit:

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| e285d8a62fafbf5acea45252d95abfe532eaaa5c | 2014-10-17 | hash3g | update .travis.yml |

This is an initial commit that populates the entire repository with:
- TTX table dumps of LaBelleAurore.ttf (split into individual table files)
- `src/LaBelleAurore.vfb` (FontLab binary source, 92458 bytes)
- `src/VERSIONS.txt` (records "Version 1.001 2001")
- `src/METADATA_comments.txt` (font-optimizer subset commands)
- `METADATA.json`, `DESCRIPTION.en_us.html`, `OFL.txt`
- `.travis.yml` (fontbakery CI configuration)

### Source Files

The only source file is `src/LaBelleAurore.vfb`, a FontLab binary format file. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files were found. VFB files are not supported by gftools-builder.

### Build Configuration

No `config.yaml` exists in the upstream repository, and none is needed since the VFB source format is not compatible with gftools-builder.

## Google Fonts History

The font file in google/fonts was modified by these commits:

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 90abd17b4 | 2015-03-07 | Dave Crossland | Initial commit |
| 8ccda7bf7 | 2015-08-05 | Dave Crossland | Fix fsType for 40 font files |

The current font file (`LaBelleAurore.ttf`, 59364 bytes, SHA256: `ed67462999e05f0cdac92f686374661e4d68c56fdcd7d05725c6df7b41eabd2a`) matches the version from the fsType fix commit (8ccda7bf7). The font has not been rebuilt from source since; the fsType fix was a binary patch to correct embedding permissions.

Note: Commit 76adaf1d2 ("deploy: c7e2740...") from 2021-11-01 appeared to delete the file, but this commit exists only on an abandoned deployment branch and is not part of the main branch history.

No override `config.yaml` exists in the `ofl/labelleaurore/` directory of google/fonts.

## Commit Hash Verification

The upstream repository has only one commit (`e285d8a`), which is the initial population of the repository by `hash3g` on 2014-10-17. This predates the google/fonts initial commit (2015-03-07), confirming it was available at onboarding time.

Since this is a `librefonts` repository (the Google Fonts project's archival organization for early font sources), and the repository contains TTX dumps that correspond to the font binary in google/fonts, `e285d8a` is the correct and only possible commit hash.

## Proposed Source Block

```
source {
  repository_url: "https://github.com/librefonts/labelleaurore"
  commit: "e285d8a62fafbf5acea45252d95abfe532eaaa5c"
}
```

No `config_yaml` field is needed because the upstream sources are VFB-only, which is not compatible with gftools-builder.

## Conclusion

La Belle Aurore's upstream repository was identified and verified. The repository contains VFB-only sources, so no config.yaml is applicable. The single commit `e285d8a` is the correct reference. The source block is ready to be added to METADATA.pb on the main branch of google/fonts.
