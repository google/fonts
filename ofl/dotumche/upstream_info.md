# Investigation Report: DotumChe

## Family Overview

- **Family name**: DotumChe
- **Designer**: HanYang I&C Co.
- **License**: OFL
- **Category**: Sans Serif
- **Primary script**: Korean (Kore)
- **Date added**: 2024-05-15
- **Description**: DotumChe is a well-known gothic-style Korean font that first shipped with Windows 95, designed with clean, simple strokes for clarity in user interfaces. This version includes monospace, half-width Latin characters.

## Source Block (Current)

The METADATA.pb at `ofl/dotumche/METADATA.pb` already contains a source block:

```
source {
  repository_url: "https://github.com/googlefonts/gulim"
  commit: "012723a8d5b6a6dc920330f26d165422c3014fd6"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/hinted/dotumche-Regular.ttf"
    dest_file: "DotumChe-Regular.ttf"
  }
  branch: "main"
}
```

## Upstream Repository

- **URL**: https://github.com/googlefonts/gulim
- **Local cache**: `upstream_repos/fontc_crater_cache/googlefonts/gulim`
- **Remote verified**: Yes (origin points to https://github.com/googlefonts/gulim)

### Repository Structure

The gulim repository hosts four related Korean font families: Gulim, GulimChe, Dotum, and DotumChe. All four originate from HanYang I&C Co. legacy fonts.

```
sources/
  ttf/
    Dotum.ttf        (original TTF source)
    DotumChe.ttf     (original TTF source)
    Gulim.ttf        (original TTF source)
    GulimChe.ttf     (original TTF source)
  ttc/
    gulim.ttc        (TrueType Collection containing all four)
fonts/
  ttf/
    hinted/          (processed outputs with hinting)
    unhinted/        (processed outputs without hinting)
    bitmap/          (processed outputs with bitmap tables)
  ttc/
    gulim-Regular.ttc
```

### Source File Format

The sources are **pre-compiled TTF binaries** (TrueType Font data with 19 tables including EBDT bitmap data). There are NO standard editable source files (.glyphs, .ufo, .designspace, .sfd) in the repository.

The build process is a Python script (`process.py`) that:
1. Reads the source TTFs from `sources/ttf/`
2. Removes control character glyphs
3. Updates copyright and license strings
4. Sets `fontRevision` to 2.210
5. Applies hinting fixes via `gftools fix-hinting`
6. Creates subsets: bitmap (with EBLC/EBDT), hinted (without bitmaps), and unhinted (dehinted)
7. Creates a TTC from the four static TTFs

Dependencies: `fontbakery[googlefonts]>=0.9.2`, `gftools[qa]>=0.9.23`, `dehinter`

### No config.yaml

There is **no `config.yaml`** file anywhere in the upstream repository. The build process uses a custom `process.py` script and `Makefile`, not gftools-builder. This is because the sources are pre-compiled TTFs that undergo post-processing, not standard font source files that gftools-builder would compile.

There is also **no override `config.yaml`** in `ofl/dotumche/` in google/fonts.

## Commit Verification

### Referenced Commit

- **Hash**: `012723a8d5b6a6dc920330f26d165422c3014fd6`
- **Author**: Aaron Bell <aaron@sajatypeworks.com>
- **Date**: 2024-05-15 21:35:03 -0700
- **Message**: "updating filenames"
- **This is the HEAD commit** of the gulim repository (the latest and last commit)

This commit is confirmed to exist in the upstream repository and is the most recent commit.

### Onboarding History in google/fonts

1. **`485993a9e`** (2024-05-15) by Aaron Bell: "Dotumche: Version 2.21 added" -- Initial onboarding with `dotumche-Regular.ttf` (lowercase, 4,568,076 bytes). Commit message explicitly references upstream repo and commit `012723a`.

2. **`aeb0fac6f`** (2024-06-04) by Aaron: "Update DESCRIPTION.en_us.html" -- Replaced placeholder description text.

3. **`c035cf0f1`** (2024-06-24) by Aaron: "Delete dotumche-Regular.ttf" -- Removed the lowercase-named file (4,568,076 bytes).

4. **`685530dc5`** (2024-06-24) by Aaron: "Updating vertical metrics and metadata" -- Added new `DotumChe-Regular.ttf` (capitalized, 4,568,508 bytes) with updated vertical metrics.

5. **`15d222b8e`** (2024-06-28) by Viviana Monsalve: "Dotumche Japanese deleted" -- Removed Japanese subset from METADATA.pb.

### PR History

- **PR #7674**: "Dotumche: Version 2.21 added" by @aaronbell, merged 2024-06-27 by @emmamarichal.
  - PR body states: "Taken from the upstream repo https://github.com/googlefonts/gulim at commit https://github.com/googlefonts/gulim/commit/012723a8d5b6a6dc920330f26d165422c3014fd6"

### Binary File Discrepancy

The font binary in google/fonts (`DotumChe-Regular.ttf`, 4,568,508 bytes) does NOT exactly match the file at the referenced upstream commit (`fonts/ttf/hinted/dotumche-Regular.ttf`, 4,568,076 bytes). The google/fonts version is 432 bytes larger because Aaron updated vertical metrics during the PR review process (commit `685530dc5`). This modification happened in the google/fonts PR branch, not in the upstream repository.

This means the `source_file` path in the METADATA.pb source block (`fonts/ttf/hinted/dotumche-Regular.ttf`) points to the original file at that commit, but the actual binary shipped in google/fonts has been locally modified.

## Assessment

### Status: complete (with caveats)

The source block is correctly populated with the right repository URL and commit hash. The commit hash `012723a` is indeed the commit that was used as the basis for onboarding, as confirmed by both the google/fonts commit message and the PR body.

### Why no config.yaml is appropriate

A gftools-builder `config.yaml` is **not applicable** for this family. The upstream repo does not contain standard editable font sources -- it contains pre-compiled legacy TTF binaries that are post-processed via a custom Python script. gftools-builder cannot be used to build fonts from TTF sources. Creating an override config.yaml would serve no purpose.

### Confidence: HIGH

- Repository URL is correct and verified
- Commit hash is explicitly documented in both the google/fonts commit message and the PR body
- The commit is the HEAD of the upstream repository
- The onboarder (Aaron Bell) is the same person who created the upstream repository

### Remaining Notes

- The binary in google/fonts was locally modified during the PR process (vertical metrics update), so it does not byte-for-byte match the upstream file at the referenced commit
- The source block uses the `files` mapping pattern (explicit source_file to dest_file), not config_yaml, which is the correct approach for TTF-sourced fonts
- Four related families (Gulim, GulimChe, Dotum, DotumChe) all share the same upstream repo `googlefonts/gulim` and the same commit hash
- DotumChe was merged one day before its sibling Dotum: DotumChe PR #7674 merged 2024-06-27, Dotum PR #7673 merged 2024-06-28
