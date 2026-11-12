# Investigation Report: Estonia

## Family Overview

- **Family name**: Estonia
- **Designer**: Robert Leuschke
- **License**: OFL
- **Category**: HANDWRITING
- **Classifications**: DISPLAY, HANDWRITING
- **Date added**: 2021-08-26
- **Path in google/fonts**: `ofl/estonia/`
- **Subsets**: latin, latin-ext, menu, vietnamese

## Source Metadata in METADATA.pb

The `source {}` block is already present and complete:

```
source {
  repository_url: "https://github.com/googlefonts/estonia"
  commit: "d4ee6f0558f9af9ad0cc950e740a81eb95b36526"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Estonia-Regular.ttf"
    dest_file: "Estonia-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Upstream Repository

- **URL**: https://github.com/googlefonts/estonia
- **Branch**: master
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/estonia`
- **Repo status**: Clean, up to date with origin

### Repository Structure

```
AUTHORS.txt
CONTRIBUTORS.txt
DESCRIPTION.en_us.html
Documentation/
fonts/
  EstoniaPro.ttf
  otf/Estonia-Regular.otf
  ttf/Estonia-Regular.ttf
  webfonts/Estonia-Regular.woff2
OFL.txt
README.md
requirements.txt
sources/
  config.yml
  EstoniaPro.glyphs
```

### Commit History

The upstream repo contains a single commit:

| Hash | Message | Author | Date |
|------|---------|--------|------|
| `d4ee6f0558f9af9ad0cc950e740a81eb95b36526` | v1.014 fonts, inits and final fea fixes | Viviana Monsalve | 2021-10-06 |

## Build Configuration

The upstream repo has a `sources/config.yml` file:

```yaml
sources:
  - EstoniaPro.glyphs
familyName: "Estonia"
buildVariable: false
#autohintTTF: false
```

This is a gftools-builder compatible configuration. The source file is `EstoniaPro.glyphs` (Glyphs format). No override config.yaml is needed in google/fonts.

## Commit Hash Verification

### Referenced commit: `d4ee6f0558f9af9ad0cc950e740a81eb95b36526`

This is the only commit in the upstream repository. It was created by Viviana Monsalve on 2021-10-06.

### Cross-verification with google/fonts history

The font was onboarded through three updates in google/fonts:

1. **PR #3768** (commit `647b05b59`): Initial onboarding as Version 1.010, referencing upstream commit `dffcd97fe95d0766d2bd257be51c1a07de2fd4ea` (this commit no longer exists in the repo since the repo was recreated with a single squashed commit)
2. **PR #3848** (commit `3fcb9f90e`): Update to Version 1.012, referencing upstream commit `38911566061dea1009f92e6dbabf0b5944b9ae64` (also no longer in history)
3. **PR #3917** (commit `c1c96b174`): Final update to Version 1.014 on 2021-10-08, referencing upstream commit `d4ee6f0558f9af9ad0cc950e740a81eb95b36526` -- this is the current and only commit in the repo

All three updates were done by Viviana Monsalve using gftools-packager.

### Binary file verification

The binary font file `Estonia-Regular.ttf` in google/fonts matches the file `fonts/ttf/Estonia-Regular.ttf` at the referenced upstream commit:

- **SHA-256**: `03087597ea24879c19d51ca4622f8c4e9cd867d081e7ad0ad3e7dccfdb1933b2`
- **File size**: 1,470,272 bytes

The files are byte-identical, confirming the commit hash is correct.

## Source File Formats

- **Primary source**: `sources/EstoniaPro.glyphs` (Glyphs format)
- **Build tool**: gftools-builder (config.yml present)
- **Output**: Static TTF only (buildVariable: false)

## Summary

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/googlefonts/estonia |
| **Commit** | `d4ee6f0558f9af9ad0cc950e740a81eb95b36526` |
| **Branch** | master |
| **Config** | `sources/config.yml` (in upstream repo) |
| **Override config needed** | No |
| **Status** | **COMPLETE** |
| **Confidence** | **HIGH** |

All source metadata is present and verified. The repository URL is valid, the commit hash is correct (confirmed by binary file comparison), the config.yml exists at the referenced path, and the source files are in Glyphs format compatible with gftools-builder. No action is needed for this family.
