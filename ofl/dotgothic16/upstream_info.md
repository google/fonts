# DotGothic16 - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | DotGothic16 |
| Repository URL | https://github.com/fontworks-fonts/DotGothic16 |
| Commit Hash | `e44ca7bb46e7f353302c1431bf752af007c4fdfe` |
| Config YAML | Override `config.yaml` in google/fonts family directory |
| Source Files | `sources/DotGothic16.glyphs` |
| Designer | Fontworks Inc. |
| Date Added | 2020-12-15 |
| License | OFL |
| Status | complete |
| Confidence | HIGH |

## How Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { }` block at `ofl/dotgothic16/METADATA.pb`:

```
source {
  repository_url: "https://github.com/fontworks-fonts/DotGothic16"
  ...
  branch: "master"
}
```

The copyright string in METADATA.pb also confirms this URL:
```
copyright: "Copyright 2020 The DotGothic16 Project Authors (https://github.com/fontworks-fonts/DotGothic16/)"
```

The upstream repo is cached at `upstream_repos/fontc_crater_cache/fontworks-fonts/DotGothic16` and the remote URL matches: `https://github.com/fontworks-fonts/DotGothic16`.

## How Commit Hash Was Identified

### Onboarding History in google/fonts

The font has two commits in google/fonts:

1. **Initial onboarding** (2021-01-28): Commit `a7a3d2143` - "DotGothic16: Version 1.000; ttfautohint (v1.8.3) added (#2907)"
   - gftools-packager message references upstream commit `a31d5b53faf6900125a95a7a1bea4fffe380e995`

2. **Version 1.100 update** (2021-08-27): Commit `d5ef17558` - "DotGothic16: Version 1.100 added (#3477)"
   - gftools-packager message references upstream commit `e44ca7bb46e7f353302c1431bf752af007c4fdfe`
   - PR #3477 by @aaronbell, merged 2021-08-27

The most recent update is the one that produced the current binary file.

### Verification of Commit e44ca7b

The upstream commit `e44ca7b` ("Hinting removed", 2021-06-08) modifies:
- `build.py` (build script changes)
- `fonts/ttf/DotGothic16-Regular.ttf` (2069236 bytes)
- `sources/DotGothic16.glyphs`

**Binary file verification**: The SHA256 hash of `fonts/ttf/DotGothic16-Regular.ttf` at upstream commit `e44ca7b` matches the file in google/fonts exactly:
```
SHA256: 3ad9af88726d42b40f7f365f0dcac785af73cf20ea6f1d5b44e57cc21150b8f1
File size: 2,069,236 bytes (both locations)
```

This confirms that the font binary in google/fonts was taken directly from the upstream repo's pre-built `fonts/ttf/` directory at commit `e44ca7b`, not rebuilt from sources.

### Newer Upstream Commits

There are 3 commits after `e44ca7b` that are NOT in google/fonts:
- `95c2a57` (2021-06-22) - Fix jp90 feature
- `fec9a21` (2021-10-19) - Fix monospaced metadata
- `1451718` (2021-10-22) - Version 1.101

These would require a separate review and QA process before incorporation.

## How Config YAML Was Resolved

The upstream repository does **not** have a `config.yaml` file at any commit. The repo uses a custom `build.py` script that calls fontmake directly and applies post-processing (DSIG stub, OS/2 adjustments, name table modifications, GASP table, optional autohinting).

An override `config.yaml` was created in the google/fonts family directory at `ofl/dotgothic16/config.yaml` (added in commit `5ddf312e6` on 2026-02-20):

```yaml
sources:
  - sources/DotGothic16.glyphs
```

This override config points to the `.glyphs` source file in the upstream repo. Note that the original build process used a custom `build.py` with post-processing steps that are not captured in this simple config, so a rebuild from sources may produce slightly different output than the pre-built TTF.

Since an override `config.yaml` exists in the google/fonts family directory, the `config_yaml` field does NOT need to be set in METADATA.pb (google-fonts-sources auto-detects local overrides).

## Verification

| Check | Result |
|---|---|
| Repository URL valid | Yes - repo exists and is accessible |
| Repo cached locally | Yes - `upstream_repos/fontc_crater_cache/fontworks-fonts/DotGothic16` |
| Repo clean | Yes - no local modifications |
| Commit exists in repo | Yes - `e44ca7b` found on master branch |
| Binary SHA256 match | Yes - exact match between upstream and google/fonts |
| Binary file size match | Yes - 2,069,236 bytes in both locations |
| Source files present | Yes - `sources/DotGothic16.glyphs` at commit `e44ca7b` |
| Config YAML | Override in google/fonts (upstream has no config.yaml) |
| METADATA.pb has source block | Yes - has repository_url and branch, missing commit hash |

### What Needs to Be Fixed in METADATA.pb

The source block is missing the `commit` field. It should be updated to:

```
source {
  repository_url: "https://github.com/fontworks-fonts/DotGothic16"
  commit: "e44ca7bb46e7f353302c1431bf752af007c4fdfe"
  files {
    source_file: "fonts/ttf/DotGothic16-Regular.ttf"
    dest_file: "DotGothic16-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

The override `config.yaml` is already in place, so no `config_yaml` field is needed.

## Confidence

**HIGH** - The commit hash `e44ca7b` is explicitly referenced in both the google/fonts commit message and PR #3477 body (via gftools-packager), and the binary SHA256 hash matches exactly between the upstream repo at that commit and google/fonts. All data is consistent and verified.
