# Investigation Report: Flamenco

## Family Details

- **Family name**: Flamenco
- **Designer**: LatinoType (Luciano Vergara)
- **Category**: Display
- **Date added to Google Fonts**: 2011-12-19
- **License**: OFL
- **Weights**: Light (300), Regular (400)
- **Current version in Google Fonts**: 1.003
- **Google Fonts path**: ofl/flamenco

## Upstream Repository

- **URL**: https://github.com/librefonts/flamenco
- **Status**: Active (not archived), publicly accessible
- **Default branch**: master
- **Total commits**: 1 (single commit: `908f93e`)
- **Last push**: 2014-10-17

## Source Files Analysis

The upstream repository contains only legacy source formats:

- `src/Flamenco-Light-TTF.sfd` (FontForge SFD)
- `src/Flamenco-Regular-TTF.sfd` (FontForge SFD)
- `src/Flamenco-Light-OTF.vfb` (FontLab VFB)
- `src/Flamenco-Regular-OTF.vfb` (FontLab VFB)

No `.glyphs`, `.glyphx`, `.ufo`, or `.designspace` files exist. No `config.yaml` is present. These sources are **not compatible with gftools-builder**.

The repo also contains TTX dumps of the font tables (in both the root directory and `src/`) and a `.travis.yml` for legacy fontbakery CI.

## Version History

| Version | Location | Notes |
|---------|----------|-------|
| 1.002 | Upstream repo (SFD/VFB sources, TTX dumps) | Only version in the repo |
| 1.003 | google/fonts (current binaries) | Updated via PR #887 (May 2017) |

## Commit Hash Verification

The upstream repo has only a single commit:

- **Commit**: `908f93e92b13062e172153d04b96a9301ca1c7c5`
- **Date**: 2014-10-17
- **Author**: hash3g (hash.3g@gmail.com)
- **Message**: "update .travis.yml"

This is an initial import commit that added all files at once (72 files). Since there is only one commit in the entire repo, this is trivially the correct reference point.

## Google Fonts History

1. **Initial commit** (`90abd17b4`, 2015-03-07): Font first added to google/fonts repo.
2. **PR #887** (`f1fe299e0`, 2017-05-08): Marc Foley updated fonts to v1.003 ("hotfix-flamenco: v1.003 added"). This updated both .ttf files and adjusted METADATA.pb. The PR body was empty -- no link to upstream sources or details about what was fixed.
3. **Copyright fixup** (`ac5149724`, 2017-05-08): Dave Crossland fixed a double-space in copyright strings in METADATA.pb.
4. Various METADATA.pb-only changes (language support, formatting, etc.)

The v1.003 binaries in google/fonts do **not** correspond to any commit in the upstream repo, which only contains v1.002 sources. The v1.003 update was done by Marc Foley directly without updating the upstream repo.

## METADATA.pb Source Block

Current METADATA.pb on upstream/main has **no source block**.

A source block was added on the local branch `sources_info_2026-02-25`:

```
source {
  repository_url: "https://github.com/librefonts/flamenco"
  commit: "908f93e92b13062e172153d04b96a9301ca1c7c5"
}
```

## Config.yaml Assessment

**No config.yaml can be created.** The upstream repo has only SFD (FontForge) and VFB (FontLab) sources. These formats are not supported by gftools-builder, so no override config.yaml is applicable.

## Findings

- The upstream repo `librefonts/flamenco` is the correct source repository for this font family.
- The repo has a single commit (`908f93e`) which is the only possible reference point.
- The current fonts in google/fonts (v1.003) were updated beyond what the upstream repo contains (v1.002). The v1.003 hotfix by Marc Foley was done without updating the upstream repo.
- Sources are SFD/VFB only -- not gftools-builder compatible. No config.yaml is needed or possible.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/flamenco"
  commit: "908f93e92b13062e172153d04b96a9301ca1c7c5"
}
```

## Status

- **Status**: no_config (SFD-only sources)
- **Confidence**: HIGH
- The repository URL and commit hash are verified. The single-commit repo makes hash verification trivial.
- No config.yaml is applicable due to SFD/VFB-only sources.
