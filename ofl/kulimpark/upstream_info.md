# Kulim Park — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kulimpark`
**Status**: complete

## Initial State

METADATA.pb already contained a source block with:
- `repository_url`: `https://github.com/noponies/Kulim-Park`
- `commit`: `e080ee92d3f56075f641d0c988a480c0590a4426`
- No `config_yaml` field (override config.yaml present in google/fonts family directory)

The tracking file (`data/gfonts_library_sources.json`) listed this family as "complete" with `override_config: true` and `has_investigation_report: false`.

## Investigation

### Onboarding History

The font was onboarded to Google Fonts on 2019-09-25 by Yanone (Jan Gerner) in commit `7fe093689` with the message:

> kulimpark: v1.000 added
> Taken from the upstream repo https://github.com/noponies/Kulim-Park at commit https://github.com/noponies/Kulim-Park/commit/e080ee92d3f56075f641d0c988a480c0590a4426

This was submitted via PR #2181, authored by Yanone, with the body: "Dale has just merged my PR to his upstream repo." The PR was merged by Marc Foley on 2019-09-26.

### Upstream Repository

The upstream repo at `https://github.com/noponies/Kulim-Park` is cached at `upstream_repos/fontc_crater_cache/noponies/Kulim-Park/`. The repo is clean (no local modifications) and on branch `master`, up to date with origin.

The referenced commit `e080ee92d3f56075f641d0c988a480c0590a4426` is the HEAD of the repository — a merge commit from 2019-09-26 titled "Merge pull request #6 from yanone/master" with body "Updated for Google Fonts". This is the latest commit in the repo (58 total commits), meaning no additional upstream work has been done since onboarding.

### Sources

The upstream repo contains gftools-buildable sources at the referenced commit:
- `sources/kulim-park-master.glyphs`
- `sources/kulim-park-master-italic.glyphs`

The repo has a `build.sh` that uses `fontmake` to build from these `.glyphs` files, confirming the source structure. There is no `config.yaml` in the upstream repo.

### Override config.yaml

An override `config.yaml` exists in the google/fonts family directory (`ofl/kulimpark/config.yaml`), added in commit `c66c1f3b3` ("sources info for Kulim Park (PR #2181)") on 2025-10-24. The config contains:

```yaml
buildVariable: false
sources:
  - sources/kulim-park-master.glyphs
  - sources/kulim-park-master-italic.glyphs
```

This correctly references the two `.glyphs` source files and sets `buildVariable: false` since this is a static-only family (10 TTF files across 5 weights, each with roman and italic).

### Source Block Verification

The METADATA.pb source block has no `config_yaml` field, which is correct: when an override `config.yaml` exists in the google/fonts family directory, the `config_yaml` field should be omitted because `google-fonts-sources` auto-detects the local override.

### Commit Hash Verification

The commit hash `e080ee92d3f56075f641d0c988a480c0590a4426` was explicitly stated in the onboarding commit message by the onboarder (Yanone), who was also the person who contributed to the upstream repo (PR #6). The upstream merge happened on 2019-09-26, and the google/fonts PR was merged the same day. The commit is HEAD of the upstream repo with no subsequent changes. **Confidence: HIGH** — the hash is directly cited by the onboarder in the commit message and is the latest upstream commit.

## Actions Taken

No actions were needed. The source block, commit hash, and override config.yaml were all already in place and verified correct.

## Final State

| Field | Value |
|-------|-------|
| repository_url | `https://github.com/noponies/Kulim-Park` |
| commit | `e080ee92d3f56075f641d0c988a480c0590a4426` |
| config_yaml | (omitted — override `config.yaml` in google/fonts) |
| override config | Yes (`ofl/kulimpark/config.yaml`) |
| Status | complete |
| Confidence | HIGH |

## Source Block

```
source {
  repository_url: "https://github.com/noponies/Kulim-Park"
  commit: "e080ee92d3f56075f641d0c988a480c0590a4426"
}
```
