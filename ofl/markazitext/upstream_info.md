# Markazi Text — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/BornaIz/markazitext"
  commit: "a876c4f0111b96f407741a877e79f207e9117338"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

The upstream repository is at https://github.com/BornaIz/markazitext, created on 2017-03-24, with the default branch `master`. The repository was cloned in the local cache.

The repository contains:
- **Source file**: `sources/MarkaziText.glyphs` (Glyphs format)
- **Build configuration**: `sources/config.yaml` (gftools-builder compatible)
- **Build system**: `Makefile` using `gftools builder sources/config.yaml`
- **CI**: `.github/workflows/build.yaml` (GitHub Actions for building and testing)
- **Compiled fonts**: `fonts/` directory with `otf/`, `ttf/`, `variable/`, and `webfonts/` subdirectories

The `config.yaml` defines:
- Source: `MarkaziText.glyphs`
- Axis order: `wght`
- Family name: `Markazi Text`
- STAT table configuration for the `MarkaziText[wght].ttf` output

The repository has 37 total commits. The history shows it was initially set up by Marc Foley (m4rc1e) in early 2018, with contributions from Borna Izadpanah (the original designer) and later significant work by Aaron Bell (aaronbell) in 2021 to convert to the UFR (Universal Font Repository) format.

### Key Contributors

- **Borna Izadpanah** (BornaIz) — original designer, repository owner
- **Marc Foley** (m4rc1e) — initial setup, fontmake rebuilds, onboarding to google/fonts
- **Aaron Bell** (aaronbell) — UFR conversion in 2021, maintained a fork at https://github.com/aaronbell/markazitext
- **Florian Runge** — Latin complement designer
- **Fiona Ross** — credited designer

## Onboarding History

### Initial Onboarding (2018)

- **PR #1594**: "markazitext: v1.000 added." — Merged 2018-06-06 by Marc Foley
- PR body stated: "Taken from the upstream repo, https://github.com/BornaIz/markazitext"
- Initial file was `MarkaziText-Roman-VF.ttf`
- The font existed in google/fonts at the time alongside a beta version in `ofl/markazitextvfbeta/`

### VF Rename (2019)

- **PR #2216**: "Canonical names" — Merged 2019-11-18 by Thomas Linard
- Renamed variable font files to follow canonical naming conventions

### v1.001 Update (2021) — Last Binary Update

- **PR #3644**: "Markazi Text v1.001 (stat fix)" — Merged 2021-08-10 by Aaron Bell
- PR body: "Font repro updated to the UFR format (https://github.com/aaronbell/markazitext). PR'd to upstream. Font files rebuilt."
- Aaron Bell worked on his fork (`aaronbell/markazitext`) from 2021-07-06 to 2021-07-22
- His last commit was `51bb67c` ("Rebuilding static instances with autohinting", 2021-07-22)
- The binary in google/fonts was updated from 218,808 bytes to 296,896 bytes
- This is the commit that produced the currently-serving binary

### Post-Update History in Upstream

After the google/fonts PR #3644 was merged (2021-08-10), the following happened in BornaIz/markazitext:
- `d816f8f` (2021-08-27): Merge of aaronbell's PR #15 into BornaIz's master
- `d04484a` (2022-12-14): "Support for Crimean Tatar" — new glyphs/features NOT in google/fonts
- `ccc1945` (2022-12-14): "Shadda connection Issue fixed!" — NOT in google/fonts
- `a876c4f` (2024-10-27): "Arabic diacritics fix – Shadda with other marks did not work properly" — NOT in google/fonts

### Source Block Addition

- `6392e4f` (2023-12-14): Simon Cozens added `repository_url` in "Update upstreams"
- `4ad8ac6` (2025-03-31): Batch 2/4 added `commit` and `config_yaml` from fontc_crater targets.json

## Build Configuration

The `sources/config.yaml` file was introduced by Aaron Bell's UFR conversion (commit `38c03b2`, 2021-07-06) and was present at all subsequent commits. The config is gftools-builder compatible and was identical across all relevant commits.

The `config_yaml` path `sources/config.yaml` in METADATA.pb is correct.

## Findings

### Critical Issue: Wrong Commit Hash

The commit `a876c4f0111b96f407741a877e79f207e9117338` referenced in METADATA.pb is the HEAD of the upstream repository as of October 2024. It was sourced from fontc_crater's `targets.json`, which recorded the latest commit at the time fontc_crater was last updated — NOT the commit that was used to build the font binary currently in google/fonts.

The binary in google/fonts was last updated via PR #3644 (merged 2021-08-10), which used Aaron Bell's fork. The relevant commit is `51bb67c` ("Rebuilding static instances with autohinting", 2021-07-22) on the aaronbell/markazitext fork. This same commit exists in BornaIz/markazitext as it was merged via PR #15 (`d816f8f`, 2021-08-27).

After the binary was added to google/fonts, THREE additional commits were made to the upstream source file `MarkaziText.glyphs`:
1. `d04484a` — Support for Crimean Tatar (2022-12-14)
2. `ccc1945` — Shadda connection Issue fixed (2022-12-14)
3. `a876c4f` — Arabic diacritics fix (2024-10-27)

These changes have NOT been incorporated into the google/fonts binary and would need separate review and QA before inclusion.

### Correct Commit

The correct commit hash for the currently-serving binary is **`51bb67cce0bb3609f8318077ab0f74b93d365007`**. This commit:
- Was authored by Aaron Bell on 2021-07-22
- Was the HEAD of both aaronbell/markazitext and (after merge) BornaIz/markazitext at the time PR #3644 was submitted
- Predates the google/fonts merge date (2021-08-10)
- Contains the config.yaml at `sources/config.yaml`

## Recommended Source Block

```
source {
  repository_url: "https://github.com/BornaIz/markazitext"
  commit: "51bb67cce0bb3609f8318077ab0f74b93d365007"
  config_yaml: "sources/config.yaml"
}
```

**Changes from current**:
- `commit`: Changed from `a876c4f0111b96f407741a877e79f207e9117338` (latest HEAD, Oct 2024) to `51bb67cce0bb3609f8318077ab0f74b93d365007` (actual commit used for the binary, Jul 2021)

**Note**: The upstream repo has 3 newer commits modifying the source file that have not been incorporated into google/fonts. These would need to go through a separate review and QA process before being onboarded.
