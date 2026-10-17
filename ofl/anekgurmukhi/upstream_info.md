# Anek Gurmukhi

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Confidence**: HIGH

## Designer

Ek Type

## Source Data

| Field | Value |
|---|---|
| repository_url | https://github.com/EkType/Anek |
| commit | `34074c6b406f4112e20c7ad10254a6e954d0324b` |
| config_yaml | `sources/AnekGurmukhi/builder.yaml` |
| branch | main |

## Repository URL Verification

The upstream repository URL `https://github.com/EkType/Anek` is confirmed correct:
- The cached repo at `EkType/Anek` has remote origin matching this URL.
- The copyright string in METADATA.pb references `https://github.com/EkType/Anek`.
- The google/fonts commit `315b62b7` (gftools-packager add) explicitly references this repo URL.

**Note**: This is a monorepo containing multiple Anek script variants (Gurmukhi, Devanagari, Bangla, etc.), each under `sources/Anek{Script}/`.

## Commit Verification

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` is verified:
- **Exists in repo**: Yes, confirmed.
- **Date**: 2022-02-14 (merge commit by Girish Dalvi).
- **Message**: "Merge pull request #3 from yanone/main" -- merging Yanone's contributions for fresh binaries and build fixes.
- **Is HEAD of main**: Yes, this is the latest commit on the main branch. No newer commits exist.
- **Cross-reference**: The google/fonts commit `315b62b70` from 2022-02-18 explicitly states: "Anek Gurmukhi Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b".
- **Timeline**: Upstream commit (2022-02-14) predates the google/fonts merge (2022-02-18) by 4 days, which is consistent.

The commit hash is correct with high confidence.

## Config Verification

The builder config at `sources/AnekGurmukhi/builder.yaml` exists at the referenced commit and contains:

```yaml
sources:
  - "Masters/AnekGurmukhi.designspace"
outputDir: "../../fonts/AnekGurmukhi"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

- The designspace file `sources/AnekGurmukhi/Masters/AnekGurmukhi.designspace` exists at the commit, along with 9 UFO masters covering the width/weight design space.
- The output directory `../../fonts/AnekGurmukhi` resolves to `fonts/AnekGurmukhi/` from the repo root.
- The binary `fonts/AnekGurmukhi/variable/AnekGurmukhi[wdth,wght].ttf` exists at the commit.
- No override `config.yaml` exists in the google/fonts family directory.

## Google Fonts History

| Commit | Date | Description |
|---|---|---|
| `315b62b70` | 2022-02-18 | [gftools-packager] Anek Gurmukhi: Version 1.003 added (#4278) |
| `28b492c0f` | 2022-05-04 | Clear languages from METADATA.pb for non-Noto |
| `c6307ba83` | 2022-05-05 | Roll back 28b492c0, then re-do in chunks (#4677) |
| `bc09b2c5c` | 2022-05-09 | Undo rollback, remove languages from METADATA (#4703) |
| `7902aa1d3` | 2023-04-07 | Add articles to various families (#5523) |
| `235532ac5` | 2023-05-15 | Apply requested article edits (#5710) |
| `66f91f10f` | 2025-09-11 | Merge upstream.yaml into METADATA.pb |
| `8b70d4c34` | 2025-09-22 | Primary scripts identified by review |
| `b2496ed68` | 2025-09-24 | sources info for Anek Gurmukhi: Version 1.003 (#4278) |

The font was initially added via PR #4278 on 2022-02-18 using gftools-packager. The source block was later added in commit `b2496ed68` (2025-09-24), which correctly references the original packager commit.

## Conclusion

All source metadata for Anek Gurmukhi is **complete and verified**:
- Repository URL is correct and points to the EkType/Anek monorepo.
- Commit hash matches the one explicitly referenced in the original gftools-packager onboarding commit, and is the latest (HEAD) commit on main.
- The builder.yaml config path is valid and contains a proper gftools-builder configuration with .designspace sources.
- No action needed.
