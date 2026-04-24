# Ranga — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [antonxheight/Ranga](https://github.com/antonxheight/Ranga) |
| Commit | `15fadcc52c43bfbe15915c530b2409f8bcf244e4` |
| Binary Date | 2017-05-09 |
| Source Types | .sfd |
| Buildable | No |
| Confidence | High (canonical designer repo) |

## Notes

Source repository for ranga. Commit determined by date correlation with the last binary modification in google/fonts (2017-05-09).

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/ranga/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `15fadcc52c`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.
