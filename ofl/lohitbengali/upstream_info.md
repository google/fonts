# Lohit Bengali — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (SFD-only sources, no gftools-builder compatibility)

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/pravins/lohit"
}
```

The source block was added in commit `658d6674` ("Update upstreams") on 2024-03-04, as part of PR #7343 ("Update more upstreams (1/2)") by Simon Cozens, merged on 2024-03-06. The block contains only the `repository_url` field; it is missing a `commit` hash and has no `config_yaml` field.

## Repository Analysis

**Repository**: https://github.com/pravins/lohit
**Default branch**: master
**Archived**: No
**Description**: "Lohit fonts family project to supporting Indian scripts."
**Cached at**: `upstream_repos/fontc_crater_cache/pravins/lohit/` (clean, up-to-date with remote)
**Latest commit**: `7a8b554` ("updated auto_test for CI/CD")

This is a **monorepo** containing source files for 13 Indic script font families:
- Assamese, Bengali, Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Marathi, Nepali, Odia, Tamil, Tamil Classical, Telugu

The Bengali sources reside in the `bengali/` subdirectory and consist of:
- `Lohit-Bengali.sfd` — FontForge SFD source file
- `Lohit-Bengali.fea` — OpenType feature file
- `Makefile` — FontForge-based build system
- Various test files, metadata, and configuration files

**Source type**: SFD (FontForge Spline Font Database)
**No gftools-builder compatible sources exist** (.glyphs, .ufo, .designspace) — neither in the current state nor anywhere in the repo's history.

The build system uses:
- `generate.pe` — FontForge script for TTF generation
- `apply_featurefile.py` — Script to apply .fea features to SFD
- Per-directory `Makefile` for building, testing, and packaging

## Onboarding History

The font was added to Google Fonts on **2012-05-09** (per `date_added` in METADATA.pb).

The font binary in google/fonts (`Lohit-Bengali.ttf`, 139,460 bytes) has been present since the initial repository commit (`90abd17b`, 2015-03-07, by Dave Crossland), which was the bulk import of all existing Google Fonts into the git repository. The font file has **never been updated** since that initial commit.

**Font binary metadata** (extracted via `strings`):
- Version: **2.5.1**
- FontForge generation date: **26-9-2012** (September 26, 2012)
- Copyright: "Copyright 2011-12 Lohit Fonts Project contributors."
- Copyright URL: `http://fedorahosted.org/lohit` (Fedora Project, now defunct)
- Unique ID: "FontForge 2.0 : Lohit Bengali : 26-9-2012"

**Identifying the upstream commit**:
- The SFD version was set to 2.5.1 in commit `0df83ad` ("prepared for next release", 2012-02-29) by Pravin Satpute.
- The next commit touching `Lohit-Bengali.sfd` was `04c8c91` ("fixed in lohit bengali and assamese for harfbuzz", 2012-10-18).
- Since the font binary was generated on September 26, 2012, which falls between these two commits, the font was compiled from the source state at commit **`0df83ad`**.
- The SFD copyright string "Copyright 2011-12" matches the copyright in the binary, further confirming this identification.
- Note: The current SFD version is 2.91.5 — significantly newer than the 2.5.1 version in Google Fonts.

The original Lohit project was hosted at fedorahosted.org (Fedora Project infrastructure) and was later migrated to GitHub at `pravins/lohit`. The repo history goes back to 2006 (converted from CVS/SVN via `cvs2svn` and `git-svn`). There is also a separate `pravins/lohit2` repository described as "Rewriting lohit open type tables," which was the source of the Bengali SFD migration into the main lohit repo (commit `9609e21`, 2014-12-02, "updated lohit bengali from lohit2").

## Build Configuration

**No `config.yaml` exists** in the upstream repo. The project uses FontForge-based tooling (SFD files compiled with `generate.pe` script and per-directory Makefiles), which is **not compatible with gftools-builder**.

There are no gftools-compatible source formats (.glyphs, .ufo, .designspace) anywhere in the repo, so creating an override `config.yaml` is not feasible.

**Build process** (as documented in `bengali/Makefile`):
1. Apply feature file to SFD: `fontforge -lang=py -script apply_featurefile.py Lohit-Bengali.sfd Lohit-Bengali.fea`
2. Generate TTF: `./generate.pe *.sfd`
3. Optional: generate WOFF/EOT via sfntly

## Findings

1. **Repository URL is correct**: The `repository_url` field (`https://github.com/pravins/lohit`) correctly points to the upstream repository. The repo is active and accessible.

2. **Commit hash is missing**: The source block lacks a `commit` field. Based on version analysis, the correct onboarding commit is **`0df83ad734a061144754601fc4984f72e3636108`** (short: `0df83ad`), dated 2012-02-29.

3. **Font is significantly outdated**: The font in Google Fonts is version 2.5.1 (from 2012), while the upstream repo is at version 2.91.5 (from 2017). There have been substantial updates including Unicode 8.0 character additions, bug fixes for Bengali rendering, and Latin character support with ttfautohint.

4. **SFD-only sources**: The project uses FontForge SFD files exclusively. No gftools-builder compatible sources exist, making it impossible to create a config.yaml for automated builds.

5. **Monorepo**: The `pravins/lohit` repository is a monorepo containing 13 Indic font families. Other Lohit families in Google Fonts (e.g., Lohit Tamil) reference the same repository URL.

6. **Legacy project infrastructure**: The original project was hosted at `fedorahosted.org/lohit` (Fedora Project), which is now defunct. The GitHub repository appears to be the authoritative successor.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/pravins/lohit"
  commit: "0df83ad734a061144754601fc4984f72e3636108"
}
```

No `config_yaml` field should be added because:
- The project uses SFD sources compiled with FontForge, not gftools-builder
- No gftools-compatible source formats exist in the repository
- An override config.yaml cannot be created without compatible source files

**Confidence**: MEDIUM — The commit hash identification is based on version string matching (2.5.1) and date range analysis (the font was generated on 2012-09-26, between commit `0df83ad` on 2012-02-29 and the next Bengali-touching commit `04c8c91` on 2012-10-18). The font could theoretically have been generated from a different checkout or release tarball, though this is unlikely given the matching version and copyright strings.
