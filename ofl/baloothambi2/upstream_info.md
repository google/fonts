# Investigation Report: Baloo Thambi 2

- **Family Name**: Baloo Thambi 2
- **Slug**: baloothambi2
- **Designer**: Ek Type
- **Status**: complete
- **Confidence**: HIGH
- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/yanone/Baloo2-Variable"
  commit: "ffd6308743a5829fe6980ce86f5629ba0250df98"
  config_yaml: "builder/BalooThambi2.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BalooThambi2[wght].ttf"
    dest_file: "BalooThambi2[wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Repository Information

- **Repository URL**: https://github.com/yanone/Baloo2-Variable
- **Branch**: master
- **Copyright string**: "Copyright 2019 The Baloo 2 Project Authors (https://github.com/EkType/Baloo2)"

The copyright string references the original EkType/Baloo2 repository, while the font binaries were produced from the yanone/Baloo2-Variable fork. This is expected — yanone (Yanone) maintained the variable font rebuild of the Baloo 2 family.

## Commit Verification

- **Referenced commit**: `ffd6308743a5829fe6980ce86f5629ba0250df98`
- **Commit message**: "Update BalooChettan2[wght].ttf"
- **Commit date**: Fri Nov 19 11:34:42 2021 +0100
- **Commit exists in repo**: Yes

The referenced commit (`ffd6308`) was part of a batch of updates on 2021-11-19 that updated multiple Baloo 2 variant binaries. The commit itself only touched `BalooChettan2[wght].ttf`, but it was the latest commit on the master branch at the time of onboarding, and was used as the snapshot reference for the entire Baloo 2 family set.

### Binary File Verification

The SHA-256 hash of `fonts/variable/BalooThambi2[wght].ttf` at commit `ffd6308` matched the binary in google/fonts exactly:

| Source | SHA-256 |
|--------|---------|
| Upstream at `ffd6308` | `6739a11d3557b7426f0f43ce3a22ff6fbfee2d3be56ffb4df093d35d3460bf73` |
| Upstream at `8844491` (last BalooThambi2-specific commit) | `6739a11d3557b7426f0f43ce3a22ff6fbfee2d3be56ffb4df093d35d3460bf73` |
| google/fonts | `6739a11d3557b7426f0f43ce3a22ff6fbfee2d3be56ffb4df093d35d3460bf73` |

All three hashes were identical. The BalooThambi2 binary was last updated at commit `8844491` (2021-11-19), and remained unchanged through `ffd6308` (also 2021-11-19). This confirmed the commit hash was correct.

### Later Upstream Commits

There were two later commits in the repo after `ffd6308`:
- `ccefc89` — Merge pull request #3 from yanone/master
- `29ddd81` — Regenerated fonts as 1.701 without data changes (2022-09-09)

These were made after the onboarding, so they were not relevant to the referenced commit.

## Config YAML Verification

- **Config path in METADATA.pb**: `builder/BalooThambi2.yaml`
- **File exists at referenced commit**: Yes
- **File exists on current master**: Yes

Content of `builder/BalooThambi2.yaml`:

```yaml
sources:
  - ../sources/BalooThambi2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The config referenced the Glyphs source file at `sources/BalooThambi2.glyphs`, which was verified to exist at the referenced commit. The config was a valid gftools-builder configuration.

## google/fonts History

- **Onboarding commit**: `397ea6e1a` — "Baloo Thambi 2: Version 1.700 added (#3986)" (2021-11-26)
  - gftools-packager message explicitly referenced commit `ffd6308743a5829fe6980ce86f5629ba0250df98` from `https://github.com/yanone/Baloo2-Variable`
- **Repository URL initially populated**: `f7455d788` — "Populate source.repository_url" (2023-08-15) — set it to `https://github.com/EkType/Baloo2-Variable`
- **Source info enrichment**: `f7ab4c51f` — "sources info for Baloo Thambi 2: Version 1.700 (#3986)" (2025-09-24) — corrected the repository URL from EkType to yanone, and added commit hash and config_yaml

## Override Config Assessment

No override `config.yaml` was needed. The upstream repository had a proper `builder/BalooThambi2.yaml` config file at the referenced commit, and this path was correctly recorded in METADATA.pb.

## Conclusion

All source metadata for Baloo Thambi 2 was verified as complete and correct:

- **Repository URL**: Correctly pointed to `https://github.com/yanone/Baloo2-Variable`
- **Commit hash**: `ffd6308` was verified — the binary at this commit matched google/fonts exactly
- **Config YAML**: `builder/BalooThambi2.yaml` existed at the referenced commit with valid gftools-builder configuration
- **Branch**: master (correct)

No corrections were needed. The source block was already complete with accurate data.
