# Molengo — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [moyogo/molengo-fonts](https://github.com/moyogo/molengo-fonts) |
| Commit | `9e390dcfd861f8774bc5ae369732a66861a2dc4a` |
| Binary Date | 2015-03-07 |
| Source Types | .sfd |
| Buildable | No |
| Confidence | High (canonical designer repo) |

## Notes

Source repository for molengo. Commit determined by date correlation with the last binary modification in google/fonts (2015-03-07).

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/molengo/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `9e390dcfd8`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.
