# Marko One — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/cyrealtype/Marko-One"
  commit: "d5cfae97a173fc09d182a391fb78dd3d8a727cd8"
}
```

A `config.yaml` override file also exists in the google/fonts family directory:
```yaml
buildVariable: false
sources:
  - sources/MarkoOne.glyphs
```

## Repository Analysis

**Repository**: https://github.com/cyrealtype/Marko-One
**Default branch**: master
**Cached at**: `upstream_repos/fontc_crater_cache/cyrealtype/Marko-One`
**Repository status**: Clean, up to date with origin

The upstream repository was created on January 10, 2016 by Alexei Vanyashin (alexeiva, Cyreal). The initial commit contained VFB source files (`src/MarkoOne-Regular-OTF.vfb`, `src/MarkoOne-Regular-TTF.vfb`, `src/MarkoOne-Regular.vfb`) along with compiled TTF/OTF binaries.

The repository has 16 commits total, all on the master branch. The most significant activity occurred on November 25-26, 2017, when alexeiva reorganized the repo structure and converted sources to a Glyphs format file (`sources/MarkoOne.glyphs`).

**Source files at HEAD (354c730)**:
- `sources/MarkoOne.glyphs` — Glyphs format source (14,067 lines)

**No config.yaml exists in the upstream repository.**

### Commit Timeline

| Commit | Date | Description |
|--------|------|-------------|
| 0cd1147 | 2016-01-10 | Initial commit (VFB sources, compiled fonts) |
| ... | 2016-01-10 to 2016-04-06 | README and image updates |
| d5cfae9 | 2017-11-25 | Reorganized repo structure, added .glyphs source |
| 4d035a1 | 2017-11-25 | Version bump to 1.100 |
| 3e974eb | 2017-11-25 | Fix Google Fonts specs |
| c8f325a | 2017-11-25 | Updated features, made combining marks |
| 7b7af16 | 2017-11-25 | Added missing Latin Core glyphs |
| 5b2dd4e | 2017-11-25 | Updated FONTLOG |
| 2415283 | 2017-11-26 | Regenerated fonts (52,172 byte TTF) |
| d669125 | 2017-11-26 | Updated authors and README |
| 354c730 | 2017-11-26 | Removed old VFB files |

## Onboarding History

The font was added to google/fonts in the initial commit (90abd17, March 7, 2015) by Dave Crossland. This predates the upstream GitHub repository, which was not created until January 2016. The font binary (`MarkoOne-Regular.ttf`, 34,484 bytes) has never been updated since that initial commit.

**Key timeline conflict**: The google/fonts binary (34,484 bytes) does not match any TTF ever committed to the upstream repository:
- Initial upstream TTF (0cd1147, 2016): 76,560 bytes (SHA256: b827d39f...)
- Regenerated upstream TTF (2415283, 2017): 52,172 bytes

This means the font binary in google/fonts was built from sources that predate the upstream GitHub repository. The original source was likely a VFB (FontLab) project that was later added to the GitHub repo.

### google/fonts Commit History for ofl/markoone/

| Commit | Description |
|--------|-------------|
| 90abd17 | Initial commit (2015-03-07) — original onboarding |
| 480630d | Tentative update to METADATA.pb textprotos |
| 27f377a | Update copyright field in METADATA.pb |
| 8839397 | Remove METADATA.json files |
| 633ebad | Add language support metadata (PR #4160) |
| da09c78 | Temporarily fix build, remove latin-ext |
| e25c8f0 | Update METADATA.pb |
| 28b492c | Clear languages from METADATA.pb for non-Noto |
| c6307ba | Roll back 28b492c0 (PR #4677) |
| 701bd39 | Undo rollback, remove languages (PR #4706) |
| c891a9b | Update upstreams — added repository_url (PR #7344, merged 2024-03-06) |
| b10633f | Sources info — added commit hash and config.yaml (PR #9979, merged 2025-11-07) |

## Build Configuration

The upstream repository does not contain a `config.yaml` file. An override `config.yaml` was created in the google/fonts family directory (commit b10633f, PR #9979) with the following content:

```yaml
buildVariable: false
sources:
  - sources/MarkoOne.glyphs
```

This references the Glyphs source file at `sources/MarkoOne.glyphs`, which exists at commit `d5cfae9` (where it was first introduced) and at all subsequent commits through HEAD (354c730).

## Findings

1. **Commit hash is problematic**: The currently recorded commit `d5cfae9` is the commit that reorganized the repo and first introduced the `.glyphs` source file. However, this commit was followed by 8 more commits that made substantial improvements: version bump, Google Fonts spec fixes, added combining marks, added missing Latin Core glyphs, and regenerated fonts. The commit `d5cfae9` represents an intermediate state rather than a final, tested version.

2. **Font binary was never rebuilt from upstream**: The font in google/fonts (34,484 bytes, from 2015) does not match any binary in the upstream repo. It was onboarded before the GitHub repository existed, likely from FontLab VFB sources provided directly by the designer.

3. **The upstream repo has newer, improved sources**: The latest commit (354c730) includes additional glyphs (Latin Core), improved features, combining marks, and GF spec compliance fixes. These improvements were never incorporated into google/fonts.

4. **The commit hash should reference HEAD**: Since the font has never been updated from the upstream repo, and the `.glyphs` source file was introduced at `d5cfae9` and then improved through `354c730`, the most appropriate commit to reference for future rebuilding would be HEAD (354c730), as it represents the most complete and corrected state of the sources. However, if the goal is to reference the commit that corresponds to the current binary in google/fonts, no upstream commit matches — the binary predates the repo.

5. **Override config.yaml is correct**: The config.yaml correctly references `sources/MarkoOne.glyphs` which exists at both the referenced commit and HEAD. Since the override is in google/fonts, the `config_yaml` field is properly omitted from METADATA.pb.

6. **Previous investigation noted uncertainty**: The commit message from b10633f explicitly stated "Exact upstream commit that was used for onboarding is unclear, though." This is accurate — no upstream commit corresponds to the current binary.

## Recommended Source Block

Given that the font binary in google/fonts was never built from the upstream GitHub repository, and the upstream repo represents a later rework of the sources, the best approach depends on the project's goals:

**Option A — Reference HEAD for future builds (recommended)**:
```
source {
  repository_url: "https://github.com/cyrealtype/Marko-One"
  commit: "354c73092231c4f47a9bc5bf1e7279b30f60b042"
}
```
This references the latest commit which includes all improvements (Latin Core glyphs, GF spec fixes, combining marks). The override `config.yaml` in google/fonts would remain as-is.

**Option B — Keep current reference (status quo)**:
```
source {
  repository_url: "https://github.com/cyrealtype/Marko-One"
  commit: "d5cfae97a173fc09d182a391fb78dd3d8a727cd8"
}
```
This is the first commit with the `.glyphs` source file but is missing subsequent improvements.

**Recommendation**: Update the commit hash to `354c730` (HEAD), which represents the complete, improved state of the Glyphs sources. The current commit `d5cfae9` is an intermediate state that was immediately followed by substantial fixes and additions. Since no upstream commit matches the current binary anyway, the commit reference should point to the best available sources for a future rebuild. The override `config.yaml` would continue to work correctly at either commit.
