# Investigation Report: Libre Bodoni

**Family Name**: Libre Bodoni
**Directory**: `ofl/librebodoni`
**Designer**: Pablo Impallari, Rodrigo Fuenzalida
**License**: OFL
**Date Added**: 2022-04-13
**Model**: Claude Opus 4.6

## Source Block in METADATA.pb

The METADATA.pb file contains a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/Libre-Bodoni"
  commit: "37d048938a8a32e6ba3992072cb3857659a7828f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/LibreBodoni[wght].ttf"
    dest_file: "LibreBodoni[wght].ttf"
  }
  files {
    source_file: "fonts/variable/LibreBodoni-Italic[wght].ttf"
    dest_file: "LibreBodoni-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Repository Verification

- **Repository URL**: https://github.com/googlefonts/Libre-Bodoni (valid, accessible)
- **Branch**: master (confirmed as default branch)
- **Remote verified**: Matches `origin` remote in local cache at `upstream_repos/fontc_crater_cache/googlefonts/Libre-Bodoni`

## Commit Hash Verification

The referenced commit `37d048938a8a32e6ba3992072cb3857659a7828f` was verified:

- It is the HEAD of the `master` branch in the upstream repository.
- It is a merge commit by Marc Foley dated 2023-02-08, merging PR #2 from emmamarichal/master ("Update Libre Bodoni").
- The commit message in google/fonts (`f0c0ed41b`) explicitly states: "Libre Bodoni Version 2.005;gftools[0.9.23] taken from the upstream repo https://github.com/googlefonts/Libre-Bodoni at commit 37d048938a8a32e6ba3992072cb3857659a7828f".

### Binary File Verification

Both variable font files in google/fonts matched exactly (SHA-256) with the files at the referenced commit in the upstream repo:

- `LibreBodoni[wght].ttf`: `0d543665bd869819ffd7d46608804e245497ba835960832d44be89e561b0c717`
- `LibreBodoni-Italic[wght].ttf`: `6a9b0c88764dcf6c094653e3c28da045fcebca48734254afdcbfec46b9ab4fcd`

This confirmed that the binary fonts in google/fonts were taken directly from the upstream repo's `fonts/variable/` directory (pre-built binaries), not compiled from sources.

## Config.yaml Verification

The file `sources/config.yaml` existed at the referenced commit in the upstream repo. Its contents:

```yaml
sources:
  - LibreBodoni.glyphs
  - LibreBodoni-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: "Libre Bodoni"
stat:
  LibreBodoni[wght].ttf:
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
  - name: Italic
    tag: ital
    values:
    - name: Roman
      value: 0
      linkedValue: 1
      flags: 2
  LibreBodoni-Italic[wght].ttf:
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
  - name: Italic
    tag: ital
    values:
    - name: Italic
      value: 1
```

The config referenced two Glyphs sources: `LibreBodoni.glyphs` and `LibreBodoni-Italic.glyphs`, both present in the `sources/` directory at the referenced commit. No override `config.yaml` existed in the google/fonts family directory.

## Onboarding History

### Initial Onboarding (v2.003) - PR #4498

- **Author**: Emma Marichal (@emmamarichal)
- **Merged**: 2022-04-13 by Rosalie Wagner (@RosaWagner)
- **Commit hash at the time**: `1f06b4544f846b1a9cafd855a5b767483d536f34`
- **Description**: Initial addition of the variable font version of Libre Bodoni to Google Fonts with version 2.003.

### Update (v2.005) - PR #5873

- **Author**: Emma Marichal (@emmamarichal)
- **Merged**: 2023-02-08 by Marc Foley (@m4rc1e)
- **Commit hash**: `37d048938a8a32e6ba3992072cb3857659a7828f` (current)
- **Description**: Updated the font to version 2.005. This update addressed accent placement issues (upstream issue: google/fonts#5741) and added the SemiBold weight. The upstream PR #2 was merged on the same day.

### Subsequent Metadata Updates

- **2024-04-03**: `upstream.yaml` data was merged into METADATA.pb (commit `66f91f10f`), adding file mappings and branch info.
- **2025-03-31**: `config_yaml: "sources/config.yaml"` was added by the Batch 2/4 commit (`4ad8ac680`), porting data from fontc_crater's targets list.

## Status

- **Repository URL**: Correct and verified
- **Commit Hash**: Correct and verified (binary match confirmed)
- **Config.yaml**: Present in upstream repo at `sources/config.yaml`; correctly referenced in METADATA.pb
- **Overall Status**: **COMPLETE** -- All source metadata fields are present and verified.
- **Confidence**: **HIGH**

No action needed. The source block is fully populated with verified data.
