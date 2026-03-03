# Investigation Report: Cause

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Cause |
| **Designer** | Saurabh Sharma |
| **License** | OFL |
| **Date Added** | 2025-12-05 |
| **Repository URL** | https://github.com/xconsau/Cause |
| **Commit Hash** | `d7259fb3079c4d310c89a731c647829fba251495` |
| **Branch** | main |
| **Config YAML** | `sources/config.yaml` |
| **Status** | complete |

## How URL Was Found

The repository URL is set in the METADATA.pb source block, originally added during onboarding. The copyright string in METADATA.pb also references `https://github.com/xconsau/cause`. The cached clone at `upstream_repos/fontc_crater_cache/xconsau/Cause/` confirms the remote URL.

## How Commit Was Determined

The onboarding commit in google/fonts (`0b585e1cc`) by Emma Marichal explicitly states in its commit message:

> "Cause: Version 1.000 added - Taken from the upstream repo https://github.com/xconsau/Cause at commit https://github.com/xconsau/Cause/commit/d7259fb3079c4d310c89a731c647829fba251495."

The commit `d7259fb` ("Add files via upload") exists in the upstream repo and was verified by unshallowing the cache clone.

## Config YAML Status

**Present at `sources/config.yaml` in the upstream repo at the tracked commit.** Contents verified:

```yaml
sources:
  - Cause.designspace

axisOrder:
  - wght

familyName: Cause

autohintTTF: false
```

The `config_yaml` field is set to `sources/config.yaml` in the METADATA.pb source block.

## Verification

- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/xconsau/Cause/`
- **Commit exists**: Yes, verified after unshallowing the repo
- **Commit matches onboarding**: The google/fonts onboarding commit (`0b585e1cc`) explicitly references this exact commit hash
- **config.yaml exists at commit**: Yes, at `sources/config.yaml`
- **METADATA.pb has complete source block**: Yes, with repository_url, commit, archive_url, files mapping, branch, and config_yaml
- **One newer commit exists**: `418f170` ("Correct GitHub link case in copyright notice") - this is post-onboarding work

## Confidence Level

**HIGH** - All data is explicitly documented. The onboarding commit message directly references the upstream commit. The METADATA.pb source block is complete with all fields. This family is fully documented.

## Open Questions

None. This is a fully complete entry.
