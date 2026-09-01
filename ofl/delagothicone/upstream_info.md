# Dela Gothic One - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Dela Gothic One |
| Designer | artakana |
| License | OFL |
| Repository URL | https://github.com/syakuzen/DelaGothic |
| Commit Hash | da8b03e57a8977132b3d0358c48c8463374c74ab |
| Branch | master |
| Config YAML | Override in google/fonts (Sources/DelaGothic.glyphs) |
| Status | complete |
| Date Added | 2020-12-14 |

## How URL Found

The repository URL `https://github.com/syakuzen/DelaGothic` is documented in the METADATA.pb source block and is referenced in the original onboarding PR #2877. The copyright string in the font also references this URL.

## How Commit Determined

### Initial Onboarding (v1.003)
- PR #2877 by aaronbell: "Dela Gothic One Version 1.003; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/syakuzen/DelaGothic.git at commit https://github.com/syakuzen/DelaGothic/commit/c00d3aa11584648f76ce32e3f8d3993933903941"
- Merged 2021-02-24

### Font Update (v1.005)
- PR #3618 by aaronbell: Manual update with designer name correction, OFL update, autohinting removal, and version bump
- Merged 2021-08-26
- No specific upstream commit referenced in the PR
- The latest upstream commit `da8b03e` ("Updated ttf", 2021-03-29) is the last commit that modified the font file in the upstream repo
- This commit predates the PR merge, and the METADATA.pb source block references files directly from the upstream repo (`fonts/ttf/DelaGothicOne-Regular.ttf`)

The commit `da8b03e57a8977132b3d0358c48c8463374c74ab` is the latest commit in the upstream repo (also the HEAD of master). It represents the latest state of the font sources used for the v1.005 update. Note that the font in google/fonts (2,508,848 bytes) is significantly smaller than the upstream TTF (5,469,244 bytes) because autohinting was removed as described in PR #3618.

## Config YAML Status

- No `config.yaml` exists in the upstream repository
- An override `config.yaml` exists in google/fonts at `ofl/delagothicone/config.yaml`:
  ```yaml
  sources:
    - Sources/DelaGothic.glyphs
  ```
- The upstream repo contains `Sources/DelaGothic.glyphs` as the source file
- Since an override config exists in google/fonts, the `config_yaml` field can be omitted from METADATA.pb

## Verification

- Repository URL is valid and accessible
- Upstream repo cloned at `upstream_repos/fontc_crater_cache/syakuzen/DelaGothic/`
- Commit `da8b03e` verified as HEAD of master branch
- Source file `Sources/DelaGothic.glyphs` exists in the upstream repo
- Override config.yaml in google/fonts correctly references the source file
- METADATA.pb source block has no commit hash (should be added)

## Confidence Level

**High** - The repository URL is well-documented in PR history and copyright strings. The commit hash `da8b03e` is the latest commit and is the right reference for the v1.005 update, as it's the last commit that modified the font files before the PR was created.

## Open Questions

- The METADATA.pb source block currently has no `commit` field. This should be added with value `da8b03e57a8977132b3d0358c48c8463374c74ab`.
- The font was built by Aaron Bell with custom processing (autohinting removal), so the TTF in google/fonts doesn't directly match the upstream TTF.
