# Investigation Report: Figtree

## Family Details
- **Family name**: Figtree
- **Designer**: Erik Kennedy
- **License**: OFL
- **Category**: Sans Serif
- **Date added to Google Fonts**: 2022-07-21
- **Minisite**: https://www.erikdkennedy.com/projects/figtree.html

## Upstream Repository
- **URL**: https://github.com/erikdkennedy/figtree
- **Description**: A friendly, simple geometric sans serif font
- **Branch**: master
- **Verified**: Yes, repository exists and is accessible

## Source Files
- **Source format**: Glyphs (.glyphs)
- **Source files**: `sources/Figtree.glyphs`, `sources/Figtree-Italic.glyphs`
- **Config file**: `sources/config.yaml` (in upstream repo)
- **Variable axes**: wght (300-900)
- **Output files**: `fonts/variable/Figtree[wght].ttf`, `fonts/variable/Figtree-Italic[wght].ttf`

## Current METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/erikdkennedy/figtree"
  commit: "032dfa7fe219ef3a02890d6d3add84eacc9aebfe"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Figtree[wght].ttf"
    dest_file: "Figtree[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Figtree-Italic[wght].ttf"
    dest_file: "Figtree-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Commit History in google/fonts

### Version 1.000 (Initial Onboarding)
- **google/fonts PR**: [#4968](https://github.com/google/fonts/pull/4968)
- **Merged**: 2022-07-22
- **Author**: Emma Marichal (@emmamarichal)
- **Upstream commit**: `10a64f0df00a6b098639cce402ab4b60d519bd1d` ("updating vibes image white pixels", 2022-07-20)
- **google/fonts commit**: `59f428d689f570e2929fbcaa59eeb15012deb460`
- **Note**: Initial onboarding added the upright variable font only.

### Version 2.000
- **google/fonts PR**: [#5505](https://github.com/google/fonts/pull/5505)
- **Merged**: 2022-11-04
- **Author**: Emma Marichal (@emmamarichal)
- **Upstream commit**: `200de49f71e1dd2b01290bc3bc2c98118e10c62d` ("Merge pull request #17 from emmamarichal/master", 2022-11-03)
- **google/fonts commit**: `9442a512899380dae15e520deafa12f2b2954e31`
- **Note**: This update added the italic variable font (Figtree-Italic[wght].ttf).

### Version 2.001 (via gftools-packager)
- **google/fonts PR**: [#6465](https://github.com/google/fonts/pull/6465)
- **Merged**: 2023-06-28
- **Author**: Emma Marichal (@emmamarichal)
- **Upstream commit**: `efdedb2a9337b5baa897771e91ac9203f99e2084` ("Merge pull request #29 from emmamarichal/master", 2023-06-26)
- **google/fonts commit**: `4f3944184f136bb1e73cc7ff12b0397e85af87c4`
- **Note**: Upstream PR #29 was titled "Figtree update" -- fonts exported and checked for version 2.001.

### fontc_crater Batch Source Block Update
- **google/fonts commit**: `19cdcec59967f4aa6defb86bd0550dff1ac43abb` (2025-03-31)
- **Change**: Changed commit hash from `efdedb2` to `937cfe8`, added `config_yaml: "sources/config.yaml"`
- **Note**: The fontc_crater targets list had `937cfe8` ("exporting fonts", 2023-07-17) which was actually a later upstream commit made AFTER the google/fonts PR #6465 merged on 2023-06-28. This was an incorrect commit hash from the fontc_crater data.

### Version 2.002 (Current)
- **google/fonts PR**: [#9328](https://github.com/google/fonts/pull/9328)
- **Merged**: 2025-04-09
- **Author**: Emma Marichal (@emmamarichal)
- **Upstream commit**: `032dfa7fe219ef3a02890d6d3add84eacc9aebfe` ("Merge pull request #48 from emmamarichal/master", 2025-04-04)
- **google/fonts commits**: `98dcd735` (font update) + `7888febb3` (article + bump version) + `bbb14ea37` (image size optimization)
- **Context**: Upstream PR #48 was titled "Small update" -- merged paths to solve rendering issues reported in [google/fonts#8723](https://github.com/google/fonts/issues/8723) (related to [#7380](https://github.com/google/fonts/issues/7380) and [#7594](https://github.com/google/fonts/issues/7594), unmerged paths causing rendering problems).

## Upstream Repository Analysis

### Commit Verification
The current METADATA.pb commit `032dfa7` is verified:
- It is the HEAD of the upstream `master` branch (the latest commit)
- It was created on 2025-04-04, five days before the google/fonts PR #9328 merged on 2025-04-09
- There are no additional commits after this hash in the upstream repo
- The referenced files (`fonts/variable/Figtree[wght].ttf`, `fonts/variable/Figtree-Italic[wght].ttf`, `OFL.txt`) all exist at this commit

### Config File Verification
The `sources/config.yaml` exists at commit `032dfa7` and contains valid gftools-builder configuration:
- References `Figtree.glyphs` and `Figtree-Italic.glyphs` as sources
- Specifies `axisOrder: [wght, ital]`
- Includes STAT table configuration for both upright and italic variable fonts
- Sets `familyName: Figtree` and `cleanUp: true`

### Tags
The upstream repo has the following tags:
- `v1.0.1` (2022-08-29) at commit `fde3420`
- `v1.0.2` (2022-09-05) at commit `c3da16d`
- `v2.0.0` (2022-10-20) at commit `2769da0`
- `v2.0.1` (2022-12-28) at commit `455d917`
- `v2.0.2` (2023-03-09) at commit `c522826`
- `v2.0.3` (2023-04-05) at commit `be6cb01`

Note: No tag was created for the current HEAD commit `032dfa7`.

## Status
- **Status**: complete
- **Confidence**: HIGH
- **Repository URL**: Correct (verified accessible, matches copyright string)
- **Commit hash**: Correct (`032dfa7` -- verified as HEAD, matches PR #9328 which is the most recent update)
- **Config path**: Correct (`sources/config.yaml` exists at the referenced commit)
- **No override config needed**: Upstream repo has a proper `config.yaml`

## Summary
Figtree is fully documented with correct source metadata. The font was originally onboarded in 2022 by Emma Marichal and has been updated multiple times since. The current binaries in google/fonts correspond to upstream commit `032dfa7` (the latest upstream commit as of the most recent update in April 2025), which was merged via google/fonts PR #9328 to address rendering issues from unmerged paths. All source block fields (repository_url, commit, config_yaml, branch, files) are accurate and verified. No action needed.
