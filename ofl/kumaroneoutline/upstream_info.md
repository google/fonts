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

An override `config.yaml` has been created in the google/fonts family directory, referencing `Kumar One.glyphs (shared with Kumar One)` from `itfoundry/kumar`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.
