# Doto

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Oliver Lalan
**METADATA.pb path**: `ofl/doto/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/oliverlalan/Doto |
| Commit | `1c587f2eed62cb257055540ac2a15f356070414f` |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field: `https://github.com/oliverlalan/Doto`. This URL is also confirmed by the font copyright string in METADATA.pb: "Copyright 2024-2024 The Doto Project Authors (https://github.com/oliverlalan/Doto)". The onboarding commit `2c982e6bd` in google/fonts explicitly states: "Taken from the upstream repo https://github.com/oliverlalan/Doto at commit https://github.com/oliverlalan/Doto/commit/1c587f2eed62cb257055540ac2a15f356070414f." The remote URL in the cached repo confirms the same address.

## How the Commit Hash Was Identified

The commit hash `1c587f2eed62cb257055540ac2a15f356070414f` was pre-existing in the METADATA.pb `source { commit }` field. It was also explicitly referenced in the onboarding commit message (`2c982e6bd` in google/fonts, authored by Emma Marichal on 2024-10-09).

**Note on PR body discrepancy**: The google/fonts PR #8212 body text references a different commit: `f46a14819db0a833967774625e0f22edd2bf5319`. However, examining the commit object `1c587f2` reveals it is a merge commit with two parents:
- `f46a148` (first parent, the initial repo state)
- `b5569f2` (second parent, Emma Marichal's v-metrics update from upstream PR #5)

The upstream PR #5 ("Update v-metrics") was merged on 2024-10-06 to center uppercase letterforms by adjusting typoAscender/typoDescender from 900/-300 to 950/-250. Emma Marichal opened the PR in the upstream repo, the designer merged it, and then Emma used the post-merge commit (`1c587f2`) for the google/fonts onboarding. This explains the discrepancy: the PR #8212 body was written referencing the earlier state (`f46a148`), but the actual METADATA.pb and onboarding commit correctly reference the final merged state (`1c587f2`).

The upstream repo has only this single merge commit as its entire visible history (prior commits appear to have been squashed or the repo was initialized fresh with a merge).

## How Config YAML Was Resolved

The upstream repo contains a `config.yaml` at `sources/config.yaml`. This matches the `config_yaml: "sources/config.yaml"` field in METADATA.pb. Its contents:

```yaml
sources:
  - Doto.designspace
axisOrder:
  - ROND
  - wght
buildOTF: false
```

The config references `Doto.designspace` in the same `sources/` directory, which defines a 2-axis variable font (ROND: Roundness 0-100, wght: Weight 100-900) using four UFO masters:
- `Doto-ThinSquare.ufo`
- `Doto-BlackSquare.ufo`
- `Doto-ThinRound.ufo`
- `Doto-BlackRound.ufo`

No override `config.yaml` exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is also HEAD of the `main` branch)
- Commit date: 2024-10-07 04:01:26 +0700
- Commit message: "Merge pull request #5 from emmamarichal/main - Update v-metrics"
- Binary file verification: SHA-256 hash of `Doto[ROND,wght].ttf` matches exactly between google/fonts (`ofl/doto/`) and the upstream repo (`fonts/variable/`): `6f4fe7d37853b91df3698daa84cde2dbe1c9695d88c986e6510134910337d426`
- Source files at commit: `sources/Doto.designspace`, four UFO masters, `sources/config.yaml`
- Onboarding PR: google/fonts PR #8212, merged 2024-10-15 by Emma Marichal

## Confidence

**High**: All data points are fully consistent. The repository URL is confirmed by METADATA.pb, the font copyright string, and the onboarding commit message. The commit hash is verified present in the upstream repo and matches the binary files exactly (identical SHA-256). The config.yaml path is correct and points to a valid gftools-builder configuration. The discrepancy between the PR body commit reference (`f46a148`) and the METADATA.pb commit (`1c587f2`) is explained by Emma Marichal's v-metrics fix being merged into the upstream repo between PR creation and font onboarding.

## Open Questions

None. This family is fully documented with consistent evidence across METADATA.pb, google/fonts commit history, binary file verification, and the upstream repository.
