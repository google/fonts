# LXGW WenKai TC — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/aaronbell/LxgwWenkaiTC"
  commit: "a5cf76f5bd1f26cdf74ca1b22b9f6fe17b8d5bc5"
  config_yaml: "sources/project.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiTC-Regular.ttf"
    dest_file: "LXGWWenKaiTC-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiTC-Light.ttf"
    dest_file: "LXGWWenKaiTC-Light.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiTC-Bold.ttf"
    dest_file: "LXGWWenKaiTC-Bold.ttf"
  }
}
```

## Repository Analysis

The `repository_url` in METADATA.pb points to `https://github.com/aaronbell/LxgwWenkaiTC`, which is Aaron Bell's **fork** of the original upstream repository `https://github.com/lxgw/LxgwWenkaiTC`.

- **Original upstream**: `lxgw/LxgwWenkaiTC` — created 2021-07-14, still actively maintained (last push 2026-03-03)
- **Fork used for onboarding**: `aaronbell/LxgwWenkaiTC` — created 2024-05-07, forked from `lxgw/LxgwWenkaiTC`, last pushed 2024-12-12

The fork was created by Aaron Bell specifically for the Google Fonts onboarding process. Aaron restructured the repo with a `sources/project.yaml` gftools-builder config, UFO sources, designspace files, and a Makefile-based build pipeline.

The cached repo at `upstream_repos/fontc_crater_cache/aaronbell/LxgwWenkaiTC` has HEAD detached at commit `a5cf76f5`, matching the referenced commit.

### Repository Structure (at commit a5cf76f5)

```
sources/
  project.yaml          — gftools-builder config
  features.fea          — OpenType feature code
  LXGWWenKaiTC-Bold.ufo/
  LXGWWenKaiTC-Light.ufo/
  LXGWWenKaiTC-Regular.ufo/
  LXGWWenKaiMonoTC-Bold.ufo/
  LXGWWenKaiMonoTC-Light.ufo/
  LXGWWenKaiMonoTC-Regular.ufo/
  LXGWWenKaiTC_common-Bold.ufoz
  LXGWWenKaiTC_common-Light.ufoz
  LXGWWenKaiTC_common-Regular.ufoz
  build/
    LXGWWenKaiTC-Bold.designspace
    LXGWWenKaiTC-Light.designspace
    LXGWWenKaiTC-Regular.designspace
    LXGWWenKaiMonoTC-Bold.designspace
    LXGWWenKaiMonoTC-Light.designspace
    LXGWWenKaiMonoTC-Regular.designspace
  scripts/
fonts/TTF/
  LXGWWenKaiTC-Bold.ttf
  LXGWWenKaiTC-Light.ttf
  LXGWWenKaiTC-Regular.ttf
  LXGWWenKaiMonoTC-Bold.ttf
  LXGWWenKaiMonoTC-Light.ttf
  LXGWWenKaiMonoTC-Regular.ttf
Makefile
```

### Build Process

The Makefile reveals a multi-step build process:
1. `extract` — runs `sources/scripts/extract.py` (likely extracts compressed UFO sources)
2. `merge` — runs `sources/scripts/merge.py` (merges common glyph sets)
3. `export` — runs `gftools builder sources/project.yaml`
4. `post` — runs `sources/scripts/post.py` (post-processing)

The `sources/project.yaml` references designspace files in `sources/build/`:
```yaml
sources:
  - build/LXGWWenKaiMonoTC-Bold.designspace
  - build/LXGWWenKaiMonoTC-Light.designspace
  - build/LXGWWenKaiMonoTC-Regular.designspace
  - build/LXGWWenKaiTC-Bold.designspace
  - build/LXGWWenKaiTC-Light.designspace
  - build/LXGWWenKaiTC-Regular.designspace
removeOutlineOverlaps: False
buildOTF: False
buildTTF: True
buildWebfont: False
autohintTTF: False
```

Note: The `project.yaml` builds both the TC and Mono TC families together.

## Onboarding History

The font was onboarded on 2024-05-16 via PR #7690 by Aaron Bell (`aaronbell`).

**PR #7690**: "LXGW WenKai TC: Version 1.330;April 28, 2024 added"
- Merged: 2024-05-17
- Branch: `gftools_packager_ofl_lxgwwenkaitc`
- Author: Aaron Bell
- PR body: "Taken from the upstream repo https://github.com/aaronbell/LxgwWenkaiTC at commit https://github.com/aaronbell/LxgwWenkaiTC/commit/a5cf76f5bd1f26cdf74ca1b22b9f6fe17b8d5bc5."

