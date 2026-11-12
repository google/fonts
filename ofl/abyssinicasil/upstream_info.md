# Abyssinica SIL

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: SIL International
**METADATA.pb path**: `ofl/abyssinicasil/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/silnrsi/font-abyssinica |
| Commit | `1f7e65b0e7367681198c980647b3049559ebefa0` |
| Config YAML | override config.yaml in google/fonts |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/silnrsi/font-abyssinica` is recorded in the METADATA.pb `source` block. It was explicitly referenced in the google/fonts commit `044faf160` (2024-10-30, authored by Emma Marichal) which states: "Taken from the upstream repo https://github.com/silnrsi/font-abyssinica at commit https://github.com/silnrsi/font-abyssinica/commit/1f7e65b0e7367681198c980647b3049559ebefa0."

The upstream repo is cached at `upstream_repos/fontc_crater_cache/silnrsi/font-abyssinica` and confirmed accessible.

## How the Commit Hash Was Identified

The commit `1f7e65b0e7367681198c980647b3049559ebefa0` is explicitly referenced in:
1. The METADATA.pb `source` block
2. The google/fonts commit message for `044faf160`

This commit was verified to exist in the upstream repo. It is dated 2024-10-29 15:33:26 -0500 with the message "Update font in references and in test files. [nobuild]" by Lorna Evans. It is 2 commits after the v2.300 tag (`037d134`, dated 2024-10-29 09:13:25 -0500) — both from the same day. The commit updates the reference binary font file in `references/AbyssinicaSIL-Regular.ttf` to match the v2.300 release build.

The binary font at this commit (`references/AbyssinicaSIL-Regular.ttf`, 268,264 bytes) matches the file in google/fonts exactly (268,264 bytes), confirming this is the correct commit. The font was distributed via the `archive_url` pattern — the pre-built binary from the GitHub release `v2.300` was used directly rather than building from source.

## How Config YAML Was Resolved

The upstream repo does **not** have a `config.yaml` at the referenced commit (or at HEAD). The font was onboarded using the `archive_url` pattern: the pre-built binary from the GitHub release at `https://github.com/silnrsi/font-abyssinica/releases/download/v2.300/AbyssinicaSIL-2.300.zip` was extracted directly into google/fonts. The METADATA.pb `source` block includes `files` mappings that specify how to copy files from the archive.

However, the upstream repo does contain gftools-builder-compatible sources:
- `source/AbyssinicaSIL.designspace` (designspace format 3)
- `source/AbyssinicaSIL-Regular.ufo`

A local override `config.yaml` was added to the google/fonts family directory in commit `f6c68379a` (2026-02-16, by Felipe Sanches) as part of a batch adding override configs for 50 families. This override points to `source/AbyssinicaSIL.designspace` and configures static builds without OTF output:

```yaml
sources:
  - source/AbyssinicaSIL.designspace
familyName: Abyssinica SIL
buildStatic: true
buildOTF: false
```

Since the override config.yaml exists locally in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb `source` block (google-fonts-sources auto-detects local overrides).

## Conclusion

Abyssinica SIL is fully documented. The repository URL, commit hash, and branch are all present in METADATA.pb and have been verified. The font was onboarded via the archive distribution pattern (pre-built binary from a GitHub release), but the upstream repo also contains designspace/UFO sources suitable for building with gftools-builder. A local override config.yaml has been added to the google/fonts family directory to enable source builds. All data is consistent and the binary sizes match exactly.
