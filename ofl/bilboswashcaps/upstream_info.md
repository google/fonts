# Bilbo Swash Caps

**Status**: `missing_config`
**Date**: 2026-02-26
**Designer**: TypeSETit
**License**: OFL
**METADATA.pb**: `ofl/bilboswashcaps/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/bilboswashcaps |
| Commit | `7fb5653f339a4a574c26a8df75b6e7fac7db9280` |
| Config YAML | N/A (SFD-only sources, not gftools-builder compatible) |
| Source types | sfd, vfb |

## Methodology

### Repository URL
The repository URL `https://github.com/librefonts/bilboswashcaps` is documented in the tracking data. The repo is in the `librefonts` organization, which was used for many early Google Fonts families. Note that Bilbo Swash Caps is in a DIFFERENT repo from Bilbo (which is at `googlefonts/bilbo`).

### Commit Hash
The commit `7fb5653f339a4a574c26a8df75b6e7fac7db9280` is the HEAD of master in the upstream repo (shallow clone). It is dated 2014-10-17 with message "update .travis.yml".

This is a legacy font that predates gftools-packager. The font was last modified in google/fonts via PR #858 ("hotfix-bilboswashcaps: v1.003 added", 2017-08-07) by Marc Foley. The hotfix modified the binary without referencing a specific upstream commit.

The upstream repo does NOT contain a compiled .ttf file -- only TTX (XML table dumps) and SFD/VFB source files. The font binary in google/fonts was compiled externally and cannot be traced to a specific upstream repo commit via binary verification.

The commit `7fb5653` represents the latest state of the repo, which is the most appropriate reference since there's no way to identify the exact commit used for the original compilation.

### Config YAML
**Not applicable**. The upstream repo only contains:
- `src/BilboSwashCaps-Regular-TTF.sfd` (FontForge SFD format)
- `src/Bilbo-SwashCaps-OTF.vfb` (FontLab VFB format)
- TTX table dumps

There is no `.glyphs`, `.ufo`, or `.designspace` source file, and no `config.yaml` or `config.yml`. This font cannot be built with gftools-builder from the available sources.

No override config.yaml exists in the google/fonts family directory either.

## Evidence

### METADATA.pb (current main)
```
name: "Bilbo Swash Caps"
designer: "TypeSETit"
license: "OFL"
category: "HANDWRITING"
date_added: "2011-12-13"
fonts {
  name: "Bilbo Swash Caps"
  style: "normal"
  weight: 400
  filename: "BilboSwashCaps-Regular.ttf"
  ...
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
```
Note: No source block on main branch.

### google/fonts history
- `9a14639f3` (PR branch): "Add source blocks to 602 more METADATA.pb files" -- added source block (not merged to main yet)
- `4c45f1981` (2017-08-07): "hotfix-bilboswashcaps: v1.003 added (#858)" -- last font binary modification
- `c7136cb84`: "Updating ofl/bilboswashcaps/*ttf with nbspace and fsType fixes" (earlier modification)
- `90abd17b4`: "Initial commit" (original addition)

### PR #858
- Title: "hotfix-bilboswashcaps: v1.003 added"
- Author: Marc Foley
- Modified font binary and DESCRIPTION, no upstream commit reference

### Upstream repo structure
```
BilboSwashCaps-Regular.ttf.*.ttx    (TTX table dumps, not compiled font)
src/BilboSwashCaps-Regular-TTF.sfd  (FontForge source)
src/Bilbo-SwashCaps-OTF.vfb        (FontLab source)
src/*.ttx                           (OTF TTX dumps)
DESCRIPTION.en_us.html
FONTLOG.txt
METADATA.json
OFL.txt
.travis.yml
```

### Upstream repo cache
- Cached at: `librefonts/bilboswashcaps` (shallow clone, depth=1)
- Only commit visible: `7fb5653` ("update .travis.yml", 2014-10-17)
- No compiled .ttf binary in the repo
- No config.yaml or config.yml present

## Confidence

**Medium**: The repository URL is correct (matches the librefonts pattern for early Google Fonts families). The commit hash is the repo HEAD and represents the most recent known state. However, binary verification is not possible since the upstream repo does not contain compiled font files. The actual font binary in google/fonts was likely compiled separately from the SFD source.

## Open Questions
1. Was the v1.003 hotfix (PR #858) compiled from the SFD source in this repo, or from a different source?
2. Should a new source be created (e.g., converting the SFD to .glyphs or .ufo) to enable gftools-builder compatibility?

## Notes
- Bilbo and Bilbo Swash Caps are in DIFFERENT upstream repos:
  - Bilbo: `googlefonts/bilbo` (with .glyphs source and config.yml)
  - Bilbo Swash Caps: `librefonts/bilboswashcaps` (SFD-only, no config)
- Originally added to Google Fonts 2011-12-13
- Last binary update was 2017 (hotfix by Marc Foley)
- SFD-only sources mean this font cannot be rebuilt with gftools-builder
- The METADATA.pb on main does not have a source block yet (added on PR branch only)
- Static font only (single weight)
