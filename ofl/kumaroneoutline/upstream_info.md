# Kumar One Outline — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kumaroneoutline`
**Status**: missing_config (complex source structure)

## Initial State

The `ofl/kumaroneoutline/METADATA.pb` file contained no source block — only basic family metadata (name, designer, license, category, fonts, subsets). No `DESCRIPTION.en_us.html` file existed in the directory. No `repository_url`, `commit`, or `config_yaml` fields were present.

The tracking file (`data/gfonts_library_sources.json`) already had a preliminary entry identifying `https://github.com/itfoundry/kumar` as the upstream repository with commit `3192a79a79202eb715d83fd044e9234a6d0dde66`, status `missing_config`.

## Investigation

### Google Fonts Git History

The `ofl/kumaroneoutline/` directory was added in a single commit:

- **Commit** `7d1c962b6` (2025-04-10) — "Missing in GH (#9332)" by Rod Sheeter (`rsheeter`)

PR #9332 explained that Simon Cozens noted some files existed internally (in the Google Fonts API) but were missing from the GitHub repository. This commit added the binary `KumarOneOutline-Regular.ttf` (128,948 bytes) and `METADATA.pb`. The `date_added` field in METADATA.pb is `2016-06-15`, confirming the font was served by Google Fonts long before the binary appeared in the repo.

### Related Family: Kumar One

The sibling family "Kumar One" (directory `ofl/kumarone/`) shares the same upstream repository. It was onboarded in commit `06463af` (2017-05-23) — "hotfix-kumarone: v1.001 added (#973)" by Marc Foley. That PR referenced GitHub issue #271 and added the font family "already in the API back to this repo." The DESCRIPTION.en_us.html in the Kumar One directory explicitly links to `https://github.com/itfoundry/kumar`.

### Upstream Repository

The repository `https://github.com/itfoundry/kumar` (HTTP 200, accessible) was found cached at `upstream_repos/fontc_crater_cache/itfoundry/kumar/`. It was clean (`nothing to commit, working tree clean`) on branch `master`, up to date with `origin/master`.

The repository contains a **single commit**:

- `3192a79a79202eb715d83fd044e9234a6d0dde66` (2016-04-12) — "Merge branch 'develop'" by Liang Hai

This commit contains the full project:
- `masters/Kumar One.glyphs` — the single Glyphs source file (binary, ~1.5 MB)
- `build.py` — build script using `hindkit`
- `features/GSUB.fea`, `features/GSUB_lookups.fea` — OpenType feature files
- `GlyphOrderAndAliasDB` — glyph ordering file
- `products/KumarOne-Regular.ttf` (92,076 bytes)
- `products/KumarOneOutline-Regular.ttf` (125,148 bytes)
- `products/KumarOne-Regular.otf`, `products/KumarOneOutline-Regular.otf`

### Source Structure (Non-Standard)

The `.glyphs` file contains **two masters**: "Outlined" and "Filled". No instances are defined. The `build.py` script uses `hindkit` to build each master as a separate font family:

- "Kumar One" uses the "Filled" master
- "Kumar One Outline" uses the "Outlined" master

This is a non-standard arrangement where two distinct font families are encoded as two masters in a single `.glyphs` file. A standard gftools-builder setup would interpret multiple masters as an interpolation axis for a variable font, which is NOT the intent here.

### Binary Comparison

The binary in google/fonts (128,948 bytes, SHA256 prefix `571c34cf`) does not match the product in the upstream repo (125,148 bytes, SHA256 prefix `b62ee667`). The google/fonts binary is larger, suggesting it may have been rebuilt (possibly with updated tooling or subsetting) after the upstream products were generated. The `date_added` of `2016-06-15` and the METADATA.pb `fontRevision` would likely correspond to v1.001 as referenced in the kumarone PR #973 commit message.

### Config.yaml Assessment

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in `ofl/kumaroneoutline/` in google/fonts.

Creating a standard gftools-builder config.yaml for this family is **non-trivial** because:
1. The single `.glyphs` source contains two different families as two masters (not a variable font axis)
2. gftools-builder would need to be told to only process the "Outlined" master as a static font
3. The original build system (`hindkit`) had special logic to select individual masters by tag name
4. It is unclear whether gftools-builder supports extracting a single master from a multi-master source as a standalone family

## Actions Taken

- Read METADATA.pb for `ofl/kumaroneoutline/` — confirmed no source block
- Inspected git history in google/fonts — found single commit from PR #9332 (2025-04-10)
- Read PR #9332 body — "files exist internally but not externally"
- Investigated sibling family Kumar One (`ofl/kumarone/`) for shared context
- Read DESCRIPTION.en_us.html from Kumar One — found upstream repo link `https://github.com/itfoundry/kumar`
- Verified upstream repository accessibility (HTTP 200)
- Inspected cached upstream repo — single commit `3192a79`, clean state
- Analyzed `build.py` — uses `hindkit`, builds both families from same `.glyphs` file
- Analyzed `masters/Kumar One.glyphs` — two masters ("Outlined", "Filled"), no instances
- Compared binary sizes — google/fonts (128,948 B) vs upstream products (125,148 B), mismatch

## Final State

- **Repository URL**: `https://github.com/itfoundry/kumar` (confirmed, accessible)
- **Commit**: `3192a79a79202eb715d83fd044e9234a6d0dde66` (the only commit in the repo, 2016-04-12)
- **Config**: Missing. The source structure (two families as two masters in one `.glyphs` file, built with `hindkit`) makes creating a standard gftools-builder override config.yaml non-trivial. Expert guidance may be needed to determine whether gftools-builder can handle this source arrangement.
- **Status**: `missing_config` — upstream repo identified, commit confirmed, but config.yaml creation requires understanding of how gftools-builder handles multi-master sources intended as separate families.

## Source Block

If a source block were to be added to METADATA.pb (without config_yaml, pending resolution of the config question):

```
source {
  repository_url: "https://github.com/itfoundry/kumar"
  commit: "3192a79a79202eb715d83fd044e9234a6d0dde66"
}
```

**Note**: The `config_yaml` field is omitted because no config exists yet. If/when an override config.yaml is created in the google/fonts family directory, the field can remain omitted (auto-detected). If a config is created in the upstream repo, the field should point to its path relative to the repo root.
