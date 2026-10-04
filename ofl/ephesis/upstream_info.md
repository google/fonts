# Investigation Report: Ephesis

## Family Overview

- **Family name**: Ephesis
- **Designer**: Robert Leuschke
- **License**: OFL
- **Category**: Handwriting, Display
- **Date added to Google Fonts**: 2021-08-06

## Source Block in METADATA.pb

A complete source block already exists in METADATA.pb:

```
source {
  repository_url: "https://github.com/googlefonts/ephesis"
  commit: "8b303b53193b302c8894fb4635bbd49d4420d433"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Ephesis-Regular.ttf"
    dest_file: "Ephesis-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Repository Verification

- **Repository URL**: https://github.com/googlefonts/ephesis
- **Remote verified**: Yes, matches the cached clone at `googlefonts/ephesis`
- **Branch**: `master` (only branch)
- **Repo status**: Clean, up to date with origin

## Commit Hash Verification

- **Commit in METADATA.pb**: `8b303b53193b302c8894fb4635bbd49d4420d433`
- **Commit message**: "v1.010 fonts added"
- **Commit date**: 2021-08-06 20:13:56 -0500
- **Commit author**: Viviana Monsalve

This is the only commit in the upstream repository. The font binary in google/fonts is an exact byte-for-byte match with the file at this commit:

- **File**: `Ephesis-Regular.ttf`
- **Size**: 142,188 bytes
- **SHA-256**: `8fb4729a918f992a37ab45f1466783c78ea8caa77a7b0e69545322e1dbe9c5f9`

No subsequent commits exist in the upstream repo, so there are no concerns about newer changes.

## Onboarding History

- **google/fonts PR**: [#3678](https://github.com/google/fonts/pull/3678) — "Ephesis: Version 1.010; ttfautohint (v1.8.3) added"
- **Author**: Viviana Monsalve (vv-monsalve)
- **Merged**: 2021-08-13
- **Merge commit**: `a05014f87817156a67def15e8b8b906ec8182136`
- **Method**: gftools-packager

The PR body explicitly states the font was taken from `https://github.com/googlefonts/ephesis` at commit `8b303b53193b302c8894fb4635bbd49d4420d433`, which matches the METADATA.pb source block.

## Config File

- **Path in upstream repo**: `sources/config.yml`
- **Referenced in METADATA.pb**: `sources/config.yml`
- **Override in google/fonts**: None needed

Contents of `sources/config.yml`:

```yaml
sources:
  - Ephesis.glyphs
familyName: "Ephesis"
buildVariable: false
# autohintTTF: false
```

## Source Files

- **Source format**: Glyphs (`sources/Ephesis.glyphs`)
- **Build type**: Static only (`buildVariable: false`)
- **Output format**: TTF (single weight, Regular)

## Conclusion

- **Status**: Complete
- **Confidence**: HIGH
- **No action needed**: The METADATA.pb source block is fully populated with correct data. The repository URL, commit hash, branch, config_yaml path, and file mappings are all verified and accurate. The font binary matches the upstream source exactly. No changes to google/fonts are required.
