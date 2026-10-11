# Commissioner - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Commissioner |
| Designer | Kostas Bartsokas |
| Repository URL | https://github.com/m4rc1e/Commissioner |
| Commit | 7f7dc8e9ed7ffeb3f7a91261f2b9549436ab3d02 |
| Branch | flair-rename |
| Config YAML | sources/config.yml |
| Status | complete |

## How URL Found

The repository URL was established through the gftools-packager process. PR #5850 (by Marc Foley) updated Commissioner to Version 1.001. The PR body references `kosbarts/Commissioner` as the upstream, but the auto-generated commit message and METADATA.pb point to `m4rc1e/Commissioner` (Marc Foley's fork).

The original designer's repo is at `https://github.com/kosbarts/Commissioner` (copyright in METADATA.pb references `github.com/kosbarts/Commissioner`). However, the `m4rc1e/Commissioner` fork is the one used for the gftools-builder integration and is correctly referenced in METADATA.pb because:
- The m4rc1e fork HEAD (`7f7dc8e`) matches the commit used for onboarding
- The kosbarts repo has evolved beyond that commit (current HEAD is `fad98e9`)
- The m4rc1e fork preserves the exact state used for font compilation

## How Commit Determined

The commit history shows two distinct commit hashes:
1. **`9bf35952a56ff7ba7d7fa1b0380e4bf2a63fcc35`**: Referenced in the gftools-packager commit message (`ff73ff5e7`) as the source commit from `m4rc1e/Commissioner`
2. **`7f7dc8e9ed7ffeb3f7a91261f2b9549436ab3d02`**: Set by the fontc_crater batch port (`19cdcec59`), this is the HEAD of `m4rc1e/Commissioner` master branch

The PR #5850 body says: "Commissioner Version 1.001 taken from the upstream repo https://github.com/kosbarts/Commissioner at commit https://github.com/kosbarts/Commissioner/commit/7f7dc8e9ed7ffeb3f7a91261f2b9549436ab3d02"

The upstream.yaml merge (`66f91f10f`) originally had commit `9bf3595` but the batch port updated it to `7f7dc8e`. The commit `7f7dc8e` is the master HEAD of the m4rc1e fork, which is a merge commit "Merge pull request #47 from RosaWagner/googlefonts" that added gftools-builder support.

Note: The commit `9bf3595` does not exist in the current (shallow) clone of `m4rc1e/Commissioner`. It may have been from a different branch or the repo may have been force-pushed. The `7f7dc8e` commit is verifiable as the master HEAD.

## Config YAML Status

- `sources/config.yml` exists in the upstream repo at both master and flair-rename branches
- The config uses `.glyphs` source format (Commissioner.glyphs)
- Configures variable font build with FLAR, VOLM, wght, slnt axes
- No override config.yaml in google/fonts

## Verification

- Repository URL returns HTTP 200
- Commit `7f7dc8e` is the HEAD of master on `m4rc1e/Commissioner`
- Branch `flair-rename` exists remotely (head commit `31d41bb`)
- `sources/config.yml` is present and properly configured
- Note: The METADATA.pb references commit `7f7dc8e` on branch `flair-rename`, but this commit is actually on master. The flair-rename branch HEAD is `31d41bb`. This is a minor inconsistency in the source block.

## Confidence Level

**High** - The repository URL and commit are well-documented through the gftools-packager process and PR history. The config.yaml is verified to exist.

## Open Questions

1. The METADATA.pb has `branch: "flair-rename"` but `commit: "7f7dc8e"` which is on master, not flair-rename. Should the branch field be updated to "master", or should the commit be updated to `31d41bb` (the flair-rename HEAD)?
2. Should the repository_url point to `kosbarts/Commissioner` (original designer) instead of `m4rc1e/Commissioner` (fork used for builder integration)?
