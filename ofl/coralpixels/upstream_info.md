# Coral Pixels

## Source Data

| Field | Value |
|---|---|
| Family Name | Coral Pixels |
| Repository URL | https://github.com/tanukifont/Coral-Pixels |
| Commit Hash | `2817da74e36af89291ed233f6e2d799554eff991` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| Status | complete |

## How URL Found

The repository URL `https://github.com/tanukifont/Coral-Pixels` is documented in:
1. The `METADATA.pb` source block in google/fonts
2. The copyright string: "Copyright 2024 The Coral Pixels Project Authors (https://github.com/tanukifont/Coral-Pixels)"
3. The onboarding commit message (`c7ee9d632`): "Taken from the upstream repo https://github.com/tanukifont/Coral-Pixels"

The URL matches the git remote of the cached upstream repo at `upstream_repos/fontc_crater_cache/tanukifont/Coral-Pixels`.

## How Commit Determined

The commit hash `2817da74e36af89291ed233f6e2d799554eff991` is explicitly documented in:
1. The `METADATA.pb` source block
2. The onboarding commit message (`c7ee9d632`): "at commit https://github.com/tanukifont/Coral-Pixels/commit/2817da74e36af89291ed233f6e2d799554eff991"

The upstream repository contains exactly **one commit** (a merge of PR #1 from emmamarichal/main), and this commit hash matches. The onboarding was performed by Emma Marichal on 2025-03-28.

## Config YAML Status

**config.yaml exists** in the upstream repository at `sources/config.yaml`. Contents:
```yaml
sources:
  - CoralPixels.glyphs
familyName: "Coral Pixels"
outputDir: ../fonts
ttDir: $outputDir/ttf
buildTTF: true
buildOTF: false
```

The source file is `sources/CoralPixels.glyphs` (Glyphs format), which is fully compatible with gftools-builder. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml`.

## Verification

- **Repository accessible**: Yes (verified via git remote URL)
- **Commit hash valid**: Yes - matches the only commit in the repo, and explicitly referenced in onboarding commit
- **Source block complete**: Yes - has repository_url, commit, config_yaml, files mapping, and branch
- **Config.yaml valid**: Yes - properly configured for gftools-builder with Glyphs source

## Confidence Level

**High** - Modern onboarding with explicit commit reference in the google/fonts commit message. Complete source block in METADATA.pb. Single commit in upstream repo makes the hash unambiguous.

## Open Questions

None. This family is fully complete with all source documentation in place.
