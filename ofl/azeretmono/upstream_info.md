# Azeret Mono

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Displaay, Martin Vacha

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/displaay/Azeret |
| commit           | 3d45a6c3e094f08bfc70551b525bd2037cac51ba |
| config_yaml      | sources/config.yaml |
| branch           | main |
| Confidence       | HIGH |

## How URL Found

The repository URL `https://github.com/displaay/Azeret` was already present in METADATA.pb. It matches the copyright string in the font files ("Copyright 2021 The Azeret Project Authors (https://github.com/displaay/azeret)"). The cached clone at `displaay/Azeret` has this URL as its git remote origin.

## How Commit Identified

The commit `3d45a6c3e094f08bfc70551b525bd2037cac51ba` was already recorded in METADATA.pb. It was verified through multiple lines of evidence:

1. **Explicit reference in google/fonts onboarding commit**: The original onboarding commit `c44cf77` (PR #3475, 2021-06-09) by Rosalie Wagner states: "Azeret Version 1.002 taken from the upstream repo https://github.com/displaay/Azeret at commit https://github.com/displaay/Azeret/commit/3d45a6c3e094f08bfc70551b525bd2037cac51ba."

2. **Binary file identity**: The font files in google/fonts are byte-for-byte identical to those in the upstream repo at the referenced commit:
   - `AzeretMono[wght].ttf`: 106,092 bytes, SHA256 `f13962c26c1baa864aff7768364001f9bca6e506f41b9a3037c0d6a31e2ca736` -- matches in both locations
   - `AzeretMono-Italic[wght].ttf`: 112,284 bytes -- sizes match

3. **Only commit in repo**: The upstream repo contains only a single commit (the merge commit `3d45a6c`), so there is no ambiguity. No additional work has been done in the upstream repo since onboarding.

## How Config Resolved

The upstream repo contains `sources/config.yaml` at the referenced commit. The config file was introduced in that same (and only) commit. Contents:

```yaml
    sources:
      - AzeretMono.glyphs
      - AzeretMono-Italic.glyphs
    axisOrder:
      - wght
      - ital
    familyName: Azeret Mono
```

METADATA.pb correctly references this as `config_yaml: "sources/config.yaml"`. The source files (`AzeretMono.glyphs` and `AzeretMono-Italic.glyphs`) are present in the `sources/` directory. No override config is needed.

## History in google/fonts

| Date | Commit | Description |
|------|--------|-------------|
| 2021-06-09 | c44cf77 | Initial onboarding as `ofl/azeret` (PR #3475, by Rosalie Wagner via gftools-packager) |
| 2021-08-16 | 641a022 | Renamed from `ofl/azeret` to `ofl/azeretmono` (PR #3739, by Dave Crossland) |
| 2021-12-12 | 633ebad | Language support metadata added (PR #4160) |
| 2022-04-15 | 28b492c | Clear languages from METADATA.pb for non-Noto |
| 2022-05-16 | c6307ba | Roll back + redo in chunks (PR #4677) |
| 2022-05-23 | bc09b2c | Undo rollback, remove languages (PR #4703) |
| 2024-04-03 | 66f91f1 | Merge upstream.yaml into METADATA.pb |
| 2025-03-31 | 19cdcec | Batch 1/4: port info from fontc_crater targets list |

## Conclusion

Azeret Mono is fully documented. The METADATA.pb source block is complete and correct:
- **repository_url** points to a valid, accessible upstream repo
- **commit** is verified as the exact commit used for onboarding (confirmed by gftools-packager message, binary identity, and the fact that it is the only commit in the repo)
- **config_yaml** correctly points to `sources/config.yaml` which exists at the referenced commit with valid gftools-builder configuration
- **No action required** -- all source metadata is accurate and complete
