# Miltonian Tattoo — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [impallari/Miltonian](https://github.com/impallari/Miltonian) |
| Commit | `95d180e8744380f93a8437226e58032d484882c7` |
| Date | 2016-01-15 |
| Confidence | High |

## Investigation

The METADATA.pb for Miltonian Tattoo had no source block. The upstream repository is impallari/Miltonian, which is a shared repository containing both Miltonian and Miltonian Tattoo sources.

### Source Types Available

- **VFB** (FontLab): `source/MiltonianTattoo-Regular.vfb`, `source/MiltonianTattoo-Regular-OTF.vfb`, `source/MiltonianTattoo-Regular-TTF.vfb`
- **Binary fonts**: `fonts/TTF/MiltonianTattoo-Regular-TTF.ttf`, `fonts/OTF/MiltonianTattoo-Regular.otf`

### Buildability

VFB-only editable sources (FontLab Studio proprietary format). No `.glyphs`, `.ufo`, or `.designspace` files are present. Not directly buildable with gftools-builder.

### Notes

- Same repository as Miltonian (impallari/Miltonian contains both families)
- The designer Pablo Impallari passed away in 2021; the repo is unlikely to receive further updates
- Commit `95d180e` (2016-01-15, "v1.7") is the latest content commit, matching the google/fonts update (2016-01-25)
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `95d180e` at impallari/Miltonian.

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/miltoniantattoo/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `95d180e874`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.
