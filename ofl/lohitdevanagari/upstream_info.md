# Lohit Devanagari — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No METADATA.pb file exists for this family. The directory `ofl/lohitdevanagari/` contains only:
- `Lohit-Devanagari.ttf`
- `DESCRIPTION.en_us.html`
- `EARLY_ACCESS.category` (content: "Sans Serif")
- `OFL.txt`

This font remains an Early Access font that was never fully onboarded into the Google Fonts catalog. It does not appear on the main Google Fonts website (returns 404). Other Lohit fonts in the same situation (Lohit Bengali, Lohit Tamil) do have METADATA.pb files with source blocks, but Lohit Devanagari was never given one.

## Repository Analysis

**Upstream repository**: https://github.com/pravins/lohit

The Lohit project is a multi-script font family project originally hosted at https://fedorahosted.org/lohit/ (which now redirects to https://pagure.io/lohit). The GitHub repository at `pravins/lohit` is the primary development repository, maintained by Pravin Satpute (Red Hat / Fedora Project).

The repository contains font sources for multiple Indian scripts organized in subdirectories:
- `devanagari/` — Lohit Devanagari sources
- `bengali/` — Lohit Bengali sources
- `tamil/` — Lohit Tamil sources
- (and others: assamese, gujarati, gurmukhi, kannada, malayalam, marathi, nepali, odia, telugu, tamil-classical)

A separate repository exists at https://github.com/pravins/lohit2 (HTTP 200), which was used as a development branch before being merged back into the main repo.

**Source files in `devanagari/`**:
- `Lohit-Devanagari.sfd` — FontForge SFD source (684,365 bytes)
- `Lohit-Devanagari.fea` — OpenType feature file (57,619 bytes)
- `Makefile` — Build script using FontForge + ttfautohint (in later versions)
- Various test files, config files, and changelog

**Build process**: The font was built using FontForge (via `generate.pe` script) with OpenType features applied from the `.fea` file via `apply_featurefile.py`. Later versions (post-2.95.0) also used ttfautohint for hinting.

**Key contributors** (from AUTHORS file): Pravin Satpute, Sneha Kore, Rahul Bhalerao, Eduardo Rodriguez Tunni, Bernard Massot, Shriramana Sharma, and others.

**Cached repo status**: Clean, on branch `master`, up to date with `origin/master`.

## Onboarding History

The font was added to google/fonts in the initial commit (`90abd17b4`) by Dave Crossland on March 7, 2015. This massive initial commit included the entire Google Fonts library. The TTF file has never been updated since.

No PRs or subsequent commits have ever modified the font binary. The only later commits touching this directory were:
- `4f889caf0` (Apr 22, 2015) — Adding Early Access category files
- `28fff5fa7` (Apr 23, 2015) — Renaming EARLYACCESS.category to EARLY_ACCESS.category

**Font binary analysis**:
- Version: **2.94.0**
- Copyright: "Copyright 2011-12 Lohit Fonts Project contributors"
- FontForge unique ID: "FontForge 2.0 : Lohit Devanagari : 17-9-2013"
- No ttfautohint markers (ttfautohint was added to the Makefile in November 2014, after 2.94.0)
- File size: 72,328 bytes
- MD5: `2163a90b9f68b2e9e5559d8ae8aa9658`

**Version 2.94.0 in upstream repo**: The changelog records version 2.94.0 as released on Feb 19, 2014 by Pravin Satpute. The last commit touching `devanagari/` for this release was `4e6568ba` ("updated changelog", Feb 19, 2014). The SFD file at that commit shows:
- Version: 2.94.0
- Copyright: "Copyright 2011-12 Lohit Fonts Project contributors"
- CreationTime: 2006-09-28 (original font creation)
- ModificationTime: 2014-02-19

The FontForge date "17-9-2013" in the TTF's unique ID is puzzling. This date falls between the lohit2 merge (Oct 1, 2013, commit `8ed137d`) and the 2.94.0 release (Feb 19, 2014). The most likely explanation is that the TTF binary was generated on September 17, 2013 from an intermediate state of the source files, and the version string was later updated in the SFD without regenerating the binary. Alternatively, the binary may have been downloaded from a pre-built release tarball that was generated at that date.

**Recommended commit**: `4e6568ba026afde20c89333a888e1cf41d3c165a` — the last commit touching `devanagari/` for the version 2.94.0 release (Feb 19, 2014). While the exact build state that produced the TTF may have been slightly different, this is the best documented reference point for version 2.94.0.

## Build Configuration

**No config.yaml exists** in the upstream repository. The font is built using:
1. FontForge SFD source files (`.sfd`)
2. OpenType feature files (`.fea`)
3. A Makefile that calls FontForge scripts (`generate.pe`, `apply_featurefile.py`)

This is a **SFD-only source** project. It does not use gftools-builder and cannot be built with the standard Google Fonts toolchain without significant rework. The build process relies on:
- FontForge for TTF generation
- sfntly for WOFF/EOT generation
- ttfautohint for hinting (added in version 2.95.0, not present in 2.94.0)

An override config.yaml would not be straightforward to create because gftools-builder does not natively support SFD sources. The font would need to be converted to a UFO or Glyphs source format first.

## Findings

1. **No METADATA.pb**: This is an Early Access font that was never fully onboarded. It lacks METADATA.pb entirely, unlike sibling fonts Lohit Bengali and Lohit Tamil which have METADATA.pb with source blocks pointing to `https://github.com/pravins/lohit`.

2. **SFD-only sources**: The upstream repo uses FontForge SFD format, not gftools-builder compatible formats (.glyphs, .ufo, .designspace). This means no config.yaml can be meaningfully created for gftools-builder.

3. **Outdated binary**: The font in google/fonts is version 2.94.0 (Feb 2014). The upstream repo has progressed to version 2.95.4 (Apr 2017), with several bug fixes and improvements including Unicode 8.0 character support and ttfautohint integration.

4. **Shared repository**: The upstream repo `pravins/lohit` is a monorepo containing sources for all Lohit script variants. The Devanagari sources are in the `devanagari/` subdirectory.

5. **FontForge date discrepancy**: The TTF reports a FontForge generation date of September 17, 2013, but the version is 2.94.0 which was released February 19, 2014. This suggests the binary may have been compiled from an intermediate state or the date reflects a different build artifact.

6. **Not on Google Fonts catalog**: The font returns 404 on fonts.google.com/specimen/Lohit+Devanagari, confirming it remains in Early Access status only.

## Recommended Source Block

If a METADATA.pb were to be created for this font, the source block should be:

```
source {
  repository_url: "https://github.com/pravins/lohit"
  commit: "4e6568ba026afde20c89333a888e1cf41d3c165a"
}
```

Notes:
- No `config_yaml` field is included because the project uses SFD sources with no gftools-builder configuration.
- The commit references the last devanagari change for version 2.94.0 (Feb 19, 2014).
- An override config.yaml is not feasible since gftools-builder does not support SFD sources.
- For consistency with Lohit Bengali and Lohit Tamil (which already have source blocks pointing to this repo), the same repository_url should be used.
- Before creating a METADATA.pb, the font would need to be fully onboarded (graduated from Early Access), which would likely also involve updating to a newer version and possibly converting sources to a gftools-builder compatible format.
