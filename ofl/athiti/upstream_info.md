# Athiti

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Cadson Demak
**METADATA.pb path**: `ofl/athiti/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/cadsondemak/athiti |
| Commit | `541c0b5034964f8db50ef52921fede1422194abe` |
| Config YAML | override in google/fonts |
| Branch | --- |

## How the Repository URL Was Found

The repository URL `https://github.com/cadsondemak/athiti` was already present in the METADATA.pb source block. It was added by the commit "Add more upstreams (a,b)" (`46a7c0576`), which was part of a batch upstream URL addition effort. Cadson Demak is a well-known Thai type foundry, and this is their official GitHub repository for the Athiti font family.

## How the Commit Hash Was Identified

The commit hash `541c0b5034964f8db50ef52921fede1422194abe` was added to METADATA.pb by commit `29ce2921d` ("sources info for Athiti: v1.033 (PR #999)"), dated 2025-11-19. The PR #999 in google/fonts was titled "hotfix-athiti: v1.033 added" (created by user `m4rc1e`, merged 2017-05-23). The PR body references issue #271, indicating it was part of an effort to add families back to the repository.

The upstream commit (dated 2015-11-30) has the message "source and font files updated. fix nikahit and tone marks problem." This is the latest commit in the upstream repository at the time of the font's last update in google/fonts, and version v1.033 corresponds to this commit.

## How Config YAML Was Resolved

There is no `config.yaml` in the upstream repository. However, an override `config.yaml` exists at `google/fonts/ofl/athiti/config.yaml`. This override specifies:

```yaml
buildVariable: false
sources:
  - source/Athiti-200.glyphs
  - source/Athiti-300.glyphs
  - source/Athiti-400.glyphs
  - source/Athiti-500.glyphs
  - source/Athiti-600.glyphs
  - source/Athiti-700.glyphs
```

The upstream repo has 6 `.glyphs` source files (one per weight) plus corresponding `.ufo` directories, which are compatible with gftools-builder through this override config.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2015-11-30 10:58:32 +0700
- Commit message: "source and font files updated. fix nikahit and tone marks problem."
- Source files at commit: `source/Athiti-200.glyphs`, `source/Athiti-300.glyphs`, `source/Athiti-400.glyphs`, `source/Athiti-500.glyphs`, `source/Athiti-600.glyphs`, `source/Athiti-700.glyphs`, plus UFO directories for each weight

## Confidence

**High**: The repository URL is from the official Cadson Demak GitHub organization. The commit hash matches the version (v1.033) referenced in the google/fonts onboarding PR #999. The override config.yaml correctly references the .glyphs source files present at the commit. The font was added by Marc Foley (m4rc1e), a known Google Fonts team member.

## Open Questions

None
