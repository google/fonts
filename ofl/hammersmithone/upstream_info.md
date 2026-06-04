# Investigation Report: Hammersmith One

## Summary

Hammersmith One is a low-contrast sans-serif display family designed by Nicole Fally, with spacing and mastering by Eben Sorkin (Sorkin Type Co.). It was added to Google Fonts in the initial commit (2015-03-07, but date_added is 2011-06-29). The upstream repository at `librefonts/hammersmithone` is an archive-style repo containing SFD (FontForge) and VFB (FontLab) source files, plus TTX decomposed tables. There is no gftools-builder compatible source, no config.yaml, and no designspace. The repo has only a single commit and the sources are in legacy formats only.

## Key Findings

| Field              | Value                                                        |
|--------------------|--------------------------------------------------------------|
| Family Name        | Hammersmith One                                              |
| Designer           | Nicole Fally                                                 |
| License            | OFL                                                          |
| Date Added         | 2011-06-29                                                   |
| Repository URL     | https://github.com/librefonts/hammersmithone                 |
| Commit Hash        | a5fae41a3eabe8ec4e1d8ff7b3fa6dfde5c4fa87                     |
| Branch             | master                                                       |
| Config YAML        | None                                                         |
| Source Types       | SFD (FontForge), VFB (FontLab), TTX                         |
| Weights            | Regular only                                                 |
| Google Fonts Ver.  | 1.003                                                        |
| Upstream Repo Ver. | 1.003 (per VERSIONS.txt)                                     |
| Status             | **no_config_possible**                                       |
| Confidence         | HIGH                                                         |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb on the main branch of google/fonts has no source block. A source block was added on the `sources_info_2026-02-25` branch (commit 9a14639f3) but has not yet been merged.

### Git History in google/fonts

The font was included in the initial commit `90abd17b4f` (2015-03-07) by Dave Crossland. Key subsequent changes:

1. **ff6fd2655** (2020-10-14) - "hammersmithone: name table updated to match API (#2351)" -- Co-authored by Micah Stupak. Updated the TTF with corrected name table entries.
2. No other TTF-modifying commits beyond the initial and the name table fix.

### Upstream Repository Analysis

The repository `librefonts/hammersmithone` is cached at `upstream_repos/fontc_crater_cache/librefonts/hammersmithone/`. It contains:

- **Single commit**: `a5fae41a3e` (2014-10-17): "update .travis.yml"
- **Source files in `src/`**:
  - `HammersmithOne-Regular.vfb` -- Original FontLab source with contour overlaps
  - `HammersmithOne-Regular-OTF.sfd` -- FontForge SFD for OTF output
  - `HammersmithOne-Regular-TTF.sfd` -- FontForge SFD for TTF output with hinting
  - Various TTX table decompositions
- **No UFO, Glyphs, or designspace files**
- **No config.yaml**
- **Travis CI config**: Uses `fontbakery-build.py` for build/test, not gftools-builder

The repo is a `librefonts` archive -- these were created as mirrors of Google Fonts families with their sources decomposed to TTX. The original source is the VFB file.

### Source Format Assessment

The only editable sources are:
- VFB (FontLab proprietary binary format) -- not supported by gftools-builder
- SFD (FontForge format) -- not supported by gftools-builder

The TTX files are decomposed table dumps, not a primary source format for font compilation.

### Version Match

The VERSIONS.txt in the repo states `HammersmithOne-Regular.ttf: Version 1.003`, matching the version string in the google/fonts binary. The google/fonts copy was later updated with a name table fix in PR #2351, but the version number remained 1.003.

## Conclusion

The upstream repository is correctly identified. The commit hash `a5fae41a3eabe8ec4e1d8ff7b3fa6dfde5c4fa87` is the only commit in the repo. The sources are exclusively in SFD/VFB formats, which are not compatible with gftools-builder. No config.yaml is possible without converting the sources to a supported format (UFO or Glyphs).

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/hammersmithone"
  commit: "a5fae41a3eabe8ec4e1d8ff7b3fa6dfde5c4fa87"
}
```

### Status: no_config_possible

SFD/VFB-only sources. These legacy formats are not compatible with gftools-builder, and creating a config.yaml is not possible without first converting the sources to UFO or Glyphs format.
