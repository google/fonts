# Love Light — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/love-light"
  commit: "e4fc541136be7d2814ac542a930be1ebaa17b5e1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LoveLight-Regular.ttf"
    dest_file: "LoveLight-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Repository Analysis

- **Repository**: https://github.com/googlefonts/love-light
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/love-light`
- **Remote verified**: Yes, matches `https://github.com/googlefonts/love-light`
- **Repo status**: Clean, up-to-date with origin/master
- **Branches**: `master` only
- **Total commits**: 1 (initial commit only)

The repository contains a single commit (`e4fc541`) dated 2021-11-30, authored by Viviana Monsalve. This is both the initial and the only commit in the repository.

### Source Files

- `sources/LoveLight.glyphs` — Glyphs source file
- `sources/config.yml` — gftools-builder configuration

### Build Configuration (sources/config.yml)

```yaml
sources:
  - LoveLight.glyphs
familyName: "Love Light"
buildVariable: false
# autohintTTF: false
```

The config references a single Glyphs source and builds a static (non-variable) font family.

### Font Outputs in Upstream Repo

- `fonts/ttf/LoveLight-Regular.ttf`
- `fonts/otf/LoveLight-Regular.otf`
- `fonts/webfonts/LoveLight-Regular.woff2`

## Onboarding History

Love Light was added to Google Fonts on 2021-12-08 via PR #4135, titled "Love Light: Version 1.010; ttfautohint (v1.8.3) added". The PR was authored by Viviana Monsalve (vv-monsalve) and merged as commit `6612051d7`.

The PR body confirmed the font was taken from the upstream repo at commit `e4fc541136be7d2814ac542a930be1ebaa17b5e1`, using gftools-packager.

### Binary Verification

The SHA-256 hash of `LoveLight-Regular.ttf` in google/fonts matches the binary in the upstream repo at the referenced commit exactly:
`2036790ee211f84616197d5bdb90cd519d51a20013df2ffb8c9f3df996f1e016`

This confirms the commit hash is correct — the font binary in google/fonts was taken directly from this commit.

### Source Block History

The source block was originally added during onboarding (PR #4135) with `repository_url`, `files`, and `branch` fields. A subsequent gftools-packager invocation removed the source block (referenced in the same PR body as issue google/fonts#2587). The source block was later restored via the "Merge upstream.yaml into METADATA.pb" batch process (`66f91f10f`). The `commit` and `config_yaml` fields were added by the "[Batch 2/4] port info from fontc_crater targets list" commit (`4ad8ac680`), which ported data from fontc_crater's target.json.

## Build Configuration

The upstream repo has a valid `sources/config.yml` at the referenced commit. The METADATA.pb correctly references it as `config_yaml: "sources/config.yml"`. Note the `.yml` extension (not `.yaml`), which matches the actual file in the upstream repo.

## Findings

1. **Repository URL**: Correct. Points to `https://github.com/googlefonts/love-light`.
2. **Commit hash**: Correct. `e4fc541` is the only commit in the repo and matches the binary in google/fonts (SHA-256 verified).
3. **Config path**: Correct. `sources/config.yml` exists in the upstream repo at the referenced commit with valid gftools-builder configuration.
4. **Branch**: Correct. The repo has only the `master` branch.
5. **No corrections needed**: All source block fields are accurate and complete.

## Recommended Source Block

The current source block is correct and complete. No changes are recommended.

```
source {
  repository_url: "https://github.com/googlefonts/love-light"
  commit: "e4fc541136be7d2814ac542a930be1ebaa17b5e1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LoveLight-Regular.ttf"
    dest_file: "LoveLight-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```
