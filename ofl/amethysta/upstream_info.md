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


## Source-metadata review (2026-06-02) — WON'T FIX (unreproducible)

**Model**: Claude Opus 4.8

fontc_crater reports `missing source 'sources/Amethysta-Regular.glyphs'`: at the pinned commit `10ae36bc` (2016) the repository has no `.glyphs` source at all. The only commit that contains `sources/Amethysta-Regular.glyphs` is `d3cd4cae` (tag v1.002, 2024-12-29). However the shipped google/fonts binary is **Version 1.003**, which no upstream commit produces (the repo only ever builds v1.002). Repointing to `d3cd4cae` would make the family buildable but would **downgrade** it (v1.002 < the shipped v1.003), so it is not a valid provenance correction.

Decision: **WON'T FIX** here — the METADATA.pb source block is left unchanged. Resolving this requires either locating the lost v1.003 source upstream or a deliberate decision to refresh the family down to the available v1.002 source; both are owner/maintainer calls, not a mechanical metadata fix.
