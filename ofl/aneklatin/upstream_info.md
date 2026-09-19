# Anek Latin

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Confidence**: HIGH
- **Designer**: Ek Type

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/EkType/Anek |
| Commit | `34074c6b406f4112e20c7ad10254a6e954d0324b` |
| Config YAML | `sources/AnekLatin/builder.yaml` |
| Branch | main |

## Repository URL Verification

The repository URL `https://github.com/EkType/Anek` is confirmed valid. The cached clone at `EkType/Anek` has the matching remote origin. This is a multi-script Anek project by Ek Type containing sources for Anek Latin along with Bangla, Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Odia, Tamil, and Telugu variants.

## Commit Verification

The commit `34074c6b406f4112e20c7ad10254a6e954d0324b` is verified to exist in the upstream repository. It is a merge commit dated 2022-02-14 with the message "Merge pull request #3 from yanone/main — Anek 1.003, revised". This is the latest commit on the main branch (HEAD).

**Cross-verification with google/fonts onboarding:**
- The google/fonts onboarding commit `ba4334505` (2022-02-18) by Yanone explicitly references this exact upstream commit in its message: "Anek Latin Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit ...34074c6b...".
- The binary font file at the upstream commit (`fonts/AnekLatin/variable/AnekLatin[wdth,wght].ttf`) is exactly 404,880 bytes, matching the file in `ofl/aneklatin/` in google/fonts (also 404,880 bytes).
- The upstream commit (Feb 14, 2022) predates the google/fonts merge (Feb 18, 2022) by 4 days.
- No additional upstream commits exist after this hash, confirming it is the correct and final onboarding commit.

## Config Verification

The builder config at `sources/AnekLatin/builder.yaml` exists at the referenced commit with the following content:

```yaml
sources:
  - "Masters/AnekLatin.designspace"
outputDir: "../../fonts/AnekLatin"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

This is a valid gftools-builder configuration pointing to a `.designspace` source file. No override config.yaml exists in the google/fonts family directory; the upstream config is used directly.

## google/fonts Commit History

| Commit | Date | Description |
|--------|------|-------------|
| `ba4334505` | 2022-02-18 | [gftools-packager] Anek Latin: Version 1.003 added (#4280) — initial onboarding by Yanone |
| `28b492c0f` | — | Clear languages from METADATA.pb for non-Noto |
| `c6307ba83` | — | Roll back 28b492c0, then re-do in chunks (#4677) |
| `bc09b2c5c` | — | Undo rollback, remove languages from METADATA (#4703) |
| `7902aa1d3` | — | Add articles to various families (#5523) |
| `235532ac5` | — | Apply requested article edits (#5710) |
| `66f91f10f` | — | Merge upstream.yaml into METADATA.pb |
| `58a753c7f` | 2025-09-24 | sources info for Anek Latin: Version 1.003 (#4280) — added source block |

The font binary has not been updated since the initial onboarding.

## Conclusion

The source metadata for Anek Latin is **complete and correct**. All three fields (repository_url, commit, config_yaml) are present and verified:
- The repository URL points to the correct upstream project.
- The commit hash matches the exact commit used during onboarding, confirmed by the gftools-packager message, matching binary file sizes, and timeline consistency.
- The builder.yaml path is valid and contains a proper gftools-builder configuration.

No changes are needed.
