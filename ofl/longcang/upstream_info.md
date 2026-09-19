# Long Cang — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

No source block exists in METADATA.pb. The file contains basic font metadata (name, designer, license, category, date_added, fonts, subsets, primary_script) but no `source { }` block with repository_url, commit hash, or config_yaml.

## Repository Analysis

**Repository**: https://github.com/m4rc1e/longcang
**Default branch**: master
**Archived**: No
**Fork**: No

The copyright string in METADATA.pb and OFL.txt references `https://github.com/googlefonts/longcang`, but that repository does not exist (returns 404). The actual upstream repository is at `https://github.com/m4rc1e/longcang`, maintained by Marc Foley.

The repository has only 3 commits:

| Commit | Date | Message |
|--------|------|---------|
| `37b9a6c` | 2019-05-08 | uncamelcase names |
| `3b48ca7` | 2019-02-13 | updated ofl copyright string |
| `969c9b5` | 2019-02-13 | First commit |

### Repository Structure

```
.ci/
  run_fb.sh
  viz_pr.py
fonts/
  LongCang-Regular.ttf
sources/
  build.sh
  LongCang.glyphs
.gitignore
.travis.yml
OFL.txt
README.md
requirements.txt
```

### Source Files

- `sources/LongCang.glyphs` — Glyphs source file (37 MB), family name "Long Cang"
- `sources/build.sh` — Custom shell build script using `gftools fix-dsig` and `gftools fix-nonhinting`

The build process was not gftools-builder based; it used a custom shell script that applied post-processing fixes to an already-compiled TTF. The `.glyphs` source file is compatible with gftools-builder, so an override config.yaml can be created.

## Onboarding History

### Initial Onboarding (v2.000)

- **PR**: [#1852](https://github.com/google/fonts/pull/1852) — "longcang: v2.000 added"
- **Author**: Marc Foley (m4rc1e)
- **Merged**: 2019-03-15
- **Commit in google/fonts**: `784037aa9567639573ce7b2f8ad41c17ab9ebbe3`
- **Referenced upstream commit**: `3b48ca703015194520219386a91944b96e0410f3` (2019-02-13, "updated ofl copyright string")

### Update (v2.001)

- **Commit in google/fonts**: `20da2e7644bac5325abbc9f30848ae3162bfc974`
- **Author**: Marc Foley
- **Date**: 2019-05-08
- **Commit message**: "longcang: v2.001 added — Taken from the upstream repo https://github.com/m4rc1e/longcang at commit https://github.com/m4rc1e/longcang/commit/37b9a6c0b6e1f07d3d2bd4fb2674050be72b98a6"
- **Referenced upstream commit**: `37b9a6c0b6e1f07d3d2bd4fb2674050be72b98a6` (2019-05-08, "uncamelcase names")
- **No associated PR** — committed directly without a pull request

### Binary Verification

The SHA256 hash of the font file in google/fonts matches the font file at commit `37b9a6c` in the upstream repo:
- SHA256: `e5bf2c3f24ef2327c6f136d8f73e2f9dfdf44896fdbeb35a9515f44777bb91bc`

This confirms `37b9a6c0b6e1f07d3d2bd4fb2674050be72b98a6` is the correct onboarding commit for the current version in google/fonts. This is also the latest (and most recent) commit in the upstream repo.

## Build Configuration

No `config.yaml` exists in the upstream repository. The original build process used a custom `sources/build.sh` script.

Since the source file is a `.glyphs` file, an override `config.yaml` can be created for gftools-builder in the google/fonts family directory.

### Recommended Override config.yaml

```yaml
sources:
  - sources/LongCang.glyphs
```

## Findings

1. **No source block** in METADATA.pb — needs to be added.
2. **Repository URL discrepancy**: The copyright string references `googlefonts/longcang` which does not exist. The actual repo is `m4rc1e/longcang`.
3. **Correct upstream commit**: `37b9a6c0b6e1f07d3d2bd4fb2674050be72b98a6` — confirmed via SHA256 binary match. This is the latest commit in the repo (HEAD of master).
4. **No config.yaml** in the upstream repo — an override config.yaml should be placed in the google/fonts family directory.
5. **Simple repo**: Only 3 commits, all by Marc Foley, all in February-May 2019.
6. **Chinese handwriting font**: The font's Chinese name is "有字库龙藏体" (YouZiKu LongCang Ti), designed by Chen Xiaomin, trademarked by ZHONGQI Electronic Co., Shanghai.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/m4rc1e/longcang"
  commit: "37b9a6c0b6e1f07d3d2bd4fb2674050be72b98a6"
}
```

Note: `config_yaml` is omitted because an override `config.yaml` should be placed in the google/fonts family directory. The google-fonts-sources tool will auto-detect the local override.
