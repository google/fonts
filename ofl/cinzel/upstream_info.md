# Cinzel - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Cinzel |
| Designer | Natanael Gama |
| Repository URL | https://github.com/NDISCOVER/Cinzel |
| Commit Hash | `8271e162a7c6064ff1e539ba86011b16b6a6184f` |
| Config YAML | Override in google/fonts (`ofl/cinzel/config.yaml`) |
| Status | Complete |
| Date Added | 2012-10-24 |

## How URL Found

The repository URL `https://github.com/NDISCOVER/Cinzel` was already recorded in the METADATA.pb source block. NDISCOVER is Natanael Gama's GitHub organization. Note that the original onboarding PR #2566 referenced `https://github.com/TypeNetwork/Cinzel`, which is a fork. The NDISCOVER repo is the canonical upstream that includes the TypeNetwork work merged via pull request #3.

## How Commit Determined

PR #2566 ("cinzel: v2.000 added", by Marc Foley, 2020-07-22) explicitly states: "Taken from the upstream repo https://github.com/TypeNetwork/Cinzel at commit https://github.com/TypeNetwork/Cinzel/commit/7d1404e1291800023c9bd3cf0daa7252d0ba722d".

The commit `7d1404e` from TypeNetwork/Cinzel corresponds to the same commit in NDISCOVER/Cinzel (merged via PR #3). The recorded commit `8271e16` ("Tweak to accent placement for a future build") is one commit after `7d1404e` and was made the same day (2020-07-22). This appears to be a follow-up tweak that was included in the NDISCOVER repo's master branch at the time the source block was documented.

The commit graph shows:
```
dd59849 Merge pull request #3 from TypeNetwork/master
  8271e16 Tweak to accent placement for a future build  <-- recorded commit
    7d1404e Merge pull request #6 from TypeNetwork/update-vf  <-- PR #2566 referenced commit
```

The recorded commit `8271e16` is the most accurate representation of the source state used, as it is one commit ahead of the onboarding commit with a minor accent tweak, and sits on the NDISCOVER/Cinzel master branch.

## Config YAML Status

- **No config.yaml in upstream**: The NDISCOVER/Cinzel repository does not contain a config.yaml file at any commit.
- **Override config.yaml exists**: An override `config.yaml` is present in `ofl/cinzel/config.yaml` in the google/fonts repository.

Override config.yaml contents:
```yaml
buildVariable: true
sources:
  - sources/Cinzel.designspace
```

The source path `sources/Cinzel.designspace` is confirmed to exist at the recorded commit `8271e16`.

## Verification

- Commit hash `8271e16` verified to exist in NDISCOVER/Cinzel repo
- Source file `sources/Cinzel.designspace` confirmed present at the recorded commit
- PR #2566 explicitly documents the upstream repo and commit used for onboarding
- Override config.yaml correctly references the designspace source
- The variable font `Cinzel[wght].ttf` in google/fonts matches this being a variable font build

## Confidence Level

**High** - PR #2566 provides explicit documentation of the upstream source. The recorded commit `8271e16` is one commit ahead of the PR-referenced commit `7d1404e`, which is a minor discrepancy but the overall data is well-documented.

## Open Questions

- The recorded commit `8271e16` is one commit after the PR-referenced `7d1404e`. Since `8271e16` says "Tweak to accent placement for a future build", it's unclear if the actual binary in google/fonts was built from `7d1404e` or `8271e16`. However, since the METADATA.pb records `8271e16` as the canonical reference, this is acceptable.
