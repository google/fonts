# Madimi One — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/TaVaTake/madimi"
  commit: "b0fedf3bfa1ac17a00bdbcbf06e8fe2aecfa009e"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/MadimiOne-Regular.ttf"
    dest_file: "MadimiOne-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

- **Repository**: https://github.com/TaVaTake/madimi
- **Cached at**: `upstream_repos/fontc_crater_cache/TaVaTake/madimi/` (shallow clone)
- **Branch**: `main`
- **Total commits**: 1 (only the merge commit `b0fedf3` exists; the repository appears to have had its history rewritten/force-pushed at some point)
- **Remote status**: Up-to-date; no additional commits beyond `b0fedf3`

The repository follows the googlefonts project template structure with standard directories:
- `sources/` — contains `madimi.glyphs` (Glyphs format), `config.yaml`, and `CustomFilter_GF_Latin_All.plist`
- `fonts/ttf/` — contains compiled `MadimiOne-Regular.ttf`
- `fonts/otf/` — contains compiled `MadimiOne-Regular.otf`
- `fonts/webfonts/` — contains `MadimiOne-Regular.woff2`
- `.github/workflows/build.yaml` — CI build configuration using gftools

## Onboarding History

The font had two onboarding attempts:

1. **First attempt** (2024-02-02): Commit `0ab3871` by Emma Marichal added the font as "Madimi" (directory `ofl/madimi/`) from upstream commit `037e703ab41450ae5531f4b6d468036a9795182a`. This commit referenced a "Madimi-Bold.ttf" file, suggesting the font had different naming at that stage. The upstream commit `037e703` no longer exists in the repository (likely removed by a force-push when the font was renamed).

2. **Final onboarding** (2024-02-14): Commit `a9eb13b` by Emma Marichal re-onboarded the font as "Madimi One" (directory `ofl/madimione/`) from upstream commit `b0fedf3`. This was followed by commit `440c885` which updated the description and metadata. Both commits were merged via PR #7282, merged on 2024-02-14.

3. **Source metadata enrichment** (2024-04-03): Commit `66f91f1` by Simon Cozens merged `upstream.yaml` into `METADATA.pb`, adding the `source { }` block with `repository_url`, `commit`, `files`, and `branch` fields.

4. **config_yaml addition** (2025-03-31): Commit `4ad8ac6` by Felipe Sanches (Batch 2/4) added the `config_yaml: "sources/config.yaml"` field to the source block, ported from fontc_crater's targets list.

The old `ofl/madimi/` directory no longer exists in google/fonts.

## Build Configuration

- **config.yaml location**: `sources/config.yaml` (in upstream repo)
- **config.yaml content**:
  ```yaml
  sources:
    - madimi.glyphs
  familyName: Madimi One
  ```
- **Source file**: `sources/madimi.glyphs` (Glyphs 3 format, appVersion 3236, formatVersion 3)
- **Present at referenced commit**: Yes, confirmed at `b0fedf3`

The config.yaml is minimal and valid — it references a single `.glyphs` source file and specifies the family name.

## Findings

1. **Commit hash verified**: The binary font file `MadimiOne-Regular.ttf` in google/fonts matches exactly (MD5: `f3176b75b22ef9065ab6206cf52e830c`) with the file at `fonts/ttf/MadimiOne-Regular.ttf` in the upstream repo at commit `b0fedf3`. This confirms the commit hash is correct.

2. **Source block is complete**: The METADATA.pb already contains all required fields: `repository_url`, `commit`, `files` mappings, `branch`, and `config_yaml`.

3. **History note**: The upstream repository's history was rewritten (force-pushed) at some point, leaving only a single merge commit. The earlier commit `037e703` referenced in the first onboarding attempt no longer exists. This is consistent with the font being renamed from "Madimi" to "Madimi One" between the two onboarding attempts.

4. **Single weight family**: The font is a single-weight (Regular 400) sans-serif/display family.

5. **No corrections needed**: All metadata is accurate and complete.

## Recommended Source Block

The current source block is correct and complete. No changes are needed:

```
source {
  repository_url: "https://github.com/TaVaTake/madimi"
  commit: "b0fedf3bfa1ac17a00bdbcbf06e8fe2aecfa009e"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/MadimiOne-Regular.ttf"
    dest_file: "MadimiOne-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
