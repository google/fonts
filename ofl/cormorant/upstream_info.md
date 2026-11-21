# Cormorant - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Cormorant |
| **Designer** | Christian Thalmann |
| **Repository URL** | https://github.com/CatharsisFonts/Cormorant |
| **Commit** | `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` |
| **Branch** | master |
| **Config YAML** | `sources/build.yaml` |
| **Date Added** | 2017-01-18 |
| **License** | OFL |
| **Status** | Complete |

## How URL Found

The repository URL `https://github.com/CatharsisFonts/Cormorant` is documented in METADATA.pb and confirmed through multiple sources:

1. Copyright strings in font files: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
2. PR #4694 body: "Cormorant Version 4.000 taken from the upstream repo https://github.com/CatharsisFonts/Cormorant"
3. google/fonts commit a4f9e6c0d message references this URL

This is a shared upstream repo used by all Cormorant variants (Cormorant, Cormorant Garamond, Cormorant Infant, Cormorant SC, Cormorant Unicase, Cormorant Upright).

## How Commit Determined

The commit `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` is explicitly referenced in:

1. **METADATA.pb source block**: `commit: "cc1bfb51ce6568cb3abf9199ab718d543f6fa189"`
2. **google/fonts commit a4f9e6c0d** (PR #4694): "Cormorant Version 4.000 taken from the upstream repo https://github.com/CatharsisFonts/Cormorant at commit https://github.com/CatharsisFonts/Cormorant/commit/cc1bfb51ce6568cb3abf9199ab718d543f6fa189"
3. **PR #4694 body**: Same explicit reference

This commit is "Merge pull request #67 from m4rc1e/gf-mastering" in the upstream repo, authored by Marc Foley. It is NOT the latest commit; the repo HEAD is `6d210fd3` (used for later Cormorant Garamond and Cormorant Infant v4.001 updates).

The Cormorant (base) family was added at v4.000 from cc1bfb5 and has not been updated to the newer commit. The newer commit (6d210fd) added separate per-family config files and variable font builds for Garamond and Infant.

## Config YAML Status

At commit `cc1bfb51`, the file `sources/build.yaml` exists and contains a valid gftools-builder config:
```yaml
sources:
  - Cormorant.glyphs
  - Cormorant-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Cormorant
buildStatic: False
buildWebfont: False
stat:
  ...
```

Note: At the newer HEAD commit (`6d210fd`), the config was renamed to `sources/config-cormorant.yaml` with additional changes. The `build.yaml` reference in METADATA.pb is correct for the cc1bfb5 commit.

No override config.yaml exists in the google/fonts family directory.

## Verification

- **Upstream repo cached**: Yes, at `upstream_repos/fontc_crater_cache/CatharsisFonts/Cormorant/`
- **Commit exists**: Yes, verified with `git log`
- **Config file exists at commit**: Yes, `sources/build.yaml` is present at cc1bfb5
- **Font files match**: METADATA.pb maps variable fonts `Cormorant[wght].ttf` and `Cormorant-Italic[wght].ttf` from `fonts/variable/`
- **Repository accessible**: Yes

## Confidence Level

**HIGH** - All data is explicitly documented in commit messages, PR body, and METADATA.pb. The commit hash is confirmed through multiple independent sources.

## Open Questions

None. This family is fully documented. Note that the base Cormorant is still at commit cc1bfb5 (v4.000) while Cormorant Garamond and Cormorant Infant have been updated to 6d210fd (v4.001).
