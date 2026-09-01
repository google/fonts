# Kumar One — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/itfoundry/kumar |
| Commit | `3192a79a79202eb715d83fd044e9234a6d0dde66` |
| Confidence | High |

## Source Types

The repository contains Glyphs sources:
- `masters/Kumar One.glyphs` — primary Glyphs source

This is a monorepo that contains both Kumar One and Kumar One Outline variants.

## Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs source could potentially be built with gftools-builder given an override config.

## Investigation Notes

Indian Type Foundry's repository is the canonical upstream for the Kumar font family. The binary in google/fonts was last updated on 2017-05-23 (v1.001 hotfix). The repository contains the filled variant (Kumar One) used by this family entry.

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Indian Type Foundry (itfoundry) is the original designer/publisher.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: ["Kumar One.glyphs"]` — a repository-root path. fontc_crater failed with `missing source 'Kumar One.glyphs'`.

### Investigation
At the recorded commit `3192a79` the Glyphs source is `masters/Kumar One.glyphs`, not at the repository root. The override config path was missing the `masters/` directory prefix. The recorded commit is correct.

### Actions taken
The override `config.yaml` source path was corrected from `Kumar One.glyphs` to `masters/Kumar One.glyphs`.

### Final state
The override `config.yaml` references `masters/Kumar One.glyphs`, which exists at the recorded commit `3192a79`. The companion family Kumar One Outline shares the same repository, commit and source file and received the same correction.
