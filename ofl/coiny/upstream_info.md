# Coiny - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Coiny |
| Designer | Marcelo Magalhaes |
| Repository URL | https://github.com/marcelommp/Coiny |
| Commit Hash | 0341b95f0c79f0e0b33ab7b5404cf9265be88516 |
| Branch | gh-pages |
| Config YAML | N/A (override config.yaml in google/fonts) |
| Override Config | Yes |
| Status | complete |

## How URL Was Found

The repository URL `https://github.com/marcelommp/Coiny` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") on January 14, 2024. The repository is owned by Marcelo Magalhaes (marcelommp), who is credited as the designer in the METADATA.pb.

## How Commit Was Determined

The commit `0341b95f0c79f0e0b33ab7b5404cf9265be88516` (dated October 3, 2016) is the HEAD of the `gh-pages` branch, which is the default (and only) branch in the repository. The commit message is "Adjustments in Horn and others accents plus Tamil".

The font was last updated in google/fonts via PR #1091 ("coiny: v1.001 added") by Marc Foley on August 7, 2017, which fixed issue #334. The PR only updated the TTF binary. Since the commit `0341b95f` is the latest commit in the upstream repo (from October 2016, before the PR merge), this was the state of the repo at the time of onboarding.

The source block was added in commit `2cca1f64a` ("sources info for Coiny: v1.001 (PR #1091)") which is on main.

## Config YAML Status

**Override config.yaml exists** in google/fonts at `ofl/coiny/config.yaml`:

```yaml
buildVariable: false
sources:
  - UFO/Coiny-Regular.ufo
```

The upstream repository contains:
- `UFO/Coiny-Regular.ufo` - the primary source file
- Various other files (FontForge files, concept sketches, specimens)
- No config.yaml in the upstream repo

The override config.yaml correctly references the UFO source at the path where it exists in the upstream repository.

## Verification

- **Repository accessible**: Yes, https://github.com/marcelommp/Coiny is accessible
- **Commit exists**: Yes, `0341b95f` is the HEAD of gh-pages
- **Branch correct**: Yes, gh-pages is the only branch
- **Source block on main**: Yes, the full source block (repository_url + commit + branch) is on main
- **Override config exists**: Yes, at `ofl/coiny/config.yaml`
- **Config references correct files**: Yes, `UFO/Coiny-Regular.ufo` exists at the recorded commit

## Confidence Level

**High**. The repository URL, commit hash, and branch are all correct and verified. The designer's repository contains the expected UFO source file, and an override config.yaml is already in place referencing it correctly.

## Open Questions

None. This family is complete.
