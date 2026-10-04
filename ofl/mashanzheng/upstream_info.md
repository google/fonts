# Ma Shan Zheng — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The METADATA.pb at `ofl/mashanzheng/METADATA.pb` already contains a fully populated source block:

```
source {
  repository_url: "https://github.com/googlefonts/mashanzheng"
  commit: "6bfdbe288f5935c6e9072cdd6ab1aa102a006aab"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/MaShanZheng-Regular.ttf"
    dest_file: "MaShanZheng-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

**Repository**: https://github.com/googlefonts/mashanzheng
**Default branch**: master
**Created**: 2019-02-15 (originally as `m4rc1e/mashanzheng`, later transferred to `googlefonts`)
**Last pushed**: 2026-01-23
**Status**: Active, not archived

The repository was originally created by Marc Foley (`m4rc1e`) as `m4rc1e/mashanzheng` and later transferred to the `googlefonts` organization. The old URL `https://github.com/m4rc1e/mashanzheng` now redirects (HTTP 301) to `https://github.com/googlefonts/mashanzheng`.

### Commit History (full, 7 commits)

| Hash | Date | Author | Message |
|------|------|--------|---------|
| `6bfdbe2` | 2026-01-23 | Aaron | Update build.yaml |
| `4a468e1` | 2026-01-23 | Aaron | Merge pull request #2 from googlefonts/update |
| `69b989c` | 2026-01-23 | Aaron | installing cairo |
| `3a76bca` | 2026-01-23 | Aaron | Update requirements.txt |
| `4c2ec3b` | 2026-01-23 | Aaron | Rebuild & update |
| `fb124f9` | 2019-05-08 | Marc Foley | uncamelcase name |
| `27e58ea` | 2019-02-15 | Marc Foley | First commit |

### Repository Structure (at HEAD)

```
.github/workflows/build.yaml
.gitignore
Makefile
OFL.txt
README.md
documentation/ARTICLE.en_us.html
fonts/ttf/MaShanZheng-Regular.ttf
requirements.txt
scripts/read-config.py
sources/config.yaml
sources/MaShanZheng.glyphspackage/
```

### Source Files

The source is a `.glyphspackage` directory at `sources/MaShanZheng.glyphspackage/`. This was converted from the original `.glyphs` file during Aaron Bell's January 2026 update (commit `4c2ec3b`).

## Onboarding History

### Initial onboarding (v2.000) — PR #1853

- **Author**: Marc Foley (`m4rc1e`)
- **Merged**: 2019-03-15
- **Commit in google/fonts**: `b5de0899`
- **Upstream commit referenced**: `27e58eac77c306a10978ab9385236f3ab1631caa` (First commit)
- **Upstream repo at the time**: `m4rc1e/mashanzheng`
- **Description**: Initial onboarding of Ma Shan Zheng v2.000, a Chinese simplified handwriting font reminiscent of traditional "yinglian" calligraphy.

### Update to v2.001 — PR #1971

- **Author**: Marc Foley (`m4rc1e`)
- **Merged**: 2019-07-08
- **Commit in google/fonts**: `c09952432`
- **Upstream commit referenced**: `fb124f9b3246a54a934d6ce6deba36c0bd2e2812` ("uncamelcase name")
- **Description**: Updated font to version 2.001.

### Repository URL history in METADATA.pb

1. **Added** (commit `f7455d788`, 2023-08-15): `repository_url: "https://github.com/googlefonts/mashanzheng"` was added as part of a bulk "Populate source.repository_url" operation.
2. **Removed** (commit `959a8eec4`, 2023-08-15): The source block was removed with the message "Not a real GitHub repo." — this was likely because the repo had no source files suitable for building at that time (only pre-built binaries and a `.glyphs` source without a config.yaml).
3. **Re-added** (commit `c08e58a56`, 2026-01-23): Full source block added by Aaron Bell as part of the v2.002 update.

### Update to v2.002 — PR #10153

- **Author**: Aaron Bell (`aaronbell`)
- **Merged**: 2026-01-29
- **Commit in google/fonts**: `8737a6c78` (font binary) + `c08e58a56` (METADATA.pb update)
- **Upstream commit referenced in METADATA.pb**: `6bfdbe288f5935c6e9072cdd6ab1aa102a006aab` (HEAD)
- **Issue**: Closes #10133 — glyph mismatch for U+4E95 (reported by Shaohua Yang)
- **Changes**: Fixed glyphs for 佛 (path issue), 冷 (added bottom stroke), 舞 (removed extra top stroke), 井 (replaced incorrect glyph). Also added `fwid` OpenType features. Version bumped to 2.002.
- **Description**: Aaron modernized the source repository, converting the `.glyphs` source to `.glyphspackage`, adding `config.yaml`, CI build workflow, Makefile, and requirements. The font was rebuilt and glyph bugs were fixed.

## Build Configuration

### Config at upstream repo (`sources/config.yaml`)

```yaml
familyName: Ma Shan Zheng
sources:
- MaShanZheng.glyphspackage
buildVariable: False
autohintTTF: False
buildOTF: False
buildWebfont: False
removeOutlineOverlaps: False
```

The `config.yaml` is a valid gftools-builder configuration. The source file path `MaShanZheng.glyphspackage` is relative to the `sources/` directory where the config resides. The config disables variable font building, OTF building, web font building, autohinting, and outline overlap removal — consistent with a static-only CJK font.

**No override config.yaml** exists in the google/fonts family directory — the METADATA.pb correctly points to the upstream config at `sources/config.yaml`.

## Findings

1. **Source block is complete and correct**: The current METADATA.pb source block was added by Aaron Bell (the font engineer who performed the v2.002 update) and contains accurate information.

2. **Commit hash is correct**: `6bfdbe288f5935c6e9072cdd6ab1aa102a006aab` is the HEAD of the `master` branch and matches the commit used for the v2.002 update. The font binary at this commit matches the one in google/fonts (verified via MD5 checksum: `e47f68d28821725fd22a8a6e1f875e61`).

3. **Repository URL is correct**: `https://github.com/googlefonts/mashanzheng` is the current canonical URL. The original `m4rc1e/mashanzheng` URL redirects here.

4. **Config path is correct**: `sources/config.yaml` exists in the upstream repo at the referenced commit and contains valid gftools-builder configuration.

5. **Font binary is pre-built, not CI-built**: The `files` entries in the source block reference `fonts/ttf/MaShanZheng-Regular.ttf` as the source file, indicating the font was copied from the upstream repo's pre-built binary rather than being compiled from sources during the google/fonts PR process.

6. **No action needed**: All metadata is accurate and complete. The source block was added by the same engineer who performed the update, providing high confidence in its accuracy.

## Recommended Source Block

The current source block is correct and complete. No changes are recommended:

```
source {
  repository_url: "https://github.com/googlefonts/mashanzheng"
  commit: "6bfdbe288f5935c6e9072cdd6ab1aa102a006aab"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/MaShanZheng-Regular.ttf"
    dest_file: "MaShanZheng-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

**Confidence**: HIGH — The source block was added by the engineer (Aaron Bell) who performed the v2.002 update. The commit hash, repository URL, config path, and file mappings have all been independently verified.
