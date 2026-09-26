# Baloo Chettan 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete
- **Designer**: Ek Type

## Source Data

| Field | Value |
|---|---|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | `ffd6308743a5829fe6980ce86f5629ba0250df98` |
| Config YAML | `builder/BalooChettan2.yaml` |
| Branch | master |

## Repository URL

The METADATA.pb `source` block listed the repository URL as `https://github.com/yanone/Baloo2-Variable`. This was verified against the cached clone at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable`, whose remote origin matched. The repository is a multi-family project maintained by Yanone, housing the Baloo 2 variable font family variants. The copyright string in METADATA.pb references `https://github.com/EkType/Baloo2`, which is the original Ek Type repository; yanone/Baloo2-Variable is the variable-font conversion maintained by Yanone.

## Commit Verification

The referenced commit `ffd6308` was authored by Yanone on 2021-11-19 with the message "Update BalooChettan2[wght].ttf". It modified only the file `fonts/variable/BalooChettan2[wght].ttf`, changing its size from 258,712 to 339,860 bytes.

The google/fonts commit `164f84fe` (2021-11-25, PR #3985) brought in Version 1.700 of Baloo Chettan 2 via gftools-packager. The commit message explicitly stated: "Baloo Chettan 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/ffd6308743a5829fe6980ce86f5629ba0250df98."

Binary verification confirmed the match:
- Upstream binary at `ffd6308:fonts/variable/BalooChettan2[wght].ttf`: 339,860 bytes, SHA256 `8f0de4f81b40d314a129c55a3a9e58411868ca9a452edb57537488853f46db86`
- google/fonts binary `ofl/baloochettan2/BalooChettan2[wght].ttf`: 339,860 bytes, SHA256 `8f0de4f81b40d314a129c55a3a9e58411868ca9a452edb57537488853f46db86`

The SHA256 hashes were identical, confirming the binary was taken verbatim from the referenced upstream commit.

One later upstream commit existed (`29ddd81`, 2022-09-09, "Regenerated fonts as 1.701 without data changes") which was not yet incorporated into google/fonts.

## Config YAML

The `config_yaml` field in METADATA.pb pointed to `builder/BalooChettan2.yaml`. This file was verified to exist in the upstream repository both at the referenced commit `ffd6308` and at HEAD. Its contents were:

```yaml
sources:
  - ../sources/BalooChettan2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The source file `sources/BalooChettan2.glyphs` was confirmed to exist in the upstream repo. No override `config.yaml` existed in the google/fonts family directory.

## Conclusion

All source metadata for Baloo Chettan 2 was verified as complete and correct. The repository URL, commit hash, and config YAML path were all confirmed through binary hash comparison and git history analysis. The commit hash matched the exact binary shipped in google/fonts via PR #3985. The config file existed in the upstream repository at the referenced commit. No changes were needed.
