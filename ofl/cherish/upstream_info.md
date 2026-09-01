# Cherish - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Cherish |
| **Designer** | Robert Leuschke |
| **License** | OFL |
| **Category** | HANDWRITING |
| **Date Added** | 2021-08-13 |
| **Repository URL** | https://github.com/googlefonts/cherish |
| **Commit Hash** | fd3a5b6b7fa7865540892380eb94290c2d49227b |
| **Branch** | master |
| **Config YAML** | sources/config.yml |
| **Status** | complete |

## How URL Found

The repository URL `https://github.com/googlefonts/cherish` is documented in the METADATA.pb source block and was confirmed via the onboarding PR.

PR #3735 ("Cherish: Version 1.005 added") by Viviana Monsalve explicitly states:
> Cherish Version 1.005 taken from the upstream repo https://github.com/googlefonts/cherish at commit https://github.com/googlefonts/cherish/commit/fd3a5b6b7fa7865540892380eb94290c2d49227b.

The copyright notice in the font also references this repository: "Copyright 2004-2021 The Cherish Project Authors (https://github.com/googlefonts/cherish)"

## How Commit Determined

The commit hash `fd3a5b6b7fa7865540892380eb94290c2d49227b` is explicitly stated in:
1. The METADATA.pb source block
2. PR #3735 body text
3. The onboarding commit message (`384d51f85`)

This commit ("Description file fix") is also the HEAD of the master branch in the upstream repo, meaning no additional work was done after onboarding. The upstream repository has only this single commit.

## Config YAML Status

**Complete.** The upstream repository contains `sources/config.yml` at the recorded commit:

```yaml
sources:
  - Cherish.glyphs
familyName: "Cherish"
buildVariable: false
autohintTTF: false
```

The source file `sources/Cherish.glyphs` exists at the recorded commit, confirmed via `git ls-tree`. The config_yaml field in METADATA.pb correctly points to `sources/config.yml`.

## Verification

- **Repository URL**: Verified - cloned at `upstream_repos/fontc_crater_cache/googlefonts/cherish/`, remote matches
- **Commit hash**: Verified - exists in repo, matches HEAD, confirmed by PR #3735 and onboarding commit message
- **Config YAML**: Verified - `sources/config.yml` exists at the recorded commit with valid gftools-builder configuration
- **Source files**: Verified - `sources/Cherish.glyphs` exists at the recorded commit
- **METADATA.pb source block**: Complete with repository_url, commit, branch, config_yaml, and file mappings

## Confidence Level

**HIGH** across all fields. The repository URL, commit hash, and config_yaml are all explicitly documented in the PR, commit message, and METADATA.pb. The upstream repo confirms all data.

## Open Questions

- None. This family is fully documented and verified.
