# Bytesized - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Bytesized |
| **Designer** | Baltdev |
| **License** | OFL |
| **Date Added** | 2025-02-13 |
| **Repository URL** | https://github.com/balt-dev/bytesized-gf |
| **Commit Hash** | `11abbf2db0602d93f35ec9d493a074e384f0cdb3` |
| **Branch** | main |
| **Config YAML** | `sources/config.yaml` |
| **Status** | complete |

## How URL Was Found

The repository URL is documented in the METADATA.pb `source { }` block, which was set during onboarding. The copyright string in the font itself also references the same repository URL: "Copyright 2024 The Bytesized Project Authors (https://github.com/balt-dev/bytesized-gf)".

## How Commit Was Determined

The onboarding commit in google/fonts (`e91890c80`, "Bytesized: Version 1.000 added", by Emma Marichal, 2025-02-13) explicitly states in the commit message:

> Taken from the upstream repo https://github.com/balt-dev/bytesized-gf at commit https://github.com/balt-dev/bytesized-gf/commit/11abbf2db0602d93f35ec9d493a074e384f0cdb3.

This commit hash `11abbf2db0602d93f35ec9d493a074e384f0cdb3` is the HEAD of the upstream `main` branch. It was authored by baltdev on 2025-02-01 with the message "Alter glyphs for uniqueness and better kerning".

## Config YAML Status

**config.yaml exists** at `sources/config.yaml` in the upstream repository, and it is present at the recorded commit. The config is correctly referenced in the METADATA.pb `source { }` block as `config_yaml: "sources/config.yaml"`.

Contents of `sources/config.yaml`:
```yaml
sources:
    - Bytesized-Regular.ufo
familyName: "Bytesized Regular"
autohintTTF: false
includeSourceFixes: true
buildOTF: false
```

The source file `sources/Bytesized-Regular.ufo` exists alongside the config.

## Verification

- **Repository URL**: Confirmed valid; repo is cloned at `upstream_repos/fontc_crater_cache/balt-dev/bytesized-gf/`
- **Commit hash**: Verified -- exists in the repo and is HEAD of `main`; explicitly referenced in the google/fonts onboarding commit message
- **Config YAML**: Verified -- `sources/config.yaml` exists at the recorded commit with valid gftools-builder configuration
- **Source files**: `sources/Bytesized-Regular.ufo` (UFO format, gftools-compatible)
- **METADATA.pb source block**: Complete with `repository_url`, `commit`, `branch`, `config_yaml`, and `files` mappings

## Confidence Level

**HIGH** -- All fields are fully documented and verified. The onboarding commit message explicitly cites the upstream commit hash. The config.yaml is present and correctly referenced. This is a recently onboarded family (February 2025) with clean, modern tooling.

## Open Questions

None. This family is fully complete.
