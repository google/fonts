# Barrio

**Date investigated**: 2026-02-26
**Status**: complete (commit hash corrected)
**Designer**: Omnibus-Type
**METADATA.pb path**: `ofl/barrio/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Omnibus-Type/Barrio |
| Commit | 4cb00e50284f63512cce98d382b495955bde4e72 |
| **Config YAML** | Override in google/fonts |
| Branch | master |

## How the Repository URL Was Found
The METADATA.pb already contains `repository_url: "https://github.com/Omnibus-Type/Barrio"`. This matches the copyright "Copyright 2016 The Barrio Project Authors (omnibus.type@gmail.com)" and is confirmed by PR #491 which was authored by Marc Foley from Omnibus-Type content.

## How the Commit Hash Was Identified
The last commit to modify .ttf files in `ofl/barrio/` was `f10784f5c52eab5dff74c4aa970558da6c07df40` (2016-12-02, "barrio: v1.005 added (#491)"). PR #491 body says: "Another new addition from @Omnibus-Type."

Looking at the upstream repository commit history, commit `4cb00e50284f63512cce98d382b495955bde4e72` (2016-12-02, "fonts | sources: Removed non ascii characters from name table") was made by Marc Foley on the same day as the PR merge. This and the preceding commits on 2016-12-01 were all part of the onboarding preparation (restructuring, GF spec updates, copyright updates).

The previous tracking data incorrectly listed commit `ced3c1e` (2015-02-03, "Editing style"), which predates the onboarding work by over a year. The correct commit is `4cb00e5`, the last upstream commit before the google/fonts PR was merged.

## How Config YAML Was Resolved
No `config.yaml` exists in the upstream repository at any commit. No override `config.yaml` exists in the google/fonts `ofl/barrio/` directory. The sources at the onboarding commit are `sources/Barrio.glyphs` and `sources/Barrio.ufo/`.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2016-12-02
- Commit message: "fonts | sources: Removed non ascii characters from name table"
- Commit author: Marc Foley (m.foley.88@gmail.com)
- Source files at commit: `sources/Barrio.glyphs`, `sources/Barrio.ufo/`
- Fonts directory at commit: `Fonts/Barrio-Regular.ttf` (and other formats)

## Confidence
**High**: The commit date matches the PR merge date, and the commit was made by Marc Foley who also authored the google/fonts PR. The prior incorrect commit (`ced3c1e`) was clearly wrong as it predated the onboarding preparation by over a year.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Barrio.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions
- A config.yaml needs to be created for building Barrio from source.
- Note: The upstream repo was later restructured (around 2018) into `BarrioGF/` and `Barriecito/` subdirectories. The original Barrio sources were at the repo root in `sources/Barrio.glyphs` during onboarding, but are now in `BarrioGF/sources/Barrio.glyphs`.
