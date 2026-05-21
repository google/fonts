# Neuton — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [anoxic/neuton](https://github.com/anoxic/neuton) |
| Commit | `b376055d272ab8a54d490bfad487e96c1d047c97` |
| Binary Date | 2016-12-02 |
| Source Types | .ufo, .sfd |
| Buildable | Yes |
| Confidence | High (canonical designer repo) |

## Notes

Source repository for neuton. Commit determined by date correlation with the last binary modification in google/fonts (2016-12-02).

## Build Configuration (Override)

An override `config.yaml` had been created in the google/fonts family directory referencing `NL.ufo`. See the fontc_crater fix below — that override has since been removed because the referenced file does not exist.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: [NL.ufo]`. fontc_crater failed with `missing source 'NL.ufo'`.

### Investigation
The recorded commit `b376055` is a genuine ancestor of `master`, but no file named `NL.ufo` exists in the repository as a production master at that commit or any other. The repo is an in-progress personal project containing only FontForge `.sfd` snapshots and a single partial UFO (`Tools/Glyphs/Neuton-light.ufo`). Files literally named `NL.ufo`/`NB.ufo` appear only later under `proof/tests/` as fragmentary test UFOs (95 glyphs), not production masters. The shipped six-style family cannot be reproduced from any single source present in the repo — it has no gftools-builder-compatible source set. (This corrects the "Source Types: .ufo, .sfd / Buildable: Yes" note above.)

### Actions taken
The misleading override `config.yaml` (which referenced a non-existent `NL.ufo`) was removed. The METADATA.pb `source` block was left unchanged as the historical record of the repository.

### Final state
The family is recorded as not reproducible: the upstream repository contains only FontForge `.sfd` masters and fragmentary test UFOs, with no gftools-builder-compatible source. No override `config.yaml` is provided.
