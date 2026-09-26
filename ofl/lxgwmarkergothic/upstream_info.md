# LXGW Marker Gothic — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/aaronbell/LxgwMarkerGothic"
  commit: "fe8357007423a983e696d2d3ff545ac9bb1bb89e"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/gf/LXGWMarkerGothic-Regular.ttf"
    dest_file: "LXGWMarkerGothic-Regular.ttf"
  }
  branch: "main"
}
```

## Repository Analysis

The METADATA.pb points to `https://github.com/aaronbell/LxgwMarkerGothic`, which is a **fork** of the original repository `https://github.com/lxgw/LxgwMarkerGothic`. The original repository by LXGW contains the primary open-source Chinese font derived from Tanugo.

Aaron Bell (aaronbell) forked the repository and adapted it for Google Fonts onboarding. The fork's sole commit (`fe83570`) is titled "Updating to apply GF-specific requirements separately from the source" (dated 2025-04-02), which set up the entire repository structure including:

- Source files: `sources/LXGWMarkerGothic-Regular.ufoz` (compressed UFO3 format)
- Build config: `sources/config.yaml` (gftools-builder compatible)
- Post-processing: `sources/post.py` (applies GF-specific metric overrides and GASP table)
- Extraction: `sources/scripts/extract.py` (decompresses .ufoz to .ufo in `sources/temp/`)
- Output: `fonts/gf/LXGWMarkerGothic-Regular.ttf` (post-processed binary for Google Fonts)

The `sources/config.yaml` contains:
```yaml
sources:
  - temp/LXGWMarkerGothic-Regular.ufo
familyName: LXGW Marker Gothic
autohintTTF: False
buildOTF: False
buildWebfont: False
removeOutlineOverlaps: False
```

Note: The source path `temp/LXGWMarkerGothic-Regular.ufo` is relative to the `sources/` directory. The `.ufo` directory is generated at build time by extracting the `.ufoz` archive.

The repository is based on the Google Fonts project template (uses the standard Makefile, customize.py, and GitHub Actions workflow).

## Onboarding History

The font was onboarded through a series of commits in google/fonts:

1. **e04d4ae** (2025-05-08) — "LXGW Marker Gothic : 1.001 added" by Aaron Bell (aaronbell). This was the initial onboarding commit, adding the font binary, METADATA.pb, OFL.txt, and article HTML. The commit message states: "Taken from upstream repro https://github.com/aaronbell/LxgwMarkerGothic at fe8357007423a983e696d2d3ff545ac9bb1bb89e".

2. **d847d6cf** — "Adding image into the article." — Added article imagery.

3. **7a41139f** — "lxgwmarkergothic: fix metadata" — Fixed a missing closing brace `}` in the METADATA.pb `files` block (the `branch` field was inside the second `files` block instead of outside it).

4. **77074ea8** — "sources info for LXGW Marker Gothic: 1.001 (PR #9429)" — Corrected `config_yaml` from `"sources/project.yaml"` to `"sources/config.yaml"`.

The onboarding PR was **#9429**, authored by Aaron Bell (aaronbell), merged on 2025-05-22 by Emma Marichal (emmamarichal). The PR body described the GF-specific adaptations made (softhyphen unicode cleared, GPOS data removed from legacy marks, metadata updated, vertical metrics adjusted per GF issue #8911, GASP table set to full blur, vhea table adjusted).

## Build Configuration

The upstream repository at the referenced commit (`fe83570`) contains a valid `sources/config.yaml` for gftools-builder. The build process is:

1. Extract `.ufoz` to `.ufo` (via `sources/scripts/extract.py` into `sources/temp/`)
2. Run gftools-builder with `sources/config.yaml` (references `temp/LXGWMarkerGothic-Regular.ufo`)
3. Apply post-processing via `sources/post.py` (sets vertical metrics, GASP table, removes prep table, sets fsSelection)

The `config_yaml: "sources/config.yaml"` field in METADATA.pb is correct. No override config.yaml exists in the google/fonts family directory.

## Findings

**Binary verification**: The SHA-256 hash of `fonts/gf/LXGWMarkerGothic-Regular.ttf` in the upstream repo at the referenced commit matches exactly with the binary in google/fonts (`e6a55cfd5f18dc393f92670a164397a69242cb4eabe1d3feb5dc22fc4947a8ba`). This confirms the commit hash is correct.

**Repository URL**: The METADATA.pb correctly points to the aaronbell fork, not the original lxgw repo. This is intentional — Aaron Bell's fork contains the GF-specific build pipeline, source configuration, and post-processing scripts necessary for Google Fonts onboarding. The original lxgw/LxgwMarkerGothic repository does not have these adaptations.

**Commit hash**: `fe8357007423a983e696d2d3ff545ac9bb1bb89e` is the only commit in the aaronbell fork (the initial commit creating the entire repository). This is confirmed as the correct onboarding commit.

**Config path**: After correction in commit `77074ea8`, the `config_yaml` field correctly points to `sources/config.yaml`.

**Source format note**: The source is a `.ufoz` (compressed UFO3) file that requires extraction before building. The config.yaml references the extracted path (`temp/LXGWMarkerGothic-Regular.ufo`), which is generated at build time. This means automated rebuilds using google-fonts-sources would need to handle the extraction step, which is outside the standard gftools-builder workflow.

**No issues found**: The source block is complete and accurate. All fields (repository_url, commit, config_yaml, files, branch) are correctly set.

## Recommended Source Block

The current source block is correct and complete. No changes are needed:

```
source {
  repository_url: "https://github.com/aaronbell/LxgwMarkerGothic"
  commit: "fe8357007423a983e696d2d3ff545ac9bb1bb89e"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/gf/LXGWMarkerGothic-Regular.ttf"
    dest_file: "LXGWMarkerGothic-Regular.ttf"
  }
  branch: "main"
}
```

**Confidence**: HIGH — Binary hash match confirmed, commit hash verified (only commit in the fork), config path corrected in google/fonts history and now accurate.

## Correction (2026-06-02) — override config builds from the committed `.ufoz`

**Model**: Claude Opus 4.8

fontc_crater reported `missing source 'temp/LXGWMarkerGothic-Regular.ufo'`: the upstream `sources/config.yaml` declares the build-time-extracted `temp/…ufo`, which the repo's Makefile produces by unzipping the committed `sources/LXGWMarkerGothic-Regular.ufoz` and then `.gitignore`s. fontc_crater never runs that Makefile, so the source appears absent.

An override `config.yaml` was added in this family directory that builds **directly from the committed `sources/LXGWMarkerGothic-Regular.ufoz`** (a zipped UFO), with the path relative to the repository root. This removes the dependency on the build-time extraction step. The `.ufoz` is confirmed present at the pinned commit `fe83570`.

Dependencies / caveats:
- **fontmake** already reads `.ufoz`. Building this override in fontc_crater also relies on two pending PRs, and the override should land together with (or after) them:
  - **[googlefonts/fontc#2028](https://github.com/googlefonts/fontc/pull/2028)** — `ufo2fontir` reads `.ufoz` (otherwise the fontc side reports an unrecognized extension).
  - **[googlefonts/gftools#1192](https://github.com/googlefonts/gftools/pull/1192)** — `gftools.builder` recognises `.ufoz` as a font source (otherwise `File.family_name` crashes before the build starts).
- The shipped binary is produced by gftools-builder **plus** `sources/post.py` (vertical-metrics / GASP / fsSelection overrides), which the config alone does not run. So a crater build from this override will *build successfully* but still differ from the shipped binary by those post-processing changes — i.e. it fixes the "missing source" failure but is not yet a byte-exact reproduction.
