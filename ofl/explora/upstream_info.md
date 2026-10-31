# Explora

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/explora/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/explora |
| Commit | `b0d0e026f48eefee38dc06821f2c9088a347fa9b` |
| Config YAML | `sources/config.yml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/explora`. This matches the copyright string in the font file ("Copyright 2011 The Explora Project Authors (https://github.com/googlefonts/explora)") and the link in the DESCRIPTION.en_us.html file. The onboarding PR #3686 also explicitly references this repository.

## How the Commit Hash Was Identified

The METADATA.pb records commit `b0d0e026f48eefee38dc06821f2c9088a347fa9b` (2022-03-31, "sample image updated"), which is the HEAD of the `master` branch. However, the original onboarding commit referenced in PR #3686 is `b4dd93de15b0451de234df3aa3de61e20ba6116d` (2021-08-10, "version bumped to 1.010").

The PR #3686 body explicitly states: "Explora Version 1.010 taken from the upstream repo https://github.com/googlefonts/explora at commit https://github.com/googlefonts/explora/commit/b4dd93de15b0451de234df3aa3de61e20ba6116d."

PR #3686 was authored by Viviana Monsalve (vv-monsalve) and merged on 2021-08-13. The font was deployed via commit `76adaf1d2` on 2021-11-01.

### Commit comparison

The difference between the onboarding commit `b4dd93de` and the METADATA.pb commit `b0d0e02` is only documentation:
- `Documentation/image1.png` (image size change)
- `Documentation/image1.py` (new file)

The font binary (`fonts/ttf/Explora-Regular.ttf`), the source file (`sources/ExploraPro.glyphs`), the config file (`sources/config.yml`), and the OFL.txt are all **identical** between both commits. The git blob hash for the TTF file is `b2498f6e463c8bf97c1b5d37a9cddb8dfd26bc29` at both commits, and it matches the blob in google/fonts.

The METADATA.pb source block was added by the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported information from fontc_crater's target.json. That process used the latest commit `b0d0e02` rather than the original onboarding commit `b4dd93de`.

## How Config YAML Was Resolved

The config file `sources/config.yml` exists in the upstream repository at both the onboarding commit and the current HEAD. Its content is:

```yaml
sources:
  - ExploraPro.glyphs
familyName: "Explora"
buildVariable: false
autohintTTF: false
```

Note the file extension is `.yml` (not `.yaml`), and METADATA.pb correctly references `sources/config.yml`. No override config.yaml exists in the google/fonts family directory (`ofl/explora/`).

## Verification

- Repository URL valid: Yes
- Commit `b0d0e02` exists in upstream repo: Yes
- Original onboarding commit `b4dd93de` exists in upstream repo: Yes
- Commit `b0d0e02` date: 2022-03-31 17:52:28 -0500
- Commit `b0d0e02` message: "sample image updated"
- Font binary blob match (google/fonts vs upstream at `b4dd93de`): Yes (blob `b2498f6e`)
- Font binary blob match (google/fonts vs upstream at `b0d0e02`): Yes (blob `b2498f6e`)
- OFL.txt MD5 match: Yes (`3b7c6139e0a04e27347256bd649c27ff`)
- Source files at commit: `sources/ExploraPro.glyphs`, `sources/config.yml`
- Config YAML valid: Yes

## Confidence

**HIGH**: The repository URL is confirmed by multiple sources (METADATA.pb, copyright string, DESCRIPTION.en_us.html, PR #3686). The config.yml is present and valid at the referenced commit. The font binary and source files are identical between the onboarding commit (`b4dd93de`) and the METADATA.pb commit (`b0d0e02`) -- the only difference is an unrelated documentation image update. While the METADATA.pb commit `b0d0e02` is technically not the original onboarding commit, it is functionally equivalent for build purposes since no source or font files changed.

## Notes

- The original onboarding commit is `b4dd93de15b0451de234df3aa3de61e20ba6116d` (2021-08-10, "version bumped to 1.010"), as documented in PR #3686. The METADATA.pb instead records the later commit `b0d0e026f48eefee38dc06821f2c9088a347fa9b` (2022-03-31, "sample image updated"). Since the source and font files are unchanged, either commit is valid for reproducible builds.
- The upstream repo was initially a shallow clone in the cache; it was unshallowed during this investigation to access the full history (23 commits total).
- Designer is Robert Leuschke. Onboarder was Viviana Monsalve (vv-monsalve).
- The font supports Latin, Latin Extended, Vietnamese, and Cherokee character sets.
