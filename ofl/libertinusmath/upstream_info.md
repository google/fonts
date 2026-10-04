# Investigation Report: Libertinus Math

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD-only sources, no config.yaml applicable)
**Confidence**: HIGH

## 1. METADATA.pb Analysis

The METADATA.pb file at `ofl/libertinusmath/METADATA.pb` contained a source block with the following information:

- **repository_url**: `https://github.com/googlefonts/libertinus`
- **commit**: `88dfbb0a7715817a43499e613fc8e6645174cd6a`
- **branch**: `main`
- **config_yaml**: not set

The source block also included file mappings:
- `documentation/ARTICLE.en_us.html` -> `article/ARTICLE.en_us.html`
- `documentation/preview.jpg` -> `article/preview.jpg`
- `OFL.txt` -> `OFL.txt`
- `fonts/ttf/LibertinusMath-Regular.ttf` -> `LibertinusMath-Regular.ttf`

## 2. google/fonts Commit History

The font was added to google/fonts in a single commit:

- **Commit**: `c02c7b312e5c893e4288dce140ce58ed6fd58d55`
- **Date**: 2025-04-03
- **Author**: Yanone (post@yanone.de)
- **Message**: "Libertinus Math: Version 7.051;RELEASE added"
- **Body**: "Taken from the upstream repo https://github.com/googlefonts/libertinus at commit https://github.com/googlefonts/libertinus/commit/88dfbb0a7715817a43499e613fc8e6645174cd6a. Resolves #12"
- **PR**: #9302, merged on 2025-04-10 by Yanone

## 3. Upstream Repository Analysis

### googlefonts/libertinus (Packaging Repository)

The repository at `https://github.com/googlefonts/libertinus` is **not a source repository** in the traditional sense. As documented in its README:

> "This repository is not a fork, but a Google-Fonts-centered working repository, of the popular https://github.com/alerque/libertinus font family."

The repository was created by Yanone specifically to package Libertinus fonts for Google Fonts. It contains:
- Pre-compiled TTF binaries downloaded from `alerque/libertinus` releases
- A `build.sh` script that downloads the latest release, unpacks it, and applies hotfixes using `fontspector` and `gftools-fontsetter`
- `.fontsetter` files for metric adjustments (e.g., `LibertinusMath-Regular.fontsetter` sets `OS/2->usWinAscent: 3813` and `OS/2->usWinDescent: 1641`)
- Documentation files (ARTICLE.en_us.html, preview.jpg)
- **No font source files** (.glyphs, .ufo, .designspace, .sfd)
- **No config.yaml** (not applicable since fonts are not built from sources here)

The complete commit history of this repository (5 commits total, all by Yanone):
1. `d165379` (2025-04-02) - Initial commit (template)
2. `943f733` (2025-04-02) - Initial commit (added font files and build infrastructure)
3. `7b49cf8` (2025-04-03) - "7.051 publishable" (documentation updates, hotfixed TTFs)
4. `88dfbb0` (2025-04-03) - "Update README.md" **(referenced commit)**
5. `63b24ea` (2025-04-14) - "Dropped two instances of 'Linux' in descriptions" (documentation-only)

The repository was clean with no local modifications.

### alerque/libertinus (True Source Repository)

The actual font sources reside at `https://github.com/alerque/libertinus`. This repository contains:
- **SFD source files** (FontForge Spline Font Database format) in `sources/`
- Sources include `LibertinusMath-Regular.sfd` among 14 SFD files
- The build system uses `fontship.mk` (a custom Makefile-based build tool), not gftools-builder
- The latest release is **v7.051**, published on 2024-09-26

The `googlefonts/libertinus` packaging repo's `build.sh` script downloads the v7.051 release ZIP from `alerque/libertinus`, extracts the static TTF files, and applies Google Fonts-specific hotfixes.

## 4. Commit Hash Verification

The referenced commit `88dfbb0a7715817a43499e613fc8e6645174cd6a` was verified:

- **What it changed**: Only `README.md` (1 line change)
- **Date**: 2025-04-03, same day as the google/fonts onboarding commit
- **Binary verification**: The `LibertinusMath-Regular.ttf` file in google/fonts matches the one at this commit exactly (MD5: `80838af4cab960dc26b377b5a5ba927e`)

One commit was made after the referenced commit (63b24ea on 2025-04-14), but it only changed `README.md` and `documentation/ARTICLE.en_us.html` -- no font files were modified. The referenced commit hash is correct and appropriate.

## 5. Config.yaml Assessment

**No config.yaml is applicable for this family.**

The font sources are SFD files in the `alerque/libertinus` repository, which are built using FontForge via a custom `fontship.mk` build system, not gftools-builder. The `googlefonts/libertinus` packaging repository distributes pre-compiled TTF binaries with hotfixes applied -- it does not compile fonts from sources.

Since gftools-builder cannot process SFD source files, creating a config.yaml (either in the upstream repo or as an override in google/fonts) is not possible. The current METADATA.pb source block correctly points to the packaging repository where the binary TTFs are maintained.

## 6. Summary

| Field | Value |
|-------|-------|
| Family | Libertinus Math |
| Repository URL | https://github.com/googlefonts/libertinus |
| Commit | 88dfbb0a7715817a43499e613fc8e6645174cd6a |
| Branch | main |
| Config | none (SFD-only sources in alerque/libertinus; packaging repo uses pre-built binaries) |
| Status | complete |
| Confidence | HIGH |
| PR | google/fonts#9302 (merged 2025-04-10) |
| Onboarder | Yanone (Jens Kutilek) |
| Binary match | Confirmed (MD5 match) |

The source block in METADATA.pb is complete and correct. The repository URL, commit hash, and branch are all verified. No config.yaml is needed because the font sources (SFD format) are not compatible with gftools-builder. The true upstream source is `alerque/libertinus`, while `googlefonts/libertinus` serves as a Google Fonts packaging layer.
