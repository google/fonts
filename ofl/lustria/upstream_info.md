# Lustria — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD-only sources)

## METADATA.pb Source Block (current)

The current METADATA.pb on upstream main has **no source block**. A source block was added on the local branch `sources_info_2026-02-25` (commit `9a14639f3`) but has not been merged to upstream google/fonts main yet.

Current METADATA.pb contents (upstream main):
```
name: "Lustria"
designer: "MADType"
license: "OFL"
category: "SERIF"
date_added: "2012-01-18"
fonts {
  name: "Lustria"
  style: "normal"
  weight: 400
  filename: "Lustria-Regular.ttf"
  post_script_name: "Lustria-Regular"
  full_name: "Lustria"
  copyright: "Copyright (c) 2011, Matthew Desmond (http://www.madtype.com | mattdesmond@gmail.com), with Reserved Font Name Lustria"
}
subsets: "menu"
subsets: "latin"
subsets: "latin-ext"
```

## Repository Analysis

**Upstream repository**: https://github.com/librefonts/lustria

The repository was created on 2014-07-16 under the `librefonts` GitHub organization. It contains a single commit (`a796e0e874e34d163ac3aceb3f6014af1ef66d3c`) dated 2014-10-17, authored by `hash3g <hash.3g@gmail.com>` with the message "update .travis.yml". The repo is not archived and not a fork.

**Contributors**: vitalyvolkov, xen

### Repository Structure

The repository contains:
- `Lustria-Regular.ttf.*.ttx` — TTX decomposed tables of the TTF binary (root level)
- `src/Lustria-Regular-TTF.sfd` — FontForge SFD source (327 KB)
- `src/Lustria-Regular-OTF.vfb` — FontLab VFB source (80 KB)
- `src/Lustria-Regular.otf.*.ttx` — TTX decomposed tables of the OTF binary
- `src/METADATA_comments.txt` — Build comments referencing `~/googlefontdirectory/` workflow
- `src/VERSIONS.txt` — Records "Version 001.001"
- `.travis.yml` — CI configuration using fontbakery-build.py (legacy tooling)
- `METADATA.json`, `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `OFL.txt`

**No modern source files found**: No `.glyphs`, `.glyphx`, `.ufo`, or `.designspace` files exist. The only editable sources are SFD (FontForge) and VFB (FontLab) formats, which are not compatible with gftools-builder.

**No `config.yaml` found** in the repository.

## Onboarding History

Lustria was added to Google Fonts in the "Initial commit" (`90abd17b4`) dated 2015-03-07, authored by Dave Crossland. The `date_added` field in METADATA.pb is "2012-01-18", indicating the font was part of the Google Fonts catalog before the current git repository was created.

The font binary (`Lustria-Regular.ttf`, 37,400 bytes) has never been updated since the initial commit. Its SHA-256 hash is `8b50753779d151674dcc74bdf9cdde1e788d8fb2b9ace8fb183a0def0f7361ce` and remained unchanged throughout the repository history.

The `librefonts/lustria` repository predates the initial google/fonts commit (created July 2014 vs. March 2015), and appears to be part of the `librefonts` organization's effort to provide source repositories for Google Fonts families. The repository was set up with Travis CI for automated font building using the legacy `fontbakery-build.py` toolchain.

The METADATA_comments.txt file references `~/googlefontdirectory/` paths, indicating this font was processed using the original Google Fonts directory tooling (font-optimizer, subset.py) before the current repository structure was established.

## Build Configuration

**No `config.yaml` exists** in the upstream repository.

The only available sources are:
- `src/Lustria-Regular-TTF.sfd` — FontForge format
- `src/Lustria-Regular-OTF.vfb` — FontLab format

These legacy formats are **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources. An override `config.yaml` cannot be created because there are no buildable source files for gftools-builder.

The `.travis.yml` used the legacy `fontbakery-build.py` pipeline with FontForge and fontcrunch, which is no longer the standard build system.

## Findings

1. **Repository identified**: The upstream repository is `https://github.com/librefonts/lustria` with a single commit `a796e0e`.
2. **SFD-only sources**: The repository contains only FontForge (SFD) and FontLab (VFB) source files. These are legacy formats not supported by the modern gftools-builder toolchain.
3. **No config.yaml possible**: Since there are no `.glyphs`, `.ufo`, or `.designspace` sources, no `config.yaml` can be created (neither in the upstream repo nor as an override).
4. **Font unchanged**: The binary TTF in google/fonts has never been modified since the initial commit in 2015.
5. **Commit hash verified**: The single commit `a796e0e874e34d163ac3aceb3f6014af1ef66d3c` is the only commit in the repository, making it the correct reference.
6. **Pending source block**: A source block was prepared on the `sources_info_2026-02-25` branch but has not been merged to upstream google/fonts main.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lustria"
  commit: "a796e0e874e34d163ac3aceb3f6014af1ef66d3c"
}
```

No `config_yaml` field is needed because the sources are SFD-only (FontForge format) and cannot be built with gftools-builder. No override `config.yaml` is applicable.
