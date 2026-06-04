# Amethysta

**Status**: `complete`
**Date**: 2026-02-25
**Designer**: Cyreal
**License**: OFL
**METADATA.pb**: `ofl/amethysta/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/cyrealtype/Amethysta |
| Commit | `10ae36bc060bec28f1c504c42ce6871b7c034add` |
| Config YAML | Override in google/fonts family directory |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Identified via google/fonts PR body analysis, commit message references, or date correlation with upstream history.
- Commit date: 2016-04-06 22:55:09 +0300
- Commit message: "adding img"

### Config YAML
Override `config.yaml` exists in the google/fonts family directory. Per policy, `config_yaml` field is omitted from METADATA.pb.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/cyrealtype/Amethysta`
- `commit`: `—`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `4e23b59c52af`
- Date: 2017-08-07 21:42:29 +0100
- Subject: "hotfix-amethysta: v1.003 added (#760)"

### Upstream repo cache
- Cached at: `cyrealtype/Amethysta`
- Commit `10ae36bc060b` verified ✓

### Override config
Override `config.yaml` exists in `ofl/amethysta/config.yaml`.

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

Second commit in upstream (2016-04-06, adds sample image). Font files present since initial commit. Used for gfonts PR #760 merged 2017-08-07.
