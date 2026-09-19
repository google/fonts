# Lovers Quarrel — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/lovers-quarrel"
  commit: "bf3a5fd5bf11cd96b5545ee9191a16460296eb71"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LoversQuarrel-Regular.ttf"
    dest_file: "LoversQuarrel-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

The source block was assembled in two stages:
1. Commit `66f91f10f` (2024-04-03, Simon Cozens) merged the `upstream.yaml` into METADATA.pb, adding the repository_url, branch, and file mappings.
2. Commit `4ad8ac680` (2025-03-31, batch 2/4 from fontc_crater targets) added the `commit` hash and `config_yaml` field.

## Repository Analysis

**Repository**: [googlefonts/lovers-quarrel](https://github.com/googlefonts/lovers-quarrel)
**Default branch**: master
**Single branch**: Yes (only master)

The upstream repository was created by Viviana Monsalve (vv-monsalve) to prepare the font for a Google Fonts upgrade. It contains:

- `sources/LoversQuarrel.glyphs` — Glyphs source file (36,232 lines)
- `sources/config.yml` — gftools-builder configuration
- `fonts/ttf/LoversQuarrel-Regular.ttf` — Pre-built binary
- `fonts/otf/LoversQuarrel-Regular.otf` — Pre-built OTF binary
- `fonts/webfonts/LoversQuarrel-Regular.woff2` — Pre-built WOFF2 binary
- `.github/workflows/CI-static-ttf.yml` — CI workflow
- Standard metadata files (OFL.txt, AUTHORS.txt, CONTRIBUTORS.txt, README.md, DESCRIPTION.en_us.html)

The `config.yml` at `sources/config.yml` contains:

```yaml
sources:
  - LoversQuarrel.glyphs
familyName: "Lovers Quarrel"
buildVariable: false
# autohintTTF: false
```

This is a valid gftools-builder configuration pointing to the `.glyphs` source.

## Onboarding History

**Original designer**: Robert Leuschke
**Added to Google Fonts**: 2012-03-29 (initial commit `90abd17b4`)
**Last font upgrade**: PR #3443, merged 2021-05-25, by Viviana Monsalve (vv-monsalve)

### Font Upgrade Timeline (PR #3443)

The font was upgraded from Version 1.000 to Version 1.010 via PR #3443 ("Lovers Quarrel: Version 1.010; ttfautohint (v1.8.3) added"). The PR was authored and merged by vv-monsalve.

The upstream repository had active development from 2021-03-25 through 2021-05-25. Key commits:

| Hash | Date | Description |
|------|------|-------------|
| `697ff7c` | 2021-03-25 | initial files added |
| `fc51230` | 2021-05-13 | Merge PR #4 from crystaltype (path direction, L1 improvements) |
| `e6c03f1` | 2021-05-13 | config file added |
| `d25a15d` | 2021-05-14 | new source and font files |
| `a20c251` | 2021-05-20 | Merge PR #6 from crystaltype (missing glyphs recovery) |
| `c7c687a` | 2021-05-21 | version bumped to 1.010 |
| `de6ca22` | 2021-05-21 | quotes small fix |
| `bf2edcda` | 2021-05-25 10:10 | Description changes saved and pushed |
| `bf3a5fd` | 2021-05-25 15:29 | github repo fixed |
| PR merged | 2021-05-25 21:14 | google/fonts PR #3443 merged |

### Commit Hash Discrepancies

Three different commit hashes appeared across references:

1. **`de6ca22`** — Referenced in the PR #3443 body ("taken from the upstream repo ... at commit de6ca22b...")
2. **`bf2edcda`** — Referenced in the google/fonts merge commit body
3. **`bf3a5fd`** — Referenced in the current METADATA.pb (added by fontc_crater batch 2/4)

Investigation revealed:
- The gftools-packager initially referenced `de6ca22`, then `bf2edcda` was added as a follow-up commit to the PR body.
- Between `de6ca22` and `bf3a5fd`, only `DESCRIPTION.en_us.html` was modified (no font binary changes).
- The SHA-256 hash of `fonts/ttf/LoversQuarrel-Regular.ttf` at commit `bf3a5fd` matches the binary in `ofl/loversquarrel/LoversQuarrel-Regular.ttf` exactly (`a856cd5a36d050a6e7fb4b976143e6ddad8271bd...`).
- All three commits predated the PR merge (2021-05-25 21:14 UTC).
- `bf3a5fd` is the HEAD of the master branch and represents the final state used for onboarding.

The current METADATA.pb correctly references `bf3a5fd`, which is the latest commit and the actual state from which the font binary was taken.

## Build Configuration

**Config file**: `sources/config.yml` (in upstream repo)
**Config path in METADATA.pb**: `sources/config.yml`
**Override config in google/fonts**: Not needed (upstream has config)
**Build type**: Static only (`buildVariable: false`)
**Source format**: `.glyphs` (Glyphs)
**Source file**: `sources/LoversQuarrel.glyphs`

The config.yml is valid and correctly references the source file. The METADATA.pb `config_yaml` field correctly points to `sources/config.yml`.

## Findings

1. **Source block is complete and correct.** The repository_url, commit hash, branch, config_yaml, and file mappings are all accurate.

2. **Commit hash is verified.** The binary font file SHA-256 hash matches between the upstream repo at the referenced commit and the google/fonts copy. The commit `bf3a5fd` is the correct reference — it is the latest commit in the upstream repo and was made before the PR merge.

3. **Config.yaml is present in upstream.** The `sources/config.yml` file exists in the upstream repo with valid gftools-builder configuration. No override config is needed.

4. **Historical note on commit hash discrepancies.** The gftools-packager message in the google/fonts merge commit referenced `bf2edcda`, and the PR body originally referenced `de6ca22`. Both are earlier commits from the same day (or a few days prior). The fontc_crater batch import correctly identified `bf3a5fd` as the HEAD commit, which is the most accurate reference since the font binary was identical across all three commits and `bf3a5fd` represents the final state.

5. **No further action needed.** The source block metadata is complete and accurate.

## Recommended Source Block

The current source block is correct. No changes are needed.

```
source {
  repository_url: "https://github.com/googlefonts/lovers-quarrel"
  commit: "bf3a5fd5bf11cd96b5545ee9191a16460296eb71"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LoversQuarrel-Regular.ttf"
    dest_file: "LoversQuarrel-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```
