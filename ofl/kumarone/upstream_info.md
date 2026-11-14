# Kumar One — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/itfoundry/kumar |
| Commit | `551e277f8fc8f18a5ee11935cf5007bda9930364` |
| Confidence | High |

## Source Types

The repository contains Glyphs sources:
- `masters/Kumar One.glyphs` — primary Glyphs source

This is a monorepo that contains both Kumar One and Kumar One Outline variants.

## Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs source could potentially be built with gftools-builder given an override config.

## Investigation Notes

Indian Type Foundry's repository is the canonical upstream for the Kumar font family. The binary in google/fonts was last updated on 2017-05-23 (v1.001 hotfix). The repository contains the filled variant (Kumar One) used by this family entry.

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Indian Type Foundry (itfoundry) is the original designer/publisher.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: ["Kumar One.glyphs"]` — a repository-root path. fontc_crater failed with `missing source 'Kumar One.glyphs'`.

### Investigation
At the recorded commit `3192a79` the Glyphs source is `masters/Kumar One.glyphs`, not at the repository root. The override config path was missing the `masters/` directory prefix. The recorded commit is correct.

### Actions taken
The override `config.yaml` source path was corrected from `Kumar One.glyphs` to `masters/Kumar One.glyphs`.

### Final state
The override `config.yaml` references `masters/Kumar One.glyphs`, which exists at the recorded commit `3192a79`. The companion family Kumar One Outline shares the same repository, commit and source file and received the same correction.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`3192a79a`](https://github.com/itfoundry/kumar/commit/3192a79a) (the 1.001 release, 2016-04-12) to [`551e277f`](https://github.com/itfoundry/kumar/commit/551e277f) ("Compile 1.000, OTF and TTF", 2016-04-03, on `master`). Google Fonts never took 1.001, whose masters drop `idotaccent` and rename conjuncts (847 glyphs against 868).

The shipped `KumarOne-Regular.ttf` is the 1.000 build, hotfixed to 1.001 by [google/fonts#973](https://github.com/google/fonts/pull/973) ([google/fonts `06463af0`](https://github.com/google/fonts/commit/06463af0)). Its glyf, hmtx, GSUB, GDEF and hinting tables are byte-identical to `products/KumarOne-Regular.ttf` at `551e277f`; google/fonts changed name, head, OS/2 fsType (4 to 0) and the vertical metrics, and cmap differs only in serialization. md5 shipped `19cceb556885c8267a5b1c00cae372a8`, upstream `30fbc2b4eaf58f048ebb18be96f64e38`. The next upstream commit, [`b339c2a2`](https://github.com/itfoundry/kumar/commit/b339c2a2), only changes the hhea values in `build.py` (to 1150/-650), which the shipped font does not have.

The override `config.yaml` (`masters/Kumar One.glyphs`) resolves at `551e277f` and is not changed here.
