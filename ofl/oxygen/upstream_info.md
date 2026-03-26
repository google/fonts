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

An override `config.yaml` has been created in the google/fonts family directory, referencing `Oxygen-Regular.ufo` from `vernnobile/oxygenFont`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.
