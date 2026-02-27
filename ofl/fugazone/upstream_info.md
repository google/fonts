# Investigation Report: Fugaz One

## Summary

Fugaz One is a display typeface designed by LatinoType, added to Google Fonts on 2011-12-19. The upstream repository is at `https://github.com/librefonts/fugazone`, which contains only SFD and VFB source files. No gftools-builder compatible sources exist, so no config.yaml is possible. The repo has a single commit.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Fugaz One |
| Designer          | LatinoType |
| Repository URL    | https://github.com/librefonts/fugazone |
| Commit Hash       | d6fef0584e47767dc53d0144d0d41de77088184b |
| Config YAML       | N/A (SFD-only sources) |
| Status            | **no_config_possible** |
| Confidence        | HIGH |

## Investigation Details

### Google Fonts History

The font was part of the initial commit to the google/fonts repository (commit `90abd17b4`, dated 2015-03-07, by Dave Crossland). The font was originally added to Google Fonts on 2011-12-19 per METADATA.pb.

No source block exists in the current METADATA.pb on the main branch. A source block was added in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files") but this commit appears to be on a local branch, not yet merged to the upstream google/fonts main.

### Upstream Repository

- **URL**: https://github.com/librefonts/fugazone
- **Cached at**: `upstream_repos/fontc_crater_cache/librefonts/fugazone`
- **Single commit**: `d6fef05` (2014-10-17) - "update .travis.yml"
- The repo was created as a migration/archive of the original font sources

### Source Files

The repository contains:
- `src/FugazOne-Regular-TTF.sfd` - Spline Font Database (FontForge format)
- `src/FugazOne-Regular-OTF.vfb` - FontLab VFB binary format
- TTX decomposed font tables in root and `src/` directories

No `.glyphs`, `.ufo`, or `.designspace` files exist. The sources are in legacy formats (SFD, VFB) that are not compatible with gftools-builder.

### Config YAML

No config.yaml exists in the upstream repository, and none can be created because the sources are in SFD/VFB format only, which gftools-builder does not support.

## Conclusion

The source metadata is straightforward. The repository URL and commit hash are verified. No config.yaml is possible due to SFD-only sources.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/librefonts/fugazone"
  commit: "d6fef0584e47767dc53d0144d0d41de77088184b"
}
```
