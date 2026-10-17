# Strichpunkt Sans

**Status**: `complete`
**Date**: 2026-04-27
**Designer**: René Bieder
**License**: OFL
**METADATA.pb**: `ofl/strichpunktsans/METADATA.pb`
**Model**: Claude Opus 4.7 (1M context)

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/strichpunkt-design/Strichpunkt_Sans |
| Commit | `9a24fe35f229db9d86724550255429a86a9bb308` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field. Verified to be the canonical upstream: the repo is owned by `strichpunkt-design`, the GitHub org of the German design and branding agency Strichpunkt (Stuttgart/Berlin/Hamburg/Basel), and the repo description is "Open source variable brand font family by Strichpunkt Design". The README credits René Bieder as the designer, matching METADATA.pb.

### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field. Verified to exist upstream as the merge commit of `strichpunkt-design/Strichpunkt_Sans#7` "Add Strichpunkt Sans" (merged 2026-03-27, author emmamarichal) — the same person who onboarded the family in google/fonts.

### Config YAML
Found `sources/config.yaml` in the upstream repository at the recorded commit. It uses `recipeProvider: googlefonts` over `StrichpunktSans.glyphs` and produces `StrichpunktSans[wdth,wght].ttf` plus weight-only subspace variants (standard/Wide/Exp). No override needed in google/fonts.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/strichpunkt-design/Strichpunkt_Sans`
- `commit`: `9a24fe35f229db9d86724550255429a86a9bb308`
- `branch`: `main`
- `config_yaml`: `sources/config.yaml` (added 2026-04-27 by this commit)
- `files`: `OFL.txt` → `OFL.txt`, `fonts/variable/StrichpunktSans[wdth,wght].ttf` → `StrichpunktSans[wdth,wght].ttf`

### Font binary verification
`StrichpunktSans[wdth,wght].ttf` head/name tables:
- `fontRevision`: 1.0
- `head.created`: 2026-01-26 15:01:20
- `head.modified`: 2026-03-26 16:51:09
- `name[5]` Version: `Version 1.000`
- `name[3]` Unique ID: `1.000;RENE;StrichpunktSans-Regular`
- `name[8]` Manufacturer: `Studio Rene Bieder`
- `name[11]` Vendor URL: `https://www.renebieder.com`

The build modification date (2026-03-26) is one day prior to the upstream PR merge (2026-03-27), consistent with the binaries being committed to upstream by the merge, and four days before the google/fonts onboarding (2026-04-01). Designer string matches.

### google/fonts history
- Onboarding commit: `e4391053f` "Strichpunkt Sans: Version 1.000 added" (Emma Marichal, 2026-04-01) — added METADATA.pb, OFL.txt, the variable TTF, and stub article via `gftools-packager`.
- Followups same day: `d17d28369` "Add article", `73d69bea3` "Add images", `4a067470d` "Update OFL.txt".
- Onboarding PR: [google/fonts#10402](https://github.com/google/fonts/pull/10402) (branch `gftools_packager_ofl_strichpunktsans`, merged 2026-04-02). The packager commit message references the exact upstream commit `9a24fe35f...`.

### Upstream repo archive
Not yet mirrored in `/home/fsanches/compartilhado/upstream_repos/repo_archive/strichpunkt-design/`. Recommended to mirror when disk space permits (currently 21 GB free, near the 15 GB threshold).

## Initial state
- METADATA.pb already had a `source { ... }` block with `repository_url`, `commit`, `branch=main`, and `files` mappings (added by gftools-packager in `e4391053f`).
- No `upstream_info.md` existed.
- `config_yaml` field not set in METADATA.pb.

## Actions taken
- Verified the upstream repository is canonical and owned by Strichpunkt Design (designer René Bieder).
- Confirmed commit `9a24fe35f` exists upstream as the merge commit of upstream PR #7 (merged 2026-03-27).
- Confirmed `sources/config.yaml` exists at that commit with a googlefonts recipe over `StrichpunktSans.glyphs`.
- Cross-checked font binary head/name tables: version 1.000, modified 2026-03-26, designer "Studio Rene Bieder" — consistent with the recorded commit.
- Cross-checked onboarding PR #10402 description against the recorded commit hash — match.
- Added `config_yaml: "sources/config.yaml"` to the METADATA.pb source block (the upstream config exists at the recorded commit and is fully functional; explicit field aids tooling).
- Authored this `upstream_info.md`.

## Final state
- `upstream_info.md` present with full provenance.
- METADATA.pb source block has `config_yaml: "sources/config.yaml"` set.
- No override `config.yaml` needed.

## Onboarding
The family was onboarded to google/fonts in PR [#10402](https://github.com/google/fonts/pull/10402) by Emma Marichal on 2026-04-01 via `gftools-packager`, which produced the initial commit `e4391053f` referencing upstream commit `9a24fe35f229db9d86724550255429a86a9bb308`. The PR also included follow-up commits adding the article (`d17d28369`), uploading article images (`73d69bea3`), and an `OFL.txt` correction (`4a067470d`). The `4a067470d` "Update OFL.txt" commit on 2026-04-01 fixed a 1-line discrepancy in the OFL header (the copyright/repo URL).

## Confidence
**High**: Upstream URL verified canonical; commit verified to exist upstream and to predate the google/fonts merge; binary version, designer, and dates align with the recorded commit; onboarding PR description corroborates the commit hash.
