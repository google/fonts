# Investigation Report: Big Shoulders Inline Display SC

- **Family Name**: Big Shoulders Inline Display SC
- **Slug**: bigshouldersinlinedisplaysc
- **Designer**: Patric King
- **Status**: complete
- **Confidence**: HIGH
- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6

## METADATA.pb Source Block (existing)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "0b3d09a86862b19efae28eae0cd868f17c476b20"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders-Inline/fonts/variable/display/BigShouldersInlineDisplaySC[wght].ttf"
    dest_file: "BigShouldersInlineDisplaySC[wght].ttf"
  }
  branch: "master"
}
```

## Repository

- **URL**: https://github.com/xotypeco/big_shoulders
- **Cached at**: upstream_repos/fontc_crater_cache/xotypeco/big_shoulders
- **Branch**: master
- **Repository verified**: Yes, remote URL matched and repo was accessible.

## Commit Verification

- **Referenced commit**: `0b3d09a86862b19efae28eae0cd868f17c476b20`
- **Commit message**: "regenerate font files"
- **Commit date**: 2024-02-26
- **Commit found in repo**: Yes

### Timeline Cross-Reference

The onboarding was performed by Simon Cozens via PR #7786 (`google/gftools_packager_ofl_bigshouldersinlinedisplaysc`), merged on 2024-06-25. The initial commit in google/fonts (`ab4f392c8`) was dated 2024-05-30 and explicitly stated: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit 0b3d09a86862b19efae28eae0cd868f17c476b20."

Commit `0b3d09a` was the HEAD of the `master` branch at the time the PR was created. The next upstream commits did not appear until January 2025, well after the google/fonts merge in June 2024. The commit hash was confirmed to be correct for the onboarding.

## Source Files

At commit `0b3d09a`, the upstream repo contained:

- **Source**: `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs`
- **Upstream config**: `Big-Shoulders-Inline/sources/config.yml` (basic gftools-builder config for the full 2-axis VF)

The upstream `config.yml` built the full 2-axis (`opsz`, `wght`) Big Shoulders Inline variable font. It did NOT handle subspacing for the Display-only variant or the small caps (SC) remapping needed for this family.

## Config YAML

An override `config.yaml` existed in the google/fonts family directory at `ofl/bigshouldersinlinedisplaysc/config.yaml`. This override was included in the original onboarding commit by Simon Cozens.

The override config.yaml performed the following operations:
1. Built the variable font from `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs`
2. Subspaced the `opsz` axis to `72` (Display only)
3. Applied `remapLayout` to convert `smcp` (small caps) features to `ccmp`, creating the SC variant
4. Renamed the family to "Big Shoulders Inline Display SC"

Since the override `config.yaml` existed in the google/fonts family directory, no `config_yaml` field was needed in METADATA.pb (google-fonts-sources auto-detects local overrides).

### Note on files entries

The METADATA.pb `files` block referenced `Big-Shoulders-Inline/fonts/variable/display/BigShouldersInlineDisplaySC[wght].ttf` as a source file, but this file did not exist in the upstream repository at the referenced commit. The SC variant was entirely produced by the override config.yaml's build process. The pre-built binary in the upstream repo was `BigShouldersInlineDisplay[wght].ttf` (without "SC"). This was part of the convention used during onboarding for families with override configs.

## google/fonts History

| Commit | Date | Message |
|--------|------|---------|
| `ab4f392c8` | 2024-05-30 | Big Shoulders Inline Display SC: Version 2.002 added |
| `3806b5243` | 2024-05-30 | Add SC line to description |
| `ffa7805f7` | 2024-06-25 | Update DESCRIPTION.en_us.html |
| `b7f7489f0` | 2024-06-25 | Update OFL.txt |

All changes were merged via PR #7786 on 2024-06-25.

## Conclusion

The source metadata for Big Shoulders Inline Display SC was **complete and correct**. The repository URL, commit hash, and override config.yaml were all present and verified. The commit `0b3d09a` was confirmed as the HEAD of upstream `master` at the time of onboarding, with no subsequent upstream changes until well after the google/fonts merge. The override config.yaml correctly handled the specialized build process (subspacing + small caps remapping) that the upstream config did not support. No changes were needed.
