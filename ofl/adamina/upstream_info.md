# Adamina

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Cyreal
**METADATA.pb path**: `ofl/adamina/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/cyrealtype/Adamina |
| Commit | `719bd2a68700963ef0870bc707c77bc2b915dc7a` |
| **Config YAML** | Override in google/fonts |
| Branch | -- |

## How the Repository URL Was Found

The METADATA.pb file contains a source block with `repository_url: "github.com/cyrealtype/Adamina"` (note: missing `https://` prefix). This was added by Simon Cozens in commit `d60eded8e` (2023-12-20: "Add upstream"). The full URL `https://github.com/cyrealtype/Adamina` has been verified as accessible (HTTP 200).

The `cyrealtype` GitHub organization is the official home of Cyreal's open-source typefaces, consistent with the designer credit "Cyreal" in METADATA.pb.

## How the Commit Hash Was Identified

The upstream repo at `cyrealtype/Adamina` contains only **one commit**:

- `719bd2a68700963ef0870bc707c77bc2b915dc7a` (2023-10-05): "regenned fonts with updated OT code v1.012"

This is the sole commit, so it is the only possible reference. However, there is a **version mismatch**: the font in google/fonts is **v1.013**, added via PR #744 (2017-05-01: "hotfix-adamina: v1.013 added") by Marc Foley (`m4rc1e`). The upstream repo's single commit describes v1.012, suggesting:

1. The v1.013 hotfix was done outside the upstream repo (likely directly by a Google Fonts engineer)
2. The upstream repo may have been force-pushed or recreated after the original onboarding

The google/fonts font-modifying commit (`baf1d1a9`, PR #744) has an empty PR body, so no upstream commit reference was recorded at the time of the hotfix.

## How Config YAML Was Resolved

**No config.yaml exists** in the upstream repo, despite having gftools-compatible source files:

- `sources/Adamina.glyphs` -- Glyphs format, suitable for gftools-builder
- `sources/archive/Adamina-Regular.ufo/` -- UFO format (in archive subdirectory)
- `sources/archive/Adamina-Regular-OTF.vfb` and `sources/archive/Adamina-Regular-TTF.vfb` -- Legacy VFB files

No override `config.yaml` exists in `ofl/adamina/` in google/fonts either. A config.yaml could be created (either as an override in google/fonts or contributed to the upstream repo) since the `.glyphs` source file is present.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2023-10-05 21:12:08 +0600
- Commit message: "regenned fonts with updated OT code v1.012"
- Source files at commit: `sources/Adamina.glyphs`, `sources/archive/Adamina-Regular.ufo/`, plus VFB archives

## Confidence

**Medium**: The repository URL was pre-existing in METADATA.pb (added by Simon Cozens) and is confirmed valid. The commit hash is unambiguous (only one commit exists). However, the version mismatch between the upstream repo (v1.012) and google/fonts (v1.013) indicates the upstream repo does not fully represent the source state used for the current google/fonts binary. The v1.013 hotfix was likely done externally.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Adamina.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. The METADATA.pb `repository_url` field is missing the `https://` prefix -- should this be fixed?
2. Where are the actual sources for v1.013 that was added in PR #744? Were they generated from a different state of the repo that was later force-pushed?
3. Should an override `config.yaml` be created in `ofl/adamina/` for gftools-builder compatibility, using `sources/Adamina.glyphs` as the source?
4. Should a `commit` field be added to the METADATA.pb source block?
