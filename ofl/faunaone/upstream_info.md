# Investigation Report: Fauna One

## Family Overview

- **Family name**: Fauna One
- **Designer**: Eduardo Tunni
- **License**: OFL
- **Category**: Serif
- **Date added to Google Fonts**: 2013-06-05
- **Subsets**: latin, latin-ext, menu

## Upstream Repository

- **URL**: https://github.com/etunni/fauna-one
- **Branch**: master
- **Status**: Active, clean, up-to-date

## Source Block in METADATA.pb

The METADATA.pb already contains a complete source block:

```
source {
  repository_url: "https://github.com/etunni/fauna-one"
  commit: "ed89976413a322f9d84aae5d97c17cfe5cf0d95d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/FaunaOne-Regular.ttf"
    dest_file: "FaunaOne-Regular.ttf"
  }
  branch: "master"
}
```

## Commit Hash Verification

### Referenced Commit

- **Hash**: `ed89976413a322f9d84aae5d97c17cfe5cf0d95d`
- **Date**: 2023-01-26 10:41:50 -0300
- **Author**: Eduardo Rodriguez Tunni (edu@tipo.net.ar)
- **Message**: "Merge pull request #1 from emmamarichal/master -- Fauna upgrade"
- **Is HEAD**: Yes, this is the latest commit on the master branch

### Timeline of Events

1. **2023-01-25/26**: Emma Marichal (emmamarichal) submitted upstream PR #1 "Fauna upgrade" to etunni/fauna-one, which added `.glyphs` sources, restructured the repo (removed old UFO sources, added compiled fonts to `fonts/` directory), added `requirements.txt`, and updated `OFL.txt`.
2. **2023-01-26 13:41 UTC**: Eduardo Tunni merged upstream PR #1.
3. **2023-01-26 13:59 UTC**: Emma Marichal created the gftools-packager commit (fb14d63) in google/fonts referencing commit `ed89976`.
4. **2023-01-31 10:35 UTC**: Marc Foley (m4rc1e) merged google/fonts PR #5833.

### Binary Verification

The font binary `FaunaOne-Regular.ttf` in google/fonts matches the one in the upstream repo at the referenced commit:
- **SHA256**: `3c636067331e86fbf349924f3c1964155b99072a390caaffe60ce6c0866363fe` (identical in both locations)

### Assessment

The commit hash is **correct**. The referenced commit `ed89976` is the tip of the master branch and represents the merge of Emma Marichal's upgrade PR. The timeline is consistent: the upstream PR was merged the same day as the gftools-packager commit was created, and the google/fonts PR was merged 5 days later. No additional upstream commits exist after this hash.

## Build Configuration (config.yaml)

### Upstream Repository

The upstream repo does **not** contain a `config.yaml` file. However, it does contain gftools-builder compatible sources:
- `sources/FaunaOne.glyphs` (Glyphs format source file)

### Override config.yaml in google/fonts

An override `config.yaml` exists at `ofl/faunaone/config.yaml` in google/fonts:

```yaml
buildVariable: false
sources:
  - sources/FaunaOne.glyphs
```

This was added via commit `18b0d776c` ("sources info for Fauna One: Version 2.001 (PR #5833)") as part of a batch addition of automatically generated config.yaml files for 119 families.

The `config_yaml` field is correctly **not set** in METADATA.pb, since google-fonts-sources auto-detects the local override.

## History in google/fonts

1. **2015-03-07**: Initial commit (90abd17) by Dave Crossland with `FaunaOne-Regular.ttf` (30,244 bytes)
2. **2021-11-01**: Temporarily removed in a deploy commit (76adaf1) but subsequently restored
3. **2023-01-26**: Updated via gftools-packager (fb14d63) by Emma Marichal to Version 2.001 with new binary (58,804 bytes), adding the source block to METADATA.pb
4. **2023-01-31**: google/fonts PR #5833 merged by Marc Foley
5. **2024-04-03**: Simon Cozens merged upstream.yaml data into METADATA.pb (66f91f1), adding `files {}` entries and `branch` field
6. **Later**: Override `config.yaml` added as part of batch generation (18b0d77)

## Conclusion

- **Status**: complete
- **Confidence**: HIGH
- **Repository URL**: Correct (https://github.com/etunni/fauna-one)
- **Commit hash**: Correct (`ed89976413a322f9d84aae5d97c17cfe5cf0d95d`) -- latest commit, verified via binary match and timeline analysis
- **Config**: Override `config.yaml` in google/fonts (correctly omitted from METADATA.pb)
- **Notes**: Everything is in order. The source block is complete with repository URL, commit hash, file mappings, and branch. The override config.yaml correctly references the Glyphs source. No action needed.
