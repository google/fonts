# Investigation: Fragment Mono

## Family Details
- **Family name**: Fragment Mono
- **Designer**: Wei Huang, URW Design Studio
- **License**: OFL
- **Date added**: 2022-10-24
- **Category**: Sans Serif, Monospace
- **Subsets**: cyrillic-ext, latin, latin-ext, menu

## Upstream Repository
- **URL**: https://github.com/weiweihuanghuang/fragment-mono
- **Status**: Active (last commit 2024-06-28)
- **Cached at**: upstream_repos/fontc_crater_cache/weiweihuanghuang/fragment-mono/

## Source Files
- **Glyphs source**: `sources/Fragment-Mono.glyphs`
- **Config**: `sources/config.yaml`
- **Built fonts**: `fonts/ttf/FragmentMono-Regular.ttf`, `fonts/ttf/FragmentMono-Italic.ttf`

## Onboarding History

### PR #5461: Fragment Mono : 1.010 added
- **Author**: Wei Huang (weiweihuanghuang)
- **Created**: 2022-10-24
- **Merged**: 2022-10-27 by Rosalie Wagner (RosaWagner)
- **Commit in google/fonts**: `8db5a9256b34ffad61e53aafeecb4a612faa0080`
- **Fonts added**: FragmentMono-Regular.ttf (125,368 bytes), FragmentMono-Italic.ttf (128,052 bytes)

The commit message says "Fragment Mono : 1.010 added" initially, then "Fragment Mono : 1.011 added" after subsequent pushes during the PR review.

### Source block history in METADATA.pb
1. **2023-12-14**: Simon Cozens added the initial `source { repository_url }` in commit `2423d2aef` ("Update upstreams").
2. **2024-06-04**: Simon Cozens added `branch`, `files` entries in commit `ed48cf7b4`/`d7d812ce4` ("Add files data to upstream fragmentmono for rebuilding"), as part of PR #7813 (Fragment Mono SC onboarding).
3. **2025-03-31**: Felipe Sanches added `commit` hash (`177a79b`) and `config_yaml` (`sources/config.yaml`) in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

## Commit Hash Verification

### Current METADATA.pb commit: `177a79b53ae0c8f02e56a8671c29c57144f609e9`
- This is the latest commit in the upstream repo (2024-06-28), titled "Fixed specimen images again".
- This commit was NOT used for the original onboarding. It is from fontc_crater's targets list.
- At this commit, the TTF files have SHA256 hashes that do NOT match the files in google/fonts.

### Correct onboarding commit: `3ff027831f9a8b5820b35e251e5914d5a3f5fac4` (tag `1.011`)
- Date: 2022-10-26
- Message: "Moved PANOSE metadata into instances"
- The TTF files at this commit have SHA256 hashes that EXACTLY match the files in google/fonts:
  - `FragmentMono-Regular.ttf`: `0fe011f425873c2e0fc73a189e394e340ad48d2b9a99a576bdeec75cee000460`
  - `FragmentMono-Italic.ttf`: `c9dd3c7b24c11ba05ab1a6ec3a659c823f0e14fb26c14df0e93e82ebb60f3a25`
- The OFL.txt also matches between this commit and google/fonts.

### Evidence
Binary file SHA256 comparison across upstream commits:
| Commit | Tag | Regular TTF hash (prefix) | Match? |
|--------|-----|---------------------------|--------|
| `3ff0278` | 1.011 | `0fe011f4...` | YES |
| `4f006f6` | (pre-1.011) | `758cb35c...` | no |
| `766d607` | (v1.012+) | `3637ea29...` | no |
| `177a79b` | HEAD | `bf891131...` | no |

The font files were onboarded at tag `1.011` (commit `3ff0278`), 1 day before the PR was merged.

## Config Verification
- **Upstream config at onboarding commit** (`3ff0278`): exists at `sources/config.yaml`
  ```yaml
  sources:
    - Fragment-Mono.glyphs
  familyName: Fragment Mono
  buildVariable: False
  ```
- **Current upstream config** (`177a79b`): exists at `sources/config.yaml`
  ```yaml
  sources:
    - Fragment-Mono.glyphs
  familyName: Fragment Mono
  buildVariable: false
  checkCompatibility: false
  buildSmallCap: false
  autohintTTF: true
  autohintOTF: true
  ```
- **Override config in google/fonts**: None

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml`.

## Issues Found

### ISSUE: Incorrect commit hash in METADATA.pb
- **Current**: `177a79b53ae0c8f02e56a8671c29c57144f609e9` (2024-06-28, HEAD)
- **Correct**: `3ff027831f9a8b5820b35e251e5914d5a3f5fac4` (2022-10-26, tag 1.011)
- **Reason**: The commit hash `177a79b` was ported from fontc_crater's targets list, which tracks the latest upstream commit for rebuilding purposes, not the original onboarding commit. The actual onboarding used pre-built TTF files from tag 1.011.

### ISSUE: files block references pre-built TTFs, not source-built
- The `files` entries in the source block reference `fonts/ttf/FragmentMono-*.ttf`, which are pre-built binaries checked into the upstream repo, not files produced by running gftools-builder with the config.yaml. This is correct for how the font was originally onboarded (pre-built TTFs were copied), but means the `config_yaml` field is somewhat misleading -- the config was not actually used to build the fonts that are in google/fonts.

## Upstream Changes Since Onboarding
Since the onboarding commit (`3ff0278`, 2022-10-26), the upstream repo has had significant development:
- v1.012 (2024-03-04): Added box drawing glyphs, updated source
- v1.20 (2024-06-28): Major update with alternate characters (ss03-ss07), circled numerals/letters, box drawing characters, Powerline glyphs
- v1.21 (2024-06-28): Updated fonts and documentation

The source file has approximately 14,000 lines of diff between the onboarding commit and the SC onboarding commit (`766d607`). These changes would need to go through a separate review process.

## Status
- **Repository URL**: Correct
- **Commit hash**: INCORRECT (should be `3ff0278`, currently `177a79b`)
- **Config YAML**: Correct path (`sources/config.yaml`)
- **Override config**: Not needed (upstream has config.yaml)
- **Overall status**: needs_correction
- **Confidence**: HIGH (binary hash match confirms the correct commit)
