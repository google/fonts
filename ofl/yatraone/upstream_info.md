# Yatra One — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [cathschmidt/yatra-one](https://github.com/cathschmidt/yatra-one) |
| Commit | `b991e49f275db52a5b59ee959c87d0f7ba5325f5` |
| Date | 2016-09-26 |
| Confidence | High |

## Investigation

The METADATA.pb for Yatra One had no source block. The upstream repository was identified as cathschmidt/yatra-one, the designer Catherine Leigh Schmidt's own GitHub repository.

### Source Types Available

- **VFB** (FontLab): `source/masters/YatraOne.vfb`
- **Build scripts**: Custom Python build pipeline (`source/build.py`, `source/config.py`)
- **Feature files**: `source/family.fea` and related `.fea` files
- **Binary TTF**: Hinted and unhinted TTFs in root directory

### Buildability

The repository uses a custom build pipeline (not gftools-builder compatible). The VFB source format requires FontLab for editing. No `config.yaml`, `.glyphs`, `.ufo`, or `.designspace` sources are present. Not directly buildable with gftools-builder.

### Actions Taken

A source block was added to METADATA.pb pointing to commit `b991e49` (2016-09-26, "getting specimen in"), which is the latest commit in the repository and predates the google/fonts onboarding (2017-05-16).

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing the UFO source from `cathschmidt/yatra-one`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: [YatraOne_0.ufo]`. fontc_crater failed with `missing source 'YatraOne_0.ufo'`.

### Investigation
At the recorded commit `b991e49` a UFO source does exist, at `source/masters/YatraOne_0.ufo` — correcting the "no `.ufo` sources are present" note in the original investigation above. The UFO is nested under `source/masters/` alongside `YatraOne.vfb`. The `_0.ufo` suffix is the literal master filename used by the Indian Type Foundry build setup, not a stale rename. The override config path was missing the `source/masters/` directory prefix. The recorded commit is correct.

### Actions taken
The override `config.yaml` source path was corrected from `YatraOne_0.ufo` to `source/masters/YatraOne_0.ufo`.

### Final state
The override `config.yaml` references `source/masters/YatraOne_0.ufo`, which exists at the recorded commit `b991e49`.
