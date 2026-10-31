# Investigation: Charm

## Source Data

| Field | Value |
|---|---|
| Family Name | Charm |
| Designer | Cadson Demak |
| License | OFL |
| Date Added | 2018-08-23 |
| Repository URL | https://github.com/cadsondemak/Charm |
| Commit | `873c5516023ae978e5a9de9e67b654d9ed92fc30` |
| Branch | (not specified) |
| Config YAML | Override in google/fonts |
| Status | complete |

## How URL Found

The repository URL `https://github.com/cadsondemak/Charm` was already present in the METADATA.pb `source` block. It is also referenced in the copyright strings of the font files and in the onboarding commit message and PR #1720: "Taken from the upstream repo, https://github.com/cadsondemak/Charm".

## How Commit Determined

The commit `873c5516023ae978e5a9de9e67b654d9ed92fc30` is recorded in METADATA.pb. This commit is the HEAD of the upstream repository (confirmed: `git rev-parse HEAD` matches).

Timeline analysis:
- **2018-10-11**: Marc Foley (m4rc1e) created commit `e56cb5b72` in google/fonts: "charm: v1.001 added. Taken from the upstream repo"
- **2018-10-10 to 2018-10-17**: Several commits were made in the upstream repo by Cadson Demak and m4rc1e (expanding characters, restoring vertical metrics, renaming glyphs)
- **2018-12-05**: PR #1720 was merged, and commit `873c551` (Merge PR #11 from m4rc1e/scale) was created in the upstream repo on the same day

The commit `873c551` represents the final state of the upstream repo after all fixes by Marc Foley for the Google Fonts onboarding were complete. This is the HEAD of master and no further commits have been made since December 2018. The recorded commit is the correct onboarding reference.

The sources info commit (`931eaee0c`) added by the project confirms: "sources info for Charm: v1.001 (PR #1720)".

## Config YAML Status

An override `config.yaml` exists in the google/fonts family directory at `ofl/charm/config.yaml`. It specifies:
- `buildVariable: false`
- Source: `source/Charm.glyphs`

The upstream repo contains a `source/Charm.glyphs` file, confirming the override config is valid.

## Verification

- **Repository URL**: Verified -- the upstream repo is cached at `upstream_repos/fontc_crater_cache/cadsondemak/Charm`.
- **Commit**: Verified as HEAD of master in the upstream repo. The commit is the final merge of m4rc1e's fixes for Google Fonts onboarding.
- **Source files**: Upstream contains `source/Charm.glyphs` as referenced in the override config.
- **Override config**: Confirmed present and valid.

## Confidence Level

**High** -- All data is well-documented through the PR, commit messages, and upstream history. The commit hash is the HEAD of the upstream repo, representing the final onboarding state.

## Open Questions

None. This family is fully documented and verified.
