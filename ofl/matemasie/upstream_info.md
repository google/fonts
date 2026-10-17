# Matemasie — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The source block was present and fully populated:

```
source {
  repository_url: "https://github.com/YADAMSS/Matemasie-Font"
  commit: "a6dbde5f9eb448066e8c751ee4c5b4146a7fbc99"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Matemasie-Regular.ttf"
    dest_file: "Matemasie-Regular.ttf"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/1.png"
    dest_file: "article/1.png"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/2.png"
    dest_file: "article/2.png"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/3.gif"
    dest_file: "article/3.gif"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/4.png"
    dest_file: "article/4.png"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

**Repository**: https://github.com/YADAMSS/Matemasie-Font
**Owner**: YADAMSS (Adam Yeo)
**Branch**: main
**Cached**: Yes, at `YADAMSS/Matemasie-Font` in the upstream repos cache.

The upstream repository was built from the googlefonts project template. It contained:
- **Source files**: `sources/Matemasie.glyphspackage` (Glyphs 3 package format)
- **Config**: `sources/config.yaml` with gftools-builder configuration
- **Font binary**: `fonts/ttf/Matemasie-Regular.ttf` (pre-built)
- **Build system**: Makefile and GitHub Actions workflow (`build.yaml`)
- **Documentation**: Article HTML, social media assets, proofs

The repository had only one branch (`main`) and the entire visible history consisted of a single commit (`a6dbde5`), which was a merge of PR #34 ("Restore Actions with change to build.yaml") dated 2024-10-09. This indicated the repository was force-pushed or rebased at some point, squashing all prior history.

### Force-Push Evidence

Multiple commit hashes referenced in google/fonts history no longer existed in the upstream repo:
- `f8b28b0ecb71e4556e18b2f4af23ca151243cac0` (referenced in PR #7875 body)
- `05f20fba79c6e780b125220555909646f29b999c` (referenced in onboarding commit `f4e074ab6` message)
- `982fb1ec023f63c0da05a11a2bec15efd1470484` (referenced in PR #8208 body)
- `a53371edff5c32131e93492ccb7618f4c567fbe0` (referenced in update commit `7e509860f` message)

All of these hashes were lost when the repo was apparently reset/force-pushed. The only surviving commit was the final `a6dbde5` merge commit.

### config.yaml

The config file at `sources/config.yaml` contained:

```yaml
sources:
  - Matemasie.glyphspackage
familyName: Matemasie
autohintOTF: False
```

This was a valid gftools-builder configuration referencing the `.glyphspackage` source.

### Binary Verification

The font binary in google/fonts (`ofl/matemasie/Matemasie-Regular.ttf`) was verified to be identical to the one in the upstream repo (`fonts/ttf/Matemasie-Regular.ttf`):
- MD5: `d2e20b8efc02a584dd916c92a1f7cfaa`
- Size: 143,128 bytes

This confirmed that the current HEAD commit (`a6dbde5`) contained the same font file that was onboarded.

## Onboarding History

### Initial Onboarding (PR #7875, merged 2024-07-17)

- **Title**: "Matemasie: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added"
- **Author**: Nathan Willis (@n8willis)
- **Commit in google/fonts**: `f4e074ab6` (2024-07-10)
- **Upstream commit cited in body**: `f8b28b0ecb71e4556e18b2f4af23ca151243cac0`
- **Upstream commit cited in commit message**: `05f20fba79c6e780b125220555909646f29b999c`
- **Files added**: METADATA.pb, Matemasie-Regular.ttf, OFL.txt, article/ARTICLE.en_us.html

The discrepancy between the PR body and the commit message hashes was notable. This was a known gftools-packager behavior where the commit message could reference a different hash than the PR body if the packager ran at a different time or the upstream was updated between runs.

### Article Update (PR #8208, merged 2024-10-01)

- **Title**: "Matemasie: Update article"
- **Author**: Nathan Willis (@n8willis)
- **Commit in google/fonts**: `7e509860f` (2024-10-01)
- **Upstream commit cited in body**: `982fb1ec023f63c0da05a11a2bec15efd1470484`
- **Upstream commit cited in commit message**: `a53371edff5c32131e93492ccb7618f4c567fbe0`
- **Files changed**: METADATA.pb (source block expanded), article images and HTML added

This update added social media images, expanded the ARTICLE.en_us.html, and updated the source block in METADATA.pb with file mappings. The font binary was not modified in this commit.

### Additional Related PRs

- **PR #7989** (merged 2024-08-01): "Matemasie description" by Viviana Monsalve (@vv-monsalve)
- **PR #8035** (merged 2024-08-16): "Add designer: Adam Yeo" by Viviana Monsalve
- **PR #8229** (merged 2024-10-01): "Matemasie image size fix" by Viviana Monsalve
- **PR #8253** (merged 2024-10-03): "Matemasie is failing to push" by Rod Sheeter (@rsheeter)

### Source Block Enrichment (Batch 2/4, commit 4ad8ac6)

The commit `4ad8ac6` (2025-03-31) by Felipe Sanches updated the source block:
- Changed commit hash from `a53371edff5c32131e93492ccb7618f4c567fbe0` to `a6dbde5f9eb448066e8c751ee4c5b4146a7fbc99`
- Added `config_yaml: "sources/config.yaml"`

The new hash `a6dbde5` was the only commit remaining in the repository after the force-push, and it was sourced from fontc_crater's targets list.

## Build Configuration

- **Config file**: `sources/config.yaml` in the upstream repo
- **Source format**: Glyphs 3 package (`.glyphspackage`)
- **Build tool**: gftools-builder (via Makefile)
- **Override config in google/fonts**: None (not needed; config existed in upstream)
- **METADATA.pb config_yaml field**: `sources/config.yaml` (correct)

## Findings

1. **Source block is complete**: The METADATA.pb contained all necessary fields — repository_url, commit, branch, config_yaml, and file mappings.

2. **Commit hash is the best available**: The referenced commit `a6dbde5` was the only commit available in the upstream repository. Since all prior history was lost due to a force-push, this was the only valid reference. The binary font file at this commit matched the one in google/fonts, confirming it contained the correct sources.

3. **Repository was force-pushed**: The upstream repository lost its entire commit history at some point (likely around the Oct 9, 2024 merge of PR #34). All previously referenced commit hashes (from PRs #7875 and #8208) no longer existed. This was a known risk with designer-maintained repositories.

4. **config.yaml is valid**: The upstream `sources/config.yaml` correctly referenced the `Matemasie.glyphspackage` source file.

5. **No corrections needed**: The current source block accurately represented the state of the upstream repository.

## Recommended Source Block

The current source block was correct and complete. No changes were needed:

```
source {
  repository_url: "https://github.com/YADAMSS/Matemasie-Font"
  commit: "a6dbde5f9eb448066e8c751ee4c5b4146a7fbc99"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Matemasie-Regular.ttf"
    dest_file: "Matemasie-Regular.ttf"
  }
  files {
    source_file: "ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/1.png"
    dest_file: "article/1.png"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/2.png"
    dest_file: "article/2.png"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/3.gif"
    dest_file: "article/3.gif"
  }
  files {
    source_file: "documentation/social-media-posts/1440px-x-765px/1/4.png"
    dest_file: "article/4.png"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
