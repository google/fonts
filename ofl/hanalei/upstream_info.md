# Investigation Report: Hanalei

## Summary

Hanalei is a Polynesian-inspired display font designed by Brian J. Bonislawsky of Astigmatic (AOETI). It was added to Google Fonts in the initial commit (2015-03-07, but date_added is 2012-11-26). The upstream repository at `librefonts/hanalei` is an archive-style repo containing VFB (FontLab) source files and TTX table decompositions. There are no gftools-builder compatible sources, no config.yaml, and no UFO or Glyphs files. The repo has a single commit.

## Key Findings

| Field              | Value                                                        |
|--------------------|--------------------------------------------------------------|
| Family Name        | Hanalei                                                      |
| Designer           | Astigmatic (Brian J. Bonislawsky)                            |
| License            | OFL                                                          |
| Date Added         | 2012-11-26                                                   |
| Repository URL     | https://github.com/librefonts/hanalei                        |
| Commit Hash        | ec0b5be2259cfe4261f530047d60de8617eabf80                     |
| Branch             | master                                                       |
| Config YAML        | None                                                         |
| Source Types       | VFB (FontLab), TTX                                           |
| Weights            | Regular only                                                 |
| Google Fonts Ver.  | 1.000                                                        |
| Upstream Repo Ver. | 1.000 (per VERSIONS.txt)                                     |
| Status             | **no_config_possible**                                       |
| Confidence         | HIGH                                                         |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb on the main branch of google/fonts has no source block. A source block was added on the `sources_info_2026-02-25` branch (commit 9a14639f3) but has not yet been merged.

### Git History in google/fonts

The font was included in the initial commit `90abd17b4f` (2015-03-07) by Dave Crossland. There have been no subsequent modifications to the TTF file -- it has remained unchanged since the initial commit. All later commits touching the `ofl/hanalei/` directory only modified METADATA.pb (language support, format changes).

### Upstream Repository Analysis

The repository `librefonts/hanalei` is cached at `upstream_repos/fontc_crater_cache/librefonts/hanalei/`. It contains:

- **Single commit**: `ec0b5be225` (2014-10-17): "update .travis.yml"
- **Source files in `src/`**:
  - `Hanalei-Regular.vfb` -- Original FontLab source with contour overlaps
  - `Hanalei-Regular-OTF.vfb` -- Merged contours for OTF
  - `Hanalei-Regular-TTF.vfb` -- TrueType outlines with hinting
  - `METADATA_comments.txt`
  - `VERSIONS.txt`
- **TTX decompositions at root level**: Multiple `.ttx` table files
- **No UFO, Glyphs, SFD, or designspace files**
- **No config.yaml**
- **Travis CI config**: Uses `fontbakery-build.py`, not gftools-builder

The repo is a `librefonts` archive -- created as a mirror of the Google Fonts family with sources. The primary source format is VFB (FontLab proprietary binary).

### Source Format Assessment

The only editable sources are VFB files (FontLab proprietary binary format). These are not supported by gftools-builder. The TTX files are decomposed table dumps from the compiled binary, not a primary design source.

### Version Match

The VERSIONS.txt states `Hanalei-Regular.ttf: Version 1.000`, matching the version string in the google/fonts binary. The font has never been updated since its initial addition.

### Comparison with Hanalei Fill

Note: There is also a `librefonts/hanaleifill` repo in the cache, which is the companion font "Hanalei Fill" -- a separate family with filled letterforms vs. Hanalei's outline style.

## Conclusion

The upstream repository is correctly identified. The commit hash `ec0b5be2259cfe4261f530047d60de8617eabf80` is the only commit in the repo. The sources are exclusively in VFB format, which is not compatible with gftools-builder. No config.yaml is possible without first converting the sources to a supported format.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/hanalei"
  commit: "ec0b5be2259cfe4261f530047d60de8617eabf80"
}
```

### Status: no_config_possible

VFB-only sources. The FontLab proprietary binary format is not compatible with gftools-builder, and creating a config.yaml is not possible without first converting the sources to UFO or Glyphs format.
