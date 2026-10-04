# Bai Jamjuree

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Cadson Demak
**METADATA.pb path**: `ofl/baijamjuree/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/cadsondemak/Bai-Jamjuree |
| Commit | `e35cafdf694905d1ac0f27afc587c0e972be1260` |
| Config YAML | Override in google/fonts (`ofl/baijamjuree/config.yaml`) |
| Branch | master (inferred) |

## How the Repository URL Was Found

The repository URL appears in multiple places:
1. The METADATA.pb `source {}` block (added by Simon Cozens in commit `5f2b22f48` on 2023-12-14)
2. The copyright string: "Copyright 2018 Bai Jamjuree (https://github.com/cadsondemak/Bai-Jamjuree)"
3. The original onboarding commit `f27b6e87a` (2018-08-24): "Taken from the upstream repo https://github.com/cadsondemak/Bai-Jamjuree"

## How the Commit Hash Was Identified

The original onboarding commit `f27b6e87a` (2018-08-24) explicitly states: "at commit https://github.com/cadsondemak/Bai-Jamjuree/commit/e35cafdf694905d1ac0f27afc587c0e972be1260"

This upstream commit `e35cafd` (2018-08-23) is a merge of PR #9 from m4rc1e with the message "Merge pull request #9 from m4rc1e/fonts". The PR chain includes:
- `44cb51a` "Generated fonts"
- `39d30d7` "Adjusted vertical metrics to reduce first line clipping"

A second TTF update happened on 2018-09-07 (commit `8192d5fe3` "baijamjuree: unhinted fonts.") with the note "In the future, we plan to release this family as an unhinted variable font." This commit does not reference a different upstream commit. Between `e35cafd` (2018-08-23) and the TTF update (2018-09-07), no new upstream commits were made (the next upstream commits were on 2018-10-08). Therefore, the unhinted fonts were derived from the same upstream commit `e35cafd`.

A third entry in the TTF history (`76adaf1d2` "deploy" on 2021-11-01) actually deleted the files (0 bytes) as part of a deploy operation, but the files were re-added. The current binaries match the 2018-09-07 update.

## How Config YAML Was Resolved

No config.yaml or builder.yaml exists in the upstream repository. An override config.yaml was created in the google/fonts family directory as part of the config_yaml enrichment effort (commit `5ddf312e6`).

The override config.yaml at `google/fonts/ofl/baijamjuree/config.yaml` contains:

```yaml
sources:
  - source/Baijam.glyphs
```

This correctly references the source file `source/Baijam.glyphs` found in the upstream repository.

Since an override config.yaml exists in the google/fonts family directory, the `config_yaml` field can be omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## Verification

- Commit exists in upstream repo: Yes (full clone available)
- Commit date: 2018-08-23 18:14:52 +0700
- Commit message: "Merge pull request #9 from m4rc1e/fonts"
- Source files at commit: `source/Baijam.glyphs`

## Confidence

**High**: The original google/fonts onboarding commit explicitly references upstream commit `e35cafd`. No upstream changes occurred between this commit and the subsequent TTF update. The override config.yaml correctly points to the source file. The METADATA.pb source block only has `repository_url` (no commit or branch), but the tracking file and override config provide the complete picture.

## Open Questions

1. The METADATA.pb source block is minimal (only `repository_url`). A PR could add the commit hash and branch, though since the override config.yaml handles the build configuration, the config_yaml field should be omitted per project policy.
