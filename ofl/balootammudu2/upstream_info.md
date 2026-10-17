# Baloo Tammudu 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete
- **Designer**: Ek Type

## Source Data

| Field | Value |
|---|---|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | `da523dfa21aa0e376253d61c21e39146dc55702a` |
| Config | `builder/BalooTammudu2.yaml` (in upstream repo) |
| Branch | `master` |

## Repository URL

The METADATA.pb `repository_url` field pointed to `https://github.com/yanone/Baloo2-Variable`. This was confirmed as the correct upstream repository. The repo was cached locally at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable` and the remote URL matched. The copyright string in METADATA.pb referenced `https://github.com/EkType/Baloo2`, which is the original Ek Type repository; the yanone fork was used for the variable font conversion and onboarding.

## Commit Verification

The commit `da523dfa21aa0e376253d61c21e39146dc55702a` (2021-10-28, by Yanone, message: "Update BalooTammudu2[wght].ttf") was verified as correct through multiple lines of evidence:

1. **PR #3987** explicitly stated: "Baloo Tammudu 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa21aa0e376253d61c21e39146dc55702a." The PR was authored by Yanone and merged on 2021-10-29.
2. **gftools-packager** recorded the same commit hash in the google/fonts commit body (commit `ece08a067`).
3. **Binary file match**: The SHA-256 hash of `BalooTammudu2[wght].ttf` in google/fonts (`4771a1c5...`) matched exactly the file at that commit in the upstream repo.
4. **No newer changes**: No subsequent commits in the upstream repo touched `fonts/variable/BalooTammudu2[wght].ttf` after this commit. The most recent upstream commit (`29ddd81`, 2022-09-09) only modified `BalooBhaijaan2` files.

## Config

The config file `builder/BalooTammudu2.yaml` existed at the referenced commit. Its contents:

```yaml
sources:
  - ../sources/BalooTammudu2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The source file `sources/BalooTammudu2.glyphs` was confirmed to exist at the referenced commit. No override `config.yaml` was present in the google/fonts family directory, so the `config_yaml` field in METADATA.pb correctly pointed to the upstream path.

## Conclusion

All source metadata was already present and correct in METADATA.pb. The repository URL, commit hash, config path, and branch were all verified. The source block was added in google/fonts commit `c0326551a` (2025-09-24, PR #3987 enrichment by Felipe Sanches). No changes are needed.
