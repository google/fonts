# Investigation Report: Libertinus Mono

**Family Name**: Libertinus Mono
**Directory**: `ofl/libertinusmono`
**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete (binary-only workflow, no config.yaml applicable)
**Confidence**: HIGH

## METADATA.pb Analysis

The METADATA.pb file was found at `ofl/libertinusmono/METADATA.pb`. It contained a fully populated `source { }` block:

- **repository_url**: `https://github.com/googlefonts/libertinus`
- **commit**: `88dfbb0a7715817a43499e613fc8e6645174cd6a`
- **branch**: `main`
- **config_yaml**: not set (none applicable)

The source block also declared file mappings:
- `documentation/ARTICLE.en_us.html` -> `article/ARTICLE.en_us.html`
- `documentation/preview.jpg` -> `article/preview.jpg`
- `OFL.txt` -> `OFL.txt`
- `fonts/ttf/LibertinusMono-Regular.ttf` -> `LibertinusMono-Regular.ttf`

## Upstream Repository Analysis

### Repository Structure

The `googlefonts/libertinus` repository is **not a standard font source repository**. As stated in its README:

> "This repository is not a fork, but a Google-Fonts-centered working repository, of the popular https://github.com/alerque/libertinus font family."

The actual font sources (SFD/FontForge files) reside in `alerque/libertinus`. The `googlefonts/libertinus` repo serves as an intermediary that:

1. Downloads pre-built TTF binaries from `alerque/libertinus` GitHub releases via `build.sh`
2. Applies hotfixes using `fontspector` for Google Fonts compliance
3. Applies metric adjustments using `gftools-fontsetter` (via `.fontsetter` files)
4. Stores the processed binaries in `fonts/ttf/`

The repo has no `.glyphs`, `.ufo`, or `.designspace` source files. It has no `config.yaml` because fonts are not built from sources using gftools-builder; they are downloaded as pre-built binaries and post-processed.

### Commit History

The repository had a short commit history (5 commits total):

| Hash | Date | Message |
|------|------|---------|
| `d165379` | 2025-04-02 | Initial commit (template from googlefonts-project-template) |
| `943f733` | 2025-04-02 | Initial commit (actual Libertinus files added) |
| `7b49cf8` | 2025-04-03 | 7.051 publishable |
| `88dfbb0` | 2025-04-03 | Update README.md |
| `63b24ea` | 2025-04-14 | Dropped two instances of "Linux" in descriptions |

### Build Workflow

The `build.sh` script:
- Fetches the latest release from `alerque/libertinus` (version 7.051, released 2024-09-26)
- Downloads the release ZIP, extracts static TTFs
- Runs `fontspector` hotfixing for Google Fonts compliance
- Applies `gftools-fontsetter` with per-font `.fontsetter` configuration files
- Renames "Semibold" to "SemiBold" in Serif variants

The `LibertinusMono-Regular.fontsetter` file adjusts OS/2 and post table values:
- `usWinAscent: 895`
- `usWinDescent: 288`
- `panose bFamilyType: 2`, `bProportion: 9`
- `isFixedPitch: 1`

### Makefile

A `Makefile` exists referencing `sources/config.yaml` and `gftools builder`, but this was inherited from the googlefonts-project-template and is not actually used. The `sources/` directory does not exist in the repo. The actual build process uses `build.sh` instead.

## Commit Hash Verification

The METADATA.pb references commit `88dfbb0a7715817a43499e613fc8e6645174cd6a` ("Update README.md", 2025-04-03).

**Binary verification**: The TTF file at this commit was compared with the file in google/fonts:
- **Git blob hash** in upstream at `88dfbb0`: `dd3bb81d182db5707f16e9c50c9eeb241cd1f5e3`
- **Git blob hash** in google/fonts: `dd3bb81d182db5707f16e9c50c9eeb241cd1f5e3`
- **MD5 checksum** (both): `42dce848a720e6ed98c72e2ce597b5bc`
- **File size**: 153,480 bytes

The binary files are **identical** (exact git blob match). The commit hash is verified as correct.

Between commit `7b49cf8` ("7.051 publishable") and `88dfbb0` ("Update README.md"), only `README.md` was modified -- the TTF files were unchanged. One additional commit (`63b24ea`, 2025-04-14) was made after `88dfbb0`, also only modifying README text, not font files.

## PR History in google/fonts

The font was added to google/fonts via **PR #9303** ("Libertinus Mono: Version 7.051;RELEASE added"), authored by Yanone (post@yanone.de), merged on 2025-04-09.

The PR body stated:
> "Taken from the upstream repo https://github.com/googlefonts/libertinus at commit https://github.com/googlefonts/libertinus/commit/88dfbb0a7715817a43499e613fc8e6645174cd6a."

The PR resolved issue #12 in the google/fonts repo. Only Copilot automated review was recorded; no human review comments were found.

The commit in google/fonts was `9713f7322` ("Libertinus Mono: Version 7.051;RELEASE added", 2025-04-03), authored by Yanone.

## Sibling Families

Libertinus Mono is part of the broader Libertinus family. Related PRs in google/fonts:
- **PR #9301**: Libertinus Keyboard (merged 2025-07-17)
- **PR #9302**: Libertinus Math (merged 2025-04-10)
- **PR #9303**: Libertinus Mono (merged 2025-04-09)
- **PR #9351**: Libertinus Sans (merged 2025-07-17)
- **PR #9352**: Libertinus Serif (merged 2025-07-17)
- **PR #9353**: Libertinus Serif Display (merged 2025-07-17)
- **PR #9354**: Libertinus Serif Initials (not yet merged)

All share the same `googlefonts/libertinus` working repository.

## Config.yaml Assessment

**No config.yaml is applicable** for this font family. The `googlefonts/libertinus` repo does not use gftools-builder to compile fonts from sources. Instead, it downloads pre-built binaries from `alerque/libertinus` releases and applies post-processing (hotfixes and fontsetter adjustments).

The actual upstream sources at `alerque/libertinus` are `.sfd` (FontForge) files, which are not compatible with gftools-builder's `config.yaml` workflow.

No override `config.yaml` exists in the google/fonts family directory, and none is needed given this binary-only workflow.

## Conclusion

The source block in METADATA.pb is **complete and correct**:
- The `repository_url` correctly points to `googlefonts/libertinus` (the Google Fonts working repo)
- The `commit` hash `88dfbb0` is verified as the exact commit from which the binary was taken (confirmed by identical git blob hashes)
- The `branch` is correctly set to `main`
- File mappings are accurate
- No `config_yaml` field is needed (binary-only workflow)

No changes are required to METADATA.pb for this family.
