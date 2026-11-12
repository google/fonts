# Amaranth

**Status**: `complete`
**Date**: 2026-02-25
**Designer**: Gesine Todt
**License**: OFL
**METADATA.pb**: `ofl/amaranth/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/amaranth |
| Commit | `f4f60a57f54a04186030913a86e3e56105bbe848` |
| Config YAML | Override in google/fonts family directory |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Used HEAD of upstream repository (latest commit at time of onboarding).
- Commit date: 2017-07-21 16:51:53 +0100
- Commit message: "generated otfs"

### Config YAML
Override `config.yaml` exists in the google/fonts family directory. Per policy, `config_yaml` field is omitted from METADATA.pb.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/googlefonts/amaranth`
- `commit`: `—`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `c0fb6f7c6193`
- Date: 2017-08-07 21:46:27 +0100
- Subject: "hotfix-amaranth: v1.001 added (#759)"

### Upstream repo cache
- Cached at: `googlefonts/amaranth`
- Commit `f4f60a57f54a` verified ✓

### Override config
Override `config.yaml` exists in `ofl/amaranth/config.yaml`.

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

Latest commit in upstream (2017-07-21), used for gfonts PR #759 merged 2017-08-07. All commits are from the same day.
