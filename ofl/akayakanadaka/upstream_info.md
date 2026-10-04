# Akaya Kanadaka

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Vaishnavi Murthy, Juan Luis Blanco
**METADATA.pb path**: `ofl/akayakanadaka/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/vaishnavimurthy/Akaya-Kanadaka |
| Commit | `24f25461789ee8642e184b43dd6d5d04ea7f49d1` |
| Config YAML | override config.yaml in google/fonts |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/vaishnavimurthy/Akaya-Kanadaka` was already present in the METADATA.pb `source` block. It is also referenced in the font's copyright string and in the onboarding PR (#2970) commit message, which explicitly states:

> "taken from the upstream repo https://github.com/vaishnavimurthy/Akaya-Kanadaka.git"

The cached clone at `fontc_crater_cache/vaishnavimurthy/Akaya-Kanadaka` has its remote set to the same URL, confirming consistency.

## How the Commit Hash Was Identified

The METADATA.pb records commit `24f2546`. The onboarding PR #2970 (merged 2021-01-27) references a different commit: `72bdbc541ee3311e0eadafc80d7f097d1d8080a9`. Investigation reveals these are closely related:

- **`24f2546`** (2021-01-21): "Enabled fsSelection bit 7 (Use Typo Metrics)" - authored by Yanone, modifying `Source/AkayaKanadaka.glyphs` and `TTF/AkayaKanadaka-Regular.ttf`
- **`72bdbc5`** (2021-01-21): Merge commit of PR #14 from yanone/master, which merges `24f2546` into the main line

The merge commit `72bdbc5` is the merge of the branch containing `24f2546`. Both commits contain the exact same TTF binary (MD5: `4dab5a2b9cad2a474cf065e04f74fb44`), and this matches the TTF in google/fonts.

Using `24f2546` (the actual content commit) instead of `72bdbc5` (the merge commit) is a reasonable choice -- both point to the same file state. The gftools-packager referenced the merge commit, but the METADATA.pb was later enriched (commit `68d9071a3`, 2025-10-24) with the content commit hash `24f2546`.

**Timeline**:
1. PR #2956 (first attempt, 2021-01-15) referenced upstream commit `7f161bd` (merge of PR #13)
2. PR #2970 (final onboarding, 2021-01-27) referenced upstream commit `72bdbc5` (merge of PR #14, which includes `24f2546`)
3. After onboarding, only one upstream commit followed: `fef8598` (2021-04-29, "Update README.md") -- a non-font change

The commit hash `24f2546` correctly identifies the state of the source files used for onboarding. Confidence is HIGH.

## How Config YAML Was Resolved

The upstream repository has never contained a `config.yaml` file (verified across all commits and branches). The source file is a Glyphs file at `Source/AkayaKanadaka.glyphs`, which is gftools-builder compatible.

An override `config.yaml` was created in the google/fonts family directory at `ofl/akayakanadaka/config.yaml` (added in commit `68d9071a3`, 2025-10-24) with content:

```yaml
buildVariable: false
sources:
  - Source/AkayaKanadaka.glyphs
```

This correctly references the Glyphs source file in the upstream repo. Since the override exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb `source` block (google-fonts-sources auto-detects local overrides).

## Conclusion

The source metadata for Akaya Kanadaka is **complete**. The repository URL is confirmed, the commit hash `24f2546` correctly identifies the source state used for onboarding (identical binary at both the content commit and the merge commit referenced by gftools-packager), and the override config.yaml properly points to the Glyphs source. No further action needed.

**Confidence**: HIGH
