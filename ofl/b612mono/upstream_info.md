# B612 Mono

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete (with commit hash note)
- **Designer**: Nicolas Chauveau, Thomas Paillot, Jonathan Favre-Lamarine, Jean-Luc Vinot

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| repository_url   | https://github.com/polarsys/b612                                   |
| commit           | 48ac6ba67ecab8123e8e36d6aa05367db0c7b638                           |
| config_yaml      | *(omitted -- override config.yaml in google/fonts)*                |

## Repository URL

The repository URL `https://github.com/polarsys/b612` was already present in METADATA.pb. It was added by Simon Cozens in commit `5f2b22f` (2023-12-14, "Update upstreams"). The cached clone at `polarsys/b612` confirmed the remote matches this URL. The repository is a shared repo containing both B612 (sans-serif) and B612 Mono families.

## Commit Hash

### Current state in METADATA.pb

The METADATA.pb records commit `48ac6ba67ecab8123e8e36d6aa05367db0c7b638`. This was added by Felipe Sanches in commit `edbfb125a` (2025-11-19, "sources info for b612mono: v1.008 (PR #1878)").

### Onboarding history

B612 Mono was onboarded in two stages:

1. **v1.005 (original onboarding)**: Commit `0655ae3b2` by Marc Foley (2018-12-05) added the font, referencing upstream commit `4ea03c61a6946bf5510fdb29630dfbe257eefa5a` (PR #1759).

2. **v1.008 (update, current binaries)**: Commit `bff0396e9` by Marc Foley (2019-03-13) updated the font files. The commit message explicitly stated: *"Taken from the upstream repo https://github.com/polarsys/b612 at commit https://github.com/polarsys/b612/commit/7b5a653a6ae2bb05479297fed05ddf8c212d5477"*.

### Verification

The binary files in google/fonts were verified against the upstream repo:
- `B612Mono-Regular.ttf` SHA-256 in google/fonts: `b98cb96cc8a6206dae08c063d60902df7e6d40f86139ebdb97256704253c9c69`
- `B612Mono-Regular.ttf` SHA-256 at upstream commit `7b5a653`: **identical** (`b98cb96c...`)

This confirmed that the TTF files currently in google/fonts were taken from upstream commit `7b5a653`.

### Commit hash discrepancy

The METADATA.pb records `48ac6ba` (the latest commit in the repo, dated 2019-03-18), but the actual onboarding commit was `7b5a653` (dated 2019-03-12). The difference between these two commits consists of:

- `48ac6ba` -- Merge PR #17: "Update links from http:// to https://" (README only)
- `ab82be3` -- "Update links from http:// to https://"
- `697af2c` -- "Update EPL from 1.0 to 2.0"

None of these three commits touched font sources or binaries. They only modified `README.md`. The source files (`sources/ufo/B612Mono-*.ufo`) were last changed in commit `8c3b6cc` (2019-03-12, "Release new ttf and ufo files (1.008)"), which is an ancestor of `7b5a653`.

**Conclusion on commit**: The more precise commit hash would be `7b5a653a6ae2bb05479297fed05ddf8c212d5477`, which is the actual commit referenced in the google/fonts onboarding message and whose TTF files match byte-for-byte. The current hash `48ac6ba` is the repo HEAD and is functionally equivalent (no font/source changes between the two), but `7b5a653` better documents the actual onboarding point.

## Build Configuration

### Upstream repo

The upstream repository had **no config.yaml** at any commit. The sources are individual UFO files without a `.designspace` or `.glyphs` wrapper, located at `sources/ufo/B612Mono-*.ufo`.

### Override config.yaml

An override `config.yaml` was already present in the google/fonts family directory at `ofl/b612mono/config.yaml`, added in commit `edbfb125a` (2025-11-19). Its contents:

```yaml
buildVariable: false
sources:
  - sources/ufo/B612Mono-Bold.ufo
  - sources/ufo/B612Mono-BoldItalic.ufo
  - sources/ufo/B612Mono-Italic.ufo
  - sources/ufo/B612Mono-Regular.ufo
```

This configuration was verified: `buildVariable: false` is correct (there is no variable font; B612 Mono has four separate static masters). The source paths match the UFO directories present at commit `7b5a653` (and `48ac6ba`). The `config_yaml` field was correctly omitted from METADATA.pb since google-fonts-sources auto-detects the local override.

## Conclusion

B612 Mono's source metadata is **complete**. The repository URL, commit hash, and override config.yaml are all present and functional. The only note is that the commit hash `48ac6ba` in METADATA.pb is the repo HEAD rather than the more precise onboarding commit `7b5a653` referenced in the google/fonts commit message. Since no font or source files changed between these two commits, the current hash is functionally correct but less precise than the original onboarding reference.
