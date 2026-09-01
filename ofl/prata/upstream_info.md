# Prata — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [cyrealtype/Prata](https://github.com/cyrealtype/Prata) |
| Commit | `db5f3799a47eb51bbfe0cb572986d26b37f8ec9e` |
| Binary Date | 2017-01-16 |
| Source Types | .glyphs |
| Buildable | Yes |
| Confidence | High (canonical designer repo) |

## Notes

Source repository for prata. Commit determined by date correlation with the last binary modification in google/fonts (2017-01-16).

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing `Prata.glyphs (from upstream sources/config.yaml)` from `cyrealtype/Prata`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.

## Correction (2026-05-28) — override config source path

**Model**: Claude Opus 4.8

fontc_crater reported `missing source 'sources/Prata.glyphs'` for this family. Inspection of the upstream tree at the pinned build commit `db5f3799` (tag v.2.000) showed the Glyphs source is named **`sources/Prata_Regular.glyphs`**, not `sources/Prata.glyphs`. The bare `sources/Prata.glyphs` name only appeared later, in 2023 (commit `68f0c02`, "regenned fonts 2.010"), which renamed `Prata_Regular.glyphs` → `Prata.glyphs` — long after the binary shipped (2017-01-16).

The override `config.yaml` source path was therefore corrected from `sources/Prata.glyphs` to `sources/Prata_Regular.glyphs`. The pinned commit is unchanged and remains correct. Verified: `git -C <Prata> ls-tree db5f3799 -- sources/` lists `sources/Prata_Regular.glyphs` and no `sources/Prata.glyphs`.
