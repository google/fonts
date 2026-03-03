# Investigation Report: Cousine

## Summary

Cousine is a monospace sans-serif font designed by Steve Matteson at Monotype Imaging, part of the Chrome OS core fonts family (alongside Arimo and Tinos). It is metrically compatible with Courier New. The current binaries in google/fonts are Version 1.21, last updated via PR #769 in August 2017. There is a development repository at `googlefonts/cousine` (created July 2020 by Marek Jeziorek) containing .glyphs sources and a variable font build, but the currently-serving static binaries predate this repo. There is also a `librefonts/cousine` mirror containing TTX dumps and no buildable sources. No config.yaml exists in either repo.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Cousine |
| Designer           | Steve Matteson |
| License            | Apache 2.0 |
| Category           | MONOSPACE |
| Date Added         | 2010-11-18 |
| Repository URL     | https://github.com/googlefonts/cousine |
| Commit Hash        | Not determinable for current v1.21 binaries |
| Config YAML        | None (no config.yaml in repo) |
| Source Types        | .glyphs (in googlefonts/cousine, for future VF build) |
| Font Version        | 1.21 |
| Status             | missing_config |
| Confidence         | MEDIUM |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/cousine/`
- **Files**: Cousine-Regular.ttf, Cousine-Italic.ttf, Cousine-Bold.ttf, Cousine-BoldItalic.ttf, DESCRIPTION.en_us.html, LICENSE.txt, METADATA.pb
- **No source block** in METADATA.pb
- **Font version**: Version 1.21 (from name table: "1.21;MONO;Cousine-Regular")
- **Copyright**: "Digitized data copyright (c) 2010-2012 Google Corporation."
- **Vendor**: Monotype Imaging Inc.

### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| b8df781 | 2017-08-07 | Marc Foley | hotfix-cousine: v1.211 added (#769) |
| 49fbebd | 2017 | (batch) | chmod -x on all font files |
| 90abd17 | 2015-03-07 | Dave Crossland | Initial commit |

The last substantive font update was PR #769, merged 2017-08-07 by Marc Foley. The PR body was empty, providing no upstream reference or commit hash.

### Upstream Repository: googlefonts/cousine

- **URL**: https://github.com/googlefonts/cousine
- **Created**: 2020-07-05 by Marek Jeziorek (marekj@google.com)
- **Default branch**: main
- **Description**: "Cousine sources, tests and development fonts"
- **Source files**: .glyphs format (sources/Cousine-Regular/Cousine-Regular.glyphs, etc.)
- **Built fonts**: Variable font only (fonts/ttf/hinted/variable_ttf/Cousine-VF.ttf)
- **No config.yaml** present in the repo
- **10 commits total**, last updated 2021-02-28

This repository was created in 2020 as a development repo for a variable font version of Cousine, using .glyphs sources. The variable font build has NOT been pushed to google/fonts yet -- the catalog still serves the older static v1.21 TTFs.

### Cached Mirror: librefonts/cousine

- **Path**: upstream_repos/fontc_crater_cache/librefonts/cousine
- **URL**: https://github.com/librefonts/cousine
- **Content**: TTX dumps of the binary fonts, plus FontForge subset scripts in src/
- **Source type**: TTX (decompiled binary, not original design sources)
- **Single commit** by hash3g (2014-10-17): "update .travis.yml"
- **Versions file**: Lists Version 1.21 for all four styles

This is a librefonts automated mirror containing decompiled TTX files. It is not a proper upstream source repository and should not be used as the repository_url in METADATA.pb.

### Origin of Current Binaries

The current v1.21 binaries were produced by Monotype Imaging (as indicated by the font name table). Cousine is one of the Chrome OS core fonts originally developed by Ascender Corporation (later acquired by Monotype). The fonts were delivered to Google as compiled binaries. The googlefonts/cousine repo was created later (2020) as a development workspace for a future variable font version.

The font version string says "Version 1.21" but the PR #769 title says "v1.211" -- this appears to be a minor discrepancy in the commit message (the actual name table says 1.21).

### Config.yaml Assessment

Neither the googlefonts/cousine repo nor the librefonts mirror has a config.yaml file. The googlefonts/cousine repo has .glyphs sources that could potentially be built with gftools-builder, but:
1. The current binaries were not built from these sources
2. There are four separate .glyphs files (one per style), not a single source
3. No build configuration exists

## Conclusion

The repository URL should be set to `https://github.com/googlefonts/cousine` as this is the official Google Fonts development repository. However, the current binaries predate this repo and were produced by Monotype. A specific onboarding commit hash cannot be determined for the v1.21 binaries. No config.yaml is available.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/cousine"
}
```

**Note**: No commit hash or config_yaml can be specified because:
- The current v1.21 binaries were produced by Monotype before the GitHub repo existed
- The googlefonts/cousine repo contains newer development work (variable font) that has not been published to google/fonts yet
- No config.yaml exists in the repo

### Status: missing_config
### Confidence: MEDIUM

The repository URL is correct (official googlefonts org), but the relationship between the repo contents and the currently-serving binaries is indirect -- the repo represents future development, not the source of the current fonts.
