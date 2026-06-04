# Andada Pro

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Huerta Tipografica, Carolina Giovagnoli
**METADATA.pb path**: `ofl/andadapro/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/huertatipografica/Andada-Pro |
| Commit | `a0b87b947003dee6c615809d3eebc8c1334dc575` |
| Config YAML | `sources/build.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/huertatipografica/Andada-Pro` was already present in the METADATA.pb source block. It is confirmed by:

1. The gftools-packager commit messages in google/fonts PR #3430 and PR #3693, which both explicitly reference `https://github.com/huertatipografica/Andada-Pro`.
2. The cached clone at `huertatipografica/Andada-Pro` has its remote origin set to the same URL.
3. The copyright string in METADATA.pb references `https://github.com/huertatipografica/Andada` (an older repo name), while the actual upstream repo is `Andada-Pro` -- a separate repository for the "Pro" variant.

## How the Commit Hash Was Identified

The commit hash `a0b87b947003dee6c615809d3eebc8c1334dc575` is confirmed through multiple lines of evidence:

1. **gftools-packager message**: The google/fonts commit `4898fbdc` (PR #3693, merged 2021-08-12) explicitly states: "Andada Pro Version 3.003 taken from the upstream repo ... at commit a0b87b947003dee6c615809d3eebc8c1334dc575."

2. **Binary file verification**: The git blob hashes of the variable font files match exactly between the upstream repo at this commit and google/fonts:
   - `AndadaPro[wght].ttf`: blob `3b23defde4760dcca210a24b2fbc7d4216b83e48` (271,784 bytes) -- matches in both repos
   - `AndadaPro-Italic[wght].ttf`: blob `3cf0761c5edf9f7169fda099dee0829c33a853bf` (268,388 bytes) -- matches in both repos

3. **Timeline consistency**: The upstream commit is dated 2021-08-05, which is 7 days before the google/fonts merge on 2021-08-12. This is a reasonable gap for review and merging.

4. **Commit is HEAD of master**: This commit (`a0b87b9`) is the latest commit on the master branch at the time it was used. The HEAD is currently detached at this commit in the cached repo, and there are no subsequent commits on master (though there are later commits on the branch after this point, totaling 27+ additional commits since then for version 3.005 and beyond).

### Prior onboarding (PR #3430)

An earlier onboarding attempt in PR #3430 (merged 2021-05-21) used commit `129785ebf91d19507bb77f321d20c0c3114cbea5`. That version was later superseded by PR #3693 with the current commit, which updated the font binaries to reflect ligature fixes and other refinements made by Carolina Giovagnoli between May and August 2021.

## How Config YAML Was Resolved

The `sources/build.yaml` file exists at the referenced commit. Its contents at commit `a0b87b9` are:

```yaml
sources:
  - AndadaPro.glyphs
  - AndadaPro-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Andada Pro
```

This is a valid gftools-builder configuration referencing two `.glyphs` source files (both present in the `sources/` directory at the same commit). No override config.yaml is needed in google/fonts since the upstream config is present and correct.

## Conclusion

The METADATA.pb source block for Andada Pro is **complete and verified**. All fields are correct:

- The repository URL points to a valid, accessible upstream repo.
- The commit hash `a0b87b9` matches exactly -- binary font files have identical git blob hashes between upstream and google/fonts.
- The `sources/build.yaml` config file exists at the referenced commit with valid gftools-builder configuration.
- The branch is correctly set to `master`.
- The file mappings (`fonts/variable/AndadaPro[wght].ttf` and `fonts/variable/AndadaPro-Italic[wght].ttf`) are correct.

No changes are needed. Note that there have been 27+ upstream commits since this onboarding (version 3.005 work), which would need separate review if an update is desired.
