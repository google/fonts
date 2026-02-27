# Investigation Report: Elsie

## Family Details
- **Family name**: Elsie
- **Designer**: Alejandro Inler (with Ana Sanfelippo)
- **License**: OFL
- **Category**: DISPLAY / SERIF
- **Date added to Google Fonts**: 2012-11-12
- **Weights**: Regular (400), Black (900)
- **Path in google/fonts**: `ofl/elsie/`

## METADATA.pb Source Block (Current State)

```
source {
  repository_url: "https://github.com/googlefonts/elsiefont (404)"
}
```

The current `repository_url` includes a literal `(404)` annotation appended by Simon Cozens in PR #7160 ("More upstreams (e,f)"), merged 2024-01-16. This is not a valid URL -- it was a note that the repository was already gone at the time it was recorded.

## Repository Investigation

### googlefonts/elsiefont (DELETED)
- **URL**: https://github.com/googlefonts/elsiefont
- **Status**: Returns HTTP 404. Repository has been deleted or never existed.
- **Evidence**: Confirmed via HTTP request on 2026-02-27.

### googlefonts/elsie (EMPTY)
- **URL**: https://github.com/googlefonts/elsie
- **Status**: Returns HTTP 200, but the repository is **completely empty** -- zero commits, zero branches, zero content.
- **Created**: 2017-09-25
- **Not a fork**: Standalone empty repo, never populated.

### librefonts/elsie (LEGACY ARCHIVE)
- **URL**: https://github.com/librefonts/elsie
- **Status**: Active (HTTP 200), contains source files.
- **Created**: 2014-07-16 by Mikhail Kashkin (xen)
- **Initial commit**: `af81473` -- "Move elsie font files to separate repository"
- **Latest commit**: `9734e9f` (2014-10-17) -- "update .travis.yml"
- **Total commits**: 12 (all in 2014, no activity since)
- **Cloned to cache**: `fontc_crater_cache/librefonts/elsie/`

#### Source Files in librefonts/elsie
The `src/` directory contains:
- `Elsie-Regular-TTF.sfd` -- FontForge Spline Font Database (Regular)
- `Elsie-Black-TTF.sfd` -- FontForge Spline Font Database (Black)
- `Elsie-Regular-OTF.vfb` / `Elsie-Regular-OTF.vfbak` -- FontLab binary (Regular)
- `Elsie-Black-OTF.vfb` / `Elsie-Black-OTF.vfbak` -- FontLab binary (Black)
- Various `.otf.*.ttx` decompositions of OTF files
- `Elsie-Black-Poster.pdf`

Root directory contains TTX decompositions of the TTF binaries (split per table), plus `METADATA.json` and `OFL.txt`.

#### Source Format Assessment
- **SFD files**: FontForge format. Not compatible with gftools-builder.
- **VFB files**: FontLab 5 binary format. Not compatible with gftools-builder.
- **No `.glyphs`, `.ufo`, or `.designspace` files** are available anywhere.
- **No `config.yaml`** exists in the repo.

## Onboarding History in google/fonts

### Initial commit (2015-03-07)
- **Commit**: `90abd17b` -- "Initial commit" by Dave Crossland
- **Note**: This was a bulk initial import; no upstream reference recorded.

### PR #884 (2017-05-08) -- hotfix-elsie: v1.002 added
- **Author**: Marc Foley (m4rc1e)
- **Changes**: Updated both `Elsie-Regular.ttf` (41044 -> 40956 bytes) and `Elsie-Black.ttf` (42424 -> 42216 bytes), plus `DESCRIPTION.en_us.html` and `METADATA.pb`.
- **No upstream reference** in commit body or PR description.

### PR #2754 (2020-10-28) -- [hotfix] ofl/elsie/Elsie-Regular.ttf updated
- **Author**: Rosalie Wagner (RosaWagner)
- **Changes**: Updated only `Elsie-Regular.ttf` (40956 -> 38936 bytes).
- **Purpose**: Fix issue #515 (fi/fj ligature problem) by removing f_i and f_j ligatures, version bumped from 1.002 to 1.003.
- **Note**: "few FAILS since it's an old font" -- hotfix was done directly on the binary, not from sources.

### PR #7522 (2024-04-08) -- Hotfix fi and fj for ElsieSwashCaps-Regular.ttf
- **Author**: Yanone
- **Key quote**: *"Reminder: We don't have sources"*
- **This confirms**: The Google Fonts team acknowledges that no usable source files exist for the Elsie family. Hotfixes were performed directly on the binary font files.

### PR #7160 (2024-01-16) -- More upstreams (e,f)
- **Author**: Simon Cozens (simoncozens)
- **Added**: The current `repository_url: "https://github.com/googlefonts/elsiefont (404)"` noting the URL was already dead.

### PR #10266 (open) -- Fix broken repository_url in 6 METADATA.pb files
- **Author**: felipesanches (AI-assisted)
- **Proposes**: Removing the invalid URL entirely from the source block.
- **Status**: Open, not yet merged.

## Related Family
- **Elsie Swash Caps** (`ofl/elsieswashcaps/`): Sibling family by the same designer. Uses `librefonts/elsieswashcaps` as upstream, which also has SFD-only sources.

## Designer Information
- **Alejandro Inler** (alejandroinler@gmail.com): No GitHub account found (HTTP 404 for `github.com/alejandroinler`).
- **Ana Sanfelippo**: Co-developer credited in the description.
- The copyright dates are 2010-2012, predating the Google Fonts onboarding.

## Config.yaml Assessment
- **No config.yaml** exists in `librefonts/elsie`.
- **No config.yaml** exists in `ofl/elsie/` in google/fonts.
- **Cannot create an override config.yaml**: The only source files are SFD (FontForge) and VFB (FontLab 5), neither of which is supported by gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` files to reference.

## Conclusions

### Repository URL
The correct upstream repository is **https://github.com/librefonts/elsie**. While this is a legacy archive (last updated 2014) and the sources are not gftools-builder compatible, it is the only repository containing actual source files for this font family. The `googlefonts/elsiefont` URL was always invalid, and `googlefonts/elsie` exists but is empty.

### Commit Hash
No specific onboarding commit can be identified in `librefonts/elsie`. The repo has only 12 commits (all from 2014), with the latest being `9734e9f` (2014-10-17, a Travis CI update). The font sources (SFD/VFB files) were all added in the initial commit `af81473` (2014-07-16) and never modified after that.

The font binaries in google/fonts have been hotfixed multiple times (PR #884, PR #2754) directly without rebuilding from sources.

### Status
- **Repository URL**: `https://github.com/librefonts/elsie` (valid, contains SFD sources)
- **Commit hash**: `af81473` (initial commit containing all source files; sources never changed after this)
- **Config**: None (SFD-only sources, not gftools-builder compatible)
- **Status**: `missing_config` -- SFD-only sources cannot be built with gftools-builder
- **Confidence**: MEDIUM -- The librefonts/elsie repo contains legitimate SFD sources but was never the official upstream used for Google Fonts onboarding. The fonts were likely compiled from VFB/SFD sources offline by the designer and submitted as binaries. Subsequent hotfixes were done directly on binaries.

## Recommended Actions
1. **Update METADATA.pb**: Replace the invalid `"https://github.com/googlefonts/elsiefont (404)"` URL with `"https://github.com/librefonts/elsie"`.
2. **Note in source block**: This is a SFD-only repo; no gftools-builder rebuild is possible without source format conversion.
3. **PR #10266 update**: The currently open PR proposes removing the URL entirely. It could instead be updated to point to `librefonts/elsie` as the best available source repository.
