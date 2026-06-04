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
| Config YAML | Not set (see notes below) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/silnrsi/font-daibannasil`. The original onboarding commit `dc2a8d8a7` (2023-07-06, "[gftools-packager] Dai Banna SIL: Version 4.000 added") by Emma Marichal explicitly references the upstream repo. The DESCRIPTION.en_us.html also links to this repository.

## How the Commit Hash Was Identified

The original onboarding used `gftools-packager` with an `archive_url` pointing to the v4.000 release ZIP (`https://github.com/silnrsi/font-daibannasil/releases/download/v4.000/DaiBannaSIL-4.000.zip`). Notably, the commit message in the onboarding commit says "at commit https://github.com/silnrsi/font-daibannasil/commit/" with an **empty commit hash**, confirming the fonts were taken from the release archive, not from a specific git commit.

The commit `dcf3e10a5a42e65b191e4d14628f2f263f41b2bc` was added by the batch commit `9a14639f3` (2026-02-25, "Add source blocks to 602 more METADATA.pb files"). This commit hash corresponds exactly to the `v4.000` git tag in the upstream repository (verified: `git rev-parse v4.000` = `dcf3e10a5a42e65b191e4d14628f2f263f41b2bc`). The commit message is "Update documentation for a release", and it is the tagged release commit for v4.000, which matches the version that was onboarded.

## How Config YAML Was Resolved

**No `config.yaml` exists at the recorded commit** (`dcf3e10` / v4.000 tag). The upstream repo uses SIL's own build system (`tirobuild.yaml`) rather than gftools-builder.

A `googlefonts.yaml` file was added later (commit `70a3b2c`, "Different tools for building variable fonts"), which is 10 commits after v4.000. This file contains gftools-builder configuration for the designspace sources. However, since it does not exist at the onboarding commit, it cannot be referenced via `config_yaml` in METADATA.pb without also updating the commit hash to a newer commit.

The upstream repo has designspace source files at v4.000 (`source/DaiBannaSIL-VF.designspace`, `source/DaiBannaSILItalic-VF.designspace`), so building from sources is technically possible -- but would require either:
1. An override `config.yaml` in the google/fonts family directory (`ofl/daibannasil/`), or
2. Updating the commit hash to a newer commit that includes `googlefonts.yaml`

No override config.yaml currently exists in `ofl/daibannasil/`.

## Verification

- Commit exists in upstream repo: Yes
- Commit corresponds to v4.000 tag: Yes (exact match)
- Commit date: 2022-08-08 (via `git log dcf3e10 -1`)
- Commit message: "Update documentation for a release"
- Source files at commit: `source/DaiBannaSIL-VF.designspace`, `source/DaiBannaSILItalic-VF.designspace`, multiple UFO masters
- Font binaries were taken from release archive, not built from git sources

## Confidence

**High** for repository URL and commit hash: The URL is well-established and the commit hash corresponds exactly to the v4.000 release tag, matching the version onboarded via archive.

**Low** for config.yaml: No build config exists at the recorded commit. The `googlefonts.yaml` added later in the repo could serve as a basis for an override config, but action is needed.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - source/DaiBannaSILUpright.designspace
  - source/DaiBannaSILItalic.designspace
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. Should an override `config.yaml` be created in `ofl/daibannasil/` based on the upstream `googlefonts.yaml`? This would enable building from sources without changing the commit hash.
2. Alternatively, should the commit hash be updated to a newer commit (e.g., `70a3b2c` or HEAD `0dee7c3`) that includes `googlefonts.yaml`? This would require verifying that the newer commit produces equivalent font output.
