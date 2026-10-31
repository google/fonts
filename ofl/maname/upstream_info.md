# Maname — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/mooniak/maname-font"
  commit: "626ceee1311626c5240a68b0ef27722f44c374af"
  archive_url: "https://github.com/mooniak/maname-font/releases/download/v1.002/maname-font-v1.002.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Maname-Regular.ttf"
    dest_file: "Maname-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

The source block is fully populated with repository URL, commit hash, archive URL, file mappings, branch, and config_yaml path.

## Repository Analysis

**Upstream repository**: https://github.com/mooniak/maname-font
**Designers**: Pathum Egodawatta, Mooniak
**Primary script**: Sinhala (Sinh)

The upstream repository is hosted by the Mooniak foundry. The cached clone was verified clean and up-to-date with origin/main.

**Repository structure at commit 626ceee**:
- `sources/Maname.glyphspackage/` — Glyphs 3 package format source
- `sources/config.yaml` — gftools-builder configuration file
- `.github/workflows/build.yaml` — CI build workflow
- `documentation/` — documentation and test suite
- `scripts/customize.py` — customization script
- `fontpackage.toml` — font package configuration
- `Makefile` — build system

The repository has a single branch (`main`) and one tag (`v1.002`). The tag v1.002 points directly to commit `626ceee1311626c5240a68b0ef27722f44c374af`, confirming it is the release commit.

There is only one commit in the repository's history (626ceee), which suggests the repository was initialized or force-pushed at some point with all files in a single commit.

## Onboarding History

### Initial onboarding (v1.000)

- **Issue**: google/fonts#3842 ("Add Maname")
  - Body: "upstream: https://github.com/mooniak/maname-font"
  - Closed: 2024-06-21
- **Commit**: `9ef6fb6fb837ddc86157fb3c521860c34a03597c` (2024-06-17)
  - Author: Yanone (post@yanone.de)
  - Message: "Maname: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added"
  - Referenced upstream commit: `45ff5d76e1cd1beab81bcfdb00ef1d6bf25659d1`
- **Date added to Google Fonts**: 2024-06-14

### Update to v1.002

- **Issue**: google/fonts#8323 ("Update Maname")
  - Body: Requested update from v1.000 to v1.001 to patch an issue in the `Sri` glyph
  - Closed: 2025-01-21
- **PR**: google/fonts#8971 ("Maname: Version 1.002; ttfautohint (v1.8.4.7-5d5b) added")
  - Author: Yanone
  - Merged: 2025-01-21
  - Body: "Taken from the upstream repo https://github.com/mooniak/maname-font at commit 626ceee1311626c5240a68b0ef27722f44c374af. Resolves #8323"
- **Commit**: `c48257652b27eea3219f5782bccbb04f70c00c2a` (2025-01-17)
  - Same message and upstream reference as the PR body

The v1.002 release was published on GitHub on 2024-12-14. The google/fonts PR was merged on 2025-01-21, approximately five weeks later.

### Metadata enrichment (Batch 2/4)

- **Commit**: `4ad8ac680573a3b43e2c9637f7cad3fcfc5648d1` (2025-03-31)
  - Added `config_yaml: "sources/config.yaml"` to the source block
  - This was ported from the fontc_crater targets list

## Build Configuration

The upstream repository contains a `sources/config.yaml` at the referenced commit:

```yaml
sources:
  - Maname.glyphspackage
familyName: Maname
buildStatic: true
buildTTF: true
buildOTF: true
buildWebfont: true
```

The config references the Glyphs 3 package source (`Maname.glyphspackage`) located in the same `sources/` directory. The path `sources/config.yaml` in METADATA.pb correctly points to this file relative to the repository root.

No override config.yaml exists in the google/fonts family directory; the upstream config is used directly.

## Findings

1. **Source block is complete**: The METADATA.pb source block has all required fields: repository_url, commit hash, archive_url, file mappings, branch, and config_yaml.

2. **Commit hash verified**: Commit `626ceee1311626c5240a68b0ef27722f44c374af` exists in the upstream repository and is the HEAD of main, as well as the commit tagged `v1.002`. The commit message ("Update images") and date (2024-12-14) are consistent with the v1.002 release date.

3. **config.yaml verified**: The file `sources/config.yaml` exists at the referenced commit and contains valid gftools-builder configuration pointing to the `Maname.glyphspackage` source.

4. **File mapping note**: The `files` block references `fonts/ttf/Maname-Regular.ttf` as a source file. This path does not exist in the repository tree at the referenced commit; it refers to a path within the release archive (`archive_url`), which is the expected behavior when `archive_url` is used.

5. **PR reference consistent**: Both the google/fonts commit body and PR #8971 explicitly reference the same upstream commit hash, and the timeline is consistent (upstream release on 2024-12-14, google/fonts merge on 2025-01-21).

6. **No corrections needed**: All metadata is accurate and complete.

## Recommended Source Block

The current source block is correct and complete. No changes are recommended:

```
source {
  repository_url: "https://github.com/mooniak/maname-font"
  commit: "626ceee1311626c5240a68b0ef27722f44c374af"
  archive_url: "https://github.com/mooniak/maname-font/releases/download/v1.002/maname-font-v1.002.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Maname-Regular.ttf"
    dest_file: "Maname-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
