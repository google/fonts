# Noto Serif Nyiakeng Puachue Hmong — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [notofonts/nyiakeng-puachue-hmong](https://github.com/notofonts/nyiakeng-puachue-hmong) |
| Commit | `6f39c5843fe2f459973c3cd57dc82ca09cccbab0` |
| Version | 1.000 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Repository Change

The `repository_url` was changed from `googlefonts/noto-fonts` (the old monorepo with pre-built binaries) to `notofonts/nyiakeng-puachue-hmong` (the per-script repo with actual source files). This enables reproducible builds because:

- The old `googlefonts/noto-fonts` monorepo only contained pre-built TTF binaries, not source files (.designspace, .ufo)
- The `notofonts/nyiakeng-puachue-hmong` repo contains the actual design sources needed by gftools-builder
- The override config.yaml references `sources/NotoSerifNPHmong.designspace` which exists in the per-script repo but not in the old monorepo

The commit `6f39c58` is the initial "Add new fonts" commit (2022-06-20) when sources were imported into the per-script repo. The v1.000 sources at this commit should match the state used to build the font originally shipped via PR #2823.

Note: the sibling family `notoserifnphmong` (the short-name v1.001 variant) already points to this same per-script repo at a later commit (`2c945bb9`, NotoSerifNPHmong-v1.001 tag).

## Previous provenance

The font was originally onboarded from the `googlefonts/noto-fonts` monorepo at commit `9232f17974e5783a5dbd862f38225e0584e73add` (Dec 25, 2020 batch). That commit was blob-hash verified against PR #2823.

## Build Configuration (Override)

An override `config.yaml` is present, copied from `sources/config-serif-nyiakeng-puachue-hmong.yaml` in the per-script repo. It references `sources/NotoSerifNPHmong.designspace`.

**Confidence**: MEDIUM (per-script repo created after onboarding; initial import commit used as best approximation)
