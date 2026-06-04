# Investigation Report: Bitter

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bitter |
| Designer | Sol Matas |
| License | OFL |
| Date Added | 2011-12-19 |
| Repository URL | https://github.com/solmatas/BitterPro |
| Commit | `3238d7ae2cb0b564b81225d68b3c893a40b1d3ce` |
| Branch | master |
| Config YAML | `sources/config.yaml` (upstream) |
| Status | complete |

## How URL Found

The repository URL is documented in the METADATA.pb `source {}` block. It also appears in the copyright string: "Copyright 2011 The Bitter Project Authors (https://github.com/solmatas/BitterPro)". The URL was populated in google/fonts through commit `f7455d788` ("Populate source.repository_url").

## How Commit Determined

The commit hash `3238d7ae2cb0b564b81225d68b3c893a40b1d3ce` is explicitly stated in the most recent update commit (ae60d31b4) by Yanone (2025-02-12):

> "Taken from the upstream repo https://github.com/solmatas/BitterPro at commit https://github.com/solmatas/BitterPro/commit/3238d7ae2cb0b564b81225d68b3c893a40b1d3ce."

This updated the font from Version 3.020 to Version 3.021.

### Cross-verification

The commit was verified in the upstream repo. The cached repo at `upstream_repos/fontc_crater_cache/solmatas/BitterPro/` is a shallow clone with only this one commit visible (`3238d7a New binaries`). The commit message "New binaries" is consistent with the font binary files being updated.

Previous update was at commit `cd40ea8b9d4cf7f5f11bc62a156136258465dc9e` (Version 3.020, onboarded 2024-05-16 by Yanone).

## Config YAML Status

The upstream repo has `sources/config.yaml` at the recorded commit with proper gftools-builder configuration:

```yaml
sources:
  - Bitter.glyphs
  - Bitter-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: "Bitter"
flattenComponents: true
stat:
  ...
buildVariable: True
buildOTF: false
buildTTF: false
buildWebfont: false
```

This is a complete and proper config.yaml that references the Glyphs source files (`Bitter.glyphs` and `Bitter-Italic.glyphs`) and configures variable font building. No override config is needed. The METADATA.pb correctly references `config_yaml: "sources/config.yaml"`.

## Verification

- **Upstream repo accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/solmatas/BitterPro/` (shallow clone)
- **Commit exists in repo**: Yes - `3238d7a New binaries`
- **Font files at commit**: Yes - `fonts/variable/Bitter[wght].ttf` and `fonts/variable/Bitter-Italic[wght].ttf`
- **Source files at commit**: Yes - `sources/Bitter.glyphs` and `sources/Bitter-Italic.glyphs`
- **Config YAML**: Exists at `sources/config.yaml` with proper gftools-builder configuration

## Confidence Level

**HIGH** - The commit hash is explicitly documented in the gftools-packager update commit message. Config.yaml is properly configured with complete build settings.

## Open Questions

None. All source data is verified.

## Notes

- Bitter has a long history in Google Fonts, dating back to 2011. It has gone through many updates.
- The font binary files were taken from the upstream repo's pre-built fonts (`fonts/variable/`), matching the source file mappings in METADATA.pb.
- The upstream repo is named "BitterPro" but the font family shipped is simply "Bitter".
- Key update history in google/fonts:
  - 2016: v1.002 hotfix
  - 2018: v2.001 added
  - 2019: v2.002 added
  - 2024: v3.020 added
  - 2025: v3.021 added (current)
