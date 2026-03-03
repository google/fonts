# Investigation Report: Libertinus Serif

**Family Name**: Libertinus Serif
**Directory**: `ofl/libertinusserif`
**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete (pre-built binaries only, no gftools-builder config applicable)

## METADATA.pb Source Block (current)

The METADATA.pb already contained a complete source block:

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
    source_file: "fonts/ttf/LibertinusSerif-Regular.ttf"
    dest_file: "LibertinusSerif-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/LibertinusSerif-Italic.ttf"
    dest_file: "LibertinusSerif-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/LibertinusSerif-SemiBold.ttf"
    dest_file: "LibertinusSerif-SemiBold.ttf"
  }
  files {
    source_file: "fonts/ttf/LibertinusSerif-SemiBoldItalic.ttf"
    dest_file: "LibertinusSerif-SemiBoldItalic.ttf"
  }
  files {
    source_file: "fonts/ttf/LibertinusSerif-Bold.ttf"
    dest_file: "LibertinusSerif-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/LibertinusSerif-BoldItalic.ttf"
    dest_file: "LibertinusSerif-BoldItalic.ttf"
  }
  branch: "main"
}
```

## Repository Analysis

### googlefonts/libertinus (referenced in METADATA.pb)

The repository at `https://github.com/googlefonts/libertinus` is **not** the original font source repository. As stated in its README:

> "This repository is not a fork, but a Google-Fonts-centered working repository, of the popular https://github.com/alerque/libertinus font family."

The repository contains a `build.sh` script that:
1. Downloads the latest release ZIP from `alerque/libertinus` via the GitHub API
2. Extracts pre-built static TTF files from the release
3. Applies fontspector hotfixes for Google Fonts compliance
4. Applies fontsetter metadata adjustments (via `.fontsetter` files)
5. Renames "Semibold" to "SemiBold" in file names and font name tables

The repo contained **no gftools-builder-compatible source files** (no `.glyphs`, `.ufo`, or `.designspace` files) and **no `config.yaml`**. The `Makefile` referenced `sources/config.yaml` (from the googlefonts project template), but that file and directory did not exist. The actual build process was entirely through `build.sh`.

### alerque/libertinus (true upstream source)

The actual font sources lived at `https://github.com/alerque/libertinus`. The source files were in **SFD format** (FontForge), which was not gftools-builder-compatible:
- `sources/LibertinusSerif-Regular.sfd`
- `sources/LibertinusSerif-Italic.sfd`
- `sources/LibertinusSerif-Bold.sfd`
- `sources/LibertinusSerif-BoldItalic.sfd`
- `sources/LibertinusSerif-Semibold.sfd`
- `sources/LibertinusSerif-SemiboldItalic.sfd`

The `alerque/libertinus` repo used its own build system (`fontship.mk`) to compile the fonts, not gftools-builder.

### Commit History (googlefonts/libertinus)

The repository had only 5 commits total:

| Commit | Date | Message |
|--------|------|---------|
| `63b24ea` | 2025-04-14 | Dropped two instances of "Linux" in descriptions |
| `88dfbb0` | 2025-04-03 | Update README.md |
| `7b49cf8` | 2025-04-03 | 7.051 publishable |
| `943f733` | 2025-04-02 | Initial commit |
| `d165379` | 2025-04-02 | Initial commit |

The referenced commit `63b24ea` was the HEAD of the `main` branch and the latest commit in the repository.

## Commit Hash Verification

The commit hash `63b24ea7904a0ae69b38732b50dc6ebc277f9b68` was verified to be correct:

1. **PR #9352** ("Libertinus Serif: Version 7.051;RELEASE added") was created by @yanone on 2025-04-16 and merged by @m4rc1e on 2025-06-27
2. The PR body explicitly stated: "Taken from the upstream repo https://github.com/googlefonts/libertinus at commit https://github.com/googlefonts/libertinus/commit/63b24ea7904a0ae69b38732b50dc6ebc277f9b68"
3. All 6 TTF file sizes matched exactly between google/fonts and the upstream repo at that commit:
   - LibertinusSerif-Regular.ttf: 603,444 bytes
   - LibertinusSerif-Italic.ttf: 605,956 bytes
   - LibertinusSerif-SemiBold.ttf: 497,840 bytes
   - LibertinusSerif-SemiBoldItalic.ttf: 616,600 bytes
   - LibertinusSerif-Bold.ttf: 510,796 bytes
   - LibertinusSerif-BoldItalic.ttf: 506,340 bytes
4. The commit was the HEAD of `main` -- no newer commits existed
5. All source_file paths in the METADATA.pb files mapping were verified to exist at this commit

## Config.yaml Assessment

A `config.yaml` was **not applicable** for this family because:

1. The `googlefonts/libertinus` working repository did not contain gftools-builder-compatible sources -- it stored pre-built TTF binaries downloaded from `alerque/libertinus` releases
2. The true upstream source at `alerque/libertinus` used SFD (FontForge) format, which was not compatible with gftools-builder
3. The METADATA.pb source block already used explicit `files { }` mappings to copy the pre-built TTFs directly, which was the correct approach for this type of font

No override `config.yaml` in google/fonts was needed or would be useful, since there were no buildable sources to configure.

## Summary

| Field | Value |
|-------|-------|
| Repository URL | `https://github.com/googlefonts/libertinus` |
| Commit | `63b24ea7904a0ae69b38732b50dc6ebc277f9b68` |
| Branch | `main` |
| Config | None (SFD-only true upstream; pre-built binaries in working repo) |
| Status | Complete |
| Confidence | **HIGH** |

The METADATA.pb source block was already complete and correct. The repository URL, commit hash, file mappings, and branch were all verified. The font used pre-built binaries from a working repository rather than gftools-builder compilation, so no `config.yaml` was needed. The true font sources (SFD files) lived in the separate `alerque/libertinus` repository.
