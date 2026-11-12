# Lohit Tamil — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/pravins/lohit"
}
```

The source block was added by Simon Cozens in commit `658d6674` ("Update upstreams", 2024-03-04), merged via PR #7343 ("Update more upstreams (1/2)"). The block contains only a `repository_url` — no `commit` hash and no `config_yaml` field.

## Repository Analysis

**Repository**: https://github.com/pravins/lohit
- **Status**: Active, not archived
- **Default branch**: master
- **Last updated**: 2026-01-07
- **Description**: "Lohit fonts family project to supporting Indian scripts."
- **Cached locally**: Yes, at `upstream_repos/fontc_crater_cache/pravins/lohit/`

This is a **monorepo** containing multiple Lohit font families for various Indian scripts: Assamese, Bengali, Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Marathi, Nepali, Odia, Tamil, Tamil Classical, and Telugu. Each script has its own subdirectory.

The Tamil sources are located at `tamil/Lohit-Tamil.sfd` (FontForge SFD format) with an associated feature file `tamil/Lohit-Tamil.fea`. The build system uses FontForge's scripting language (`generate.pe`) and Make, not gftools-builder. There are **no** `.glyphs`, `.ufo`, or `.designspace` files anywhere in the repository.

**Alternative repos**:
- `lohit-fonts/lohit-tamil-fonts` — A split-out repo created in 2020, containing individual Tamil font sources based on Fedora RPM packaging. This is not the original development repo and was created well after the font was onboarded to Google Fonts.
- The original project homepage was `https://fedorahosted.org/lohit/` (now defunct).

## Onboarding History

The font was added to google/fonts in the **initial commit** by Dave Crossland on 2015-03-07 (commit `90abd17b`, "Initial commit"). This was a massive initial import that added many font families at once. The commit included:
- `DESCRIPTION.en_us.html`
- `Lohit-Tamil.ttf` (66,184 bytes)
- `Lohit-Tamil.tamil` (same file, subset)
- `METADATA.json`
- `OFL.txt`

The TTF binary has **never been updated** since the initial commit. All subsequent commits touching `ofl/lohittamil/` modified only metadata files (METADATA.pb, subset files, etc.), never the font binary itself.

### Version Analysis

The binary in google/fonts reports **Version 2.5.0** in its name table. However, the upstream repo's Tamil SFD currently has **Version 2.91.1** (as of the latest commits from 2017). This significant version gap confirms the binary was built from a much older state of the source.

Tracing version 2.5.0 in the upstream commit history of `tamil/Lohit-Tamil.sfd`:

| Commit | Date | Version | Description |
|--------|------|---------|-------------|
| `361b23b` | 2011-09-21 | 2.5.0 | Relicensing to OFL |
| `ffb56a5` | 2012-02-27 | 2.5.0 | Improved asterisk shape in all lohit fonts |
| `9d61e32` (next) | 2012-03-02 | 2.5.1 | Updated panose value |

The last commit modifying `tamil/Lohit-Tamil.sfd` while still at version 2.5.0 was `ffb56a5` (2012-02-27). This commit modified the asterisk glyph shape and updated the SFD ModificationTime from 1316598937 (2011-09-21) to 1330332300 (2012-02-27).

The tracking data in `gfonts_library_sources.json` listed commit `cb3f884` as the reference, but this is **incorrect** for the Tamil font. That commit (2015-03-04, "Change hex id of i-mtras to 65537 onwards") did not touch the Tamil directory, and at that commit the Tamil SFD was already at version 2.91.0 — a much newer version than what is in the google/fonts binary. The `cb3f884` commit was simply the latest upstream commit before the google/fonts onboarding date.

**Best candidate commit**: `ffb56a5d3cb709861e19aa50b436a0dc8ef70a21` (2012-02-27) — the last commit modifying Tamil sources at version 2.5.0. However, since the binary may have been compiled at any point while version 2.5.0 was current (Sep 2011 to Feb 2012), and the actual compilation date is unknown, this is a **MEDIUM confidence** determination.

## Build Configuration

The upstream repository uses **FontForge + Make** for building:
- Source format: `.sfd` (FontForge SplineFont Database)
- Feature file: `.fea` (OpenType feature definitions)
- Build tool: FontForge scripting (`generate.pe`) + Makefile
- **No** `config.yaml` exists in the upstream repo
- **No** gftools-builder compatible sources exist (no `.glyphs`, `.ufo`, `.designspace`)

Since the sources are SFD-only, a gftools-builder `config.yaml` **cannot** be created. gftools-builder does not support SFD files as input.

## Findings

1. **Repository URL is correct**: `https://github.com/pravins/lohit` is accessible and contains the Tamil font sources in the `tamil/` subdirectory.

2. **Missing commit hash**: The METADATA.pb source block has no `commit` field. The best candidate is `ffb56a5` (the last Tamil SFD modification at v2.5.0), but confidence is MEDIUM because the binary could have been compiled from the earlier `361b23b` commit or from a now-lost separate build artifact.

3. **No config.yaml possible**: The font sources are in FontForge SFD format, which is not supported by gftools-builder. No override `config.yaml` can be created.

4. **Outdated binary**: The font in google/fonts (v2.5.0, from ~2012) is significantly behind the upstream version (v2.91.1, from 2017). There have been substantial changes to the Tamil font sources since the onboarded version, including width fixes, version bumps to 2.91.x, and metadata updates.

5. **Tracking data correction needed**: The `gfonts_library_sources.json` entry lists commit `cb3f884` which is incorrect for the Tamil font specifically. The status should also note this is an SFD-only project that cannot have a config.yaml.

6. **Monorepo consideration**: Since this is a monorepo, the commit hash in METADATA.pb should ideally be the one that last modified the Tamil-specific sources at the version matching the binary, not just the latest repo commit.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/pravins/lohit"
  commit: "ffb56a5d3cb709861e19aa50b436a0dc8ef70a21"
}
```

**Notes**:
- `config_yaml` is omitted because the sources are SFD-only and cannot be built with gftools-builder
- The commit `ffb56a5` represents the last modification to Tamil sources at version 2.5.0 (matching the binary in google/fonts)
- Confidence: **MEDIUM** — version match is confirmed (2.5.0), but the exact build point within the v2.5.0 range (Sep 2011 to Feb 2012) is uncertain
- Status: **incomplete** — no config.yaml is possible for SFD-only sources

## Commit Added (HIGH confidence)

Commit `a403c9b7f509dad5e58dde85ef63b1c36fde3a21` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2015-03-07). This is the most reliable method.
