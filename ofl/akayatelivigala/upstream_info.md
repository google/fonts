# Akaya Telivigala

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Vaishnavi Murthy, Juan Luis Blanco
**METADATA.pb path**: `ofl/akayatelivigala/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/vaishnavimurthy/Akaya-Telivigala |
| Commit | `93b31e45b69178ecfdb48981a5aa8a8b33bb0340` |
| Config YAML | override config.yaml in google/fonts |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/vaishnavimurthy/Akaya-Telivigala` is recorded in the METADATA.pb `source {}` block and matches the copyright string in the font metadata. The cached upstream repo at `fontc_crater_cache/vaishnavimurthy/Akaya-Telivigala` has this URL as its git remote origin, confirming it is valid and accessible.

## How the Commit Hash Was Identified

The commit `93b31e45b69178ecfdb48981a5aa8a8b33bb0340` is explicitly referenced in the google/fonts onboarding commit `7b4021c0a` (PR #3355, merged 2021-04-30), which states:

> Akaya Telivigala Version 1.002; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/vaishnavimurthy/Akaya-Telivigala.git at commit https://github.com/vaishnavimurthy/Akaya-Telivigala/commit/93b31e45b69178ecfdb48981a5aa8a8b33bb0340.

This was a gftools-packager automated onboarding. The commit exists in the upstream repo and is the HEAD of the `master` branch. It is a merge commit dated 2021-04-29 ("Merge pull request #5 from yanone/master — Akaya-Telivigala v1.002 ready for Google Fonts"), which aligns with the google/fonts PR #3355 merge date of 2021-04-30. The binary file `TTF/AkayaTelivigala-Regular.ttf` produced by this commit (561,640 bytes) matches the file size in the google/fonts directory (561,640 bytes), further confirming this is the correct onboarding commit.

No subsequent commits exist in the upstream repo, so this is also the latest commit.

## How Config YAML Was Resolved

The upstream repository does not contain a `config.yaml` file. However, the source file `Source/AkayaTelivigala.glyphs` exists at the referenced commit, which is a gftools-builder-compatible source format.

An override `config.yaml` was created in the google/fonts family directory at `ofl/akayatelivigala/config.yaml` (added in commit `fa4a17cbf`, 2025-10-24). Its contents:

```yaml
buildVariable: false
sources:
  - Source/AkayaTelivigala.glyphs
```

This references the `.glyphs` source file relative to the upstream repo root. Since the override config exists locally in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block (google-fonts-sources auto-detects local overrides).

## Conclusion

The source metadata for Akaya Telivigala is **complete**. The repository URL is valid and confirmed by the gftools-packager onboarding message. The commit hash `93b31e4` is verified as the exact commit used during onboarding (PR #3355), with matching binary file sizes as corroborating evidence. The override `config.yaml` correctly points to the `.glyphs` source in the upstream repo. **Confidence: HIGH**.
