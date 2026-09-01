# Mallanna — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/appajid/mallanna"
  commit: "52b5b8b53bd89d84ecc8a0da7b809ea241c8eb74"
}
```

An override `config.yaml` exists in the google/fonts family directory, so the `config_yaml` field is correctly omitted from the source block.

## Repository Analysis

**Repository**: https://github.com/appajid/mallanna
**Default branch**: master
**Total commits**: 2
**Cached at**: `fontc_crater_cache/appajid/mallanna/`
**Repo status**: Clean, up to date with origin

The upstream repository is minimal, containing only two commits:

1. `0443c91` (2014-11-15) — "Updating TTF SFD Copyright and version" — Initial commit adding `Mallanna.sfd`, `Mallanna.ufo/`, and `OFL.txt`
2. `52b5b8b` (2014-11-26) — "Removed Latin Characters" — Removed Latin character glyphs from the UFO and SFD sources, keeping only Telugu glyphs

The repository contains:
- `Mallanna.sfd` — FontForge SFD source file
- `Mallanna.ufo/` — UFO2 source (created by com.fontlab.ufoLib, formatVersion 2)
- `OFL.txt` — SIL Open Font License

The UFO source at HEAD (52b5b8b) contains approximately 1,253 glyph files, primarily Telugu characters (uni0C** codepoints). The Latin characters were removed in this commit.

**No config.yaml exists in the upstream repository.**

### Font details from fontinfo.plist
- Family name: Mallanna
- Designer: Purushoth Kumar Guthula
- Manufacturer: Andhrapradesh Society for Knowledge Networks
- Version: 2.00 (July 29, 2013)
- Units per em: 1000
- Style: Regular, weight 400

## Onboarding History

The font was added to google/fonts in the initial mass commit:

- **Commit**: `90abd17b` (2015-03-07) — "Initial commit"
- This commit added `Mallanna-Regular.ttf`, `DESCRIPTION.en_us.html`, `METADATA.json`, and `OFL.txt`
- The TTF file has never been modified since the initial onboarding

The source block was added in two stages:
1. **Commit** `c891a9b8` (2024-03-04) by Simon Cozens — "Update upstreams" — Added the `source { repository_url }` and `primary_script: "Telu"` fields
2. **Commit** `a33dcc2d` (2025-11-27) by Felipe Sanches — "sources info for Mallanna" — Added the `commit` hash and the override `config.yaml`

The commit message for `a33dcc2d` references the original onboarding commit: `https://github.com/google/fonts/commit/90abd17b4f97671435798b6147b698aa9087612f`.

## Build Configuration

**Upstream config.yaml**: None — the upstream repository has no config.yaml file.

**Override config.yaml** (in google/fonts family directory):
```yaml
buildVariable: false
sources:
  - Mallanna.ufo
```

This override config points to `Mallanna.ufo`, which exists in the upstream repository at the referenced commit (52b5b8b). The config correctly specifies `buildVariable: false` since this is a single-weight, non-variable font.

## Findings

1. **Repository URL is correct**: The METADATA.pb `repository_url` matches the upstream repo at `https://github.com/appajid/mallanna`, which is also referenced in the DESCRIPTION.en_us.html file.

2. **Commit hash is correct**: The referenced commit `52b5b8b` is the HEAD of the upstream master branch and is the latest (and only non-initial) commit in the repository. It was created on 2014-11-26, which predates the google/fonts onboarding on 2015-03-07. Since the repo has only 2 commits and this is the latest one, it is the correct reference.

3. **Override config.yaml is appropriate**: The upstream repo has no config.yaml, so the override in the google/fonts family directory is necessary. The config references `Mallanna.ufo`, which exists at the referenced commit.

4. **Source format note**: The UFO is format version 2 (created by FontLab's ufoLib). The primary source appears to be the SFD (FontForge) file, with the UFO being a derivative. However, the UFO is the source referenced in the config.yaml for gftools-builder compatibility.

5. **Latin characters**: The referenced commit (52b5b8b) removed Latin characters from the sources. The font in google/fonts still has Latin coverage (the subset "latin" is listed in METADATA.pb), suggesting the TTF was compiled from an earlier state or from a different build process that included the Latin glyphs. The copyright notice mentions Nunito by Vernon Adams, indicating the Latin portion came from the Nunito font.

6. **No further changes needed**: The source block is complete with repository_url, commit hash, and an appropriate override config.yaml. The `config_yaml` field is correctly omitted since google-fonts-sources auto-detects the local override.

## Recommended Source Block

The current source block is already correct and complete:

```
source {
  repository_url: "https://github.com/appajid/mallanna"
  commit: "52b5b8b53bd89d84ecc8a0da7b809ea241c8eb74"
}
```

With the override `config.yaml` in the google/fonts family directory:

```yaml
buildVariable: false
sources:
  - Mallanna.ufo
```

No changes are needed. The source metadata for Mallanna is complete.
