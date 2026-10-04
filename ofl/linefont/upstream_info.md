# Investigation Report: Linefont

**Model**: Claude Opus 4.6

## Summary

Linefont is a display/symbols variable font by Dmitry Ivanov (Dmitry Iv.) that encodes sparkline data as text. It was onboarded to Google Fonts on 2023-09-27 by Rosalie Wagner via gftools-packager. The source block in METADATA.pb was substantially complete, with repository URL, commit hash, files mapping, branch, and config_yaml all present. However, the commit hash was incorrect: it referenced the latest upstream commit (`9edec1a`, "Create tea.yaml", 2025-01-18) rather than the original onboarding commit (`347effe`, "Make rlig feature section", 2023-09-27).

## METADATA.pb Source Block (as found)

```
source {
  repository_url: "https://github.com/dy/linefont"
  commit: "9edec1a1f780db52db0297bab464451f3dbd4d5a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Linefont[wdth,wght].ttf"
    dest_file: "Linefont[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository URL

- **URL**: https://github.com/dy/linefont
- **Status**: Valid, accessible
- **Owner**: dy (Dmitry Iv.)
- **Copyright string in METADATA.pb**: "Copyright 2022 The Linefont Project Authors (https://github.com/dy/linefont)" -- matches the repository URL.

## Commit Hash Analysis

### Original Onboarding Commit

The gftools-packager commit `dfef2e4b2` in google/fonts (2023-09-27) explicitly referenced upstream commit `347effeda6955b1aa7febc34e17dcce3e04f5e15`:

> Linefont Version 3.002;gftools[0.9.33] taken from the upstream repo https://github.com/dy/linefont at commit https://github.com/dy/linefont/commit/347effeda6955b1aa7febc34e17dcce3e04f5e15.

This commit ("Make rlig feature section", authored 2023-09-27T11:40:23Z) was the HEAD of the upstream repo at onboarding time. The PR #6799 was merged on 2023-10-11.

### How the Hash Changed

1. **Original state** (commit `dfef2e4b2`, 2023-09-27): Source block had `commit: "347effeda6955b1aa7febc34e17dcce3e04f5e15"`.
2. **upstream.yaml merge** (commit `66f91f10f`, 2024-04-03): Added `files`, `branch`, and `minisite_url` to METADATA.pb, but kept the original commit hash `347effe`.
3. **Batch 2/4 fontc_crater import** (commit `4ad8ac680`, 2025-03-31): Changed the commit hash from `347effe` to `9edec1a` and added `config_yaml: "sources/config.yaml"`. This update came from the fontc_crater targets.json file, which tracked the latest upstream HEAD rather than the original onboarding commit.

### Commits Between `347effe` and `9edec1a`

A GitHub API comparison showed only 4 commits were added between these two hashes, changing only `readme.md` (modified) and `tea.yaml` (added). **No font source files were changed.** The font binary in google/fonts is byte-identical to the one in the upstream repo at `9edec1a` (SHA-256: `94cab92c51d91e7cac90f03144fa527a9fc6d1712bbbe09ab04c28cdf922026e`).

### Correct Commit Hash

The correct onboarding commit is **`347effeda6955b1aa7febc34e17dcce3e04f5e15`** ("Make rlig feature section", 2023-09-27). While `9edec1a` produces the same font sources, the policy is to reference the exact commit used during onboarding. The current hash `9edec1a` ("Create tea.yaml", 2025-01-18) postdates the onboarding by over a year and was introduced erroneously by the batch fontc_crater import.

## Config.yaml

The upstream repo has a `config.yaml` at `sources/config.yaml` that was present at the onboarding commit `347effe`. This is a valid gftools-builder configuration:

```yaml
buildVariable: true
buildStatic: true
sources:
  - Linefont.designspace
familyName: Linefont
axisOrder:
  - wdth
  - wght
stat:
  - name: Width
    tag: wdth
    values:
    - name: SuperCondensed
      value: 25
    # ... (full STAT table definitions)
  - name: Weight
    tag: wght
    values:
    - name: Thin
      value: 100
    # ... (full STAT table definitions)
```

The `config_yaml: "sources/config.yaml"` field in METADATA.pb is correct. No override config.yaml exists in the google/fonts family directory.

## Upstream Repository Notes

- The local clone at `upstream_repos/fontc_crater_cache/dy/linefont` is a shallow clone with only 1 commit (`9edec1a`). The full history (30+ commits) is available on GitHub.
- The repo contains two sets of sources: `sources/` (with the designspace and 12 UFO masters) and `_sources/` (an older version with a single master UFO). The config at `sources/config.yaml` correctly references `Linefont.designspace` relative to the `sources/` directory.
- Rosalie Wagner contributed to the upstream repo via PRs #13 and #14, adding supercondensed width and fixing design issues before the onboarding commit.

## PR History in google/fonts

| Commit | Date | Description |
|--------|------|-------------|
| `dfef2e4b2` | 2023-09-27 | [gftools-packager] Linefont: Version 3.002;gftools[0.9.33] added |
| `a67abd113` | 2023-09-27 | Linefont: updated metadata.pb and description |
| PR #6799 merged | 2023-10-11 | Onboarding PR by Rosalie Wagner |
| `9f0fe8b16` | 2023-10-12 | Linefont: custom sample text |
| `fbfbbfe45` | 2023-10-12 | Linefont: adjusted sample text |
| `16ceb1348` | 2023-10-13 | Linefont: added missing property, removed useless ones |
| `49b715cb4` | 2023-10-17 | Removed latin subsets |
| `a5e83d7a6` | 2023-11-20 | Update Linefont About page text |
| `66f91f10f` | 2024-04-03 | Merge upstream.yaml into METADATA.pb |
| `4ad8ac680` | 2025-03-31 | [Batch 2/4] port info from fontc_crater targets list |

## Recommended Fix

The commit hash in METADATA.pb should be corrected from `9edec1a1f780db52db0297bab464451f3dbd4d5a` back to `347effeda6955b1aa7febc34e17dcce3e04f5e15` (the original onboarding commit). All other fields are correct.

## Status

- **Repository URL**: Correct
- **Commit hash**: Incorrect (needs correction from `9edec1a` to `347effe`)
- **Config**: `sources/config.yaml` -- correct, present in upstream repo
- **Overall status**: needs_correction
- **Confidence**: HIGH
