# Chakra Petch

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Cadson Demak
**METADATA.pb path**: `ofl/chakrapetch/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/m4rc1e/Chakra-Petch |
| Commit | `6176529d05acf654f31e024daad77966319e499d` |
| Config YAML | N/A (override config.yaml in google/fonts) |
| Branch | N/A |

## How the Repository URL Was Found

The METADATA.pb `source { repository_url }` field points to `https://github.com/m4rc1e/Chakra-Petch`. This is Marc Foley's fork of the original `cadsondemak/Chakra-Petch` repository. The copyright string in the font files references `https://github.com/m4rc1e/Chakra-Petch.git`.

The original onboarding commit `bf577ca0d` (2018-08-22, "chakrapetch: v1.000 added") referenced the original upstream `https://github.com/cadsondemak/Chakra-Petch` at commit `57f0d77c`. However, subsequent updates were done from Marc Foley's fork, and the METADATA.pb now correctly references the fork as the working upstream.

## How the Commit Hash Was Identified

The commit `6176529d05acf654f31e024daad77966319e499d` was identified by correlating the google/fonts update history with the upstream repository.

The font update timeline in google/fonts:
1. `bf577ca0d` (2018-08-22): "chakrapetch: v1.000 added" -- initial onboarding from `cadsondemak/Chakra-Petch` at commit `57f0d77c`
2. `61b8e020a` (2018-08-24): "chakrapetch: Updated fonts to avoid clipping" -- from `cadsondemak/Chakra-Petch` at commit `3fc2b8f9` (merge of m4rc1e's metrics PR)
3. `c011968d8` (2018-09-07): "chakrapetch: unhinted fonts" -- final update, no upstream commit referenced in message

The tracked commit `6176529d` (2018-08-23, "Updated vertical metrics to stop first line clipping") is the actual fix commit in m4rc1e's fork that was merged into cadsondemak via PR #10 (merge commit `3fc2b8f9`). The final unhinted font update (`c011968d8`) was built from the same source state since `6176529d` is the latest non-merge commit before the unhinting work. This commit was likely recorded in the fontc_crater targets list.

The commit `6176529d` exists in both `m4rc1e/Chakra-Petch` and `cadsondemak/Chakra-Petch` repositories (it is part of the shared git history).

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. However, an **override `config.yaml`** exists in the google/fonts family directory at `google/fonts/ofl/chakrapetch/config.yaml` with the following content:

```yaml
sources:
  - source/Chakra Petch.glyphs
```

Since the override config.yaml exists locally, the `config_yaml` field can be omitted from the METADATA.pb `source { }` block. The google-fonts-sources tool will automatically detect the local override.

## Verification

- Repository URL accessible: Yes (both `m4rc1e/Chakra-Petch` and `cadsondemak/Chakra-Petch`)
- Commit exists in upstream repo: Yes
- Commit date: 2018-08-23 14:08:52 +0100
- Commit message: "Updated vertical metrics to stop first line clipping"
- Source files at commit: `source/Chakra Petch.glyphs` (Glyphs format)
- `m4rc1e/Chakra-Petch` is a fork of `cadsondemak/Chakra-Petch`

## Confidence

**High**: The repository URL and commit hash are well-established. The font was onboarded by Marc Foley who also maintains the fork. The commit `6176529d` represents the last source change before the unhinted fonts were built. The override config.yaml in google/fonts correctly references the Glyphs source file.

## Open Questions

1. The METADATA.pb `source { repository_url }` points to `m4rc1e/Chakra-Petch` (a fork) rather than the original `cadsondemak/Chakra-Petch`. Since the original designer's repo (Cadson Demak) is the canonical source and the commit exists in both repos, it may be more appropriate to point to `cadsondemak/Chakra-Petch`. However, the current setup works and the fork was the working repo for the mastering engineer.
