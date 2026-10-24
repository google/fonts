# Iosevka Charon — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `iosevkacharon`
**Status**: complete (no config — Iosevka custom build system)

## Initial State

METADATA.pb already contained a complete source block with:
- `repository_url`: `https://github.com/jul-sh/iosevka-charon`
- `commit`: `727f1343e957cadd354f9ec4ee98eba9b645143d`
- `archive_url`: `https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip`
- `branch`: `main`
- File mappings for all 8 TTF files (Light, LightItalic, Regular, Italic, Medium, MediumItalic, Bold, BoldItalic) from `iosevkacharon/` subdirectory in the release archive
- No `config_yaml` field (expected — see below)
- No override `config.yaml` in the google/fonts family directory
- No DESCRIPTION.en_us.html file

## Investigation

### Onboarding History

The font was onboarded via **PR #10245** ("Iosevka Charon: Version 34.100 added"), authored by **Emma Marichal** (emmamarichal), created on 2026-02-19 and merged on 2026-02-27.

The initial commit `3d418cc3ab7320c8493efebdb8048d24f3c65e25` explicitly references the upstream repo and commit:
> "Taken from the upstream repo https://github.com/jul-sh/iosevka-charon at commit https://github.com/jul-sh/iosevka-charon/commit/727f1343e957cadd354f9ec4ee98eba9b645143d."

The PR body repeats this same information. The PR contained 5 commits total:
1. `3d418cc` — Initial onboarding (fonts, METADATA.pb, OFL.txt)
2. `335885b` — Add article
3. `ac3fea7` — Update OFL link
4. `a7c1e55` — Fix formatting and content of OFL.txt
5. `13394c5` — Refine description of Iosevka Charon font

A sibling PR #10247 ("Iosevka Charon Mono: Version 34.100 added") was also merged on the same date for the monospace variant.

### Commit Hash Verification

The referenced commit `727f1343e957cadd354f9ec4ee98eba9b645143d` was verified in the upstream repo:
- It is a merge commit dated **2026-02-13**: "Merge pull request #16 from jul-sh/v34.1.0-w-almost-flat-top"
- It is tagged as **v34.100** in the upstream repo
- The `pre-727f1343e957cadd354f9ec4ee98eba9b645143d` tag also exists, pointing to the same commit
- The archive URL (`v34.100` release) corresponds to this exact commit

Timeline is consistent: upstream commit (Feb 13) predates the google/fonts onboarding commit (Feb 19) and PR merge (Feb 27).

Two commits exist after the referenced commit in the upstream repo:
- `5501bc4` (2026-02-20) — "Update README description" (README.md only)
- `343fcf7` (2026-02-20) — "Fix stray conflict marker text in README" (README.md only)

Both are documentation-only changes that do not affect font files.

### Build System Analysis

Iosevka Charon uses a **custom build system** that is fundamentally incompatible with gftools-builder:
- Fonts are built from the [Iosevka](https://github.com/be5invis/Iosevka) source using a Node.js-based build pipeline
- The `sources/iosevka/` directory is a git subtree of the upstream Iosevka project
- Build configuration is in `sources/private-build-plans.toml` (TOML format, Iosevka-specific)
- The build process uses a Makefile with Nix-based dependency management
- Post-processing scripts in `scripts/` handle Google Fonts compliance
- There are **no** `.glyphs`, `.ufo`, or `.designspace` files — the source format is Iosevka's custom parametric system

Since there are no gftools-builder compatible sources, a `config.yaml` is neither present nor applicable. The fonts are distributed as pre-built TTFs via GitHub releases, and the `archive_url` + `files` mapping in METADATA.pb correctly reflects this distribution method.

### Repository Details

- **Owner/Repo**: jul-sh/iosevka-charon
- **Designer**: Juliette Pluto (jul-sh)
- **License**: SIL OFL 1.1 (fonts), MIT (code/docs)
- **Copyright**: "Copyright 2015-2025 The Iosevka Project Authors (https://github.com/be5invis/Iosevka)"

## Actions Taken

No changes were needed. The source block in METADATA.pb is already complete and accurate. The upstream repo was cloned to the cache at `upstream_repos/fontc_crater_cache/jul-sh/iosevka-charon/` for reference.

## Final State

The METADATA.pb source block is complete with repository URL, commit hash, archive URL, branch, and file mappings. No `config_yaml` is needed because the project uses Iosevka's custom build system (not gftools-builder). The commit hash `727f134` has been verified against the upstream repo and matches the v34.100 tag.

## Source Block

```
source {
  repository_url: "https://github.com/jul-sh/iosevka-charon"
  commit: "727f1343e957cadd354f9ec4ee98eba9b645143d"
  archive_url: "https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Light.ttf"
    dest_file: "IosevkaCharon-Light.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-LightItalic.ttf"
    dest_file: "IosevkaCharon-LightItalic.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Regular.ttf"
    dest_file: "IosevkaCharon-Regular.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Italic.ttf"
    dest_file: "IosevkaCharon-Italic.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Medium.ttf"
    dest_file: "IosevkaCharon-Medium.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-MediumItalic.ttf"
    dest_file: "IosevkaCharon-MediumItalic.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Bold.ttf"
    dest_file: "IosevkaCharon-Bold.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-BoldItalic.ttf"
    dest_file: "IosevkaCharon-BoldItalic.ttf"
  }
  branch: "main"
}
```
