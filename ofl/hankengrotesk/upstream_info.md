# Investigation Report: Hanken Grotesk

## Summary

Hanken Grotesk is a sans-serif variable font designed by Alfredo Marco Pradil (Hanken Design Co.), added to Google Fonts on 2022-11-16. The upstream repository is at `https://github.com/marcologous/hanken-grotesk`. The METADATA.pb already has a complete source block with repository URL, commit hash, file mappings, branch, and config_yaml. However, the commit hash has been updated over time and warrants scrutiny.

## Key Findings

| Field            | Value |
|------------------|-------|
| Family Name      | Hanken Grotesk |
| Repository URL   | https://github.com/marcologous/hanken-grotesk |
| Commit (current) | `1ab416e82130b2d3ddb7710abf7ceabf07156a13` |
| Commit (original)| `e6e3c4df55acfe44333c587e3d97ae3c44b7dce5` |
| Branch           | master |
| Config YAML      | `sources/config.yml` |
| Source Files     | `sources/HankenGrotesk.glyphs`, `sources/HankenGrotesk-Italic.glyphs` |
| Status           | **needs_correction** |
| Confidence       | MEDIUM |

## Investigation Details

### Onboarding History in google/fonts

1. **PR #5527** (merged 2022-11-18 by Rosalie Wagner):
   - Title: "Hanken Grotesk: Version 3.013 added"
   - Author: Viviana Monsalve
   - PR body references commit `f9b0a69971aaffc1efea7a6422baf8eb2164701b`
   - Commit message body references commit `e6e3c4df55acfe44333c587e3d97ae3c44b7dce5`
   - The METADATA.pb created in this commit contained `commit: "e6e3c4df55acfe44333c587e3d97ae3c44b7dce5"`
   - An `upstream.yaml` was also created with branch and file mappings

2. **Commit 66f91f10f** (2024-04-03, Simon Cozens):
   - "Merge upstream.yaml into METADATA.pb" -- moved file mappings and branch from upstream.yaml into the METADATA.pb source block
   - Retained the original commit hash `e6e3c4d`

3. **Commit 19cdcec59** (2025-03-31, Felipe Sanches):
   - "[Batch 1/4] port info from fontc_crater targets list"
   - Changed commit hash from `e6e3c4d` to `1ab416e82130b2d3ddb7710abf7ceabf07156a13`
   - Added `config_yaml: "sources/config.yml"`

### Commit Hash Discrepancies

There are THREE different commit hashes referenced across the onboarding:

1. **`f9b0a69`** -- mentioned in the PR #5527 body text ("Version 3.012 taken from...")
2. **`e6e3c4d`** -- placed in the original METADATA.pb by gftools-packager; referenced in the commit message body ("Version 3.013 taken from...")
3. **`1ab416e`** -- the current HEAD of the repo (dated 2024-01-30), imported from fontc_crater targets list

The version numbering is also inconsistent: the PR title says "Version 3.012" while the packager message says "Version 3.013".

The original onboarding commit hash should be `e6e3c4d` (the one gftools-packager placed in METADATA.pb). The fontc_crater batch updated it to `1ab416e` which is the repo HEAD, well after the onboarding date. Per policy, gftools-packager hashes are hints but in this case it was the packager itself that set the value in METADATA.pb, making `e6e3c4d` the most authoritative original reference.

However, the repo is a shallow clone (depth 1), so only commit `1ab416e` is visible locally. Commit `e6e3c4d` cannot be verified against the cached repo without unshallowing.

### Upstream Repository Analysis

- **Repository**: `marcologous/hanken-grotesk` (cached at `fontc_crater_cache/marcologous/hanken-grotesk`)
- **Current HEAD**: `1ab416e` (2024-01-30) -- "Merge pull request #82 from marcologous/pr/76"
- **Shallow clone**: Yes (only 1 commit visible)
- **Source files at HEAD**: `sources/HankenGrotesk.glyphs`, `sources/HankenGrotesk-Italic.glyphs`
- **Config file**: `sources/config.yml` -- valid gftools-builder config referencing both .glyphs sources
- **Variable font outputs**: `fonts/variable/HankenGrotesk[wght].ttf`, `fonts/variable/HankenGrotesk-Italic[wght].ttf`

### Config YAML Verification

The `sources/config.yml` file is a valid gftools-builder configuration:
- References `HankenGrotesk.glyphs` and `HankenGrotesk-Italic.glyphs`
- Defines `wght` and `ital` axes
- Contains STAT table entries
- Family name set to "Hanken Grotesk"

## Conclusion

The source block is largely complete but the commit hash has been changed from the original onboarding value (`e6e3c4d`) to the repo HEAD (`1ab416e`). The original hash `e6e3c4d` was from the gftools-packager onboarding in Nov 2022. The current hash `1ab416e` is a later commit (Jan 2024), imported from fontc_crater targets. The correct onboarding hash should be `e6e3c4d`, but the current value `1ab416e` may be acceptable if the fontc_crater targets list is considered authoritative. Since the repo is shallow, we cannot verify `e6e3c4d` without unshallowing.

### Recommended METADATA.pb Source Block

The current source block is functional as-is. If restoring the original onboarding commit is desired:

```
source {
  repository_url: "https://github.com/marcologous/hanken-grotesk"
  commit: "e6e3c4df55acfe44333c587e3d97ae3c44b7dce5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/HankenGrotesk[wght].ttf"
    dest_file: "HankenGrotesk[wght].ttf"
  }
  files {
    source_file: "fonts/variable/HankenGrotesk-Italic[wght].ttf"
    dest_file: "HankenGrotesk-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

**Status**: needs_correction (commit hash was changed from original onboarding value by fontc_crater batch; needs verification by unshallowing the repo)
**Confidence**: MEDIUM (original hash not verifiable due to shallow clone)
