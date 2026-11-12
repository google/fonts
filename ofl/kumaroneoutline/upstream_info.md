# Kumar One Outline — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/itfoundry/kumar |
| Commit | `3192a79a79202eb715d83fd044e9234a6d0dde66` |
| Confidence | Medium |

## Source Types

The repository contains Glyphs sources:
- `masters/Kumar One.glyphs` — primary Glyphs source (monorepo with both variants)

## Build Compatibility

No `config.yaml` is present in the upstream repository. Needs verification that the Outline variant is included in the Glyphs source or as a separate source file within the repo.

## Investigation Notes

This is the same itfoundry/kumar monorepo used for Kumar One. The Outline variant shares the repository with the filled variant. The commit is the same as Kumar One since both variants are maintained together. The confidence is medium because while the repo is correct, verification is needed that the Outline variant sources are specifically present and buildable from this commit.

The binary in google/fonts was recently re-added (2025-04-10, "Missing in GH" fix).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: Medium

Same monorepo as Kumar One; needs verification that Outline variant sources are included at this commit.

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing the Glyphs source (shared with Kumar One) from `itfoundry/kumar`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: ["Kumar One.glyphs"]` — a repository-root path. fontc_crater failed with `missing source 'Kumar One.glyphs'`.

### Investigation
At the recorded commit `3192a79` the Glyphs source is `masters/Kumar One.glyphs`, not at the repository root. The override config path was missing the `masters/` directory prefix. The recorded commit is correct.

### Actions taken
The override `config.yaml` source path was corrected from `Kumar One.glyphs` to `masters/Kumar One.glyphs`.

### Final state
The override `config.yaml` references `masters/Kumar One.glyphs`, which exists at the recorded commit `3192a79`. This is the same `itfoundry/kumar` source shared with the Kumar One family.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`3192a79a`](https://github.com/itfoundry/kumar/commit/3192a79a) to [`551e277f`](https://github.com/itfoundry/kumar/commit/551e277f) ("Compile 1.000, OTF and TTF", on `master`), as for Kumar One.

The shipped `KumarOneOutline-Regular.ttf` ([google/fonts#9332](https://github.com/google/fonts/pull/9332)) has glyf, hmtx, GSUB, GPOS, GDEF, name and hinting tables byte-identical to `products/KumarOneOutline-Regular.ttf` at `551e277f`. Only OS/2 fsType (4 to 0), the vertical metrics, the head checksum and the cmap serialization differ. md5 shipped `d0d9ab6b71125c638f972492db70d802`, upstream `a6a22b313e2b001f11c8d9bc95ab413e`.

The override `config.yaml` (`masters/Kumar One.glyphs`) resolves at `551e277f` and is not changed here.
