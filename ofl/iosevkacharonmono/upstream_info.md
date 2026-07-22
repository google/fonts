# Iosevka Charon Mono — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `iosevkacharonmono`
**Status**: complete (archive-based onboarding, no gftools-builder config applicable)

## Initial State

The METADATA.pb at `ofl/iosevkacharonmono/METADATA.pb` already contained a complete `source { }` block:

```
source {
  repository_url: "https://github.com/jul-sh/iosevka-charon"
  commit: "727f1343e957cadd354f9ec4ee98eba9b645143d"
  archive_url: "https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Light.ttf" dest_file: "IosevkaCharonMono-Light.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-LightItalic.ttf" dest_file: "IosevkaCharonMono-LightItalic.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Regular.ttf" dest_file: "IosevkaCharonMono-Regular.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Italic.ttf" dest_file: "IosevkaCharonMono-Italic.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Medium.ttf" dest_file: "IosevkaCharonMono-Medium.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-MediumItalic.ttf" dest_file: "IosevkaCharonMono-MediumItalic.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Bold.ttf" dest_file: "IosevkaCharonMono-Bold.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-BoldItalic.ttf" dest_file: "IosevkaCharonMono-BoldItalic.ttf" }
  branch: "main"
}
```

The family directory contained 8 TTF files (Light, LightItalic, Regular, Italic, Medium, MediumItalic, Bold, BoldItalic), METADATA.pb, OFL.txt, and an article directory with ARTICLE.en_us.html. No DESCRIPTION.en_us.html and no override config.yaml were present.

## Investigation

### Upstream Repository

The upstream repository is https://github.com/jul-sh/iosevka-charon, maintained by Juliette Pluto (jul-sh). The repository was created on 2021-10-31 and describes both "Iosevka Charon" (quasi-proportional) and "Iosevka Charon Mono" (true monospace) as derivatives of the Iosevka open source font project by be5invis.

### Build System

This font does NOT use gftools-builder and has no `.glyphs`, `.ufo`, or `.designspace` source files. Instead, it uses Iosevka's own parametric build system:

1. **Source**: The Iosevka source code is embedded as a git subtree under `sources/iosevka/`
2. **Build plans**: Font variants are defined in `sources/private-build-plans.toml` — a TOML configuration that specifies character variants, weights (Light/300, Regular/400, Medium/500, Bold/700), slopes (Upright, Italic), and spacing (quasi-proportional for Charon, normal monospace for Charon Mono)
3. **Build pipeline**: A `Makefile` orchestrates a multi-stage build:
   - Stage 1: `scripts/iosevka_build.py` compiles raw fonts from Iosevka sources using the build plan
   - Stage 2: `scripts/fix_fonts.py` post-processes fonts for Google Fonts compliance (vertical metrics, component flattening, copyright notices, etc.)
4. **Environment**: The build uses Nix (flake.nix) for reproducible dependency management
5. **Distribution**: Pre-built TTFs are published as GitHub Release assets

Since gftools-builder cannot build Iosevka-based fonts (they require Node.js and the Iosevka build toolchain), no `config.yaml` is applicable. The fonts are onboarded via the `archive_url` and `files` mapping mechanism in METADATA.pb.

### Commit Hash Verification

The commit `727f1343e957cadd354f9ec4ee98eba9b645143d` was verified against the upstream repository:

- **Commit message**: "Merge pull request #16 from jul-sh/v34.1.0-w-almost-flat-top — v34.1.0: w = curly-almost-flat-top-serifless"
- **Commit date**: 2026-02-13T16:09:26Z
- **Author**: jul-sh
- **Release**: This commit corresponds exactly to the `v34.100` release tag, created at the same timestamp (2026-02-13T16:09:26Z)

The archive_url `https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip` correctly points to the v34.100 release asset.

Two subsequent commits were found between the referenced commit and the PR merge date (2026-02-27):
- `5501bc426a3f` (2026-02-20): "Update README description"
- `343fcf7a5004` (2026-02-20): "Fix stray conflict marker text in README"

These are documentation-only changes and do not affect font files or build configuration, confirming the referenced commit is correct for the font binaries.

### Google Fonts PR History

The font was onboarded via PR [#10247](https://github.com/google/fonts/pull/10247):
- **Title**: "Iosevka Charon Mono: Version 34.100 added"
- **Author**: Emma Marichal (@emmamarichal)
- **Created**: 2026-02-19
- **Merged**: 2026-02-27 by Marc Foley (@m4rc1e)
- **Body**: "Taken from the upstream repo https://github.com/jul-sh/iosevka-charon at commit https://github.com/jul-sh/iosevka-charon/commit/727f1343e957cadd354f9ec4ee98eba9b645143d."

The google/fonts commit history for this directory shows 4 commits:
1. `691932aca` (2026-02-19): "Iosevka Charon Mono: Version 34.100 added" — initial onboarding with font files, METADATA.pb, and OFL.txt
2. `34457f077` (2026-02-19): "article" — added ARTICLE.en_us.html
3. `7a0413213` (2026-02-19): "OFL update"
4. `c7f2c84d2` (2026-02-20): "Refine description of Iosevka Charon font"

### Sibling Family

The repository also produces "Iosevka Charon" (quasi-proportional variant), onboarded in the sibling directory `ofl/iosevkacharon/` via PR [#10245](https://github.com/google/fonts/pull/10245).

### Copyright

The font copyright reads: "Copyright 2015-2025 The Iosevka Project Authors (https://github.com/be5invis/Iosevka)" — referring to the upstream Iosevka project from which Iosevka Charon derives.

## Actions Taken

No changes were needed. The METADATA.pb already contained a complete and accurate source block. The investigation verified all existing metadata:
- Repository URL is valid and accessible
- Commit hash matches the v34.100 release and is the correct onboarding commit
- Archive URL points to the correct release asset
- File mappings correctly reference paths within the release ZIP
- Branch field is set to "main"

## Final State

The source block in METADATA.pb is complete and correct. No `config_yaml` field is needed because the font uses Iosevka's custom build system, not gftools-builder. The fonts are distributed as pre-built binaries via GitHub Releases, and the `archive_url` + `files` mechanism properly handles this onboarding pattern.

The upstream repo is not yet cloned in the local cache at `upstream_repos/fontc_crater_cache/`. If needed, it can be cloned to `upstream_repos/fontc_crater_cache/jul-sh/iosevka-charon/`.

## Source Block

The existing source block is complete and verified:

```
source {
  repository_url: "https://github.com/jul-sh/iosevka-charon"
  commit: "727f1343e957cadd354f9ec4ee98eba9b645143d"
  archive_url: "https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Light.ttf"
    dest_file: "IosevkaCharonMono-Light.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-LightItalic.ttf"
    dest_file: "IosevkaCharonMono-LightItalic.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Regular.ttf"
    dest_file: "IosevkaCharonMono-Regular.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Italic.ttf"
    dest_file: "IosevkaCharonMono-Italic.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Medium.ttf"
    dest_file: "IosevkaCharonMono-Medium.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-MediumItalic.ttf"
    dest_file: "IosevkaCharonMono-MediumItalic.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Bold.ttf"
    dest_file: "IosevkaCharonMono-Bold.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-BoldItalic.ttf"
    dest_file: "IosevkaCharonMono-BoldItalic.ttf"
  }
  branch: "main"
}
```
