# Alike Angular

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Sveta Sebyakina, Cyreal
**METADATA.pb path**: `ofl/alikeangular/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/cyrealtype/Alike-Angular |
| Commit | `20765691758ef999907b9a20950d4f57f62de1d1` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/cyrealtype/Alike-Angular` was already present in the METADATA.pb `source` block. It was originally added by Emma Marichal in commit `ba0196b6` on 2023-11-02 via gftools-packager, which explicitly referenced the upstream repo in its commit message. The URL matches the copyright notice in the font metadata.

## How the Commit Hash Was Identified

The commit hash `20765691758ef999907b9a20950d4f57f62de1d1` was set by the gftools-packager commit `ba0196b6` in google/fonts, which states:

> Alike Angular Version 1.300; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/cyrealtype/Alike-Angular at commit https://github.com/cyrealtype/Alike-Angular/commit/20765691758ef999907b9a20950d4f57f62de1d1.

**Verification**:
- The upstream repo has only one commit on the `main` branch (this merge commit), so there is no ambiguity about which commit was used.
- The `main` branch HEAD points directly to `2076569`.
- The binary TTF at `fonts/ttf/AlikeAngular-Regular.ttf` in the upstream repo at this commit has SHA256 `3706438e11bb219d6dbbb19958b637dc19470638da28fd97a620f7d7069bf448`, which matches the file in google/fonts exactly.
- The upstream commit is dated 2023-11-02, and the google/fonts packager commit is also dated 2023-11-02, consistent with same-day onboarding.

## How Config YAML Was Resolved

The `config_yaml` field is set to `sources/config.yaml` in METADATA.pb. This file exists in the upstream repo at the referenced commit and contains:

```yaml
sources:
    - AlikeAngular.glyphs
familyName: Alike Angular
```

This is a valid gftools-builder configuration pointing to the `.glyphs` source file at `sources/AlikeAngular.glyphs`. The `config_yaml` field was added by the "Batch 1/4" commit (`19cdcec5`) which ported info from the fontc_crater targets list. No override config.yaml exists in the google/fonts family directory.

## Conclusion

This family's source metadata is fully complete and verified with HIGH confidence. The repository URL, commit hash, branch, and config_yaml are all correct. The binary font file in google/fonts is an exact byte-for-byte match with the file from the upstream repo at the referenced commit. The upstream repo contains gftools-builder compatible sources (`.glyphs` file) with a proper `config.yaml`.
