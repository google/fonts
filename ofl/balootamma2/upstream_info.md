# Baloo Tamma 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Ek Type

## Source Data

| Field            | Value                                                        |
|------------------|--------------------------------------------------------------|
| repository_url   | https://github.com/yanone/Baloo2-Variable                    |
| commit           | da523dfa21aa0e376253d61c21e39146dc55702a                     |
| config_yaml      | builder/BalooTamma2.yaml                                     |
| branch           | master                                                       |

## Repository URL

The METADATA.pb `repository_url` field pointed to `https://github.com/yanone/Baloo2-Variable`. The cached clone at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable` confirmed the remote matched. This repository was maintained by Yanone (font engineer) with initial commits from girish-dalvi (Ek Type). The copyright notice in the font referenced the original source project at `https://github.com/EkType/Baloo2`.

## Commit Verification

The referenced commit `da523dfa21aa0e376253d61c21e39146dc55702a` existed in the upstream repository. It was dated 2021-10-28 and had the message "Update BalooTammudu2[wght].ttf" (it updated the Tammudu variant, not Tamma). The last commit that updated `BalooTamma2[wght].ttf` was `f98386c` (2021-10-28, "Update BalooTamma2[wght].ttf"), which was two commits before `da523df`.

Binary verification confirmed the font file was identical across all three locations:
- `google/fonts/ofl/balootamma2/BalooTamma2[wght].ttf`
- Upstream at commit `f98386c:fonts/variable/BalooTamma2[wght].ttf`
- Upstream at commit `da523df:fonts/variable/BalooTamma2[wght].ttf`

All three had SHA256 `364e7b33fafe3f94eb121b4db36423e1b0fbef278af0b1a8d3643c65567b9d3c`.

The commit `da523df` did not modify BalooTamma2 itself, but the BalooTamma2 font binary was already present and unchanged at that commit. The gftools-packager used the whole repository state at `da523df` (which was the tip of a batch of font updates Yanone pushed on 2021-10-28), and this was explicitly recorded in PR #3984's body and commit message. The google/fonts merge occurred on 2021-10-29, one day after the upstream commit.

## Config Verification

The config file `builder/BalooTamma2.yaml` existed at the referenced commit. It was created at commit `6d9f793e` (2021-10-14) with this content:

```yaml
sources:
  - ../sources/BalooTamma2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The source file `sources/BalooTamma2.glyphs` was confirmed to exist at the referenced commit. The config referenced it via relative path from the `builder/` directory. No override config.yaml existed in the google/fonts family directory. The `config_yaml` field in METADATA.pb correctly pointed to `builder/BalooTamma2.yaml`.

## google/fonts History

The font was onboarded via PR [#3984](https://github.com/google/fonts/pull/3984) ("Baloo Tamma 2: Version 1.700 added"), authored by Yanone and merged on 2021-10-29. The commit message explicitly stated: "Baloo Tamma 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa21aa0e376253d61c21e39146dc55702a."

This PR replaced the previous static font files (BalooTamma2-Bold.ttf, BalooTamma2-ExtraBold.ttf, etc.) with a single variable font `BalooTamma2[wght].ttf`. The source block was later re-added in a subsequent commit (`28e3ef2aa`, "sources info for Baloo Tamma 2: Version 1.700 (#3984)").

After the referenced commit, the upstream repository had additional activity (kerning fixes for other Baloo variants, copyright file addition, font regeneration as v1.701 in September 2022), but none of these changes affected the BalooTamma2 font binary that was shipped.

## Conclusion

All source metadata was verified as correct. The repository URL, commit hash, and config_yaml path in METADATA.pb were accurate. The font binary in google/fonts matched the upstream binary at the referenced commit. No changes were needed.
