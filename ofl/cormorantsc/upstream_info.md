# Cormorant SC - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Cormorant SC |
| **Designer** | Christian Thalmann |
| **Repository URL** | https://github.com/CatharsisFonts/Cormorant |
| **Commit** | `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` |
| **Branch** | master |
| **Config YAML** | `sources/build.yaml` |
| **Date Added** | 2017-01-18 |
| **License** | OFL |
| **Status** | Complete |

## How URL Found

The repository URL `https://github.com/CatharsisFonts/Cormorant` is the shared upstream repo for all Cormorant variants (Cormorant, Cormorant Garamond, Cormorant Infant, Cormorant SC, Cormorant Unicase, Cormorant Upright). It is documented in:

1. **METADATA.pb source block**: `repository_url: "https://github.com/CatharsisFonts/Cormorant"`
2. **Copyright strings** in all font files: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
3. **PR #4892 body** (google/fonts): "Cormorant SC Version 4.000 taken from the upstream repo https://github.com/CatharsisFonts/Cormorant"

## How Commit Determined

The commit `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` is explicitly referenced in multiple places:

1. **METADATA.pb source block**: `commit: "cc1bfb51ce6568cb3abf9199ab718d543f6fa189"`
2. **google/fonts commit 34b64bb41** (PR #4892, merged 2022-07-05 by Marc Foley): "Cormorant SC Version 4.000 taken from the upstream repo https://github.com/CatharsisFonts/Cormorant at commit https://github.com/CatharsisFonts/Cormorant/commit/cc1bfb51ce6568cb3abf9199ab718d543f6fa189"
3. **PR #4892 body**: Same explicit reference to the commit URL

In the upstream repo, this commit is "Merge pull request #67 from m4rc1e/gf-mastering" (dated 2022-05-14), authored by Christian Thalmann merging Marc Foley's branch. The merge is titled "v4.000 mastered for Google Fonts" and includes reorganized font output files and the `sources/build.yaml` config.

### Commit history of Cormorant SC binaries in google/fonts

| Commit | Date | Description |
|---|---|---|
| `34b64bb41` | 2022-07-05 | [gftools-packager] Cormorant SC: Version 4.000 added (#4892) |
| `76b26bd5f` | 2017-02-07 | cormorantsc: v3.303 added (#637) |
| `3fdd6873c` | 2017-01-23 | cormorantsc: v3.302 added (#595) |
| `bfde91b5b` | 2017-01-18 | cormorantsc: v3.301 added (#582) |

The current fonts (v4.000) were added by the gftools-packager in PR #4892.

### Cormorant SC has NOT been updated to the newer upstream commit

After `cc1bfb51`, the upstream repo has 12 additional commits up to HEAD (`e716640d`), including PR #75 (merged as `6d210fd3`) by Simon Cozens which added per-family gftools-builder configs and variable font builds. Cormorant Garamond and Cormorant Infant were updated to `6d210fd3` in google/fonts, but Cormorant SC was not. This is likely because:
- The newer work focused on variable font builds for Garamond and Infant
- There is no SC-specific gftools-builder config even at HEAD
- The SC fonts continue to be served as static fonts

## Config YAML Status

At commit `cc1bfb51`, only one config file exists: `sources/build.yaml`. This config builds the **main Cormorant variable fonts**, not Cormorant SC specifically:

```yaml
sources:
  - Cormorant.glyphs
  - Cormorant-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Cormorant
buildStatic: False
buildWebfont: False
stat:
  Cormorant[wght].ttf:
    ...
  Cormorant-Italic[wght].ttf:
    ...
```

### How Cormorant SC fonts were produced

The SC fonts are **not built by the `build.yaml` config**. Instead, Cormorant SC is defined as a set of 5 instances inside the `sources/Cormorant.glyphs` file, each with a `familyName` custom parameter set to "Cormorant SC" (Light, Regular, Medium, SemiBold, Bold). The SC static TTF files (`fonts/ttf/CormorantSC-*.ttf`) were pre-compiled binaries included directly in the upstream repo. The gftools-packager simply copied these pre-built files to google/fonts.

The upstream.yaml (from the gftools-packager commit) confirms this -- it maps files directly:
```yaml
files:
  fonts/ttf/CormorantSC-Bold.ttf: CormorantSC-Bold.ttf
  fonts/ttf/CormorantSC-Light.ttf: CormorantSC-Light.ttf
  fonts/ttf/CormorantSC-Medium.ttf: CormorantSC-Medium.ttf
  fonts/ttf/CormorantSC-Regular.ttf: CormorantSC-Regular.ttf
  fonts/ttf/CormorantSC-SemiBold.ttf: CormorantSC-SemiBold.ttf
```

### Config at HEAD

At the upstream HEAD, the `build.yaml` was removed and replaced with per-family configs (`config-cormorant.yaml`, `config-garamond.yaml`, `config-infant.yaml`, `config-unicase.yaml`, `config-upright.yaml`). Notably, **there is still no `config-sc.yaml`**. However, a variable font `fonts/variable/CormorantSC[wght].ttf` does exist at HEAD, suggesting SC variable fonts were built through the `sources/generated/` pipeline or the main Glyphs export.

No override config.yaml exists in the google/fonts family directory (`ofl/cormorantsc/`).

## Source Files at Referenced Commit

Key source files at `cc1bfb51`:
- `sources/Cormorant.glyphs` - Main Roman source (contains SC instances)
- `sources/Cormorant-Italic.glyphs` - Italic source (no SC italic variant)
- `sources/build.yaml` - gftools-builder config (builds main Cormorant only)
- `sources/CormorantSC_calt.txt` - SC-specific contextual alternates feature data
- `sources/CormorantSC_liga.txt` - SC-specific ligature feature data
- `fonts/ttf/CormorantSC-*.ttf` - 5 pre-built static font binaries

## Verification

- **Upstream repo cached**: Yes, at `upstream_repos/fontc_crater_cache/CatharsisFonts/Cormorant/`
- **Commit exists**: Yes, verified -- "Merge pull request #67 from m4rc1e/gf-mastering" (2022-05-14)
- **Config file exists at commit**: Yes, `sources/build.yaml` exists (though it builds main Cormorant, not SC specifically)
- **Font files match**: METADATA.pb maps 5 static TTF files from `fonts/ttf/CormorantSC-*.ttf`, all present at the commit
- **Repository accessible**: Yes, remote URL `https://github.com/CatharsisFonts/Cormorant` is valid
- **google/fonts source block**: Complete with repository_url, commit, config_yaml, branch, and file mappings

## Confidence Level

**HIGH** - All data is explicitly documented in the gftools-packager commit message (34b64bb41), PR #4892 body, and METADATA.pb source block. The commit hash is confirmed through multiple independent sources.

The `config_yaml` field pointing to `sources/build.yaml` is the best available option since no SC-specific config existed at that commit. The SC fonts were pre-built static binaries in the upstream repo, not compiled through the gftools-builder pipeline.

## Open Questions

- Cormorant SC has not been updated to variable fonts like Cormorant Garamond and Cormorant Infant were. At the upstream HEAD, there is a `CormorantSC[wght].ttf` variable font in `fonts/variable/`, but no dedicated build config. A future update could bring Cormorant SC to variable font format, but this would require creating a proper SC-specific config and going through the review/QA process.
- The `config_yaml` field in METADATA.pb points to `sources/build.yaml` which does not actually build the SC fonts. This is a slight inaccuracy in the metadata, but there is no better alternative at the referenced commit since the SC fonts were pre-built binaries.
