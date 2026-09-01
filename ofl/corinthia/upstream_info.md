# Corinthia - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Corinthia |
| **Designer** | Robert Leuschke |
| **Repository URL** | https://github.com/googlefonts/corinthia |
| **Commit** | `9c81839655dfec773b737abc90cb09ac94b1bea1` |
| **Branch** | master |
| **Config YAML** | `sources/config.yml` |
| **Date Added** | 2021-08-26 |
| **License** | OFL |
| **Status** | Complete |

## How URL Found

The repository URL `https://github.com/googlefonts/corinthia` is documented in the METADATA.pb `source {}` block. It is also referenced in the copyright strings of the font files: "Copyright 2010 The Corinthia Project Authors (https://github.com/googlefonts/corinthia)".

The URL was confirmed through PR #3916 ("Corinthia: Version 1.013; ttfautohint (v1.8.3) added") by vv-monsalve, which explicitly states: "taken from the upstream repo https://github.com/googlefonts/corinthia".

## How Commit Determined

The commit hash `9c81839655dfec773b737abc90cb09ac94b1bea1` is explicitly documented in:

1. **METADATA.pb source block**: `commit: "9c81839655dfec773b737abc90cb09ac94b1bea1"`
2. **google/fonts commit message** (51050e9d1): "Corinthia Version 1.013; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/corinthia at commit https://github.com/googlefonts/corinthia/commit/9c81839655dfec773b737abc90cb09ac94b1bea1"
3. **PR #3916 body**: Same explicit reference to the commit

The upstream repo has only one commit total, and HEAD equals this commit:
```
9c81839 v1.013 - fina instead of calt
```

## Config YAML Status

The file `sources/config.yml` exists at the referenced commit in the upstream repo. Contents:
```yaml
sources:
  - Corinthia.glyphs
familyName: "Corinthia"
buildVariable: false
```

This is a valid gftools-builder config. No override config.yaml exists in the google/fonts family directory.

## Verification

- **Upstream repo cached**: Yes, at `upstream_repos/fontc_crater_cache/googlefonts/corinthia/`
- **Commit exists**: Yes, it is the only commit and HEAD of the repo
- **Config file exists at commit**: Yes, `sources/config.yml` is present
- **Font files match**: METADATA.pb maps `fonts/ttf/Corinthia-Regular.ttf` and `fonts/ttf/Corinthia-Bold.ttf` from upstream, both present at the commit
- **Repository accessible**: Yes

## Confidence Level

**HIGH** - All data is explicitly documented in commit messages, PR body, and METADATA.pb. The upstream repo has a single commit matching the referenced hash.

## Open Questions

None. This family is fully documented and verified.
