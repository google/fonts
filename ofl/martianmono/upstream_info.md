# Martian Mono — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/evilmartians/mono"
  commit: "a96373b28656b2608f28761e598471c99a4599e3"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/MartianMono[wdth,wght].ttf"
    dest_file: "MartianMono[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

- **Repository**: https://github.com/evilmartians/mono
- **Cached at**: `upstream_repos/fontc_crater_cache/evilmartians/mono/`
- **Remote verified**: Yes, origin points to `https://github.com/evilmartians/mono`
- **Repo status**: Clean, HEAD detached at `a96373b`
- **Total commits**: 106

### Source Files

The repository contains two Glyphs source files in `sources/`:
- `MartianMono.glyphs` (no space) — referenced by `config.yaml` for building
- `Martian Mono.glyphs` (with space) — appears to be a secondary/archive copy

The build-relevant source file (`MartianMono.glyphs`) has blob `bfb42ba` at both commit `17865aa` and HEAD `a96373b`, meaning it was NOT modified after the onboarding commit. The file with a space in the name (`Martian Mono.glyphs`) was modified in later commits (box-drawing characters in `9007e4f`, v1.1.0 changes in `8ffa86c`/`79f2447`) but is not used by the build configuration.

### Build Configuration

A valid `sources/config.yaml` exists in the upstream repo with gftools-builder configuration:
- Source: `MartianMono.glyphs`
- Axes: wdth, wght
- Family name: Martian Mono
- Includes STAT table definitions
- Last modified: `f718952` (2022-11-25), unchanged since before onboarding

## Onboarding History

### Initial Onboarding — Version 0.930 (PR #5624)

- **google/fonts commit**: `d34d418f5` (merged 2022-11-30)
- **Author**: Emma Marichal
- **Upstream commit referenced**: `3b0c3a32c1c1e0d1f67ca8e0044568a6f25ef883` (2022-11-25, "Merge pull request #20 from emmamarichal/main")
- **Files added**: DESCRIPTION.en_us.html, METADATA.pb, MartianMono[wdth,wght].ttf, OFL.txt, upstream.yaml
- **Font binary**: 128,468 bytes

### Update — Version 1.000 (PR #5794)

- **google/fonts commit**: `1386d6284` (merged 2023-01-18)
- **Author**: Emma Marichal
- **Upstream commit referenced**: `17865aac562a1a800888de6604f7251f135cf3b5` (2023-01-16, "Merge pull request #22 from emmamarichal/main")
- **PR body**: "Martian Mono Version 1.000 taken from the upstream repo https://github.com/evilmartians/mono at commit https://github.com/evilmartians/mono/commit/17865aac562a1a800888de6604f7251f135cf3b5."
- **Files changed**: METADATA.pb (axes updated), MartianMono[wdth,wght].ttf (128,468 -> 148,460 bytes)
- **Font binary**: 148,460 bytes

### Subsequent METADATA.pb Changes

1. **`66f91f10f`** — "Merge upstream.yaml into METADATA.pb [skip ci]": Added files block, branch field, and kept commit hash as `17865aa` (correct).
2. **`4ad8ac680`** — "[Batch 2/4] port info from fontc_crater targets list" (2025-03-31): Changed commit hash from `17865aa` to `a96373b` and added `config_yaml: "sources/config.yaml"`. This introduced the incorrect commit hash.

## Binary Verification

The font binary file `MartianMono[wdth,wght].ttf` in google/fonts was verified against the upstream repo at commit `17865aa`:
- **SHA256**: `c3467843ec1c2574b05fbcfd7147c7bfbcf63ddca8fc2bcb9d117f1bfb1b22e7`
- **Size**: 148,460 bytes
- **Match**: Identical. The binary in google/fonts matches exactly the file at `fonts/variable/MartianMono[wdth,wght].ttf` at commit `17865aac562a1a800888de6604f7251f135cf3b5`.

The font binary does NOT exist at the current METADATA.pb commit `a96373b` because that commit only added README documentation (`Add section about coding ligatures`) and did not modify any font files.

## Findings

### Issue: Incorrect Commit Hash

The current METADATA.pb commit `a96373b28656b2608f28761e598471c99a4599e3` is incorrect. This was introduced by the "Batch 2/4" commit (`4ad8ac680`) which ported data from fontc_crater's targets list. The fontc_crater targets recorded the HEAD of the upstream repo at the time of data collection (2025-02-11) rather than the original onboarding commit.

The correct commit hash is `17865aac562a1a800888de6604f7251f135cf3b5`, which was:
- Referenced in the gftools-packager commit message for PR #5794
- Referenced in the PR #5794 body
- Confirmed by binary SHA256 comparison of the font file

### Source Changes After Onboarding

After commit `17865aa` (2023-01-16), three commits modified source files:
1. `9007e4f` (2023-01-22): Added box-drawing characters to `Martian Mono.glyphs` (the file with space, NOT used by config.yaml)
2. `8ffa86c` (2025-02-10): v1.1.0 — modified `Martian Mono.glyphs` and `sources/config.yaml` was NOT changed
3. `79f2447` (2025-02-11): Fixed interpolation — modified `Martian Mono.glyphs`

These changes only affected `Martian Mono.glyphs` (the non-build file). The build source `MartianMono.glyphs` and `config.yaml` remained unchanged. However, these upstream changes represent potential future updates that would need separate review before incorporation into Google Fonts.

### Positive Findings

- Repository URL is correct
- `config_yaml` path (`sources/config.yaml`) is correct and exists at the onboarding commit
- The config.yaml properly references `MartianMono.glyphs` as the source
- Branch "main" is correct

## Recommended Source Block

```
source {
  repository_url: "https://github.com/evilmartians/mono"
  commit: "17865aac562a1a800888de6604f7251f135cf3b5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/MartianMono[wdth,wght].ttf"
    dest_file: "MartianMono[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

The only change needed is correcting the commit hash from `a96373b28656b2608f28761e598471c99a4599e3` to `17865aac562a1a800888de6604f7251f135cf3b5`.
