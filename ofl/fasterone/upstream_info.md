# Faster One - Investigation Report

## Family Overview
- **Family name**: Faster One
- **Designer**: Eduardo Tunni (Eduardo Rodriguez Tunni)
- **License**: OFL
- **Category**: Display
- **Date added to Google Fonts**: 2012-10-26
- **Path in google/fonts**: `ofl/fasterone/`

## Source Repository
- **Repository URL**: https://github.com/etunni/faster
- **Branch**: master
- **Commit**: `c1eb445af08bcc5ce66380f65e56d9d3135cca3c`
- **Commit date**: 2023-02-08
- **Commit message**: "Merge pull request #1 from emmamarichal/master"
- **Commit author**: Eduardo Rodriguez Tunni

## Source Files at Referenced Commit
- `sources/FasterOne.glyphs` (Glyphs format, appVersion 3151, formatVersion 3)
- `fonts/ttf/FasterOne-Regular.ttf` (pre-compiled binary)
- `fonts/otf/FasterOne-Regular.otf`
- `fonts/webfonts/FasterOne-Regular.woff2`
- `OFL.txt`
- `README.md`
- `requirements.txt`
- `AUTHOR.txt`
- `CONTRIBUTORS.txt`
- `documentation/image1.png`, `documentation/image2.png`

## Upstream Repository Analysis

The upstream repo at https://github.com/etunni/faster has a total of 12 commits. The original commit by Eduardo Tunni dates to 2013-12-30 ("Adobe Latin 3 encoding"). On 2023-02-08, Emma Marichal submitted PR #1 which restructured the repository, adding Glyphs sources, documentation, and updated font binaries. All of Emma's commits (10 commits) and the merge commit happened on the same day. The referenced commit `c1eb445` is the merge commit of that PR, and it remains the HEAD of the master branch -- no additional commits have been made since.

There is **no config.yaml** in the upstream repository.

## Google Fonts History

### Initial onboarding (2015-03-07)
- Commit `90abd17b4`: "Initial commit" by Dave Crossland -- bulk import of the entire Google Fonts library.

### Metadata update (2015-09-21)
- Commit `b72ae9adc`: "fasterone: Update to correct internal metadata" by Dave Crossland. Updated description, fontlog, and recompiled the TTF.

### Version 1.003 update (2023-02-08)
- Commit `6bdf99d21`: "[gftools-packager] Faster One: Version 1.003; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23] added" by Emma Marichal.
- PR #5872 (https://github.com/google/fonts/pull/5872), merged 2023-02-08. Reviewed and approved by Marc Foley (@m4rc1e).
- The commit body explicitly states: "Faster One Version 1.003 taken from the upstream repo https://github.com/etunni/faster at commit c1eb445af08bcc5ce66380f65e56d9d3135cca3c."
- The METADATA.pb source block was added as part of this update (via upstream.yaml, later merged into METADATA.pb).

### Override config.yaml (2025-03-10)
- Commit `3b645f8db`: "Adding 119 automatically generated config.yaml files" by Felipe Sanches. This auto-generated a `config.yaml` for fasterone as part of a batch for repos with `.glyphs` files in their `sources/` directory.

### Sources info update (2025-10-07)
- Commit `3a3d5e034`: "sources info for Faster One: Version 1.003 (PR #5872)" by Felipe Sanches. Updated the override config.yaml.

## Commit Hash Verification

**Confidence: HIGH**

The commit hash `c1eb445af08bcc5ce66380f65e56d9d3135cca3c` is verified correct:

1. **Explicitly referenced in google/fonts**: The gftools-packager commit `6bdf99d21` body states the font was taken from this exact commit.
2. **Binary file match**: The SHA256 hash of `fonts/ttf/FasterOne-Regular.ttf` in the upstream repo at `c1eb445` matches identically with the TTF in `ofl/fasterone/FasterOne-Regular.ttf` in google/fonts (SHA256: `382877a3a497c42bfeadfbb6e1b939d5b0f3f5cfd6c1a566c0c0d3d1f9b4bcb5`).
3. **Timeline consistent**: Both the upstream merge and the google/fonts PR #5872 occurred on 2023-02-08, with the google/fonts PR merged just hours after the upstream merge.
4. **HEAD of master**: The commit is the latest on the upstream master branch, with no subsequent commits.

## Config Assessment

- **Upstream config.yaml**: Not present in the upstream repository.
- **Override config.yaml**: Present in google/fonts at `ofl/fasterone/config.yaml`, containing:
  ```yaml
  buildVariable: false
  sources:
    - sources/FasterOne.glyphs
  ```
- **Source file**: `sources/FasterOne.glyphs` exists at the referenced commit and is a valid Glyphs 3 format file.

The override config.yaml correctly references the Glyphs source file and sets `buildVariable: false` (appropriate for this single-weight display font).

## METADATA.pb Source Block

The current METADATA.pb source block is:
```
source {
  repository_url: "https://github.com/etunni/faster"
  commit: "c1eb445af08bcc5ce66380f65e56d9d3135cca3c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/FasterOne-Regular.ttf"
    dest_file: "FasterOne-Regular.ttf"
  }
  branch: "master"
}
```

Note: No `config_yaml` field is set in the source block, which is correct because the override `config.yaml` in the google/fonts family directory is auto-detected by google-fonts-sources.

## Status

- **Status**: COMPLETE
- **Repository URL**: Verified (https://github.com/etunni/faster)
- **Commit hash**: Verified (`c1eb445af08bcc5ce66380f65e56d9d3135cca3c`)
- **Config**: Override config.yaml in google/fonts (upstream has no config.yaml)
- **Source block**: Present and correct in METADATA.pb
- **No action needed**: All metadata is complete and verified.
