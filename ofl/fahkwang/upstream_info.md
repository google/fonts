# Investigation Report: Fahkwang

## Summary

| Field | Value |
|---|---|
| **Family Name** | Fahkwang |
| **Designer** | Cadson Demak |
| **License** | OFL |
| **Category** | Sans Serif |
| **Primary Script** | Thai |
| **Date Added** | 2018-08-22 |
| **Repository URL** | https://github.com/cadsondemak/Fah-Kwang |
| **Commit** | `7b16186dadf959e79ded967a7620bfb05600fcaf` |
| **Config** | Override config.yaml in google/fonts |
| **Status** | Complete |
| **Confidence** | HIGH |

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/cadsondemak/Fah-Kwang"
  commit: "7b16186dadf959e79ded967a7620bfb05600fcaf"
}
```

The `config_yaml` field is intentionally omitted because an override `config.yaml` exists in the google/fonts family directory.

## Repository Analysis

### Upstream Repository: cadsondemak/Fah-Kwang

- **Remote URL**: https://github.com/cadsondemak/Fah-Kwang
- **Default branch**: master
- **Repo status**: Clean, up to date with origin
- **Source files**: `source/Fahkwang.glyphs` (single Glyphs source)
- **No config.yaml in upstream repo**: The upstream repo does not contain a gftools-builder `config.yaml`

### Font Files in google/fonts

12 static TTF files (6 weights x 2 styles):
- Fahkwang-ExtraLight.ttf, Fahkwang-ExtraLightItalic.ttf (weight 200)
- Fahkwang-Light.ttf, Fahkwang-LightItalic.ttf (weight 300)
- Fahkwang-Regular.ttf, Fahkwang-Italic.ttf (weight 400)
- Fahkwang-Medium.ttf, Fahkwang-MediumItalic.ttf (weight 500)
- Fahkwang-SemiBold.ttf, Fahkwang-SemiBoldItalic.ttf (weight 600)
- Fahkwang-Bold.ttf, Fahkwang-BoldItalic.ttf (weight 700)

## Onboarding History

### Initial onboarding: PR #1657

- **PR**: https://github.com/google/fonts/pull/1657
- **Author**: Marc Foley (m4rc1e)
- **Merged by**: Rod Sheeter (rsheeter)
- **Merged**: 2018-09-10

The PR contained three commits modifying `ofl/fahkwang/`:

1. **`a9695abb` (2018-08-22)** -- "fahkwang: v1.000 added"
   - Commit message: "Taken from the upstream repo https://github.com/cadsondemak/Fah-Kwang at commit https://github.com/cadsondemak/Fah-Kwang/commit/9024b9fc1094b68c90bc4cfab7086232619bc341"
   - This was the initial add, taken from upstream commit `9024b9f` (Merge PR #5 from m4rc1e/gf-mastering, 2018-08-22)

2. **`c83e68fb` (2018-08-24)** -- "fahkwang: Updated fonts to avoid clipping."
   - Commit message: "Taken from the upstream repo https://github.com/cadsondemak/fah-kwang at commit https://github.com/cadsondemak/fah-kwang/commit/7b16186dadf959e79ded967a7620bfb05600fcaf"
   - Updated to upstream commit `7b16186` (Merge PR #6 from m4rc1e/metrics, 2018-08-24) which fixed vertical metrics clipping

3. **`df66d8a0` (2018-09-07)** -- "fahkwang: unhinted fonts."
   - No upstream commit reference; "In the future, we plan to release this family as an unhinted variable font."
   - This was a local recompilation by Marc Foley to produce unhinted versions, significantly reducing file sizes (e.g., Regular from 122,888 to 88,168 bytes)

### Commit Hash Verification

The commit hash `7b16186dadf959e79ded967a7620bfb05600fcaf` in METADATA.pb corresponds to the second commit in the onboarding sequence. This is the correct reference because:

1. The original onboarding started with upstream commit `9024b9f` (merge of PR #5, "gf-mastering")
2. Marc Foley then made an additional upstream fix for vertical metrics in PR #6, which was merged as `7b16186`
3. The second google/fonts commit (`c83e68fb`) explicitly references `7b16186` as the source
4. The third commit (`df66d8a0`) was a local unhinting operation that did not change the source -- it just recompiled with different build settings

Therefore `7b16186` represents the last upstream commit whose source changes were incorporated into google/fonts. The unhinting was a build-time modification, not a source change.

### Post-Onboarding Upstream Activity

Two commits exist in the upstream repo after `7b16186`, both from October 2024:
- `9948992` (2024-10-04) -- "Fix t caron" (recompiled fonts, changed binary sizes)
- `d68a0d8` (2024-10-04) -- "Update Fahkwang.glyphs" (removed 6 lines from source)

These changes have NOT been incorporated into google/fonts and would need separate review/QA if desired.

## Override config.yaml

An override `config.yaml` exists in `ofl/fahkwang/config.yaml` in google/fonts:

```yaml
buildVariable: false
sources:
  - source/Fahkwang.glyphs
```

This was added in commit `5da715e0` (2025-11-10) by Felipe Sanches. The config references `source/Fahkwang.glyphs`, which exists at the referenced upstream commit `7b16186`. The `buildVariable: false` flag is appropriate since the family was onboarded as static instances (12 individual TTF files).

## Previous Source Metadata Work

Commit `5da715e0` (2025-11-10, by Felipe Sanches) added both the commit hash to METADATA.pb and the override config.yaml. The repository_url was previously populated by commit `f7455d788` ("Populate source.repository_url").

## Designer Information

Fahkwang was designed by **Cadson Demak**, a Thai type foundry. The primary contributors in the upstream repo are:
- **Suppakit** (suppakit@katatrad.com / suppakit.cadsondemak@gmail.com) -- primary designer
- **Pongsatorn81** -- contributor (GitHub page, text updates)
- **Marc Foley** (m4rc1e) -- Google Fonts engineer who handled onboarding, fontbakery fixes, and metrics corrections

## Conclusion

This family's source metadata is **complete**. The repository URL, commit hash, and override config.yaml are all correctly set. The commit hash `7b16186` accurately represents the last upstream source state used for the fonts in google/fonts (with the subsequent unhinting being a build-time change only). No further action is needed.