**Initial commit** (590eaaa6a): Added 6 files — DESCRIPTION, 3 TTF fonts, METADATA.pb, OFL.txt

The font files were taken as **pre-built binaries** from `fonts/TTF/` in the upstream repo. All three font files match exactly in size between the upstream commit and google/fonts:
- LXGWWenKaiTC-Bold.ttf: 12,881,104 bytes
- LXGWWenKaiTC-Light.ttf: 13,771,744 bytes
- LXGWWenKaiTC-Regular.ttf: 13,110,528 bytes

**Subsequent changes to METADATA.pb**:
- `53995c52a` (2025-03-25): Added `config_yaml: "sources/project.yaml"` field, removed `branch: "main"` field

## Build Configuration

The upstream repo at `aaronbell/LxgwWenkaiTC` has a `sources/project.yaml` that serves as the gftools-builder config. The current METADATA.pb correctly references `config_yaml: "sources/project.yaml"`.

However, the build process is non-trivial: the Makefile shows that `gftools builder` is only one step in a multi-step pipeline involving custom Python scripts for extraction, merging, and post-processing. A simple `gftools builder sources/project.yaml` run may not fully reproduce the fonts without the preceding steps.

No override `config.yaml` exists in the google/fonts family directory.

## Findings

### Issue 1: Repository URL Points to Fork, Not Original Upstream

The `repository_url` points to `aaronbell/LxgwWenkaiTC`, which is a fork of the original `lxgw/LxgwWenkaiTC`. The copyright string in the fonts themselves references the original: `https://github.com/lxgw/LxgwWenkaiTC`.

Aaron Bell created the fork specifically for onboarding — he added the gftools-builder infrastructure (project.yaml, designspace files, Makefile, build scripts) that did not exist in the original repo. The referenced commit `a5cf76f5` exists in both repos (it was pushed to the fork and the original accepted it).

**Assessment**: The `repository_url` pointing to the fork is **intentional and correct for build purposes**, since the fork contains the build infrastructure. The original `lxgw/LxgwWenkaiTC` repo does not have a `sources/project.yaml` or the gftools-builder setup. However, ideally the `repository_url` should point to the canonical upstream repo, with the build infrastructure contributed there.

### Issue 2: Complex Build Pipeline

The `config_yaml` field references `sources/project.yaml`, but the actual build requires running custom scripts (extract, merge) before `gftools builder`. A standalone `gftools builder sources/project.yaml` invocation may not produce correct results without the prerequisite steps. This could be an issue for automated rebuild systems like fontc_crater.

### Issue 3: Newer Commits in Fork

The fork at `aaronbell/LxgwWenkaiTC` has commits after `a5cf76f5` (up to 2024-12-12), including:
- Updated feature code and bumped version string
- Added Chinese characters
- Glyph order rearrangements

These newer commits have not been incorporated into google/fonts.

### Summary

The commit hash `a5cf76f5` is **verified correct** — it matches the onboarding PR, the commit message, the binary file sizes, and the PR author's explicit reference. The source block data is largely accurate but the repository_url pointing to a fork rather than the canonical upstream is a potential concern.

## Recommended Source Block

The current source block is acceptable as-is, since the fork contains the necessary build infrastructure. However, if a correction is desired:

```
source {
  repository_url: "https://github.com/aaronbell/LxgwWenkaiTC"
  commit: "a5cf76f5bd1f26cdf74ca1b22b9f6fe17b8d5bc5"
  config_yaml: "sources/project.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiTC-Regular.ttf"
    dest_file: "LXGWWenKaiTC-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiTC-Light.ttf"
    dest_file: "LXGWWenKaiTC-Light.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiTC-Bold.ttf"
    dest_file: "LXGWWenKaiTC-Bold.ttf"
  }
}
```

No changes to the source block are strictly required. The current data is accurate — the repository URL, commit hash, config_yaml path, and file mappings all check out. The `branch` field was correctly removed in a prior update.

The key consideration for the future is whether the build infrastructure should be contributed back to the canonical `lxgw/LxgwWenkaiTC` repo so the `repository_url` can point there instead.
