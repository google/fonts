# Investigation Report: Englebert

## Source Data

| Field              | Value |
|--------------------|-------|
| Family Name        | Englebert |
| Designer           | Astigmatic (Brian J. Bonislawsky) |
| License            | OFL |
| Date Added         | 2012-11-02 |
| Repository URL     | https://github.com/librefonts/englebert |
| Commit Hash        | `0b03ab09eab75a39c93f8fb0432459a7dca74176` |
| Branch             | master |
| Config YAML        | Override `config.yaml` in google/fonts |
| Source Types        | VFB (FontLab Studio) |
| Status             | complete |
| Confidence         | HIGH |

## How Repository URL Was Found

The repository URL `https://github.com/librefonts/englebert` was already present in the METADATA.pb source block. It was added by Simon Cozens in commit `c8a4f855` ("More upstreams (e,f)", 2024-01-14). The URL is also referenced in:

- The copyright notice in METADATA.pb: `Copyright 2012 The Englebert Project Authors (https://github.com/librefonts/englebert)`
- The DESCRIPTION.en_us.html file, which links to the same repository
- The repository is accessible on GitHub under the `librefonts` organization

The repository was created by Mikhail Kashkin (hash3g) on 2014-07-16 with the commit message "Move englebert font files to separate repository", indicating it was migrated from a larger collection into its own repo as part of the librefonts organization.

## How Commit Hash Was Identified

The commit hash `0b03ab09eab75a39c93f8fb0432459a7dca74176` was added to METADATA.pb by a prior investigation (commit `e8c781a6`, "sources info for Englebert v1.010 (PR #8688)", 2025-10-30). This hash is the HEAD of the upstream repository's `master` branch and represents the latest commit (dated 2014-10-17, "update .travis.yml").

**Verification**: The upstream repository has only 12 commits total. All commits after the initial one (`3e3caf6`, 2014-07-16) are CI/Travis configuration changes only. A diff of the `src/` directory between the initial commit and HEAD shows no source file changes (only a file mode permission change on `src/METADATA_comments.txt`). The three VFB source files have been unchanged since the repository was created.

Since the source files never changed, this commit hash is effectively equivalent to any other commit in the repository for the purpose of identifying the sources. Using HEAD (`0b03ab0`) is acceptable and correct.

## How Config YAML Was Resolved

The upstream repository has **no** `config.yaml` file. The source files are exclusively in VFB format (FontLab Studio binary):

- `src/Englebert-Regular.vfb` — Original source with contour overlaps
- `src/Englebert-Regular-TTF.vfb` — TrueType outlines with hinting adjustments
- `src/Englebert-Regular-OTF.vfb` — Merged contours and optimized for OTF

An override `config.yaml` already exists in the google/fonts family directory (`ofl/englebert/config.yaml`), added in commit `e8c781a6` (2025-10-30). It contains:

```yaml
buildVariable: false
sources:
  - src/Englebert-Regular.vfb
  - src/Englebert-Regular-TTF.vfb
  - src/Englebert-Regular-OTF.vfb
```

**Note on VFB sources**: VFB is a proprietary FontLab Studio format. While gftools-builder lists VFB as a potential input, practical support may be limited. The current font binary in google/fonts was NOT built using gftools-builder from these VFB sources. Instead, the font was originally onboarded as a pre-built binary and later hotfixed (binary patched) by Emma Marichal in PR #8688 to fix v-metrics issues (see issue #8679).

Since the `config_yaml` field is omitted from the METADATA.pb source block (as per policy, google-fonts-sources auto-detects local override config files), this is correctly configured.

## Verification

### Repository Accessibility
- GitHub URL verified accessible: `librefonts/englebert`, default branch `master`
- Last pushed: 2014-10-17 (no activity in over 10 years)

### Source Block in METADATA.pb
The current source block contains:
```
source {
  repository_url: "https://github.com/librefonts/englebert"
  commit: "0b03ab09eab75a39c93f8fb0432459a7dca74176"
}
```
This is correct and complete. The `config_yaml` field is intentionally omitted because an override config exists locally.

### Font Binary History
The font binary in google/fonts has been modified three times:
1. **2015-03-07** (`90abd17b`) — Initial commit (the original v1.000 binary)
2. **2024-12-04** (`05636835`) — Hotfixed v-metrics by Emma Marichal (PR #8688)
3. **2024-12-12** (`b7f6aa92`) — Name table updated (copyright) by Emma Marichal (PR #8688)

The current binary (v1.010) was hotfixed directly, not rebuilt from the VFB sources. The original v1.000 binary predates the upstream repository (added to Google Fonts 2012-11-02, upstream repo created 2014-07-16).

### Upstream Repository Cache
The repository is cloned at `upstream_repos/fontc_crater_cache/librefonts/englebert/` and is clean with no local modifications.

## Confidence

**HIGH** — The repository URL is confirmed through multiple sources (METADATA.pb copyright, DESCRIPTION.en_us.html, GitHub). The commit hash points to the HEAD of the upstream repo, which is appropriate since no source files changed across any commits. An override config.yaml is already in place in google/fonts. The source block is complete and correctly configured.

## Additional Notes

- The font was designed by Brian J. Bonislawsky (Astigmatic) and released in November 2012
- The upstream repository was created as part of the librefonts organization by Mikhail Kashkin, migrating fonts from a larger collection
- PR #8688 was a hotfix to address bad line spacing (v-metrics) reported in issue #8679, merged by Viviana Monsalve on 2024-12-12
- The FONTLOG.txt in the upstream repo documents all three VFB source variants and their purposes
