# Investigation Report: Encode Sans Condensed

## Family Details
- **Family name**: Encode Sans Condensed
- **Designer**: Impallari Type, Andres Torresi, Jacques Le Bailly
- **License**: OFL
- **Category**: SANS_SERIF
- **Date added**: 2017-02-08
- **Google Fonts path**: `ofl/encodesanscondensed/`

## Upstream Repository
- **URL**: https://github.com/impallari/Encode-Sans
- **Status**: Accessible (HTTP 200)
- **Repository owner**: Pablo Impallari (impallari)

### Repository Relationship

The Encode Sans project has two upstream repositories:

1. **impallari/Encode-Sans** -- the original repository by Pablo Impallari, containing the v2.000 static fonts for all width variants (Condensed, Semi Condensed, Semi Expanded, Expanded, and the normal width). Uses a single `Encode-Sans.glyphs` source file with width masters/instances to generate all 45 static font files (9 weights x 5 widths).

2. **thundernixon/Encode-Sans** -- Stephen Nixon's fork that upgraded the family to a variable font (v3.x). This fork is used for the `encodesans` (main variable font) and `encodesanssc` (Small Caps variable font) families, which were updated to v3.002 in 2020.

**The Condensed, Semi Condensed, Semi Expanded, and Expanded width variants were NOT updated to v3.** They still use the v2.000 static fonts from the impallari/Encode-Sans repository. The thundernixon variable font subsumes these width variants via the `wdth` axis (75-125), but the separate static families remain in google/fonts as originally onboarded.

## Source Files
- **Source format**: Glyphs (.glyphs)
- **Source path**: `sources/Encode-Sans.glyphs`
- **Source description**: Single multi-master Glyphs source containing all weight (Thin through Black) and width (Condensed through Expanded) masters and instances

## Onboarding History

### Initial Addition (v1)
- **Commit**: `90abd17b4f97671435798b6147b698aa9087612f` (2015-03-07)
- **Description**: Initial commit adding all font families to google/fonts

### v2.000 Update (Current Version)
- **Google Fonts commit**: `2789b442616ea2950d014fb9b4b8e23f67b7fed4` (2017-02-07)
- **PR**: [google/fonts#626](https://github.com/google/fonts/pull/626) - "encodesanscondensed: v2.000 added"
- **Author**: Marc Foley (m4rc1e)
- **PR body**: Empty (no details)

### Source Block Addition
- **Commit**: `c8a4f8556468a3935eed9c984b30e2d138ad8b79` (2024-01-14)
- **Description**: "More upstreams (e,f)" by Simon Cozens
- **Added**: `source { repository_url: "https://github.com/impallari/Encode-Sans" }`

## Commit Hash Determination

**Identified commit**: `370cdccdb22daf862c6fca0636aad64b6835decd` (2017-02-03)

### Evidence

This is the latest (and HEAD) commit on the `master` branch of impallari/Encode-Sans. It is a merge commit for PR #3 by Marc Foley: "fonts | sources: Changed thin weight from 100 to 250."

**File size comparison** between impallari repo at commit `370cdcc` and google/fonts:

| File | impallari@370cdcc | google/fonts | Match |
|------|------------------|--------------|-------|
| EncodeSansCondensed-Black.ttf | 166,812 | 166,812 | YES |
| EncodeSansCondensed-Bold.ttf | 167,844 | 167,844 | YES |
| EncodeSansCondensed-ExtraBold.ttf | 169,456 | 169,456 | YES |
| EncodeSansCondensed-ExtraLight.ttf | 166,844 | 166,844 | YES |
| EncodeSansCondensed-Light.ttf | 168,208 | 168,208 | YES |
| EncodeSansCondensed-Medium.ttf | 169,464 | 169,464 | YES |
| EncodeSansCondensed-Regular.ttf | 168,396 | 168,396 | YES |
| EncodeSansCondensed-SemiBold.ttf | 170,560 | 170,560 | YES |
| EncodeSansCondensed-Thin.ttf | 161,668 | 161,668 | YES |

All 9 files match in size at commit `370cdcc`. At the previous commit (`2fdfa4a`), three files had different sizes (Black, SemiBold, Thin), confirming that `370cdcc` is the correct commit. SHA256 hashes differ between repos, which is expected due to post-processing (likely hinting or name table modifications) applied by Marc Foley during onboarding.

**Timeline**: The impallari commit `370cdcc` was made on 2017-02-03, and the google/fonts PR #626 was merged on 2017-02-07, only 4 days later. Marc Foley authored both the upstream commit (via PR #3 to impallari/Encode-Sans) and the google/fonts onboarding PR #626.

## Config.yaml Assessment

- **Upstream config.yaml**: None (impallari/Encode-Sans has no config.yaml)
- **Google Fonts override**: None (no config.yaml in `ofl/encodesanscondensed/`)
- **Buildable**: Yes -- the `.glyphs` source file is compatible with gftools-builder. An override config.yaml can be created to reference the source.

### Note on Override Config

An override config.yaml for this family would need to specify the Condensed width instances to extract from the single `Encode-Sans.glyphs` source. However, since the source produces ALL width variants from one file, a config for just the Condensed variant may require careful instance filtering. This is a shared source situation with `encodesansexpanded`, `encodesanssemicondensed`, and `encodesanssemiexpanded`.

## Current METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/impallari/Encode-Sans"
}
```

## Proposed METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/impallari/Encode-Sans"
  commit: "370cdccdb22daf862c6fca0636aad64b6835decd"
}
```

## Status

- **Repository URL**: Correct (impallari/Encode-Sans)
- **Commit hash**: `370cdcc` -- needs to be added to METADATA.pb
- **Config**: Missing (needs override config.yaml, but complex due to shared multi-width source)
- **Overall**: `missing_config`
- **Confidence**: HIGH

## Related Families

All width variants share the same upstream repo (impallari/Encode-Sans) and commit:
- **Encode Sans Condensed** (this report) -- `ofl/encodesanscondensed/`
- **Encode Sans Expanded** -- `ofl/encodesansexpanded/`
- **Encode Sans Semi Condensed** -- `ofl/encodesanssemicondensed/`
- **Encode Sans Semi Expanded** -- `ofl/encodesanssemiexpanded/`

The main **Encode Sans** and **Encode Sans SC** families use a different upstream (thundernixon/Encode-Sans) at commit `6407de8` (v3.002 variable font).
