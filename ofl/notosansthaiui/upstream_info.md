# Noto Sans Thai UI — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [notofonts/thai](https://github.com/notofonts/thai) |
| Commit | `a79e109f3fee8b3e5f952c8dadcae4b7b341f562` |
| Version | 2.000 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Repository Change

The `repository_url` was changed from `googlefonts/noto-fonts` (the old monorepo with pre-built binaries) to `notofonts/thai` (the per-script repo with actual source files). This enables reproducible builds because:

- The old `googlefonts/noto-fonts` monorepo only contained pre-built TTF binaries, not source files (.designspace, .ufo, .glyphs)
- The `notofonts/thai` repo contains the actual design sources needed by gftools-builder
- The override config.yaml references `sources/NotoSansThaiUI.designspace` which exists in `notofonts/thai` but not in `googlefonts/noto-fonts`

The commit `a79e109` is the initial "Add new fonts" commit (2022-06-21) when sources were imported into the per-script repo. These sources should match the state used to build the v2.000 font originally shipped via PR #2823.

## Previous provenance

The font was originally onboarded from the `googlefonts/noto-fonts` monorepo at commit `282a3a827151188c0ee4bce392e89e6ef4c16323` (Dec 25, 2020 batch). That commit was blob-hash verified against PR #2823. The binary in the monorepo was the build output; the design sources lived elsewhere and were later consolidated into the per-script repos.

## Build Configuration (Override)

An override `config.yaml` is present, copied from `sources/config-sans-thai-ui.yaml` in `notofonts/thai`. It references `sources/NotoSansThaiUI.designspace`.

**Confidence**: MEDIUM (per-script repo has the sources but was created after onboarding; initial import commit used as best approximation)
