# Investigation Report: Brawler

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Brawler |
| Designer | Cyreal |
| License | OFL |
| Date Added | 2011-05-18 |
| Repository URL | https://github.com/cyrealtype/Brawler |
| Commit Hash | `a8e1fc6a4c43dedc38394c4f4086f526b72e852d` |
| Branch | master |
| Config YAML | `sources/config.yaml` (in upstream) |
| Status | Complete |

## How URL Found

The repository URL `https://github.com/cyrealtype/Brawler` is recorded in the METADATA.pb `source {}` block and matches the copyright string. It was added to METADATA.pb during the gftools-packager update (PR #4230) by Yanone.

## How Commit Determined

The commit hash `a8e1fc6a4c43dedc38394c4f4086f526b72e852d` was ported from the fontc_crater targets list in google/fonts commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

**Important note about the original onboarding commit**: The gftools-packager commit for Version 1.101 (PR #4230, commit `d9b649cad`) referenced a different upstream commit: `628e7189feb4a17dc20059f9346356e63d531eda`. However, this commit no longer exists in the upstream repository. The upstream repo was apparently force-pushed/rewritten and now contains only a single commit (`a8e1fc6a...`), dated 2025-02-23, by Alexei Vanyashin with message "generated fonts v1.500".

The current METADATA.pb commit `a8e1fc6a...` is the only commit in the repo and represents the latest state. Since the original onboarding commit was lost due to repo rewriting, this is the best available reference.

## Config YAML Status

- `sources/config.yaml` exists in the upstream repository at the recorded commit
- It is correctly referenced in the METADATA.pb `config_yaml` field
- No override config.yaml exists in google/fonts

Config.yaml contents:
```yaml
sources:
  - Brawler.glyphs
outputDir: "../fonts"
buildStatic: true
buildVariable: true
buildTTF: true
buildOTF: true
buildWebfont: true
axisOrder:
  - wght
```

## Verification

1. **Commit exists in upstream**: Confirmed. `a8e1fc6a4c43dedc38394c4f4086f526b72e852d` is the sole commit in the cached repo at `upstream_repos/fontc_crater_cache/cyrealtype/Brawler`
2. **File paths match**: METADATA.pb references `fonts/TTF/Brawler-Regular.ttf` and `fonts/TTF/Brawler-Bold.ttf`, both present at the commit
3. **Config YAML valid**: `sources/config.yaml` exists and references `Brawler.glyphs` source
4. **Original commit lost**: The original gftools-packager commit `628e7189...` no longer exists in the repo (force-pushed)
5. **fontc_crater source**: The current commit was sourced from fontc_crater's targets.json

## Confidence Level

**MEDIUM** - The repository URL is correct. The commit hash is the only commit available in the repo after a force-push/rewrite, so it represents the current state rather than the original onboarding state. The original commit `628e7189...` was lost. The font version in google/fonts (1.101) predates the current repo state (v1.500), so the upstream has progressed significantly beyond what was onboarded.

## Open Questions

1. The upstream repo was force-pushed, losing the original onboarding commit history. The current commit represents v1.500 while google/fonts has v1.101 - are the binaries in google/fonts from a different source state?
2. The font in google/fonts (Regular + Bold only) differs from the upstream repo (Regular, Medium, SemiBold, Bold) - the upstream has expanded since onboarding.
