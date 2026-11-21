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
| Config YAML | None: the repository has only FontLab .vfb sources |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Identified via google/fonts PR body analysis, commit message references, or date correlation with upstream history.
- Commit date: 2016-04-06 22:55:09 +0300
- Commit message: "adding img"

### Config YAML
None. The repository has no source that gftools-builder reads (see the last section).

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
None (removed 2026-11-13, see the last section).

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

Second commit in upstream (2016-04-06, adds sample image). Font files present since initial commit. Used for gfonts PR #760 merged 2017-08-07.


## Source-metadata review (2026-06-02) — WON'T FIX (unreproducible)

**Model**: Claude Opus 4.8

fontc_crater reports `missing source 'sources/Amethysta-Regular.glyphs'`: at the pinned commit `10ae36bc` (2016) the repository has no `.glyphs` source at all. The only commit that contains `sources/Amethysta-Regular.glyphs` is `d3cd4cae` (tag v1.002, 2024-12-29). However the shipped google/fonts binary is **Version 1.003**, which no upstream commit produces (the repo only ever builds v1.002). Repointing to `d3cd4cae` would make the family buildable but would **downgrade** it (v1.002 < the shipped v1.003), so it is not a valid provenance correction.

Decision: **WON'T FIX** here — the METADATA.pb source block is left unchanged. Resolving this requires either locating the lost v1.003 source upstream or a deliberate decision to refresh the family down to the available v1.002 source; both are owner/maintainer calls, not a mechanical metadata fix.

## Override config removed (2026-11-13)

**Model**: Claude Fable 5.2

The override named `sources/Amethysta-Regular.glyphs`. At the pinned commit the repository holds only `src/Amethysta-Regular.vfb`, `-TTF.vfb` and `-OTF.vfb` (FontLab), an OTF and the TTF, so fontc_crater reported a missing source. No build tool reads a .vfb, so the override was removed.

The Glyphs file exists only in a later commit, [`d3cd4cae`](https://github.com/cyrealtype/Amethysta/commit/d3cd4cae0216f8ff5dac6e9c39e2202527422d76) (2024-12-29, "Release v1.002"), which moved the files and left the TTF byte-identical. That file does not build with gftools 0.10.8 and fontmake 3.12.2 (overlap removal fails on its quadratic curves; without it, the features fail: `languagesystem DFLT dflt` is not first), nor with fontc 2.0.1 (the same feature error). So the pin stays where it was.
