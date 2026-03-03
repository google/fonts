# Love Ya Like A Sister — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists in METADATA.pb. The current file contains only basic metadata:

```
name: "Love Ya Like A Sister"
designer: "Kimberly Geswein"
license: "OFL"
category: "DISPLAY"
date_added: "2011-07-06"
fonts {
  name: "Love Ya Like A Sister"
  style: "normal"
  weight: 400
  filename: "LoveYaLikeASister.ttf"
  post_script_name: "LoveYaLikeASister-Regular"
  full_name: "Love Ya Like A Sister Regular"
  copyright: "Copyright (c) 2011 by Kimberly Geswein (kimberlygeswein@gmail.com). All rights reserved."
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
classifications: "DISPLAY"
classifications: "HANDWRITING"
```

## Repository Analysis

**Repository URL**: https://github.com/librefonts/loveyalikeasister
**Repository type**: Archive/mirror (librefonts organization)
**Is NOT the designer's original repository** — the librefonts organization was an archival project that extracted font files from the old `googlefontdirectory` into individual GitHub repositories.

### Repository structure

The repository contains TTX decompositions of the font binary (not editable source files for building) and two legacy source files:

- `src/LoveYaLikeASister-TTF.sfd` — FontForge SFD file (version 1.003)
- `src/LoveYaLikeASister.vfb` — FontLab VFB file (proprietary binary format)
- Multiple `.ttx` files — XML decomposition of the compiled TTF tables
- `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt` — metadata files
- `.travis.yml` — CI configuration for fontbakery testing

No `.glyphs`, `.ufo`, `.designspace`, or `config.yaml` files exist.

### Git history

The repository was created on 2014-07-16 by Mikhail Kashkin (xen/m@xen.ru) with commit message "Move loveyalikeasister font files to separate repository". All subsequent commits (11 total, last on 2014-10-17) were by Vitaly Volkov (hash3g) updating the Travis CI configuration.

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `41b8b1e` | 2014-10-17 | hash3g | update .travis.yml |
| `0ebd3a1` | 2014-10-06 | hash3g | Rename fontbakery |
| `ae687bd` | 2014-09-19 | hash3g | Update .travis.yml |
| ... (8 more Travis CI updates) | | | |
| `b02575c` | 2014-07-16 | Mikhail Kashkin | Move loveyalikeasister font files to separate repository |

### Version mismatch

The SFD source file in the repo declares version 1.003, while the compiled TTF binary in google/fonts reports version 1.002. This indicates the SFD was modified after the binary was originally compiled, making the SFD a newer (and different) version than what was used to produce the google/fonts binary.

### Contributors

- **vitalyvolkov** (hash3g): 11 contributions (all Travis CI updates)
- **xen** (Mikhail Kashkin): 1 contribution (initial archival commit)

Neither contributor is the original designer (Kimberly Geswein).

## Onboarding History

### Google Fonts timeline

- **date_added**: 2011-07-06 — the font was added to Google Fonts
- The google/fonts repository initial commit was on 2015-03-07, which was a bulk import of all existing fonts
- The font binary (`LoveYaLikeASister.ttf`) has only been touched in two commits:
  1. `90abd17` (2015-03-07) — Initial commit (bulk import)
  2. `76adaf1` (2021-11-01) — Deploy commit by m4rc1e (repository restructuring, binary hash unchanged)
- SHA-256 of the binary: `4fbe2c1fa647de5a415acac7b2b6491542fe9767b6199719a3bd77a7cf35eb0d` (identical across both commits)

### Pre-git history

The font was onboarded to Google Fonts in 2011, before the current google/fonts repository existed. The original submission predated the `googlefontdirectory` to `google/fonts` migration. No PR history is available for the original onboarding.

### Font binary metadata (from TTF name table)

- Version: 1.002 2007
- Copyright: "Copyright (c) 2011 by Kimberly Geswein. All rights reserved."
- Unique ID: "FontForge 2.0 : Love Ya Like A Sister Regular : 18-10-2011"
- Designer: Kimberly Geswein
- Vendor URL: http://www.kimberlygeswein.com
- Designer URL: http://www.kimberlygeswein.com
- License: SIL Open Font License 1.1

The font was compiled using FontForge on 2011-10-18.

## Build Configuration

**No config.yaml exists** in the upstream repository.

The source files are SFD (FontForge) and VFB (FontLab) formats only. These are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` source formats. Creating an override `config.yaml` is not feasible because:

1. SFD files are not supported as source inputs by gftools-builder/fontmake
2. VFB files are proprietary FontLab format and not supported either
3. The SFD version (1.003) does not match the binary version (1.002), so even if conversion were possible, it would produce a different font

## Findings

1. **No source block in METADATA.pb** — needs to be added.

2. **librefonts is an archive, not a true upstream** — The `librefonts/loveyalikeasister` repository is an archival mirror created in 2014 by extracting files from the old `googlefontdirectory` project. It is not maintained by the original designer (Kimberly Geswein) and has not received any updates since October 2014.

3. **No gftools-builder compatible sources** — The only source files are SFD (FontForge) and VFB (FontLab) formats. Neither format is supported by the modern gftools-builder pipeline. An override `config.yaml` cannot be meaningfully created.

4. **Version mismatch between source and binary** — The SFD in the repo is version 1.003 while the binary in google/fonts is version 1.002, suggesting the SFD was updated independently from the binary compilation.

5. **Pre-git onboarding** — The font was added to Google Fonts in 2011, well before the current google/fonts repository was created (2015). No PR or detailed onboarding history is available.

6. **Designer has no GitHub presence** — Kimberly Geswein does not appear to have a GitHub account or any font source repositories on GitHub. Her website (kimberlygeswein.com) is still active.

7. **No googlefonts org repo** — There is no `googlefonts/loveyalikeasister` repository. The only known repository is the librefonts archive.

8. **Commit hash** — Since the librefonts repo is an archive (not the original source), the commit hash (`41b8b1e`) represents the last Travis CI update to the archive, not an actual source code change. The initial archival commit `b02575c` is equally not meaningful as an "onboarding commit."

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/loveyalikeasister"
  commit: "41b8b1e41883c6ef530bece6c906ab917a90387e"
}
```

**Notes on the recommendation**:
- The repository URL points to the librefonts archive, which is the only known public repository for this font
- The commit hash `41b8b1e` is the HEAD of master, which is the latest (and final) state of the archive
- No `config_yaml` field is included because the sources are SFD-only and not gftools-builder compatible
- Status is "incomplete" because: (a) this is an archive repo, not the designer's original source, and (b) there are no gftools-builder compatible sources
- Confidence: LOW — the librefonts repo is an archival mirror, not a true upstream source repository
