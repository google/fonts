# Investigation Report: Birthstone

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Birthstone |
| Designer | Robert Leuschke |
| License | OFL |
| Repository URL | https://github.com/googlefonts/birthstone |
| Commit | `6fb65f5dc60e40fe907e5dfe22917613bde97f73` |
| Branch | master |
| Config YAML | `sources/config.yml` |
| Date Added | 2021-08-06 |
| Status | Complete |

## How URL Found

The repository URL `https://github.com/googlefonts/birthstone` was first added by Simon Cozens in commit `f7455d788` ("Populate source.repository_url", August 2023). The copyright field in METADATA.pb also references this URL. The URL matches the gftools-packager references in the font-adding commits.

## How Commit Determined

The commit hash `6fb65f5dc60e40fe907e5dfe22917613bde97f73` was sourced from the fontc_crater targets list, ported to METADATA.pb in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

### Cross-verification with gftools-packager

The gftools-packager commits reference different commit hashes:
- PR #3676 (initial add, Version 1.010): references commit `ee85ee98a3678333faaed450ed7533e707876691`
- PR #3792 (update, Version 1.013): references commit `0d3561467bc1b4dddab19bfd722f092f5dc80718`

However, neither of these commits exists in the upstream repo. The repo has been squashed to a single commit (`6fb65f5`, "sample image updated") which is the HEAD and only commit on the `master` branch. This is typical for googlefonts repositories that undergo history cleanup.

The fontc_crater targets list uses `6fb65f5` as the reference commit, which is the only available commit in the repository. Since the repo was force-pushed/squashed, this is the correct commit to use.

### Verification that fonts match

The METADATA.pb source block maps `fonts/ttf/Birthstone-Regular.ttf` from the upstream repo, and this file exists at commit `6fb65f5`.

## Config YAML Status

**Found in upstream at `sources/config.yml`** (note: `.yml` extension, not `.yaml`)

The config at commit `6fb65f5` contains:
```yaml
sources:
  - BirthstonePro.glyphs
familyName: "Birthstone"
buildVariable: false
# autohintTTF: false
```

This builds static fonts only from `BirthstonePro.glyphs`, producing the Birthstone family.

## History

1. **2021-08-06**: Birthstone added to google/fonts (date_added)
2. **2021-08-10**: Initial add via gftools-packager (commit `09b1737b4`, PR #3676 by Viviana Monsalve), Version 1.010
3. **2021-09-08**: Updated via gftools-packager (commit `d829350c2`, PR #3792 by Viviana Monsalve), Version 1.013
4. **2023-08-15**: repository_url added by Simon Cozens (commit `f7455d788`)
5. **2025-03-31**: Commit hash added from fontc_crater targets list (commit `19cdcec59`)

## Verification

- [x] Repository URL is valid and accessible
- [x] Commit hash exists in upstream repo (HEAD and only commit on master)
- [x] Config YAML exists at `sources/config.yml` at the recorded commit
- [x] Source block in METADATA.pb is complete with files mapping and branch
- [x] Font file `fonts/ttf/Birthstone-Regular.ttf` exists at the recorded commit

## Confidence Level

**High** -- All data is verified. The commit hash is the only available commit in the squashed repo and matches fontc_crater's reference. The config.yml and font files are confirmed present.

## Open Questions

None. The repo history was squashed (common for googlefonts repos), but the current HEAD commit serves as the definitive reference.
