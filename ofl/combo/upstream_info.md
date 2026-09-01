# Combo - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Combo |
| Designer | Eduardo Tunni |
| Repository URL | https://github.com/librefonts/combo |
| Commit Hash | ae46147e06fad7d2d664c2738ae08a9262adbeb1 |
| Branch | master (default) |
| Config YAML | None |
| Override Config | No |
| Status | missing_config |

## How URL Was Found

The repository URL was not yet in the main branch of google/fonts. It was added in a pending PR branch (`sources_info_2026-02-25`) as part of commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). The librefonts organization hosts many font families originally contributed to Google Fonts, and this is the standard location for Eduardo Tunni's fonts.

## How Commit Was Determined

The commit `ae46147e06fad7d2d664c2738ae08a9262adbeb1` (dated October 17, 2014) is the **only commit** in the entire repository. The commit message is "update .travis.yml". Despite the message, this single commit contains all the font files, source files, and metadata.

Since there is only one commit, this is unambiguously the correct reference.

## Config YAML Status

**No config.yaml exists** in the upstream repository or as an override in google/fonts.

The upstream repository contains only:
- `src/Combo-Regular-OTF.vfb` - FontLab binary source
- `src/Combo-Regular-TTF.vfb` - FontLab binary source
- Various TTX decompositions of the compiled font
- `Combo-Regular.ttf.*` - TTX decompositions at the root

There are **no gftools-buildable source files** (no `.ufo`, `.glyphs`, or `.designspace` files). The only sources are `.vfb` (FontLab 5 binary format), which can be referenced in a config.yaml but are not directly buildable by modern gftools/fontc toolchains.

The tracking data notes "No buildable source files at recorded commit" which is accurate for modern build systems. However, a config.yaml could still reference the VFB files similarly to how other families handle this (e.g., Codystar).

## Verification

- **Repository accessible**: Yes, https://github.com/librefonts/combo is accessible
- **Commit exists**: Yes, `ae46147e` is the only commit and HEAD of master
- **Source block on main**: No -- the source block is only on the pending PR branch `sources_info_2026-02-25`
- **No config.yaml**: Correct, neither upstream nor override exists

## Confidence Level

**High** for repository URL and commit hash. There is only one commit in the repo, so the commit hash is unambiguous.

**Note**: The status of "missing_config" is accurate. An override config.yaml could potentially be created referencing the VFB sources, similar to what was done for Codystar:

```yaml
buildVariable: false
sources:
  - src/Combo-Regular-TTF.vfb
```

## Open Questions

1. Should an override config.yaml be created referencing the VFB source, similar to the Codystar approach?
2. The source block with repository_url and commit hash needs to be merged to main (currently only on pending PR branch).
