# Luxurious Script — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The METADATA.pb at `ofl/luxuriousscript/METADATA.pb` already contains a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/luxurious"
  commit: "234fe6f071f7e4450893f159a4ca3512310c66ee"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LuxuriousScript-Regular.ttf"
    dest_file: "LuxuriousScript-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Repository Analysis

- **Repository**: https://github.com/googlefonts/luxurious
- **Created**: 2021-02-24
- **Default branch**: master
- **Last push**: 2021-11-04
- **Status**: Valid and accessible

The repository contains a single commit (`234fe6f`, "CI fixed", 2021-11-03) after a force-push that squashed the original history. The repo structure is:

- `sources/Luxurious-Script.glyphs` — Glyphs source file
- `sources/config.yml` — gftools-builder configuration
- `fonts/ttf/LuxuriousScript-Regular.ttf` — compiled TTF binary
- `fonts/otf/LuxuriousScript-Regular.otf` — compiled OTF binary
- `fonts/webfonts/LuxuriousScript-Regular.woff2` — compiled WOFF2 binary
- `OFL.txt`, `DESCRIPTION.en_us.html`, `README.md`, `AUTHORS.txt`, `CONTRIBUTORS.txt`

The `config.yml` at `sources/config.yml` contains:

```yaml
sources:
  - Luxurious-Script.glyphs
familyName: "Luxurious Script"
buildVariable: false
#autohintTTF: false
```

The repository was clean and up-to-date with its remote at the time of investigation.

## Onboarding History

The font was added to Google Fonts on 2021-11-02 (per `date_added`) and merged on 2021-11-03 via PR #4003.

**PR #4003**: "Luxurious Script: Version 1.010; ttfautohint (v1.8.3) added"
- **Author**: Viviana Monsalve (@vv-monsalve)
- **Merged**: 2021-11-03
- **gftools-packager message**: Referenced upstream commit `884bf55ce7b09e8914b959481af6084cb09b1e75` at `https://github.com/googlefonts/luxurious`
- The PR also contained a second commit removing the METADATA "source" block per issue google/fonts#2587

**Commit history reconstruction**: The upstream repo's history was force-pushed on the same day as the onboarding merge. The original commit chain was:

1. `935cbbb` — "v1.010 fonts added" (2021-11-03T01:34:32Z) — initial commit with fonts in `fonts/Script/` subdirectory
2. `884bf55` — "repo structure rearranged" (2021-11-03T03:18:07Z) — moved files from `fonts/Script/{otf,ttf}` to `fonts/{otf,ttf}`, commented out `outputDir` in config.yml. **This was the commit gftools-packager used.**
3. `234fe6f` — "CI fixed" (2021-11-03T20:31:55Z) — force-pushed as a single squashed commit, adding CI workflow and all files in their final structure. **This is the only commit visible in the current repo.**

These orphaned commits (884bf55 and 935cbbb) are still accessible via the GitHub API but not via `git log` in the local clone.

**Binary verification**: The TTF file in google/fonts (`ofl/luxuriousscript/LuxuriousScript-Regular.ttf`, 387,952 bytes) was confirmed identical to the TTF in the upstream repo at commit 234fe6f (matching MD5: `ec13b6616638bf5e248ba7668eca8199`). Since 884bf55 only reorganized directory structure without modifying the TTF binary, both commits contain the same font binary.

## Build Configuration

- **Config file**: `sources/config.yml` (present in the upstream repo)
- **Source**: `Luxurious-Script.glyphs` (Glyphs format)
- **Build type**: Static only (`buildVariable: false`)
- **Override config in google/fonts**: None

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

## Source Block Construction

The source block was added in two stages:
1. **Commit `66f91f10f`** (2024-04-03) by Simon Cozens: "Merge upstream.yaml into METADATA.pb" — added the repository_url, files, and branch fields
2. **Commit `4ad8ac680`** (2025-03-31) by Felipe Sanches: "[Batch 2/4] port info from fontc_crater targets list" — added commit hash and config_yaml fields

## Findings

1. **Source block is complete and correct.** The METADATA.pb has repository_url, commit hash, file mappings, branch, and config_yaml all properly set.

2. **Commit hash discrepancy is benign.** The METADATA.pb references commit `234fe6f` (the only surviving commit after force-push), while the original gftools-packager in PR #4003 referenced commit `884bf55` (now orphaned). Both commits contain identical TTF binaries. The current commit hash (`234fe6f`) is the correct one to use because it is the only commit accessible via normal git operations on the repository.

3. **The `config_yaml` field correctly uses `.yml` extension** (not `.yaml`), matching the actual file in the upstream repo.

4. **No action needed.** The source block is complete with all required fields and the data is accurate.

## Recommended Source Block

The current source block is correct and complete. No changes are recommended:

```
source {
  repository_url: "https://github.com/googlefonts/luxurious"
  commit: "234fe6f071f7e4450893f159a4ca3512310c66ee"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LuxuriousScript-Regular.ttf"
    dest_file: "LuxuriousScript-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```
