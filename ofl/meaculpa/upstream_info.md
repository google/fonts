# Mea Culpa — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/mea-culpa"
  commit: "13dd5b66076ddc6706d85a30dfed8d007e2f8350"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/MeaCulpa-Regular.ttf"
    dest_file: "MeaCulpa-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

The source block is fully populated with repository URL, commit hash, file mappings, branch, and config_yaml path.

## Repository Analysis

- **Repository**: https://github.com/googlefonts/mea-culpa
- **Branch**: master (only branch)
- **Total commits**: 1 (the initial and only commit)
- **Remote status**: Clean, up to date with origin

The upstream repository contains a single commit (`13dd5b6`) dated 2021-11-26. This commit created the entire repository with the following structure:

- `sources/MeaCulpaPro.glyphs` — Glyphs source file
- `sources/config.yml` — gftools-builder configuration
- `fonts/ttf/MeaCulpa-Regular.ttf` — Pre-built TTF binary
- `fonts/otf/MeaCulpa-Regular.otf` — Pre-built OTF binary
- `fonts/webfonts/MeaCulpa-Regular.woff2` — Pre-built WOFF2 binary
- `.github/workflows/CI-static-ttf.yml` — CI workflow
- Standard project files: `OFL.txt`, `README.md`, `AUTHORS.txt`, `CONTRIBUTORS.txt`, `DESCRIPTION.en_us.html`, `requirements.txt`

The designer is Robert Leuschke, as documented in METADATA.pb.

## Onboarding History

The font was onboarded to Google Fonts via PR #4136:

- **PR title**: "Mea Culpa: Version 1.010; ttfautohint (v1.8.3) added"
- **Author**: Viviana Monsalve (@vv-monsalve)
- **Merged by**: Rosalie Wagner (@RosaWagner)
- **Merged at**: 2021-12-08
- **Tool used**: gftools-packager

The PR body explicitly states the font was taken from `https://github.com/googlefonts/mea-culpa` at commit `13dd5b66076ddc6706d85a30dfed8d007e2f8350`, which matches the current METADATA.pb entry.

The onboarding commit in google/fonts (`73ac3ca7`) added:
- `ofl/meaculpa/DESCRIPTION.en_us.html`
- `ofl/meaculpa/METADATA.pb`
- `ofl/meaculpa/MeaCulpa-Regular.ttf`
- `ofl/meaculpa/OFL.txt`
- `ofl/meaculpa/upstream.yaml`

The original `upstream.yaml` was later merged into METADATA.pb (commit `66f91f10`).

### Source Block History

The source block was partially present at onboarding (repository_url, branch, files) via the upstream.yaml. The commit hash and config_yaml fields were added later in commit `4ad8ac68` ("[Batch 2/4] port info from fontc_crater targets list") on 2025-03-31.

## Build Configuration

The upstream repository has a `sources/config.yml` file at the referenced commit:

```yaml
sources:
  - MeaCulpaPro.glyphs
familyName: "Mea Culpa"
buildVariable: false
# autohintTTF: false
```

This is a valid gftools-builder configuration that builds from the `MeaCulpaPro.glyphs` source as a static (non-variable) font. The `config_yaml` field in METADATA.pb correctly references `sources/config.yml`.

No override config.yaml exists in the google/fonts family directory, as one is not needed — the upstream repo has its own config file.

## Findings

1. **Binary verification**: The TTF file in google/fonts (`MeaCulpa-Regular.ttf`, 162,232 bytes) has an identical SHA-256 hash (`c5a29315...`) to the file in the upstream repo at the referenced commit. This confirms the commit hash is correct.

2. **Commit hash verified**: The commit `13dd5b66076ddc6706d85a30dfed8d007e2f8350` is the only commit in the repository and was explicitly referenced in the gftools-packager onboarding PR #4136. Since the repo has only one commit, there is no ambiguity about the correct hash.

3. **Source block completeness**: All fields are correctly populated:
   - `repository_url`: Valid, points to the correct repo
   - `commit`: Verified correct via binary comparison and PR cross-reference
   - `branch`: Correctly set to `master`
   - `config_yaml`: Correctly points to `sources/config.yml` (note the `.yml` extension, matching the actual file)
   - `files`: File mappings are correct

4. **No issues found**: The source block is complete and accurate. No corrections needed.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/googlefonts/mea-culpa"
  commit: "13dd5b66076ddc6706d85a30dfed8d007e2f8350"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/MeaCulpa-Regular.ttf"
    dest_file: "MeaCulpa-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```
