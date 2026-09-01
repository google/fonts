# Baloo Bhaijaan 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Designer**: Ek Type (Girish Dalvi and collaborators)

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/EkType/Baloo2-Variable |
| commit           | da4090c1dd5798a3e72d7138e379ee1f94d6349c |
| config_yaml      | builder/BalooBhaijaan2.yaml |
| branch           | master |

## Repository URL

The METADATA.pb points to `https://github.com/EkType/Baloo2-Variable`. This is the correct upstream repository owned by EkType (the original Baloo designers). The repository is a multi-family mono-repo containing sources and build configs for all ten Baloo 2 script variants: Baloo 2 (Latin), Baloo Bhai 2 (Gujarati), Baloo Bhaijaan 2 (Arabic), Baloo Bhaina 2 (Odia), Baloo Chettan 2 (Malayalam), Baloo Da 2 (Bangla), Baloo Paaji 2 (Gurmukhi), Baloo Tamma 2 (Kannada), Baloo Tammudu 2 (Telugu), and Baloo Thambi 2 (Tamil).

Notably, some sibling families (e.g., Baloo 2 Latin) point to `yanone/Baloo2-Variable` (Yanone's fork) with different commits, while Baloo Bhaijaan 2 correctly points to the EkType original. Yanone (post@yanone.de) contributed via pull requests to the EkType repo. Commit `da4090c` is a merge commit in EkType's repo merging yanone's PR #5, so this commit only exists in the EkType repo and is not present in the yanone fork.

Both repos are cached locally:
- EkType/Baloo2-Variable (remote: https://github.com/EkType/Baloo2-Variable)
- yanone/Baloo2-Variable (remote: https://github.com/yanone/Baloo2-Variable)

## Commit Verification

The referenced commit `da4090c1dd5798a3e72d7138e379ee1f94d6349c` is the HEAD of the EkType/Baloo2-Variable master branch. It is a merge commit:

```
commit da4090c1dd5798a3e72d7138e379ee1f94d6349c
Merge: 92ff4ce 29ddd81
Author: Girish Dalvi <girish-dalvi@users.noreply.github.com>
Date:   Fri Sep 9 18:21:28 2022 +0530

    Merge pull request #5 from yanone/master
    Regenerated Bhaijaan font as 1.701 without data changes
```

This commit modifies:
- `fonts/variable/BalooBhaijaan2[wght].ttf` (272864 -> 285508 bytes)
- `sources/BalooBhaijaan2.glyphs` (98289 changes)

### Binary File Verification

The font binary at this commit matches the file in google/fonts exactly:
- **Size**: 285508 bytes (both match)
- **SHA256**: `3e9f07fbc796c0ddcb3e6e0aa26f9c86741d9f5b7f5cb72f4ed3c06e55a19336` (both match)

### google/fonts Onboarding Commit

The font was onboarded via commit `d3d979f3d` in google/fonts (PR #5216):
```
[gftools-packager] Baloo Bhaijaan 2: Version 1.701 added (#5216)

Baloo Bhaijaan 2 Version 1.701 taken from the upstream repo
https://github.com/EkType/Baloo2-Variable at commit
https://github.com/EkType/Baloo2-Variable/commit/da4090c1dd5798a3e72d7138e379ee1f94d6349c
```

Date: 2022-09-13 (4 days after the upstream commit on 2022-09-09). The timeline is consistent: Yanone made the upstream changes, they were merged into EkType's repo, and then Yanone packaged the font for google/fonts.

## Config Verification

The config file `builder/BalooBhaijaan2.yaml` exists at commit `da4090c`:

```yaml
sources:
  - ../sources/BalooBhaijaan2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This is a valid gftools-builder configuration. It references `sources/BalooBhaijaan2.glyphs` which exists at the commit (a .glyphs file, 1044767 bytes). The config was created on 2021-10-22 in commit `bb4d965` ("Create BalooBhaijaan2.yaml").

No local override config.yaml exists in the google/fonts family directory (one was generated on a branch `felipesanches/add_source_config_yaml_files` but never merged to main).

## Conclusion

All source metadata for Baloo Bhaijaan 2 is **complete and verified**:

- **Repository URL**: Correct. Points to EkType/Baloo2-Variable, the original upstream repo.
- **Commit hash**: Correct. `da4090c` is confirmed by binary SHA256 match and corroborated by the gftools-packager commit message in PR #5216.
- **Config path**: Correct. `builder/BalooBhaijaan2.yaml` exists at the referenced commit with valid gftools-builder configuration.
- **No action needed**: The source block is complete with repository_url, commit, config_yaml, branch, and file mappings all present and verified.

Note: This family uses `EkType/Baloo2-Variable` with commit `da4090c` (a merge commit), while some sibling Baloo 2 families point to `yanone/Baloo2-Variable` with different commits. This is because the work was done by Yanone in a fork and merged into the EkType original at different points for different scripts.
