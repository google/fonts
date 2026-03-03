# Chiron Hei HK - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Chiron Hei HK |
| Designer | Tamcy |
| License | OFL |
| Date Added | 2025-05-08 |
| Repository URL | https://github.com/chiron-fonts/chiron-hei-hk |
| Commit | `5d80c2cecb7d0d702c23b4caa71e524b030d99d5` |
| Branch | source |
| Config YAML | `scripts/config.yaml` (in upstream on source branch) |
| Status | complete |

## How URL Found

The repository URL `https://github.com/chiron-fonts/chiron-hei-hk` is documented in the METADATA.pb source block on google/fonts main. The font was originally onboarded from a different repo (`aaronbell/chiron-hei-hk-gf`) but was later migrated to the canonical `chiron-fonts` organization repository.

### Onboarding History

1. **Initial onboarding** (2024-05-17, commit `08271f4cc`): Version 2.509 taken from `https://github.com/aaronbell/chiron-hei-hk-gf` at commit `c1531d7b87fc8fc7ea358c2730970f64508e1239`.

2. **v2.525 update** (2025-05-08, commit `4d6ad4301`): Taken from `https://github.com/aaronbell/chiron-hei-hk` at commit `9cba188cc74bd43ab7021e7a62d68ba970e71ebd`.

3. **Repository URL change**: The METADATA.pb was updated to point to `https://github.com/chiron-fonts/chiron-hei-hk` (the canonical Tamcy-maintained repository) instead of Aaron Bell's fork.

4. **Multiple subsequent rebuilds** (2025-06-25 through 2025-07-10): Font files were updated several times for v2.530, rebuilds, subset changes, and NID13 fixes.

## How Commit Determined

The commit `5d80c2cecb7d0d702c23b4caa71e524b030d99d5` was explicitly set in commit `4cfc451a1` (2025-09-12) on google/fonts main, titled "[chironheihk] Update commit hash in METADATA.pb". The commit message references a discussion in the fontc_crater PR #31 review thread.

Via the GitHub API, this commit is confirmed to exist on the `source` branch:
- SHA: `5d80c2cecb7d0d702c23b4caa71e524b030d99d5`
- Message: "Adding GF-specific fonts"
- Date: 2025-05-13

This commit represents the initial addition of Google Fonts-specific build configuration to the chiron-fonts/chiron-hei-hk source branch.

## Config YAML Status

**config.yaml exists in upstream** at `scripts/config.yaml` on the `source` branch. Verified at commit `5d80c2c` via GitHub API:

```yaml
sources:
  - ChironHeiHK.designspace
  - ChironHeiHK-Italic.designspace
axisOrder:
  - PADG
  - wght
  - ital
familyName: Chiron Hei HK
outputDir: ./
stat:
  ChironHeiHK[PADG,wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: ExtraLight
      value: 200
    # ... (full weight axis)
  - name: Italic
    tag: ital
    values:
    - name: Roman
      value: 0
      linkedValue: 1
      flags: 2
  ChironHeiHK-Italic[PADG,wght].ttf:
  - name: Weight
    tag: wght
    values:
    # ... (full weight axis)
  - name: Italic
    tag: ital
    values:
    - name: Italic
      value: 1
autohintTTF: False
buildStatic: False
```

The `config_yaml: "scripts/config.yaml"` field is already set in the METADATA.pb on main. No override config.yaml exists in the google/fonts family directory.

## Verification

- Repository URL verified: accessible at https://github.com/chiron-fonts/chiron-hei-hk
- Commit `5d80c2c` verified via GitHub API: exists on source branch, dated 2025-05-13
- config.yaml verified at `scripts/config.yaml` at the referenced commit
- METADATA.pb on main has complete source block: repository_url, commit, config_yaml, branch
- The commit was explicitly agreed upon in the fontc_crater PR #31 review discussion

## Confidence Level

**HIGH** - The commit hash was explicitly reviewed and set by the fontc_crater team in a PR discussion. The config.yaml path is verified at the referenced commit. The METADATA.pb source block is complete on main.

## Open Questions

- The commit `5d80c2c` (2025-05-13, "Adding GF-specific fonts") predates several font binary updates in google/fonts (v2.530 on 2025-06-25, rebuilds on 2025-06-26, NID13 on 2025-07-10). The font binaries currently in google/fonts may have been built from a later commit on the source branch. However, since this commit was explicitly agreed upon by the fontc_crater team, it serves as the canonical reference point.
- The local cache at `upstream_repos/fontc_crater_cache/chiron-fonts/chiron-hei-hk` only has the `release` branch fetched; the `source` branch is not cached locally. This does not affect verification since the commit was confirmed via the GitHub API.
