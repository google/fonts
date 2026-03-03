# LXGW WenKai Mono TC — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

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
    source_file: "fonts/TTF/LXGWWenKaiMonoTC-Regular.ttf"
    dest_file: "LXGWWenKaiMonoTC-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiMonoTC-Light.ttf"
    dest_file: "LXGWWenKaiMonoTC-Light.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiMonoTC-Bold.ttf"
    dest_file: "LXGWWenKaiMonoTC-Bold.ttf"
  }
  branch: "main"
}
```

## Repository Analysis

The METADATA.pb `repository_url` points to `https://github.com/aaronbell/LxgwWenkaiTC`, which is a **fork** of the original upstream repository `https://github.com/lxgw/LxgwWenkaiTC` ("The Traditional Chinese Edition of LXGW WenKai"). The fork was created on 2024-05-07 by Aaron Bell (aaronbell), who is the font engineer that onboarded this family to Google Fonts.

The original `lxgw/LxgwWenkaiTC` repository is actively maintained (714 stars, 12 forks as of investigation date) and has continued to receive updates (latest commits from March 2026, version 1.522+). However, the aaronbell fork has not been updated since its creation period — its last push was 2024-12-12.

The copyright notice in the font files and OFL.txt references `https://github.com/lxgw/LxgwWenkaiTC`, not the aaronbell fork. This is notable because the METADATA.pb `repository_url` points to the fork rather than the original upstream. The aaronbell fork was used specifically for the onboarding process where Aaron Bell restructured the sources for gftools-builder compatibility.

### Upstream Repo Structure (aaronbell/LxgwWenkaiTC at referenced commit)

```
├── documentation/
├── fonts/
│   └── TTF/
│       ├── LXGWWenKaiMonoTC-Bold.ttf
│       ├── LXGWWenKaiMonoTC-Light.ttf
│       ├── LXGWWenKaiMonoTC-Regular.ttf
│       ├── LXGWWenKaiTC-Bold.ttf
│       ├── LXGWWenKaiTC-Light.ttf
│       └── LXGWWenKaiTC-Regular.ttf
├── sources/
│   ├── build/
│   │   ├── instance_ufos/
│   │   ├── LXGWWenKaiMonoTC-Bold.designspace
│   │   ├── LXGWWenKaiMonoTC-Light.designspace
│   │   ├── LXGWWenKaiMonoTC-Regular.designspace
│   │   ├── LXGWWenKaiTC-Bold.designspace
│   │   ├── LXGWWenKaiTC-Light.designspace
│   │   └── LXGWWenKaiTC-Regular.designspace
│   ├── LXGWWenKaiMonoTC-Bold.ufo
│   ├── LXGWWenKaiMonoTC-Light.ufo
│   ├── LXGWWenKaiMonoTC-Regular.ufo
│   ├── LXGWWenKaiTC-Bold.ufo
│   ├── LXGWWenKaiTC-Light.ufo
│   ├── LXGWWenKaiTC-Regular.ufo
│   ├── LXGWWenKaiTC_common-Bold.ufoz
│   ├── LXGWWenKaiTC_common-Light.ufoz
│   ├── LXGWWenKaiTC_common-Regular.ufoz
│   ├── features.fea
│   ├── project.yaml
│   └── scripts/
├── Makefile
├── OFL.txt
├── README.md
└── requirements.txt
```

The repository contains both Mono TC and non-Mono TC variants of LXGW WenKai. The font sources are UFO files with designspace files in the `sources/build/` directory. Each designspace references a single UFO source (single-master fonts, not variable).

## Onboarding History

The font was onboarded to Google Fonts on **2024-05-16** via **PR #7691** ("LXGW WenKai Mono TC: Version 1.330 added"), authored by Aaron Bell (aaronbell). The PR was merged on **2024-05-17**.

The onboarding commit `9413469b3` explicitly stated:
> "Taken from the upstream repo https://github.com/aaronbell/LxgwWenkaiTC at commit https://github.com/aaronbell/LxgwWenkaiTC/commit/a5cf76f5bd1f26cdf74ca1b22b9f6fe17b8d5bc5."

The referenced commit `a5cf76f5` ("Fixing path directions for common set") was the HEAD of the aaronbell fork at the time. It was authored on 2024-05-16, the same day as the onboarding commit.

### Binary File Verification

All three TTF files in google/fonts are **byte-identical** to the files at the referenced commit in the upstream repo:
- LXGWWenKaiMonoTC-Bold.ttf: 12,885,112 bytes (match)
- LXGWWenKaiMonoTC-Light.ttf: 13,769,976 bytes (match)
- LXGWWenKaiMonoTC-Regular.ttf: 13,122,932 bytes (match)

### Subsequent METADATA.pb Changes

1. **2024-05-16/17**: Initial METADATA.pb created with source block (repository_url, commit, files, branch)
2. **2024-05-17 to 2024-06-07**: Various metadata updates (CJK subset policies, primary_language additions/reversions)
3. **2025-03-25** (commit `53995c52`): `config_yaml: "sources/project.yaml"` was added and `branch: "main"` was removed
4. **2025-03-26** (commit `f19b6da7d`): `branch: "main"` was re-added (revert of branch removal)
5. **2025-04-02**: Classification updated to Chinese Traditional
6. **2025-04-09**: Article images added

## Build Configuration

The upstream repository has a valid gftools-builder configuration file at `sources/project.yaml`:

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

The Makefile confirms this is the intended build config: `gftools builder sources/project.yaml`.

Note: The config builds both Mono TC and non-Mono TC variants from the same repository. The designspace files each reference a single UFO master, making these single-master static fonts (not variable).

## Findings

1. **Source block is complete and correct.** The repository_url, commit hash, config_yaml, and file mappings are all accurate and verified.

2. **Commit hash is verified.** The commit `a5cf76f5bd1f26cdf74ca1b22b9f6fe17b8d5bc5` was the HEAD of the aaronbell fork at onboarding time (2024-05-16). Binary files at this commit are byte-identical to those in google/fonts. The onboarding commit message explicitly references this commit.

3. **Repository URL points to a fork, not the original.** The METADATA.pb `repository_url` points to `aaronbell/LxgwWenkaiTC` (a fork), while the copyright notice references `lxgw/LxgwWenkaiTC` (the original). This is intentional: Aaron Bell forked the original repo, restructured the sources for gftools-builder compatibility (adding UFO files, designspace files, project.yaml, and a Makefile), and onboarded from his fork. The original `lxgw/LxgwWenkaiTC` repo does not have this build infrastructure. The fork is the correct repository URL for the purpose of source metadata since it contains the actual buildable sources.

4. **Config path is correct.** `sources/project.yaml` exists in the upstream repo and is a valid gftools-builder config file.

5. **No corrections needed.** All fields in the current source block are accurate.

## Recommended Source Block

The current source block is correct. No changes are recommended:

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
    source_file: "fonts/TTF/LXGWWenKaiMonoTC-Regular.ttf"
    dest_file: "LXGWWenKaiMonoTC-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiMonoTC-Light.ttf"
    dest_file: "LXGWWenKaiMonoTC-Light.ttf"
  }
  files {
    source_file: "fonts/TTF/LXGWWenKaiMonoTC-Bold.ttf"
    dest_file: "LXGWWenKaiMonoTC-Bold.ttf"
  }
  branch: "main"
}
```
