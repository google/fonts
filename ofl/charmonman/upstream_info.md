# Investigation: Charmonman

## Source Data

| Field | Value |
|---|---|
| Family Name | Charmonman |
| Designer | Cadson Demak |
| License | OFL |
| Date Added | 2018-08-22 |
| Repository URL | https://github.com/cadsondemak/Charmonman |
| Commit | `8590fc4aaefe8ccf9ec0abeff7f66b6bc1a83503` |
| Branch | (not specified) |
| Config YAML | Override in google/fonts |
| Status | complete |

## How URL Found

The repository URL `https://github.com/cadsondemak/Charmonman` was already present in the METADATA.pb `source` block. It is also referenced in the copyright strings of the font files and in the original onboarding commit message: "Taken from the upstream repo https://github.com/cadsondemak/Charmonman at commit https://github.com/cadsondemak/Charmonman/commit/8590fc4aaefe8ccf9ec0abeff7f66b6bc1a83503".

## How Commit Determined

The commit `8590fc4aaefe8ccf9ec0abeff7f66b6bc1a83503` is explicitly referenced in the original onboarding commit message (`fc91fcc12`): "charmonman: v1.000 added. Taken from the upstream repo https://github.com/cadsondemak/Charmonman at commit https://github.com/cadsondemak/Charmonman/commit/8590fc4aaefe8ccf9ec0abeff7f66b6bc1a83503".

This commit is also the HEAD of the upstream repository (confirmed: `git rev-parse HEAD` matches). The commit is dated 2018-08-22, the same day as the google/fonts onboarding, and represents "Merge pull request #4 from m4rc1e/gf-mastering" -- Marc Foley's work to prepare the font for Google Fonts.

The commit hash was later added to the METADATA.pb source block by commit `4fd9e2392` ("Add source metadata to 125 METADATA.pb files").

## Config YAML Status

An override `config.yaml` exists in the google/fonts family directory at `ofl/charmonman/config.yaml`. It specifies:
- Source: `source/Charmonman.glyphs`

The upstream repo contains a `source/Charmonman.glyphs` file, confirming the override config is valid.

## Verification

- **Repository URL**: Verified -- the upstream repo is cached at `upstream_repos/fontc_crater_cache/cadsondemak/Charmonman`.
- **Commit**: Verified as HEAD of master in the upstream repo. Explicitly referenced in the original onboarding commit message. The commit date (2018-08-22) matches the google/fonts onboarding date.
- **Source files**: Upstream contains `source/Charmonman.glyphs` as referenced in the override config.
- **Override config**: Confirmed present and valid.

## Confidence Level

**Very High** -- The commit hash is explicitly stated in the original onboarding commit message, confirmed as HEAD of upstream, and the dates align perfectly. This is one of the most well-documented onboarding references.

## Open Questions

None. This family is fully documented and verified.
