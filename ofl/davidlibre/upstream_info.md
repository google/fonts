# David Libre - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | David Libre |
| Designer | Monotype Imaging Inc., SIL International, Meir Sadan |
| Repository URL | https://github.com/meirsadan/david-libre |
| Commit Hash | `15496c1be77e35f3fa3d0df14a2c2c6f9adfd297` |
| Branch | master |
| Config YAML | `sources/config.yaml` (in upstream) |
| Status | complete |
| Date Added | 2021-07-23 |

## How URL Found

The repository URL `https://github.com/meirsadan/david-libre` is documented in the copyright field of the font files and in the METADATA.pb. It was present from the original onboarding PR #3595 (authored by Rosalie Wagner) and confirmed by the gftools-packager update commit `0841b9aa8`.

## How Commit Determined

The gftools-packager commit `0841b9aa8` (Marc Foley, Feb 21 2024) explicitly states: "David Libre Version 1.100; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/meirsadan/david-libre at commit https://github.com/meirsadan/david-libre/commit/15496c1be77e35f3fa3d0df14a2c2c6f9adfd297."

This commit (`15496c1`) is the HEAD of the upstream repository (a merge of PR #25 from emmamarichal/master titled "Small fixes"). The font was rebuilt from source by the packager using this commit.

### Onboarding History

1. **PR #3595 (Jul 2021)** - Rosalie Wagner added David Libre from the Google Fonts API ZIP file (not from a specific upstream commit)
2. **Commit 0841b9aa8 (Feb 2024)** - Marc Foley rebuilt the font from upstream using gftools-packager at commit `15496c1`

The current font binaries in google/fonts are from the Feb 2024 packager rebuild.

## Config YAML Status

- **config.yaml exists in upstream**: `sources/config.yaml` with content:
  ```yaml
  sources:
    - DavidLibre.glyphs
  familyName: David Libre
  buildVariable: False
  buildOTF: False
  checkCompatibility: False
  ```
- The `config_yaml` field in METADATA.pb is correctly set to `sources/config.yaml`
- No override config.yaml in google/fonts

## Verification

- Repository URL is valid and accessible: https://github.com/meirsadan/david-libre
- Commit `15496c1` exists in the upstream repo and is HEAD (master)
- The METADATA.pb `files` mapping correctly maps font files from `fonts/ttf/` to the family directory
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/meirsadan/david-libre/`
- The `sources/config.yaml` file exists in the upstream repo at commit `15496c1`

## Confidence Level

**HIGH** - The gftools-packager commit explicitly documents the upstream commit used for the most recent build. All fields are verified.

## Open Questions

None. The investigation is complete.
