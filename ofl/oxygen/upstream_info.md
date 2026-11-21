# Oxygen — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [vernnobile/oxygenFont](https://github.com/vernnobile/oxygenFont) |
| Commit | `62db0ebe3488c936406685485071a54e3d18473b` |
| Binary Date | 2017-05-08 |
| Source Types | .ufo, .sfd |
| Buildable | Yes |
| Confidence | High (canonical designer repo) |

## Notes

Source repository for oxygen. Commit determined by date correlation with the last binary modification in google/fonts (2017-05-08).

## Build Configuration (Override)

An override `config.yaml` had been created in the google/fonts family directory referencing `Oxygen-Regular.ufo`. See the fontc_crater fix below — that override has since been removed because the referenced file does not exist.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: [Oxygen-Regular.ufo]`. fontc_crater failed with `missing source 'Oxygen-Regular.ufo'`.

### Investigation
The recorded commit `62db0ebe` is valid (master HEAD, 2014-02-13), but no file named `Oxygen-Regular.ufo` exists at any commit. The repo is a legacy FontForge-era project with an irregular nested layout. The only Oxygen Sans UFOs present are `OxygenSans-version-0.4/Regular-400/src/OxygenSans-Regular.ufo` and `OxygenSans-version-0.4/Bold-700/src/OxygenSans-Bold.ufo`. There is no UFO for the Light weight at all — Light exists only as a FontForge `.sfd`. The shipped three-static family (Light/Regular/Bold) therefore cannot be reproduced from this repo. (This corrects the "Source Types: .ufo, .sfd / Buildable: Yes" note above.)

### Actions taken
The misleading override `config.yaml` (which referenced a non-existent `Oxygen-Regular.ufo`) was removed. The METADATA.pb `source` block was left unchanged as the historical record.

### Final state
The family is recorded as not reproducible: the upstream repository provides no complete, gftools-builder-compatible source set — the shipped Light weight has no UFO source, and the remaining sources are nested partial UFOs and FontForge `.sfd` files. No override `config.yaml` is provided.
