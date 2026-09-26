# Investigation Report: Hachi Maru Pop

## Summary

Hachi Maru Pop is a Japanese handwriting typeface designed by Nonty (Norio Kanisawa). It was first added to Google Fonts in December 2020 (v1.201) and later updated to v1.300 in June 2021. The upstream repository at `noriokanisawa/HachiMaruPop` contains `.glyphs` source files. The METADATA.pb already has a source block with the correct repository URL and branch. An override `config.yaml` was added to the google/fonts family directory in February 2026 to enable gftools-builder compilation.

## Key Findings

| Field             | Value |
|-------------------|-------|
| **Family Name**   | Hachi Maru Pop |
| **Designer**      | Nonty (Norio Kanisawa) |
| **Repository URL**| https://github.com/noriokanisawa/HachiMaruPop |
| **Commit Hash**   | `efaa0d31f7bcace6cf4255b746911df1243af982` |
| **Config YAML**   | Override config.yaml in google/fonts |
| **Status**        | complete |
| **Confidence**    | HIGH |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb in `ofl/hachimarupop/` contains a source block:

```
source {
  repository_url: "https://github.com/noriokanisawa/HachiMaruPop"
  files {
    source_file: "fonts/ttf/HachiMaruPop-Regular.ttf"
    dest_file: "HachiMaruPop-Regular.ttf"
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

Notable: The source block has `repository_url` and `branch` but is **missing a `commit` field**. It currently references pre-built TTF files rather than sources for compilation.

### Google Fonts Repository History

| Commit | Date | Description |
|--------|------|-------------|
| `dc1498f60` | 2020-12-09 | v1.201 initial onboarding (PR #2865) |
| `a9f5b0a28` | 2021-06-17 | v1.300 update (PR #3484) |
| `5ddf312e6` | 2026-02-20 | Override config.yaml added |

**PR #2865** (v1.201 onboarding): gftools-packager message states the font was taken from `https://github.com/noriokanisawa/HachiMaruPop.git` at commit `497409c911541b53bcf2cc7a2d759e5be9707776`.

**PR #3484** (v1.300 update): gftools-packager message states the font was taken from `https://github.com/noriokanisawa/HachiMaruPop.git` at commit `efaa0d31f7bcace6cf4255b746911df1243af982`.

### Upstream Repository Analysis

The repository at `https://github.com/noriokanisawa/HachiMaruPop` is the original source repository by the designer.

**Relevant commits timeline:**

| Commit | Date | Description |
|--------|------|-------------|
| `497409c` | 2020-12-08 | "updating font and description file" (v1.201 onboarding) |
| `246868e` | 2020-12-14 | Update README.md |
| `efaa0d3` | 2021-06-08 | "Hinting removed" (v1.300 onboarding) |
| `f81232b`..`67d96c2` | 2021-08 to 2022-07 | 17 additional "Add files via upload" commits after onboarding |

**Commit verification for v1.300 (current in google/fonts):**
- gftools-packager references commit `efaa0d31f7bcace6cf4255b746911df1243af982` (2021-06-08)
- The google/fonts merge was on 2021-06-17, just 9 days later -- timing is consistent
- The commit titled "Hinting removed" modified `fonts/ttf/HachiMaruPop-Regular.ttf`, `build.py`, and `sources/HachiMaruPop.glyphs`
- The font binary at that commit matches the size recorded in the google/fonts update (4,385,624 bytes)

**Source files found:**
- `sources/HachiMaruPop.glyphs` -- Glyphs app format (gftools-builder compatible)

**Build system:**
- The repository uses a custom `build.py` script (not gftools-builder) that calls fontmake, then applies post-processing (DSIG stub, gasp table, localized names)
- No `config.yaml` exists in the upstream repository

### Build Configuration

An override `config.yaml` was created in the google/fonts family directory (`ofl/hachimarupop/config.yaml`) in commit `5ddf312e6` (2026-02-20):

```yaml
sources:
  - sources/HachiMaruPop.glyphs
```

This enables gftools-builder to compile from the `.glyphs` source. Note that the original `build.py` in the upstream repo includes additional post-processing steps (localized Japanese names, DSIG stub, gasp table) that are not replicated in the simple config.yaml.

## Conclusion

Hachi Maru Pop has a complete source tracking setup. The upstream repository URL is correct, the commit hash `efaa0d3` corresponds to the v1.300 update that is currently in google/fonts, and an override config.yaml enables gftools-builder compilation. The METADATA.pb source block should be updated to include the commit hash.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/noriokanisawa/HachiMaruPop"
  commit: "efaa0d31f7bcace6cf4255b746911df1243af982"
  files {
    source_file: "fonts/ttf/HachiMaruPop-Regular.ttf"
    dest_file: "HachiMaruPop-Regular.ttf"
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

Note: The `config_yaml` field is intentionally omitted because an override `config.yaml` exists in the google/fonts family directory and is auto-detected by google-fonts-sources.

### Status: `complete`
### Confidence: HIGH
