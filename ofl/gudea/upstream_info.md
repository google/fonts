# Investigation Report: Gudea

## Summary

Gudea is a sans-serif typeface designed by Agustina Mingote, added to Google Fonts on 2012-01-18. The upstream repository at `https://github.com/librefonts/gudea` contains only SFD and VFB source files -- legacy formats that are not compatible with gftools-builder. There is no config.yaml and no gftools-buildable sources (.glyphs, .ufo, .designspace). The repo has a single commit (0eb36c7) from 2014 and the font binaries in google/fonts have never been updated since the initial commit. The METADATA.pb currently has no source block on the main branch.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gudea                                                              |
| Designer          | Agustina Mingote                                                   |
| Date Added        | 2012-01-18                                                         |
| Repository URL    | https://github.com/librefonts/gudea                                |
| Commit Hash       | 0eb36c75099c39430192adf41887965fdc51e819                           |
| Branch            | master                                                             |
| Config            | None (SFD/VFB-only sources)                                        |
| Source Format     | SFD (FontForge), VFB (FontLab)                                     |
| Status            | **no_config_possible**                                             |
| Confidence        | HIGH                                                               |

## Investigation Details

### Upstream Repository

The upstream repo is `https://github.com/librefonts/gudea` (HTTP 200, verified accessible). It is cached locally at `fontc_crater_cache/librefonts/gudea`.

The repo has exactly one commit:
- `0eb36c7` (2014-10-17): "update .travis.yml" -- This is the initial and only commit, which added all files including source files, TTX dumps, metadata, and a Travis CI configuration.

### Source Files

The repo contains source files in legacy formats only:
- `src/Gudea-Regular-TTF.sfd` (FontForge SFD)
- `src/Gudea-Italic-TTF.sfd` (FontForge SFD)
- `src/Gudea-Bold-TTF.sfd` (FontForge SFD)
- `src/Gudea-Regular-OTF.vfb` (FontLab VFB)
- `src/Gudea-Italic-OTF.vfb` (FontLab VFB)
- `src/Gudea-Bold-OTF.vfb` (FontLab VFB)

There are NO `.glyphs`, `.ufo`, or `.designspace` files. There is no `config.yaml`. The repo also contains TTX table dumps of the font binaries.

These source formats (SFD and VFB) are not supported by gftools-builder/fontc, so no config.yaml can be created.

### Onboarding History

1. **Initial commit** (90abd17b, 2015-03-07, by Dave Crossland): Font originally added to google/fonts in the Initial commit.
2. The font binaries (Gudea-Regular.ttf, Gudea-Italic.ttf, Gudea-Bold.ttf) have never been updated since -- the only other commit touching them was the deploy commit (76adaf1d2, 2021-11-01) which was part of a temporary deletion/restoration cycle and does not represent a font update.

### Commit Hash Verification

The commit hash `0eb36c7` is the only commit in the librefonts/gudea repository. Since the repo was created in 2014 and the font was added to google/fonts in 2015, this commit predates the onboarding and is the correct reference point. The TTF files in the repo's TTX dumps correspond to the same font data as the binaries in google/fonts.

### Source Block Status

A source block with `repository_url` and `commit` was added to Gudea's METADATA.pb in commit `9a14639f3c` (2026-02-25) on the `sources_info_2026-02-25` branch, but this has NOT been merged to main yet. The main branch METADATA.pb has no source block.

## Conclusion

**Status: no_config_possible**

The upstream repo contains only SFD and VFB source files, which are not compatible with gftools-builder. A config.yaml cannot be created. The source block should document the repository URL and commit hash for provenance tracking, even though automated rebuilding is not possible.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/gudea"
  commit: "0eb36c75099c39430192adf41887965fdc51e819"
}
```
