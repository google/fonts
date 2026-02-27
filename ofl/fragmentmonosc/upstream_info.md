# Investigation: Fragment Mono SC

## Family Details
- **Family name**: Fragment Mono SC
- **Designer**: Wei Huang, URW Design Studio
- **License**: OFL
- **Date added**: 2024-06-04
- **Category**: Sans Serif, Monospace
- **Subsets**: cyrillic-ext, latin, latin-ext, menu

## Upstream Repository
- **URL**: https://github.com/weiweihuanghuang/fragment-mono
- **Status**: Active (last commit 2024-06-28)
- **Cached at**: upstream_repos/fontc_crater_cache/weiweihuanghuang/fragment-mono/
- **Note**: Same upstream repo as Fragment Mono. The SC variant is built from the same `.glyphs` source with `buildSmallCap` enabled during the packaging process.

## Source Files
- **Glyphs source**: `sources/Fragment-Mono.glyphs` (contains 690 `.sc` glyph entries)
- **Config**: `sources/config.yaml`
- **Built SC fonts in upstream**: NONE -- SC TTF files have never existed in the upstream repository

## Onboarding History

### PR #7813: Fragment Mono SC: Version 1.012; ttfautohint (v1.8.4.7-5d5b) added
- **Author**: Simon Cozens (simoncozens)
- **Created**: 2024-06-04
- **Merged**: 2024-06-25 by Emma Marichal (emmamarichal)
- **Commit in google/fonts**: `7e044b051e7a9748a04edee290553754f33c7bb4`
- **PR body states**: "Taken from the upstream repo https://github.com/weiweihuanghuang/fragment-mono at commit https://github.com/weiweihuanghuang/fragment-mono/commit/766d60703081ca3581e17764b36e8487c7ba6225"
- **Fonts added**: FragmentMonoSC-Regular.ttf (119,716 bytes), FragmentMonoSC-Italic.ttf (122,188 bytes)

### Additional commits in PR #7813
1. `7e044b051` (2024-06-04): Initial SC onboarding with fonts and METADATA.pb
2. `d7d812ce4` (2024-06-04): Added `files` data to Fragment Mono's METADATA.pb (for rebuilding)
3. `5087a1d8d` (2024-06-25): Updated OFL.txt (minor fix by Emma Marichal)

### Source block history in METADATA.pb
1. **2024-06-04**: Created with `repository_url`, `commit: 766d607...`, `files`, `branch` by Simon Cozens in PR #7813.
2. **2025-03-31**: Felipe Sanches changed commit hash to `177a79b` and added `config_yaml: sources/config.yaml` in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

## Commit Hash Verification

### Original METADATA.pb commit: `766d60703081ca3581e17764b36e8487c7ba6225`
- Date: 2024-03-04
- Message: "Added built fonts to source"
- Referenced explicitly in the PR body and commit message as the source commit.
- This commit added updated (non-SC) TTF files to the upstream repo. It does NOT contain any SC TTF files.
- The SC fonts were built by gftools-packager from the `.glyphs` source at this commit with `buildSmallCap: true`.

### Current METADATA.pb commit: `177a79b53ae0c8f02e56a8671c29c57144f609e9`
- Date: 2024-06-28 (after the PR was merged on 2024-06-25)
- Message: "Fixed specimen images again"
- This is the HEAD of the upstream repo, ported from fontc_crater's targets list.
- This commit is AFTER the onboarding merge date, so it could not have been the source commit.

### Analysis
The correct commit for the SC onboarding is `766d60703081ca3581e17764b36e8487c7ba6225`, as explicitly stated in the PR body and commit message. However, since the SC fonts were built from source (not pre-built TTFs), exact binary verification is not possible without reproducing the gftools-packager build. The explicit reference in the PR is strong evidence.

## Config Verification
- **Upstream config at onboarding commit** (`766d607`): exists at `sources/config.yaml`
  ```yaml
  sources:
    - Fragment-Mono.glyphs
  familyName: Fragment Mono
  buildVariable: false
  checkCompatibility: false
  ```
  Note: This config does NOT have `buildSmallCap: true`. The SC fonts were built by gftools-packager overriding the config to enable small caps.
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
  Note: The current config EXPLICITLY sets `buildSmallCap: false`, which means the SC variant CANNOT be rebuilt using the upstream config alone.
- **Override config in google/fonts**: None

## Issues Found

### ISSUE 1: Incorrect commit hash in METADATA.pb
- **Current**: `177a79b53ae0c8f02e56a8671c29c57144f609e9` (2024-06-28, after merge)
- **Correct**: `766d60703081ca3581e17764b36e8487c7ba6225` (2024-03-04, referenced in PR)
- **Reason**: The commit hash was changed from the original `766d607` to `177a79b` by the "Batch 1/4" commit that ported data from fontc_crater's targets list. The original was correct.

### ISSUE 2: Incorrect files block in METADATA.pb
- The `files` entries reference `fonts/ttf/FragmentMonoSC-Regular.ttf` and `fonts/ttf/FragmentMonoSC-Italic.ttf` as source files. These files have NEVER existed in the upstream repository. The SC fonts were built by gftools-packager from the `.glyphs` source with `buildSmallCap` enabled.
- This incorrect `files` block was present from the original onboarding commit and has never been corrected.

### ISSUE 3: config_yaml field is misleading
- The METADATA.pb points to `sources/config.yaml`, but this config has `buildSmallCap: false` (or omits the field entirely at the onboarding commit). Building with this config will NOT produce SC fonts.
- To correctly rebuild Fragment Mono SC, an override config.yaml with `buildSmallCap: true` would be needed in the google/fonts family directory.

### ISSUE 4: Missing override config.yaml for SC rebuilding
- Since the upstream config.yaml does not enable `buildSmallCap`, and the `files` block is incorrect (SC TTFs don't exist in the repo), an override config.yaml should be created in `ofl/fragmentmonosc/` with `buildSmallCap: true` to enable correct rebuilding.

## Recommended Corrections

### For METADATA.pb
1. Revert commit hash to the original: `766d60703081ca3581e17764b36e8487c7ba6225`
2. Remove the incorrect `files` block (SC TTFs don't exist in the upstream repo)
3. Remove or correct the `config_yaml` field (the upstream config won't build SC fonts)

### For Override config.yaml
Create `ofl/fragmentmonosc/config.yaml`:
```yaml
sources:
  - Fragment-Mono.glyphs
familyName: Fragment Mono
buildVariable: false
checkCompatibility: false
buildSmallCap: true
autohintTTF: true
autohintOTF: true
```

## Upstream Changes Since Onboarding
Since the onboarding commit (`766d607`, 2024-03-04), the upstream repo has had significant development:
- v1.20 (2024-06-28): Major update with alternate characters (ss03-ss07), circled numerals/letters, box drawing characters, Powerline glyphs
- v1.21 (2024-06-28): Updated fonts and documentation
- `177a79b` (2024-06-28): Fixed specimen images

These changes occurred AFTER the PR was created (2024-06-04) but before it was merged (2024-06-25), though the fonts in the PR were built from the earlier `766d607` commit.

## Status
- **Repository URL**: Correct
- **Commit hash**: INCORRECT (should be `766d607`, currently `177a79b`)
- **Config YAML**: INCORRECT (upstream config won't build SC; needs override)
- **Files block**: INCORRECT (SC TTFs don't exist in upstream repo)
- **Override config**: MISSING (needs `buildSmallCap: true`)
- **Overall status**: needs_correction
- **Confidence**: HIGH (PR explicitly references commit `766d607`; SC files confirmed absent from upstream)
