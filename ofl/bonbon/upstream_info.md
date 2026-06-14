# Bonbon

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Cyreal
**METADATA.pb path**: `ofl/bonbon/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/cyrealtype/Bonbon |
| Commit | `ffac6513dd512d2a76e620c933e6d9a6f0953348` |
| Config YAML | Override in google/fonts (`ofl/bonbon/config.yaml`) |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL `https://github.com/cyrealtype/Bonbon` was added to METADATA.pb by Simon Cozens in commit `46a7c0576` ("Add more upstreams (a,b)", 2024-01-14). The Cyreal type foundry maintains this and other font repos under the `cyrealtype` GitHub organization. The URL was already established in the source block before the commit hash was added.

## How the Commit Hash Was Identified

The commit hash `ffac6513dd512d2a76e620c933e6d9a6f0953348` was added to METADATA.pb by Felipe Sanches in commit `be2c6db21` ("sources info for Bonbon: Version 1.001 (PR #862)", 2025-11-10).

The upstream repository has only two commits:
1. `3e70567` - "initial commit"
2. `ffac651` - "adding img" (HEAD)

The recorded commit `ffac651` is the latest (and essentially the only meaningful) commit in the repository. The font was originally updated in google/fonts via PR #862 ("hotfix-bonbon: v1.001 added") by Marc Foley (2017-08-07). Since the upstream repo only has 2 commits, `ffac651` (HEAD) is the correct reference.

## How Config YAML Was Resolved

There is no `config.yaml` in the upstream repository. The upstream contains only legacy VFB (FontLab) source files in `src/`:
- `Bonbon-Regular.vfb`
- `Bonbon-Regular-TTF.vfb`
- `Bonbon-Regular-OTF.vfb`

An override `config.yaml` exists in the google/fonts family directory at `ofl/bonbon/config.yaml`:

```yaml
buildVariable: false
sources:
  - src/Bonbon-Regular.vfb
  - src/Bonbon-Regular-TTF.vfb
  - src/Bonbon-Regular-OTF.vfb
```

Since an override config exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes (HEAD of master/main)
- Commit date: "adding img"
- Source files at commit: `src/Bonbon-Regular.vfb`, `src/Bonbon-Regular-TTF.vfb`, `src/Bonbon-Regular-OTF.vfb`, `Bonbon-Regular.ttf`
- Override config.yaml in google/fonts: Yes (`ofl/bonbon/config.yaml`)
- No config.yaml in upstream repo: Confirmed

## Confidence

**High**: The repository URL is well-established under the Cyreal type foundry's GitHub organization. The commit hash is the latest commit in a very small repo (only 2 commits), making it unambiguous. The override config.yaml in google/fonts handles the build configuration since the upstream has only legacy VFB sources.

## Open Questions

1. The override config.yaml references VFB sources. Can gftools-builder actually compile VFB files, or is this config for reference purposes only? If not buildable, the font may need to be rebuilt from a converted source format.
