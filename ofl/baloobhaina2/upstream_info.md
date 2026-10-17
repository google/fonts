# Baloo Bhaina 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Ek Type

## Source Data

| Field | Value |
|---|---|
| repository_url | https://github.com/yanone/Baloo2-Variable |
| commit | da523dfa21aa0e376253d61c21e39146dc55702a |
| config_yaml | builder/BalooBhaina2.yaml |

## Repository URL

The METADATA.pb `repository_url` points to `https://github.com/yanone/Baloo2-Variable`. This is the correct upstream repository. Note that the font copyright string references `https://github.com/EkType/Baloo2`, which was the original EkType organization repo, but the actual build/variable-font work was done by Yanone (Jan Gerner) in his fork. An earlier commit in google/fonts (`1061d8e4d`, PR #4104, "Correct EkType Github Repo URL") corrected the upstream URL across all Baloo 2 family variants from EkType to yanone.

The cached clone at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable` confirms remote origin matches: `https://github.com/yanone/Baloo2-Variable`.

## Commit Verification

The METADATA.pb references commit `da523dfa21aa0e376253d61c21e39146dc55702a` (2021-10-28, "Update BalooTammudu2[wght].ttf"). This commit exists in the upstream repo on the `master` branch.

**gftools-packager confirmation**: The google/fonts onboarding commit `35975c1b3` (PR #3988, "Baloo Bhaina 2: Version 1.700 added", 2021-10-29) explicitly states in its message:

> Baloo Bhaina 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/da523dfa21aa0e376253d61c21e39146dc55702a.

**Binary verification**: The SHA-256 hash of `fonts/variable/BalooBhaina2[wght].ttf` at commit `da523df` in the upstream repo matches the file in `google/fonts/ofl/baloobhaina2/BalooBhaina2[wght].ttf` exactly:
```
d22904b7337723201c910edf70be2de6136ec65be366f2b0e6489860f1343f04
```

The last upstream commit that modified `BalooBhaina2[wght].ttf` was `1f8785c` (2021-10-28, "Update BalooBhaina2[wght].ttf"), which is an ancestor of `da523df`. The binary at both commits is identical. No commits after `da523df` in the upstream repo touch any BalooBhaina2-related files (sources, builder config, or font binary).

The upstream repo has 8 additional commits after `da523df` (up to HEAD at `29ddd81`, 2022-09-09), but none of them affect BalooBhaina2 files. These later commits deal with other Baloo variants (Chettan, Da, Thambi) and a bulk font regeneration to version 1.701.

## Config Verification

The config file `builder/BalooBhaina2.yaml` exists at the referenced commit with the following content:

```yaml
sources:
  - ../sources/BalooBhaina2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The source file `sources/BalooBhaina2.glyphs` exists at the referenced commit. No local override `config.yaml` exists in the google/fonts family directory. The `config_yaml` field in METADATA.pb correctly points to `builder/BalooBhaina2.yaml`.

## Conclusion

All source metadata is complete and verified:

- **repository_url**: Correct. Points to the yanone fork where the variable font work was done.
- **commit**: Correct. Matches the gftools-packager onboarding record and binary file verification confirms the font binary is identical.
- **config_yaml**: Correct. The builder config exists at `builder/BalooBhaina2.yaml` in the upstream repo and references the correct Glyphs source.

No changes needed. Status: **complete**.
