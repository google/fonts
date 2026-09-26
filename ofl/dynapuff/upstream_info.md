# Investigation Report: DynaPuff

## Family Information
- **Family name**: DynaPuff
- **Designer**: Toshi Omagari, Jennifer Daniel
- **License**: OFL
- **Category**: Display
- **Date added**: 2022-05-19
- **Path in google/fonts**: `ofl/dynapuff/`

## Source Repository
- **Repository URL**: https://github.com/googlefonts/dynapuff
- **Verified**: Yes, repository exists and is accessible
- **Local cache**: `upstream_repos/fontc_crater_cache/googlefonts/dynapuff`

## Onboarding History

### PR #4670: "DynaPuff: Version 2.000 added"
- **Author**: Emma Marichal (@emmamarichal)
- **Merged by**: Rosalie Wagner (@RosaWagner)
- **Created**: 2022-05-13
- **Merged**: 2022-06-24
- **Commit in google/fonts**: `414f2fda12cf1967e47f07a2122a00450d82681f`

The PR body references upstream commit `6e278ec16124e504485c7b87fd17ffa48c17fe85` (2022-05-13, "Merge pull request #3 from emmamarichal/main - Add DynaPuff"). The commit message within google/fonts references a different upstream commit: `d1b4a98067a23e7ffbcf5b3665a887241983857b` (2022-05-19, "Merge pull request #4 from emmamarichal/main - Accents positions updated").

This is consistent with the gftools-packager workflow: the PR was initially generated from commit `6e278ec`, but additional upstream fixes were made (PR #4 in the upstream repo, fixing accent positions on some letters), and the final fonts delivered to google/fonts were taken from commit `d1b4a98`.

### Binary Verification

The font file `DynaPuff[wdth,wght].ttf` in google/fonts (212,600 bytes) has SHA256 hash `c3752fc6dd8aaa46a88637f061a9a4e6ab44c02c5f0afd65528b91ae8ff6f948`, which is an **exact match** with the pre-built binary at upstream commit `d1b4a98`. The earlier commit `6e278ec` has a smaller file (212,156 bytes), confirming it is not the correct onboarding commit.

### Commit Hash Issue in METADATA.pb

The current METADATA.pb has commit `0cc624ef50b654ffe1a30785396aaba308406132`, which is the **latest** commit on the upstream repo (2022-06-24, "Merge pull request #5 from emmamarichal/main - DynaPuff: Readme.md updated"). This commit only changed README.md and documentation images -- no font sources or binaries were modified.

This incorrect commit was introduced by commit `19cdcec59` in google/fonts ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported data from fontc_crater's target.json. The fontc_crater targets list used the HEAD commit of the upstream repo rather than the specific onboarding commit.

Prior to that batch change, METADATA.pb correctly had `d1b4a98067a23e7ffbcf5b3665a887241983857b` as the commit (set during the upstream.yaml merge by Simon Cozens on 2024-04-03).

**The correct onboarding commit is `d1b4a98067a23e7ffbcf5b3665a887241983857b`.**

## Source Files and Config

### Source format
- **Glyphs source**: `sources/DynaPuff.glyphs`
- **Config**: `sources/config.yaml` (present in upstream repo)

### config.yaml contents (at upstream repo)
```yaml
sources:
  - DynaPuff.glyphs
axisOrder:
  - wdth
  - wght
familyName: DynaPuff
stat:
  DynaPuff[wdth,wght].ttf:
  - name: Width
    tag: wdth
    values:
    - name: Condensed
      value: 75
    - name: Normal
      value: 100
      flags: 2
  - name: Weight
    tag: wght
    values:
    - name: Regular
      value: 400
      linkedValue: 700
      flags: 2
    - name: Medium
      value: 500
    - name: SemiBold
      value: 600
    - name: Bold
      value: 700
```

The config.yaml is the same at both commits `d1b4a98` and `0cc624e` (no changes to source files occurred between them).

### Font axes
- **wdth**: 75.0 - 100.0
- **wght**: 400.0 - 700.0

## Current METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/googlefonts/dynapuff"
  commit: "0cc624ef50b654ffe1a30785396aaba308406132"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/DynaPuff[wdth,wght].ttf"
    dest_file: "DynaPuff[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Recommended Fix

The commit hash should be corrected from `0cc624ef50b654ffe1a30785396aaba308406132` to `d1b4a98067a23e7ffbcf5b3665a887241983857b`. All other fields are correct.

```
source {
  repository_url: "https://github.com/googlefonts/dynapuff"
  commit: "d1b4a98067a23e7ffbcf5b3665a887241983857b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/DynaPuff[wdth,wght].ttf"
    dest_file: "DynaPuff[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Summary

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/googlefonts/dynapuff |
| **Correct commit** | `d1b4a98067a23e7ffbcf5b3665a887241983857b` |
| **Config** | `sources/config.yaml` (in upstream repo) |
| **Override config needed** | No |
| **Status** | needs_correction (commit hash should be fixed) |
| **Confidence** | HIGH (binary SHA256 verified) |
