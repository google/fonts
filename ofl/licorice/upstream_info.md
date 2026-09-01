# Investigation Report: Licorice

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete
**Confidence**: HIGH

## Font Family Information

- **Family Name**: Licorice
- **Designer**: Robert Leuschke
- **License**: OFL
- **Category**: HANDWRITING
- **Classifications**: DISPLAY, HANDWRITING
- **Date Added**: 2021-11-18
- **Directory**: `ofl/licorice`

## Source Block (Current METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/licorice"
  commit: "8bc5263602a190f212684ea69d5b9d3b21a59bc0"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Licorice-Regular.ttf"
    dest_file: "Licorice-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Upstream Repository

- **URL**: https://github.com/googlefonts/licorice
- **Branch**: master
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/licorice/`
- **Repository status**: Clean, up to date with origin

The upstream repository contains only a single commit (`8bc5263`), authored by Viviana Monsalve on 2021-11-12 with the message "v1.010 with latest spacing fixes". This is an initial commit that created the entire repository structure in one go.

## Commit Verification

The commit hash `8bc5263602a190f212684ea69d5b9d3b21a59bc0` was verified through multiple methods:

1. **Explicit reference in onboarding PR**: PR #4086 in google/fonts, titled "Licorice: Version 1.010; ttfautohint (v1.8.3) added", was opened by Viviana Monsalve (vv-monsalve) and merged by Rosalie Wagner (RosaWagner) on 2021-11-25. The commit message explicitly states: "Licorice Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/licorice at commit https://github.com/googlefonts/licorice/commit/8bc5263602a190f212684ea69d5b9d3b21a59bc0."

2. **Single commit in repo**: The upstream repository has exactly one commit, so there is no ambiguity about which commit was used.

3. **Binary file match**: The font file `fonts/ttf/Licorice-Regular.ttf` from the upstream repository at this commit is identical to the one in google/fonts (both 154,512 bytes, SHA-256: `c72d8cb2f56e6995b3682d8620e2d602bacf78b67121cdfbface9acc422750d8`).

4. **Timeline consistency**: The upstream commit was authored on 2021-11-12, the PR was opened on 2021-11-18, and it was merged on 2021-11-25. The timeline is coherent.

## Config File

The upstream repository contains `sources/config.yml` at the referenced commit:

```yaml
sources:
  - Licorice.glyphs
familyName: "Licorice"
buildVariable: false
# autohintTTF: false
```

The config file references `Licorice.glyphs` which exists in the `sources/` directory. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

## Source Files

The upstream repository contains gftools-builder compatible sources:
- `sources/Licorice.glyphs` -- Glyphs source file
- `sources/config.yml` -- gftools-builder configuration

## History in google/fonts

The source metadata was assembled in stages:
1. **2021-11-25** (commit `93679897`): Font was onboarded via PR #4086 by Viviana Monsalve, using gftools-packager. The commit created the family directory with the font binary, METADATA.pb, OFL.txt, DESCRIPTION, and an `upstream.yaml` file.
2. **2024-04-03** (commit `66f91f10`): Simon Cozens merged the `upstream.yaml` content into METADATA.pb as a `source { }` block, adding repository_url, branch, and file mappings but without commit hash or config_yaml.
3. **2025-03-31** (commit `4ad8ac68`): The batch port from fontc_crater targets added the commit hash and config_yaml to the source block.

## PR Details

- **Onboarding PR**: google/fonts#4086
  - **Author**: Viviana Monsalve (vv-monsalve)
  - **Merged by**: Rosalie Wagner (RosaWagner)
  - **Merged at**: 2021-11-25
  - **Note**: Part of "Batch 4 of TypeSetIT fonts"

## Conclusion

The source block in METADATA.pb is complete and correct. The repository URL, commit hash, branch, file mappings, and config_yaml are all verified. The binary font file in google/fonts is an exact match of the file in the upstream repository at the referenced commit. No corrections are needed.
