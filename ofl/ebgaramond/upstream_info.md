# EB Garamond

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Georg Duffner, Octavio Pardo
**METADATA.pb path**: `ofl/ebgaramond/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/octaviopardo/EBGaramond12 |
| Commit | `e608414f52e532b68e2182f96b4ce9db35335593` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/octaviopardo/EBGaramond12` was already present in the METADATA.pb `source { repository_url }` field. It was initially added by Simon Cozens in the "Update upstreams" commit (`cd5db6b6e`, 2023-12-14), which added a source block with only the repository_url. The commit hash and config_yaml were later added by Felipe Sanches in the "[Batch 1/4] port info from fontc_crater targets list" commit (`19cdcec59`, 2025-03-31).

The copyright string in the font files also confirms this repository: "Copyright 2017 The EB Garamond Project Authors (https://github.com/octaviopardo/EBGaramond12)".

Note: EB Garamond has a complex history. The original EB Garamond was created by Georg Duffner (hosted at `github.com/georgd/EB-Garamond`). Octavio Pardo created EBGaramond12 as a redesign/successor of the original, and it is EBGaramond12 that is currently served through Google Fonts.

## How the Commit Hash Was Identified

The commit hash `e608414f52e532b68e2182f96b4ce9db35335593` was ported from the fontc_crater targets list. This is the HEAD commit on the `master` branch of the upstream repository -- a merge commit "Merge pull request #40 from aaronbell/master" dated 2021-09-29.

### Verification of the Commit Hash

The font has gone through several updates in google/fonts:

1. **v1.000 static (2017-10-31)**: Marc Foley added static fonts (commit `62e0ebd5d`, PR #1287) from the upstream repo.

2. **v1.000 VF (2019-10-30)**: Marc Foley added variable fonts (commit `8d96f2bad`, PR #1881). The commit message explicitly references upstream commit `cbc4c4e7fa4031cb9c900e67bf5cb7f86e591986` ("VF build chain added", 2019-03-15) from PR #25 on the upstream repo.

3. **v1.001 stat fix (2021-09-24)**: Aaron Bell updated the variable fonts with STAT table fixes (commit `177c41e76`, PR #3633). The PR body states: "Rebuilding of variable fonts and static instances from the UFR structure (https://github.com/aaronbell/EBGaramond12). PR'd to upstream." Aaron did the work on his fork, submitted it to google/fonts, and then it was merged upstream via PR #40 on 2021-09-29.

The timeline is:
- **2021-06-22 to 2021-07-22**: Aaron Bell made commits on his fork (STAT table, UFR conversion, autohinting rebuild)
- **2021-09-24**: google/fonts PR #3633 merged (fonts built from Aaron's work)
- **2021-09-29**: Upstream PR #40 merged by octaviopardo (commit `e608414f`)

Since `e608414f` is the merge of Aaron's work into the upstream master, and it contains identical source files to the pre-merge commit `f1a73968` (no file differences between them), this commit hash is correct for representing the state of sources used to build the fonts currently in google/fonts. The merge happened 5 days after google/fonts merged, but the content is identical.

## Build Configuration

The `config.yaml` at `sources/config.yaml` in the upstream repository is a valid gftools-builder configuration. It specifies:
- Sources: `EBGaramond.glyphs` and `EBGaramond-Italic.glyphs`
- Axis order: `wght`, `ital`
- Family name: "EB Garamond"
- STAT table configuration for weight and italic axes
- `autohintTTF: False` (added in the autohinting rebuild commit)

The config.yaml was introduced in the UFR format conversion (commit `78b4eb2a`, 2021-06-23) and slightly updated in the autohinting rebuild (commit `f1a73968`, 2021-07-22, which added `autohintTTF: False`).

No local override config.yaml exists in the google/fonts family directory.

## Source Files

The upstream repository contains Glyphs format sources:
- `sources/EBGaramond.glyphs` (Roman)
- `sources/EBGaramond-Italic.glyphs` (Italic)

These produce two variable font files:
- `EBGaramond[wght].ttf` (weight axis: 400-800)
- `EBGaramond-Italic[wght].ttf` (weight axis: 400-800)

## Timeline

- **2011-03-23**: EB Garamond added to Google Fonts catalog (date_added in METADATA.pb)
- **2017-10-31**: Static fonts v1.000 added by Marc Foley (commit `62e0ebd5d`, PR #1287) from octaviopardo/EBGaramond12
- **2019-10-30**: Variable fonts v1.000 added by Marc Foley (commit `8d96f2bad`, PR #1881) from upstream commit `cbc4c4e7`
- **2021-09-24**: v1.001 stat fix by Aaron Bell (commit `177c41e76`, PR #3633) -- UFR rebuild with STAT table
- **2021-09-29**: Aaron's work merged upstream via PR #40 (commit `e608414f` = current METADATA.pb hash)
- **2023-12-14**: Source block (repository_url only) added by Simon Cozens (commit `cd5db6b6e`)
- **2024-01-18**: Broken merge of METADATA fixed by Simon Cozens (commit `e0845b367`)
- **2025-03-31**: Commit hash and config_yaml added from fontc_crater targets by Felipe Sanches (commit `19cdcec59`)

## Issues Found

None. The source block in METADATA.pb is complete and accurate:
- Repository URL correctly points to `octaviopardo/EBGaramond12`
- Commit hash `e608414f` is the HEAD of master and correctly represents the state of sources used for the current fonts in google/fonts
- Config YAML path `sources/config.yaml` exists at the referenced commit and is a valid gftools-builder configuration
- The upstream repository is clean and up-to-date
