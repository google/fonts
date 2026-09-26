# Investigation Report: Lacquer

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete
**Confidence**: HIGH

## Summary

Lacquer is an expressive display font featuring heavy drips and dozens of alternate glyphs. It was hand drawn using a paint pen by Niki Polyocan and extrapolated and finished by Eli Block at Google Creative Lab. The upstream repository, commit hash, and override config.yaml were all verified as correct. The source metadata in METADATA.pb is complete.

## METADATA.pb Analysis

The METADATA.pb file at `ofl/lacquer/METADATA.pb` contained a source block with:
- `repository_url`: `https://github.com/Lacquer-Font/Lacquer`
- `commit`: `efffa0e54fbf2a6cd5e1b3909a9a8082cab61b5a`
- No `config_yaml` field (override config.yaml exists in the google/fonts family directory)

The `repository_url` was originally populated by Simon Cozens on 2023-08-15 in commit `f7455d78` ("Populate source.repository_url"). The `commit` field and override `config.yaml` were added by Felipe Sanches on 2025-10-24 in commit `eaf40e51` ("sources info for lacquer: v1.100 (PR #2054)").

## Upstream Repository

- **URL**: https://github.com/Lacquer-Font/Lacquer
- **Local cache**: `upstream_repos/fontc_crater_cache/Lacquer-Font/Lacquer/`
- **Default branch**: master
- **Repository status**: Clean, up to date with origin

The upstream repository had 10 commits total. The most recent commit was the merge commit `efffa0e` ("Merge pull request #1 from m4rc1e/gf-mastering"), dated 2019-07-16. This was also the HEAD of the repository, meaning no additional changes were made after the onboarding.

## Onboarding History

Lacquer was onboarded to Google Fonts via PR #2054, authored by Marc Foley. The timeline was:

1. **2019-07-02**: Marc Foley created commit `36ea768` ("README: drop rfn") in upstream PR #1 on the `m4rc1e/gf-mastering` branch. This was the tip of a 2-commit branch that added the build chain and mastered fonts (commit `3df9107`) plus a README fix.
2. **2019-07-04**: Marc Foley created the onboarding commit `b636f76` in google/fonts, with the message: "lacquer: v1.100 added. Taken from the upstream repo https://github.com/Lacquer-Font/Lacquer at commit https://github.com/Lacquer-Font/Lacquer/pull/1/commits/36ea768ba1cadd863a3a523cc0a6c02333662590"
3. **2019-07-08**: PR #2054 was merged into google/fonts (merge commit `61872e5`).
4. **2019-07-16**: Upstream PR #1 was merged (merge commit `efffa0e`), after the font was already in google/fonts.

The onboarding commit message explicitly referenced commit `36ea768` from upstream PR #1. The METADATA.pb uses the merge commit `efffa0e` instead, which is the HEAD of the repo. Since `36ea768` is an ancestor of `efffa0e` and the merge did not modify any files, both commits contain the identical font binary.

## Binary Verification

The SHA-256 hash of `Lacquer-Regular.ttf` was compared across all locations:
- google/fonts: `140c21f71907a16952926ee354c81081092c90d599c89fe8b4557baeaebbbe83`
- Upstream at `36ea768`: `140c21f71907a16952926ee354c81081092c90d599c89fe8b4557baeaebbbe83`
- Upstream at `efffa0e` (HEAD): `140c21f71907a16952926ee354c81081092c90d599c89fe8b4557baeaebbbe83`

All three matched exactly, confirming the font binary in google/fonts was taken from the upstream repository at the referenced commit.

## Build Configuration

The upstream repository did not have a `config.yaml` file. It had a `sources/build.sh` script that used `fontmake` directly to build from `sources/Lacquer.glyphs`. The source file is a Glyphs format file, which is compatible with gftools-builder.

An override `config.yaml` was created in the google/fonts family directory (`ofl/lacquer/config.yaml`) with the following content:

```yaml
buildVariable: false
sources:
  - sources/Lacquer.glyphs
```

This override config correctly references the Glyphs source file at `sources/Lacquer.glyphs` in the upstream repo root. Since the override config exists locally, the `config_yaml` field was correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

## Conclusion

The source metadata for Lacquer is complete and verified:
- **Repository URL**: Correct, points to the legitimate upstream repository
- **Commit hash**: `efffa0e` is the HEAD/merge commit of the upstream repo, containing the same binary as the explicitly referenced onboarding commit `36ea768`
- **Override config.yaml**: Present in google/fonts, correctly configured for gftools-builder
- **No further action required**
