# Allkin

**Status**: `complete`
**Date**: 2026-02-25
**Designer**: Monotype Imaging Inc.
**License**: OFL
**METADATA.pb**: `ofl/allkin/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/allkin |
| Commit | `fffaa4201dfbd887a78e3d0c79654a7ad0d155f3` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field.

### Config YAML
Found `sources/config.yaml` in upstream repository at the recorded commit hash.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/googlefonts/allkin`
- `commit`: `fffaa4201dfbd887a78e3d0c79654a7ad0d155f3`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `b031b3c2e2ca`
- Date: 2026-01-29 17:10:27 +0100
- Subject: "Allkin: Version 1.010 added"

## Confidence

**High**: URL pre-existing in METADATA.pb; commit pre-existing in METADATA.pb

## Recent upstream/main activity (post-investigation)

Several commits between 2026-02-09 and 2026-02-20 made non-source-block edits to METADATA.pb. None of them touch the `source { ... }` block, so the `repository_url`, `commit`, `config_yaml`, and `branch` fields are unchanged from the original investigation.

### 2026-02-20: minisite URL corrections

- **2026-02-20** — Emma Marichal, commit [`0a62c3fdd`](https://github.com/google/fonts/commit/0a62c3fdd) ("Update minisite URL in METADATA.pb"): replaced `https://typetrends.monotype.com/fr/peace-conflict` with `https://www.monotype.com/type-trends/peace-conflict/` (host migration from `typetrends.monotype.com` to `www.monotype.com`).
- **2026-02-20** — Emma Marichal, commit [`dbc81e3cf`](https://github.com/google/fonts/commit/dbc81e3cf) ("Fix minisite URL in METADATA.pb — Updated minisite URL to remove trailing slash"): trimmed the trailing slash, leaving `https://www.monotype.com/type-trends/peace-conflict`.

### 2026-02-11: category change + sample-text padding adjustments

Four Emma Marichal commits on 2026-02-11 worked on family classification and sample-text padding. None affect glyphs or the source block:

- **2026-02-11** — commit [`ddd69eee5`](https://github.com/google/fonts/commit/ddd69eee5) ("Change font category and classifications to DISPLAY"): re-categorised the family — `category: "SANS_SERIF"` → `category: "DISPLAY"`, and `classifications: "SYMBOLS"` → `classifications: "DISPLAY"`.
- **2026-02-11** — commit [`dfaa39fce`](https://github.com/google/fonts/commit/dfaa39fce) ("Update styles and tester fields in METADATA.pb"): widened both `styles` and `tester` blank lengths (sample-text reference strings used by the Google Fonts catalog UI).
- **2026-02-11** — commit [`3c9cd4f9e`](https://github.com/google/fonts/commit/3c9cd4f9e) ("Update styles and tester fields in METADATA.pb"): re-balanced the lengths between `styles` and `tester`.
- **2026-02-11** — commit [`8f6e3f9df`](https://github.com/google/fonts/commit/8f6e3f9df) ("Update tester field in METADATA.pb"): shortened the `tester` blank length.

The three padding commits all landed within minutes of each other (PR-iteration tweaks). The final state of the fields after the last commit is what HEAD reflects today.

### 2026-02-09: tester field formatting

- **2026-02-09** — Emma Marichal, commit [`f6d35fe21`](https://github.com/google/fonts/commit/f6d35fe21) ("Fix tester field formatting in METADATA.pb"): corrected the formatting of the `tester` field (likely a quoting/whitespace fix in the protobuf text representation).
