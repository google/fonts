# Investigation Report: Cambay

## Source Data

| Field | Value |
|---|---|
| Family Name | Cambay |
| Designer | Pooja Saxena |
| License | OFL |
| Repository URL | https://github.com/anexasajoop/cambay |
| Commit Hash | `538b69cc50d692cb0864372cab691a9da757c498` |
| Branch | (not set) |
| Config YAML | (none) |
| **Status** | complete |

## How URL Found

The repository URL `https://github.com/anexasajoop/cambay` was added to METADATA.pb in commit `c8f729cbd` ("Add more upstreams (c,d)"). The username `anexasajoop` is Pooja Saxena's GitHub handle (reverse of "poojasaxena"). The copyright notice lists `www.poojasaxena.in` rather than a GitHub URL.

## How Commit Determined

The commit `538b69cc50d692cb0864372cab691a9da757c498` was added as part of a batch update in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). This commit is from 2014-11-24 and only changes README.md text. However, it was the HEAD of the upstream repo at the time the font was last updated in google/fonts.

Timeline analysis:
- **2014-11-24**: Upstream commit `538b69c` ("Updated text.") - HEAD at the time of google/fonts onboarding
- **2015-01-28**: Font added to Google Fonts catalog (`date_added`)
- **2017-05-08**: PR #873 ("hotfix-cambay: v1.096 added") by m4rc1e - last TTF update in google/fonts
- **2019-01-30**: Upstream commits `b21dd14` and `a8d3e6a` added new glyphs (post-onboarding)

The commit `538b69c` represents the state of the upstream repo at the approximate time of onboarding. The font files in google/fonts don't match any specific upstream font file (google/fonts has `Cambay-*.ttf` while upstream has `CambayDevanagari-*.AH.ttf`), suggesting the fonts were rebuilt or renamed during the onboarding process. The 2017 hotfix by m4rc1e also did not reference any upstream commit.

## Config YAML Status

**No config.yaml exists** in the upstream repository. No override config.yaml exists in the google/fonts family directory.

The upstream repo contains source files (Glyphs and UFO formats) organized per-style:
- `Sources/Cambay Regular/Cambay Devanagari-Regular.glyphs` (+ .ufo)
- `Sources/Cambay Bold/Cambay Devanagari-Bold.glyphs` (+ .ufo)
- `Sources/Cambay Oblique/Cambay Devanagari-Oblique.glyphs` (+ .ufo)
- `Sources/Cambay Bold Oblique/Cambay Devanagari-BoldOblique.glyphs` (+ .ufo)

This is a static font with 4 styles. The sources are organized in separate directories per style, and the Glyphs files are per-style rather than a single multi-master file, which makes creating a config.yaml non-trivial.

## Verification

- **Commit exists in upstream repo**: Yes, verified
- **Config YAML exists at commit**: No
- **Override config.yaml in google/fonts**: No
- **Repository URL accessible**: Yes (https://github.com/anexasajoop/cambay)
- **Font file names differ**: google/fonts has `Cambay-*.ttf`, upstream has `CambayDevanagari-*.AH.ttf`
- **Upstream has newer changes**: 2019 commits added new glyphs not reflected in google/fonts

## Confidence Level

**Medium** for commit hash. The commit `538b69c` was the HEAD of upstream at the time of onboarding, but it only changed README.md. There was no explicit reference to this commit in any google/fonts commit or PR. The 2017 hotfix (PR #873) by m4rc1e did not include any upstream commit reference. The commit is a reasonable proxy for "state of upstream at time of onboarding" but was not verified by binary comparison.

**High** for repository URL. The URL is correct and matches the designer's GitHub profile.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - "Sources/Cambay Regular/Cambay Devanagari-Regular.ufo"
  - "Sources/Cambay Oblique/Cambay Devanagari-Oblique.ufo"
  - "Sources/Cambay Bold/Cambay Devanagari-Bold.ufo"
  - "Sources/Cambay Bold Oblique/Cambay Devanagari-Bold Oblique.ufo"
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. The upstream repo has newer commits (2019) that added new Devanagari glyphs. Should these be reviewed for a potential update to the Google Fonts version?
2. A config.yaml would need to be created to enable gftools-builder builds. Given the per-style source organization (separate .glyphs files), this may require restructuring or a multi-source config.
3. The font names differ between upstream (`CambayDevanagari-*`) and google/fonts (`Cambay-*`). It's unclear if the fonts were renamed during onboarding or if there were separate build artifacts.
