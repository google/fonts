# Mada — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/aliftype/mada"
  commit: "2f7dea3a2bad718583bfcc1dc2030cf15401c789"
  archive_url: "https://github.com/aliftype/mada/releases/download/v1.5/Mada-1.5.zip"
  files {
    source_file: "Mada-1.5/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Mada-1.5/Mada.ttf"
    dest_file: "Mada[wght].ttf"
  }
  branch: "main"
}
```

An override `config.yaml` also exists in the google/fonts family directory with contents:

```yaml
buildVariable: true
sources:
  - sources/Mada.glyphs
```

No `config_yaml` field is set in the source block, which is correct since google-fonts-sources auto-detects the local override.

## Repository Analysis

- **Repository**: https://github.com/aliftype/mada
- **Owner/Org**: aliftype (Khaled Hosny's organization)
- **Cached locally**: Yes, at `upstream_repos/fontc_crater_cache/aliftype/mada/`
- **Repo status**: Clean, up to date with origin
- **Branches**: main only
- **Total commits**: 819
- **Tags**: v0.1, v0.2, v0.3, v1.0, v1.1, v1.2, v1.3, v1.4, v1.5

The repository is authored primarily by Khaled Hosny, with Paul Hunt (Adobe) credited as a contributor. The font is an Arabic sans-serif family with a weight axis (200-900).

### Source Files

At the referenced commit `2f7dea3a` (v1.5 tag), the source was a single Glyphs file:
- `sources/Mada.glyphs` (85,624 lines, Glyphs format v3, appVersion 3187)

The source was later converted to `.glyphspackage` format in commit `b3cd0c16` (2024-09-07), well after the v1.5 release. The current HEAD uses `sources/Mada.glyphspackage/`.

### Build System

The upstream repo used a custom `Makefile` for building (using `fontmake` directly), not gftools-builder. There was no `config.yaml` in the upstream repo at any point. The CI workflow (`.github/workflows/build.yml`) ran `make -j -B dist` using fontmake.

## Onboarding History

### Initial Onboarding (2017)

- **First addition**: Commit `e1421015` (2017-05-08) — "hotfix-mada: v1.005 added (#938)". This was PR #938, indicating Mada was originally onboarded as static instances.
- **Update**: Commit `82724194` (2017-07-26) — "mada: v1.004 added (#1078)". Despite the version number appearing lower, this was a subsequent update.

### Variable Font Update — v1.5 (2023)

- **Key commit**: `1426542a` (2023-04-26) — "[gftools-packager] Mada: Version 1.5 added"
  - This was a major update that replaced the 7 static TTF instances with a single variable font `Mada[wght].ttf`
  - The commit body referenced the upstream repo but had an incomplete commit URL: "at commit https://github.com/aliftype/mada/commit/." (missing the hash)
  - The upstream.yaml included with this commit specified `branch: main` and the archive URL for the v1.5 release
  - Filed by Khaled Hosny himself, merged in PR #5594 (titled "Mada: Version 1.5 added (#5594)") by Rosalie Wagner on 2023-04-26
  - PR #5594 was merged on 2022-11-23 for v1.4, then the same PR was reused or a separate one for v1.5 — the gftools-packager commit was dated 2023-04-26

### Source Block Addition (2025)

- **Commit**: `e9bcb1b9` (2025-12-02) — "sources info for Mada: Version 1.5 (PR #5603)"
  - Added the source block to METADATA.pb and the override `config.yaml`
  - This was part of the broader source metadata enrichment effort

### Other Changes

- `314edc18` (2023-04-26): Updated description
- `66f91f10` (2024-04-03): Merged upstream.yaml into METADATA.pb
- `3012bb6a` (2022-11-23): Added `primary_script: "Arab"`
- Various METADATA.pb updates for languages, designer info, etc.

## Build Configuration

- **Upstream config.yaml**: None. The upstream repo never had a `config.yaml`. It used a custom Makefile with direct fontmake invocations.
- **Override config.yaml**: Present in google/fonts family directory, correctly referencing `sources/Mada.glyphs`
- **config_yaml in METADATA.pb**: Not set (correct, since the override is auto-detected)
- **Build approach**: The override config enables gftools-builder to build the variable TTF from the `.glyphs` source

The override config.yaml is appropriate because:
1. The upstream repo uses fontmake via Makefile, not gftools-builder
2. The source file `sources/Mada.glyphs` exists at the referenced commit
3. The config correctly specifies `buildVariable: true` matching the variable font output

## Findings

1. **Commit hash is correct and verified**: The commit `2f7dea3a` in METADATA.pb matches the v1.5 tag exactly. The tag was created by Khaled Hosny on 2023-04-19, and the font was added to google/fonts on 2023-04-26 via gftools-packager.

2. **Archive URL is valid**: The release archive `v1.5/Mada-1.5.zip` was used by gftools-packager to import the pre-built binary, not built from source.

3. **Source block is complete**: The source block has all necessary fields — `repository_url`, `commit`, `archive_url`, `files` mappings, and `branch`.

4. **Override config.yaml is correct**: The override properly references `sources/Mada.glyphs` which is the source file at the v1.5 commit. No `config_yaml` field is needed in METADATA.pb.

5. **Post-v1.5 upstream activity**: There are approximately 20+ commits after v1.5 on the main branch, including conversion to `.glyphspackage` format, Kashmiri anchor additions, and various fixes. These would need separate review before being incorporated into Google Fonts.

6. **Incomplete commit URL in original PR**: The gftools-packager commit body had an incomplete URL ("at commit .../commit/."), but this was a known issue with gftools-packager at the time. The correct commit was recoverable from the v1.5 tag.

## Recommended Source Block

The current source block is already correct and complete. No changes are needed:

```
source {
  repository_url: "https://github.com/aliftype/mada"
  commit: "2f7dea3a2bad718583bfcc1dc2030cf15401c789"
  archive_url: "https://github.com/aliftype/mada/releases/download/v1.5/Mada-1.5.zip"
  files {
    source_file: "Mada-1.5/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Mada-1.5/Mada.ttf"
    dest_file: "Mada[wght].ttf"
  }
  branch: "main"
}
```

The override `config.yaml` in the google/fonts family directory is also correct:

```yaml
buildVariable: true
sources:
  - sources/Mada.glyphs
```

**Confidence**: HIGH — The commit hash matches the v1.5 tag exactly, the source block was already populated with verified data, and the override config.yaml correctly references the source file at the tagged commit.
