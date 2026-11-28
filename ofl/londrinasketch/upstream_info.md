# Londrina Sketch — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/marcelommp/Londrina-Typeface"
  commit: "7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060"
}
```

An override `config.yaml` exists in the google/fonts family directory (`ofl/londrinasketch/config.yaml`), so the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Repository Analysis

**Upstream repo**: https://github.com/marcelommp/Londrina-Typeface
**Owner**: marcelommp (Marcelo Magalhaes)
**Default branch**: master
**Repo status**: Clean, up to date with origin

This is a shared repository containing sources for multiple Londrina family variants:
- Londrina Outline
- Londrina Shadow
- Londrina Sketch
- Londrina Solid

All four families are present in google/fonts under `ofl/londrinaoutline`, `ofl/londrinashadow`, `ofl/londrinasketch`, and `ofl/londrinasolid`.

### Repository Structure (at referenced commit 7f4129e)

```
FONTLAB_UFO_FILES/
  LondrinaOutline-Regular.ufo/
  LondrinaShadow-Regular.ufo/
  LondrinaSketch-Regular.ufo/
  LondrinaSolid-Black.ufo/
  LondrinaSolid-Light.ufo/
  LondrinaSolid-Regular.ufo/
  LondrinaSolid-Thin.ufo/
  vfb/
  dehint.sh
OTF/
  (compiled OTF files)
TTF/
  LondrinaSketch-Regular.ttf (and others)
```

The LondrinaSketch-Regular.ufo source contains a standard UFO structure: features.fea, fontinfo.plist, glyphs, groups.plist, kerning.plist, lib.plist, metainfo.plist.

### Post-Onboarding Changes in Upstream

Significant upstream activity occurred after the onboarding commit:
- **2018-07-12**: Font adjustments (commit 6d492b4)
- **2019-04-02**: Added Glyphs source files (commit f7aed96)
- **2022-10-21**: New Glyphs App file and uploads (commits 239d89c, 80630a7, 6988bc4)
- **2023-06-15**: Major update of the entire Londrina family (commit cc7b65f) — expanded character set, added layer fonts, SVG color fonts, new font styles

The latest update (2023) represents a substantial redesign and expansion that has not been onboarded to Google Fonts.

## Onboarding History

### Initial Addition

The font was initially added to google/fonts in the initial commit (90abd17b, date unknown as part of the original bulk import).

### v1.002 Update (PR #1085)

- **PR**: google/fonts#1085
- **Title**: "londrinasketch: v1.002 added"
- **Author**: Marc Foley (m4rc1e)
- **Merged by**: Dave Crossland (davelab6)
- **Merged at**: 2017-07-31
- **Commit in google/fonts**: c238df8bf
- **PR body**: "Adds extra fonts request in #69. Upstream has been merged, marcelommp/Londrina-Typeface#2"

The PR referenced upstream PR marcelommp/Londrina-Typeface#2, which was a "gf-mastering" PR by Marc Foley. This upstream PR was merged as commit a2b7062 on 2017-07-17.

The upstream mastering work spanned several commits by Marc Foley (all dated 2017-07-13):
1. `a63f884` — renamed source filenames, moved vfbs into separate sub folder
2. `d2d4469` — Solid family mastered
3. `78eb13a` — Outline family mastered (note: Sketch was not separately mastered, likely handled together)
4. `2aa19f8` — fixed vertical metrics
5. `4e0ee2c` — ran Fix fonts for GF spec
6. `deed74a` — readjusted metrics to visually appear like previous GF release
7. `f80de6a` — fixed copyright strings
8. `0034a81` — Generated v1.002 fonts
9. `c51f8ae` — disabled subroutines
10. `3754d39` — remove hints
11. `7f4129e` — fixed RFN in copyright strings (the final commit before merge)

### Binary File Verification

The TTF file at upstream commit `7f4129e` (`TTF/LondrinaSketch-Regular.ttf`) matched the file in google/fonts exactly (MD5: `375773908d75efb116ad9ac24fdbdfe6`). This confirms that `7f4129e` is the correct onboarding commit.

### Source Block History

1. **2023-12-14** (commit e75f82401, by Simon Cozens): Added the initial `source { repository_url }` block as part of a batch "Update upstreams" commit.
2. **2025-12-12** (commit 068372ef7, by Felipe Sanches): Added the `commit` hash to the source block, and created the override `config.yaml`.

## Build Configuration

**No config.yaml in upstream repo**. The upstream repository has never contained a gftools-builder config.yaml file.

**Override config.yaml in google/fonts** (`ofl/londrinasketch/config.yaml`):

```yaml
buildVariable: false
sources:
  - FONTLAB_UFO_FILES/LondrinaSketch-Regular.ufo
```

This override was added by Felipe Sanches in commit 068372ef7 (2025-12-12). It correctly points to the UFO source for the Sketch variant within the shared Londrina-Typeface repository. The `buildVariable: false` flag is appropriate since this is a single-weight static font.

Since the override config.yaml exists in the google/fonts family directory, google-fonts-sources auto-detects it, and no `config_yaml` field is needed in METADATA.pb.

## Findings

1. **Source block is complete and correct.** The repository URL (`https://github.com/marcelommp/Londrina-Typeface`) and commit hash (`7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060`) are verified. The binary file at that commit matches the file in google/fonts exactly.

2. **Override config.yaml is correctly configured.** It references the appropriate UFO source (`FONTLAB_UFO_FILES/LondrinaSketch-Regular.ufo`) at the referenced commit.

3. **Shared repository.** The upstream repo is shared among four Londrina families (Outline, Shadow, Sketch, Solid). Each family in google/fonts requires its own source block and config.yaml pointing to the correct UFO within the same repository.

4. **Significant upstream updates not yet onboarded.** The designer (Marcelo Magalhaes) made substantial updates in 2022-2023, including expanded character sets, new font styles (Layers, SVG Color fonts), and a reorganized repository structure. These changes have not been reviewed or onboarded to Google Fonts.

5. **No corrections needed.** The current METADATA.pb source block and override config.yaml are accurate and complete.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/marcelommp/Londrina-Typeface"
  commit: "7f4129ee609e13f4dc9bcdce6f8a08f5d9bc8060"
}
```

With the override `config.yaml` in the google/fonts family directory:

```yaml
buildVariable: false
sources:
  - FONTLAB_UFO_FILES/LondrinaSketch-Regular.ufo
```

**Confidence**: HIGH
