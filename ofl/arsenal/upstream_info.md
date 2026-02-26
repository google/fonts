# Arsenal

**Status**: `complete`
**Date**: 2026-02-25
**Designer**: Andrij Shevchenko
**License**: OFL
**METADATA.pb**: `ofl/arsenal/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/alexeiva/Arsenal |
| Commit | `878af0840749599133561eb6579d84f5c94f58f5` |
| Config YAML | Override in google/fonts family directory |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Identified via google/fonts PR body analysis, commit message references, or date correlation with upstream history.
- Commit date: 2016-12-06 10:08:59 +0100
- Commit message: "fonts | sources | OFL: fixed copyright string"

### Config YAML
Override `config.yaml` exists in the google/fonts family directory. Per policy, `config_yaml` field is omitted from METADATA.pb.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/alexeiva/Arsenal`
- `commit`: `—`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `2f6c0a183f9d`
- Date: 2016-12-06 11:05:42 +0100
- Subject: "arsenal: v1.001 added (#507)"

### Upstream repo cache
- Cached at: `alexeiva/Arsenal`
- Commit `878af0840749` verified ✓

### Override config
Override `config.yaml` exists in `ofl/arsenal/config.yaml`.

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

m4rc1e's commit 'fixed copyright string' (2016-12-06) from PR #6 branch, used for gfonts PR #507 merged same day. Later merged to master as ec148f6.
