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

Several commits between 2026-02-11 and 2026-02-20 made non-source-block edits to METADATA.pb. None of them touch the `source { ... }` block, so the `repository_url`, `commit`, `config_yaml`, and `branch` fields are unchanged from the original investigation.

### 2026-02-20: minisite URL corrections

- **2026-02-20** — Emma Marichal, commit [`0a62c3fdd`](https://github.com/google/fonts/commit/0a62c3fdd) ("Update minisite URL in METADATA.pb"): replaced `https://typetrends.monotype.com/fr/peace-conflict` with `https://www.monotype.com/type-trends/peace-conflict/` (host migration from `typetrends.monotype.com` to `www.monotype.com`).
- **2026-02-20** — Emma Marichal, commit [`dbc81e3cf`](https://github.com/google/fonts/commit/dbc81e3cf) ("Fix minisite URL in METADATA.pb — Updated minisite URL to remove trailing slash"): trimmed the trailing slash, leaving `https://www.monotype.com/type-trends/peace-conflict`.

### 2026-02-11: sample-text padding adjustments

Three Emma Marichal commits on 2026-02-11 tweaked the whitespace-padded `styles` and `tester` sample-text fields (used by the Google Fonts catalog UI for sentence-length reference strings). None of these changes affect glyphs or the source block:

- **2026-02-11** — commit [`dfaa39fce`](https://github.com/google/fonts/commit/dfaa39fce) ("Update styles and tester fields in METADATA.pb"): widened both `styles` and `tester` blank lengths.
- **2026-02-11** — commit [`3c9cd4f9e`](https://github.com/google/fonts/commit/3c9cd4f9e) ("Update styles and tester fields in METADATA.pb"): re-balanced the lengths between `styles` and `tester`.
- **2026-02-11** — commit [`8f6e3f9df`](https://github.com/google/fonts/commit/8f6e3f9df) ("Update tester field in METADATA.pb"): shortened the `tester` blank length.

These three commits all landed within minutes of each other (PR-iteration tweaks). The final state of the fields after the third commit is what HEAD reflects today.
