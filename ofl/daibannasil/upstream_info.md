# Dai Banna SIL

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: SIL International
**METADATA.pb path**: `ofl/daibannasil/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/silnrsi/font-daibannasil |
| Commit | `dcf3e10a5a42e65b191e4d14628f2f263f41b2bc` |
| Config YAML | Override in google/fonts |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/silnrsi/font-daibannasil`. The original onboarding commit `dc2a8d8a7` (2023-07-06, "[gftools-packager] Dai Banna SIL: Version 4.000 added") by Emma Marichal explicitly references the upstream repo. The DESCRIPTION.en_us.html also links to this repository.

## How the Commit Hash Was Identified

The original onboarding used `gftools-packager` with an `archive_url` pointing to the v4.000 release ZIP (`https://github.com/silnrsi/font-daibannasil/releases/download/v4.000/DaiBannaSIL-4.000.zip`). Notably, the commit message in the onboarding commit says "at commit https://github.com/silnrsi/font-daibannasil/commit/" with an **empty commit hash**, confirming the fonts were taken from the release archive, not from a specific git commit.

The commit `dcf3e10a5a42e65b191e4d14628f2f263f41b2bc` was added by the batch commit `9a14639f3` (2026-02-25, "Add source blocks to 602 more METADATA.pb files"). This commit hash corresponds exactly to the `v4.000` git tag in the upstream repository (verified: `git rev-parse v4.000` = `dcf3e10a5a42e65b191e4d14628f2f263f41b2bc`). The commit message is "Update documentation for a release", and it is the tagged release commit for v4.000, which matches the version that was onboarded.

## How Config YAML Was Resolved

**No `config.yaml` exists at the recorded commit** (`dcf3e10` / v4.000 tag). The upstream repo uses SIL's own build system (`tirobuild.yaml`) rather than gftools-builder.

A `googlefonts.yaml` file was added later (commit `70a3b2c`, "Different tools for building variable fonts"), which is 10 commits after v4.000. This file contains gftools-builder configuration for the designspace sources. However, since it does not exist at the onboarding commit, it cannot be referenced via `config_yaml` in METADATA.pb without also updating the commit hash to a newer commit.

The upstream repo has designspace source files at v4.000 (`source/DaiBannaSIL-VF.designspace`, `source/DaiBannaSILItalic-VF.designspace`), and an override `config.yaml` in `ofl/daibannasil/` names them (see the last section).

## Verification

- Commit exists in upstream repo: Yes
- Commit corresponds to v4.000 tag: Yes (exact match)
- Commit date: 2022-08-08 (via `git log dcf3e10 -1`)
- Commit message: "Update documentation for a release"
- Source files at commit: `source/DaiBannaSIL-VF.designspace`, `source/DaiBannaSILItalic-VF.designspace`, multiple UFO masters
- Font binaries were taken from release archive, not built from git sources

## Confidence

**High** for repository URL and commit hash: The URL is well-established and the commit hash corresponds exactly to the v4.000 release tag, matching the version onboarded via archive.

For config.yaml: no build config exists at the recorded commit, so an override is used (see the last section for how well it reproduces the shipped fonts).


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - source/DaiBannaSIL-VF.designspace
  - source/DaiBannaSILItalic-VF.designspace
buildVariable: false
extraStaticFontmakeArgs: --overlaps-backend pathops
```

This override config enables gftools-builder to compile the font from upstream sources.

## Override config corrected (2026-11-13)

**Model**: Claude Opus 5.5

The override named `source/DaiBannaSIL{Upright,Italic}.designspace`. smith interpolates from those, but varLib can't: their default sits between the masters. The `-VF` designspaces use the same master UFOs with the default on Light, so the override now names those.

With gftools 0.10.8 and fontmake 3.12.2, all 10 styles match the shipped cmap, and every glyph's bounds and advance are within 1 unit except one glyph in three italics (2 units). This needs `--overlaps-backend pathops`, since the default overlap remover fails on the masters' quadratic curves; the override passes it as `extraStaticFontmakeArgs` (added 2026-11-14, Claude Fable 5.2: without it the gftools build fails on all 10 styles with "unsupported segment type", with it all 10 build with the shipped codepoints). The shipped fonts are Graphite-only, so layout differs.
