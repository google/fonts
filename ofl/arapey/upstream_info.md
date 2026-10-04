# Arapey

**Status**: `complete`
**Date**: 2026-02-25
**Designer**: Eduardo Tunni
**License**: OFL
**METADATA.pb**: `ofl/arapey/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/etunni/arapey |
| Commit | `9c06862616bd689aec606d630cf5ad11ec5ea6f2` |
| Config YAML | Override in google/fonts family directory |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field.
- Commit date: 2013-12-30 10:48:53 -0300
- Commit message: "Adobe Latin 3 encoding"

### Config YAML
Override `config.yaml` exists in the google/fonts family directory. Per policy, `config_yaml` field is omitted from METADATA.pb.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/etunni/arapey`
- `commit`: `9c06862616bd689aec606d630cf5ad11ec5ea6f2`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `f106b928fdac`
- Date: 2015-04-27 13:43:41 -0400
- Subject: "Updating ofl/arapey/*ttf with nbspace and fsType fixes"

### Upstream repo cache
- Cached at: `etunni/arapey`
- Commit `9c06862616bd` verified ✓

### Override config
Override `config.yaml` exists in `ofl/arapey/config.yaml`.

## Confidence

**High**: URL pre-existing in METADATA.pb; commit pre-existing in METADATA.pb

## Recent upstream/main activity (post-investigation)

- **2026-04-10** — Dave Crossland, commit [`cf9e83c23`](https://github.com/google/fonts/commit/cf9e83c23) ("ofl/arapey/METADATA.pb Add minisite URL"): added `minisite_url: "https://etunni.github.io/Arapey-Minisite"` to METADATA.pb. This is outside the `source { ... }` block and does not affect the recorded source provenance — purely a display-side metadata addition.
