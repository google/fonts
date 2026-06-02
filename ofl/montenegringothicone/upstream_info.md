# Montenegrin Gothic One

**Model**: Claude Opus 4.8 (1M context)
**Date**: 2026-06-02
**Designer**: Žarko Banović
**METADATA.pb**: `ofl/montenegringothicone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/MagicformDesign/montenegrin-gothic-one |
| Commit | `7a9c8500be19a4b3c6050dd4ea6fcf184ca59173` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

Montenegrin Gothic One is a static serif family with a single style (Regular, weight 400). It is built from a Glyphs source through the standard `googlefonts-project-template` toolchain (fontmake + gftools fixes + ttfautohint), driven by `gftools builder`.

## Initial state

The onboarding (`date_added: 2026-05-07`) left a complete `source { ... }` block in `METADATA.pb`, pinning commit `7a9c850` on branch `main` and listing `OFL.txt` and `fonts/ttf/MontenegrinGothicOne-Regular.ttf` as source files. However:

- No `upstream_info.md` report existed for the family.
- The `source` block did **not** set `config_yaml`, even though the upstream repo ships a valid gftools-builder configuration at `sources/config.yaml`.
- The commit hash had not been independently verified against the shipped binary.

## Actions taken

- **Commit verified by binary match.** The shipped `MontenegrinGothicOne-Regular.ttf` was compared against the repo's binary at the pinned commit (see evidence below). They are byte-identical, confirming both the commit and that the shipped font is the committed build verbatim.
- **Source and build config inspected.** The repo contains a Glyphs source (`sources/MontenegrinGothicOne.glyphs`), a secondary UFO export (`sources/Montenegrin Gothic One-Regular.ufo`, not referenced by the build), a legacy SFD under `sources/_Old/`, and a gftools-builder config at `sources/config.yaml`. The config (`sources: [MontenegrinGothicOne.glyphs]`, `familyName: "Montenegrin Gothic One"`, `cleanUp: true`) was validated with `gftools builder --generate sources/config.yaml` (exit 0), which emitted a coherent `googlefonts` recipe producing `fonts/ttf/MontenegrinGothicOne-Regular.ttf` via `buildTTF → autohint → fix`.
- **`config_yaml` set.** Because a valid upstream gftools-builder config exists, `source.config_yaml` was set to `sources/config.yaml` in `METADATA.pb` (no override config was needed).
- **Reproducibility confirmed by full build.** A complete `gftools builder sources/config.yaml` build was run from a throwaway checkout of the pinned commit.
- **Report written** (this file).

## Final state

`METADATA.pb` now records the upstream build configuration (`config_yaml: sources/config.yaml`), the family carries an investigation report, and the pinned commit is verified as the exact source of the shipped binary. The family can be rebuilt from source with `gftools builder sources/config.yaml`.

## How the Commit Hash Was Verified

The pinned commit `7a9c850` is the merge of upstream PR #1 (dated 2026-05-07), which matches the family's `date_added`.

The shipped binary was compared to the committed binary at that commit:

| File | sha256 | bytes |
|------|--------|-------|
| Shipped `ofl/montenegringothicone/MontenegrinGothicOne-Regular.ttf` | `9312b0cd…d292e134` | 140876 |
| Repo `fonts/ttf/MontenegrinGothicOne-Regular.ttf` @ `7a9c850` | `9312b0cd…d292e134` | 140876 |
| Repo `fonts/_archives/MontenegrinGothicOne-Regular.ttf` @ `7a9c850` (older) | `92b6f6a1…737c5909b1` | — |

The shipped font is **byte-exact** to `fonts/ttf/…` at the pinned commit, so the commit is verified and the shipped binary is the committed build verbatim (no post-merge gftools-packager re-fixing). The `fonts/_archives/…` TTF is a different, superseded build and is **not** the shipped file.

`commit_verified = true.`

## Build Configuration

- **Source**: `sources/MontenegrinGothicOne.glyphs` (Glyphs, version 1.2 — matching `head.fontRevision` 1.002 in the binary).
- **Config**: `sources/config.yaml` (upstream gftools-builder config). Decision: **set `config_yaml`** in `METADATA.pb` to `sources/config.yaml` — no override config was required because the upstream config is valid and gftools-compatible. The repo's `Makefile` builds with `gftools builder sources/config.yaml`, the same path used here.
- **Recipe** (from `gftools builder --generate`): `MontenegrinGothicOne.glyphs` → `instantiateUfo` → `buildTTF` → `autohint` (`--fail-ok`, ttfautohint) → `fix` (gftools-fix-font), with parallel OTF/WOFF2 targets.
- **Reproducibility**: `exact` (up to build timestamp). A full build from the pinned commit produced a TTF that is byte-identical to the shipped font in **every table except `head`**; within `head` the only difference is the embedded `modified` timestamp (shipped 2026-05-07T13:01:22 vs rebuild 2026-06-02). `glyf`, `name` (including the ttfautohint string in ID 5), `OS/2`, `GPOS/GSUB/GDEF`, `cmap`, and the hinting tables (`cvt`, `fpgm`, `prep`, `gasp`) are byte-equal; `head.fontRevision` matches. No `refresh` is needed.

## Timeline

- **2014** — Original design epoch (`head.created` = 2014-09-02; copyright notice "Copyright 2014 …").
- **2026-05-07** — Upstream PR #1 merged at `7a9c850`; shipped TTF `head.modified` = 2026-05-07T13:01:22.
- **2026-05-07** — Family onboarded to google/fonts (`date_added`); shipped binary equals the committed `fonts/ttf` binary at `7a9c850`.
- **2026-06-02** — This investigation: commit verified by binary match, config validated and built, `config_yaml` set, report written.

## Issues Found

- No `upstream_info.md` existed prior to this report.
- `METADATA.pb` did not set `source.config_yaml` despite a valid upstream `sources/config.yaml` (now set to `sources/config.yaml`).
- The repo also ships a secondary UFO export (`sources/Montenegrin Gothic One-Regular.ufo`) and a legacy SFD (`sources/_Old/MontenegrinGothicOne.sfd`); neither is used by the build, which compiles from `MontenegrinGothicOne.glyphs`.
- Minor reproducibility caveat: `head.modified` is stamped at build time, so a rebuild is not bit-identical, but every other table reproduces exactly.
