# Investigation Report: Libertinus Sans

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Family slug**: libertinussans
**Status**: complete (pre-built binary distribution, no config.yaml applicable)
**Confidence**: HIGH

## METADATA.pb Source Block (Current)

The METADATA.pb at `ofl/libertinussans/METADATA.pb` already contained a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/libertinus"
  commit: "63b24ea7904a0ae69b38732b50dc6ebc277f9b68"
  files {
    source_file: "documentation/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "documentation/preview.jpg"
    dest_file: "article/preview.jpg"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/LibertinusSans-Bold.ttf"
    dest_file: "LibertinusSans-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/LibertinusSans-Italic.ttf"
    dest_file: "LibertinusSans-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/LibertinusSans-Regular.ttf"
    dest_file: "LibertinusSans-Regular.ttf"
  }
  branch: "main"
}
```

## Repository Analysis

### Repository URL Verification

The upstream repository URL `https://github.com/googlefonts/libertinus` was verified as valid and accessible. The local clone at `upstream_repos/fontc_crater_cache/googlefonts/libertinus/` was clean and up-to-date with the remote.

### Nature of the Repository

This is **not** a traditional source repository. The README explicitly states:

> This repository is not a fork, but a Google-Fonts-centered working repository, of the popular https://github.com/alerque/libertinus font family.

The actual font source development happens at `https://github.com/alerque/libertinus`. The `googlefonts/libertinus` repo serves as a **packaging/intermediary repository** that:

1. Downloads pre-built TTF binaries from `alerque/libertinus` releases via `build.sh`
2. Applies hotfixes using `fontspector` for Google Fonts compliance
3. Applies fontsetter modifications using `.fontsetter` files
4. Commits the processed binaries for onboarding to Google Fonts

The `build.sh` script fetches the latest release from `alerque/libertinus` as a zip file, extracts the static TTF files, and applies post-processing.

### No Source Files in Upstream

The repository contained no font source files (no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files). The fonts are pre-built binaries downloaded from the original upstream project's releases. The `Makefile` referenced `sources/config.yaml` but this was a leftover from the `googlefonts-project-template` and no `sources/` directory existed at any commit.

### config.yaml Assessment

No `config.yaml` existed in the upstream repository at the referenced commit (or at any commit). No override `config.yaml` existed in the google/fonts family directory either.

A `config.yaml` is **not applicable** for this family because:
- The fonts are not compiled from source files using gftools-builder
- They are pre-built TTF binaries downloaded from the original upstream project (`alerque/libertinus`)
- The build process (`build.sh`) downloads, hotfixes, and fontsets existing binaries

The `config_yaml` field was correctly omitted from the METADATA.pb source block.

## Commit Hash Verification

### Referenced Commit

- **Hash**: `63b24ea7904a0ae69b38732b50dc6ebc277f9b68`
- **Date**: 2025-04-14
- **Author**: Yanone
- **Message**: "Dropped two instances of 'Linux' in descriptions"
- **Changes**: Modified `README.md` and `documentation/ARTICLE.en_us.html` only (no font file changes)

### Commit History of the Upstream Repo

The `googlefonts/libertinus` repository had only 5 commits, all by Yanone:

| Hash | Date | Message |
|------|------|---------|
| `63b24ea` | 2025-04-14 | Dropped two instances of "Linux" in descriptions |
| `88dfbb0` | 2025-04-03 | Update README.md |
| `7b49cf8` | 2025-04-03 | 7.051 publishable |
| `943f733` | 2025-04-02 | Initial commit |
| `d165379` | 2025-04-02 | Initial commit |

The referenced commit `63b24ea` was the **HEAD of main** (latest commit) and was also the latest commit on the remote.

### Binary File Verification

The SHA-256 checksums of the TTF files matched exactly between the upstream repo and google/fonts:

- `LibertinusSans-Regular.ttf`: `2d261d21add710a08b2ffbd89072d7fd2f29a19582e872da4b8f8f6d622cd78b`
- `LibertinusSans-Bold.ttf`: `92e1e56b0d949241c400e3bca9a772a5318d3b49de7c5f7ccff0413d1a4cc339`
- `LibertinusSans-Italic.ttf`: `44527ec77f40df4a9f5b306ca4db46d973ddf90929e7e875f8dde0084754ef38`

This confirmed that the fonts in google/fonts were taken directly from the `fonts/ttf/` directory of the referenced commit without modification.

## Google Fonts History

### Onboarding

The family was onboarded in commit `6c38236b3` by Yanone on 2025-04-16 via PR #9351. The commit message explicitly stated:

> Taken from the upstream repo https://github.com/googlefonts/libertinus at commit https://github.com/googlefonts/libertinus/commit/63b24ea7904a0ae69b38732b50dc6ebc277f9b68.

The PR was merged on 2025-06-27 as merge commit `b41a85f56`. The PR body contained no discussion comments.

### Subsequent Modifications

Two follow-up commits by Emma Marichal on 2025-06-20:
1. **`a06a098c4`**: Cleaned the OFL.txt to include only the Libertinus Sans copyright line (removed copyright lines for other Libertinus sub-families that had been incorrectly included)
2. **`ce0b3c96`**: Updated METADATA.pb to replace placeholder `"???."` copyright strings with proper copyright notices

## Related Families

The `googlefonts/libertinus` repo was a shared upstream for multiple Libertinus font families in Google Fonts, all onboarded together:

- **Libertinus Sans** (PR #9351) -- this family
- Libertinus Serif (PR #9352)
- Libertinus Serif Display (PR #9353)
- Libertinus Keyboard (PR #9301)
- Libertinus Math (PR #9302)
- Libertinus Mono (PR #9303)

All referenced the same upstream commit `63b24ea`.

## Conclusion

The source block in METADATA.pb was already complete and accurate. The repository URL, commit hash, file mappings, and branch were all correctly specified. The `config_yaml` field was correctly omitted because the fonts were pre-built binaries (not compiled from source via gftools-builder). No changes were needed.

### Summary

| Field | Value | Status |
|-------|-------|--------|
| repository_url | `https://github.com/googlefonts/libertinus` | Correct |
| commit | `63b24ea7904a0ae69b38732b50dc6ebc277f9b68` | Verified (HEAD of main, binary hashes match) |
| config_yaml | (omitted) | Correct (pre-built binaries, not applicable) |
| files | 6 file mappings | Correct |
| branch | main | Correct |
