# Comforter - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Comforter |
| Designer | Robert Leuschke |
| Repository URL | https://github.com/googlefonts/comforter |
| Commit | `3112f6b6990f10c7a101e5577b8267988989cff7` |
| Branch | master |
| Config YAML | `sources/config.yml` |
| Override Config | No |
| Date Added | 2021-09-29 |
| License | OFL |

## How URL Found

The repository URL `https://github.com/googlefonts/comforter` is documented in the METADATA.pb source block. It was originally set via the `upstream.yaml` file during onboarding and later merged into METADATA.pb by Simon Cozens (commit `66f91f10f`, April 2024). The URL is also referenced in the copyright string of the font files.

## How Commit Determined

The commit hash `3112f6b6990f10c7a101e5577b8267988989cff7` is explicitly mentioned in the google/fonts onboarding commit message:

> "Comforter Version 1.013; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/comforter at commit https://github.com/googlefonts/comforter/commit/3112f6b6990f10c7a101e5577b8267988989cff7."

This was PR #3845, merged on 2021-09-30 by Viviana Monsalve (@vv-monsalve).

The upstream repository has only a single commit, and this commit is both the HEAD and the only commit in the repo. This makes verification straightforward.

## Config YAML Status

The upstream repository has `sources/config.yml` (note: `.yml` extension, not `.yaml`). This matches the `config_yaml` field in METADATA.pb. The config file contains:

```yaml
sources:
  - ComforterPro.glyphs
familyName: "Comforter"
buildVariable: false
```

## Verification

- **Commit exists in upstream**: Yes - it is the only commit and HEAD of master branch
- **Branch matches**: Yes - `master` branch, matches METADATA.pb
- **Config YAML exists at commit**: Yes - `sources/config.yml` exists
- **Font files match**: The onboarding commit in google/fonts added `Comforter-Regular.ttf` from `fonts/ttf/` in upstream
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/googlefonts/comforter/`

## Confidence Level

**HIGH** - All data is fully verified. The onboarding commit message explicitly states the upstream URL and commit hash. The repo has only one commit, eliminating any ambiguity.

## Open Questions

None. All source data is complete and verified.
