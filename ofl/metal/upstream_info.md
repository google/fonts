# Metal — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/danhhong/Metal
- **Branch**: master
- **Pinned commit**: `2d74e37de805a7bc4fb3f704897fbfd2f4e0ac7f`
- **Commit date**: 2021-11-01
- **Commit message**: "Merge pull request #2 from yanone/master — Update regarding a user-reported spacing problem with *_17B6 glyphs"
- **HEAD status**: Pinned commit is the current HEAD of master. The repository has not been updated since November 2021.
- **Upstream cache**: Not available (danhhong org not present in `/mnt/shared/upstream_repos/fontc_crater_cache/`).

## Source Files

| File | Path in repo | Size |
|------|-------------|------|
| Glyphs source | `Source/Metal.glyphs` | ~1.0 MB |
| Build config | `Source/builder.yaml` | — |
| Binary TTF | `Release/ttf/Metal-Regular.ttf` | — |
| License | `OFL.txt` | — |
| Description | `DESCRIPTION.en_us.html` | — |

The repository has a clean, minimal structure with a single-master Glyphs source and pre-built binaries in `Release/ttf/`.

## Build System

The `Source/builder.yaml` uses `gftools-builder` (Glyphs App workflow). Content at pinned commit:

```yaml
sources:
  - Metal.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

- Only static TTF is built; no variable font, no OTF, no webfont.
- Build is non-variable, single weight (Regular 400).
- The `outputDir` is relative: `../Release`, which matches the `Release/ttf/` path where the binary sits.

## config.yaml Status

A `config_yaml` entry is already present in METADATA.pb pointing to `Source/builder.yaml`. This is correct and consistent with the repo layout at the pinned commit. No additional `config.yaml` is needed.

## Notes

- **Designer**: Danh Hong, a Khmer script specialist with extensive experience in Southeast Asian typography. Active in the KhmerOS project.
- **Script**: The font covers Khmer (primary) and Latin scripts. `primary_script` in METADATA.pb is correctly set to `Khmr`.
- **Subsets**: `khmer`, `latin`, and `menu` — consistent with the font's scope.
- **Category/Classification**: `DISPLAY` with `SERIF` stroke — appropriate for this decorative Khmer display face.
- **Upstream activity**: The repo is dormant since 2021. The two PRs from collaborator Yanone addressed spacing issues with Khmer vowel sign glyphs (Unicode *_17B6 range).
- **PR #1** (merged 2021-06-07): Initial spacing fix from Yanone.
- **PR #2** (merged 2021-11-01, pinned commit): Follow-up spacing fix for the same glyph range.
- **Copyright**: "Copyright 2019 The Metal Project Authors (https://github.com/danhhong/Metal)" — consistent with the OFL.txt and font binary.
- **Confidence**: High. The repo structure, build config, and binary paths all align with what is declared in METADATA.pb.
