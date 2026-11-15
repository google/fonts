# BJCree

**Status**: complete
**Date**: 2026-09-27
**Designer**: SIL International
**License**: OFL
**METADATA.pb**: `ofl/bjcree/METADATA.pb`
**Model**: Claude Opus 5.5 (1M context)

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/silnrsi/font-bjcree |
| Commit | `5f901e4186ad92623e34879bef0b746a6482bcb7` (tag `v7.000`) |
| Commit recorded at onboarding | `7476fb691e64eff8956faf2bd68911cb3e1c65b7` (HEAD of `main`) |
| Config YAML | override `ofl/bjcree/config.yaml` (no `config_yaml` field) |
| Branch | `main` |
| Archive URL | https://github.com/silnrsi/font-bjcree/releases/download/v7.000/BJCree-7.000.zip |

## Initial state

- METADATA.pb had a source block with `repository_url`, `commit` `7476fb6`, `archive_url` (the v7.000 release zip), `branch` and five file mappings, but no `config_yaml`. `ofl/bjcree/` had no override `config.yaml`.
- The upstream tree had no gftools-builder config: SIL builds BJCree with smith (`wscript`). It had buildable sources: `source/BJCree.designspace`, two UFO masters (`source/masters/BJCree-Regular.ufo`, `source/masters/BJCree-Bold.ufo`) and four static instances (Regular 400, Medium 500, SemiBold 600, Bold 700).
- The recorded commit `7476fb6` (2026-03-11) was HEAD of `main` at onboarding, two commits after the `v7.000` tag (`5f901e4`, 2026-02-11). Between them, `5d07120` ("Prep for subsequent development", 2026-02-13) set both masters to `Version 7.001` with a new `openTypeHeadCreated`. Nothing else in `source/` changed.

## Actions taken

- Updated the repo archive mirror `upstream_repos/repo_archive/silnrsi/font-bjcree.git`. `main` was still at `7476fb6` and `v7.000` at `5f901e4`.
- Downloaded the v7.000 release zip and confirmed that the four shipped TTFs are byte-identical to it (MD5: Regular `8bc789625a659af13ad20b11f47a632c`, Medium `4bc90e28ab33c70021198ec726a5daf9`, SemiBold `46d11fb24d588333f52813c72ac09e17`, Bold `3a5a3f144a7646e3f62399a2e3bd2f3a`).
- Traced the binaries to the tag. All four report `Version 7.000` and `head.created` 2026-02-10 17:46:22, the values in the Regular (default) master's `fontinfo.plist` at `5f901e4`. Their `head.modified` (2026-02-11 17:15:49 UTC) is 15 minutes after the tag commit. `source/` and `wscript` did not change from `1c6eaa3` (2026-02-10) to the tag. At `7476fb6` the masters say `Version 7.001` and 2026/02/13 09:49:01.
- Changed `commit` in METADATA.pb from `7476fb6` to `5f901e4186ad92623e34879bef0b746a6482bcb7`, the `v7.000` tag.
- Added the override `config.yaml` (source path relative to the repo root):

```yaml
sources:
  - source/BJCree.designspace
familyName: "BJCree"
buildVariable: false
autohintTTF: false
extraStaticFontmakeArgs: "--feature-writer None"
```

  - `buildVariable: false`: Google Fonts ships the four static instances only.
  - `autohintTTF: false`: the release is unhinted. The `wscript` runs `gftools fix-nonhinting`, which adds only `gasp` and `prep`.
  - `extraStaticFontmakeArgs: "--feature-writer None"`: the release has no GDEF, GSUB or GPOS (the `opentype=` line of the `wscript` is commented out). The masters carry underscore-prefixed anchors left by pysilfont's composite builder (`source/composites.txt`), for example `_ringmiddle` on U+1402. With the feature writers that ufo2ft runs by default and that the masters' lib lists, ufo2ft classed 183 glyphs as GDEF marks and HarfBuzz gave 162 Canadian Syllabics letters zero advance.
- Built the fonts from `5f901e4` with the override config and compared them with the shipped files.

## Final state

- METADATA.pb records the `v7.000` tag commit. No other field changed.
- `ofl/bjcree/config.yaml` builds all four shipped styles with gftools builder (fontmake).
- gftools-builder3 (`main-e851b8b`, fontc 1.0.0) cannot build this family faithfully yet. With `buildVariable: false` it instantiates statics only at master locations, so Medium and SemiBold fail. It also has no config key for fontc's `--skip-features` switch and no `autohintTTF` option, so its builds get GDEF marks and autohinting.

## Build test

- gftools builder (gftools from a local development checkout with unpublished builder fixes, fontmake 3.11.1, ufo2ft 3.7.0, fonttools 4.61.1), config at the repo root, checkout at `5f901e4`: four TTFs, `Version 7.000`, UPM 2048, the release's table set (no hinting, no layout tables).
- `functional_gate.py` (sfd-reland `218e487`) against the shipped files, all four styles:
  - cmap PASS (729 codepoints, exact); rendering PASS (0 diffenator3 diffs); line spacing PASS; GDEF PASS (absent in both).
  - shaping: 0 of 782425 runs differ in Regular and Bold. 528 differ in Medium and SemiBold, all by 1 unit in the vertical offset that HarfBuzz fallback mark placement derives from glyph extents. In those two interpolated weights, 97 and 98 glyphs have bounding boxes up to 1 unit apart from the release, and the ink is the same.
  - advances: 730 compared, 0 differ. The check fails only because the build keeps 7 reachable component glyphs (`_barH`, `_ring`, ...) that the release decomposes and drops.
  - names: the IDs the gate checks are equal except Regular name ID 4 (`BJCree` in the release, `BJCree Regular` in the build). Outside that set, name ID 3 (unique ID) and name ID 13 (license description) differ in all four styles.
- The build has 769 glyphs, the release 732: the 21 `_` component glyphs plus the 16 `.alt` glyphs listed in the masters' `public.skipExportGlyphs`. fontmake's instantiator replaces that list with the designspace lib's list, which is empty. None of the 37 is encoded or reachable through layout.
- The same config at `7476fb6` gave the same fonts except for `head` and `name` (`Version 7.001`).
- gftools-builder3 (`main-e851b8b`) with the same config failed: "No master was present at location ... wght: 500".

## Previous upstream_info.md (2026-04-27)

Correction: the text below says the `references/` binaries match across `5f901e4` and `7476fb6`, and that `7476fb691` "produces the binaries currently shipped". In fact `references/` was git-ignored at `5f901e4` and was first committed in `5d07120` as a copy of the v7.000 release, and the sources at `7476fb6` build `Version 7.001`. The shipped binaries correspond to the `v7.000` tag, `5f901e4`.

### BJCree (upstream_info.md of 2026-04-27, commit a7e3f7dcf)

**Status**: `complete`
**Date**: 2026-04-27
**Designer**: SIL International (Bill Jancewicz, Peter Martin, Sharon Correll)
**License**: OFL
**METADATA.pb**: `ofl/bjcree/METADATA.pb`
**Model**: Claude Opus 4.7 (1M context)

#### Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/silnrsi/font-bjcree |
| Commit | `7476fb691e64eff8956faf2bd68911cb3e1c65b7` |
| Config YAML | (none -- see Build Pipeline) |
| Branch | `main` |
| Archive URL | https://github.com/silnrsi/font-bjcree/releases/download/v7.000/BJCree-7.000.zip |
| Release tag | `v7.000` (2026-02-11) |

#### Methodology

##### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field. Verified canonical: `silnrsi` is the SIL Non-Roman Script Initiative GitHub org, and BJCree is an SIL-published typeface. WebFetch of `https://github.com/silnrsi/font-bjcree` confirms the repository is active with default branch `main`, latest release `v7.000`. No newer fork or canonical alternative was found.

##### Commit Hash
Pre-existing in METADATA.pb `source { commit }` field. Mirrored upstream into the repo archive at `upstream_repos/repo_archive/silnrsi/font-bjcree.git` and verified:
- Commit `7476fb691e64eff8956faf2bd68911cb3e1c65b7` exists, currently HEAD of `main`.
- Author: LornaSIL <lorna_evans@sil.org>, 2026-03-11.
- Message: "Update makedocs to create temporary productsite directory."
- Tag `v7.000` points to an earlier commit (`5f901e4`, "Commit rebuilt documentation"), but the `references/` ttf binaries match across both -- `7476fb691` is a docs-tooling commit on top.

##### Binary verification
MD5 of `ofl/bjcree/BJCree-Regular.ttf` matches `references/BJCree-Regular.ttf` blob at the recorded commit (both `8bc789625a659af13ad20b11f47a632c`). All four shipped TTFs report `head.fontRevision = 7.0` and name table `Version 7.000`, consistent with the v7.000 release.

##### Config YAML
No `config.yaml` (gftools-builder format) exists in the upstream repo. The repo uses SIL's own build pipeline (`smith` / `wscript`, `makedocs`, `preflight`). Sources are present (`source/BJCree.designspace`, `source/masters/BJCree-{Regular,Bold}.ufo/`), so a gftools-builder override is feasible but not currently provided. No override `config.yaml` in `ofl/bjcree/` either.

#### Evidence

##### METADATA.pb source block (current)
- `repository_url`: `https://github.com/silnrsi/font-bjcree`
- `commit`: `7476fb691e64eff8956faf2bd68911cb3e1c65b7`
- `archive_url`: `https://github.com/silnrsi/font-bjcree/releases/download/v7.000/BJCree-7.000.zip`
- `branch`: `main`
- `config_yaml`: (not set)

##### google/fonts history
- Onboarding commit: `c9a51e82b` -- "BJCree: Version 7.000 added" (Emma Marichal, 2026-03-26). Commit body explicitly cites `silnrsi/font-bjcree` at `7476fb691...`.
- Subsequent commits (article, primary_script, category fix, name normalization) -- see "Recent upstream activity" below.

##### Upstream repo archive
- Mirrored at `silnrsi/font-bjcree.git` (added 2026-04-27 by this investigation).
- Commit `7476fb691...` verified.
- v7.000 release tag verified.

#### Initial state
- METADATA.pb already had a complete source block (URL, commit, branch, archive_url, files list) added at onboarding.
- No `upstream_info.md` existed.

#### Actions taken
- Mirrored `silnrsi/font-bjcree` into the permanent repo archive.
- Verified commit `7476fb691` exists and produces the binaries currently shipped (MD5 match via `references/BJCree-Regular.ttf`).
- Confirmed font version 7.000 matches release tag.
- Confirmed no upstream `config.yaml`; documented SIL's smith-based build pipeline.
- Authored this `upstream_info.md`.

#### Final state
- METADATA.pb source block is correct and verified -- no changes required.
- No override `config.yaml` added; upstream uses SIL's smith pipeline (not gftools-builder).
- Repo is mirrored in the archive for long-term provenance.

#### Recent upstream activity (post-onboarding, in google/fonts)
- `c9a51e82b` (Emma Marichal, 2026-03-26): BJCree: Version 7.000 added -- initial onboarding from `silnrsi/font-bjcree@7476fb691`.
- `ed93d1d12` (Emma Marichal): added `article/ARTICLE.en_us.html`.
- `023c5eec4` (Emma Marichal): added `primary_script: "Cans"`.
- `b977700ca` (Emma Marichal, 2026-03-27): "BJCree: Change font category from SANS_SERIF to SERIF" -- corrected category. The Latin glyphs in v7.000 are based on URW++ C059 (New Century Schoolbook), so SERIF is the correct classification per the FONTLOG.
- `e1ecf218b` (Emma Marichal, 2026-04-16): "Rename 'BJ Cree' to 'BJCree' in METADATA.pb" -- display-name normalization to match the upstream font family name (`name` ID 1 = `BJCree`).

#### Confidence
**High**: Repository URL canonical (silnrsi org); commit hash verified against upstream mirror; binaries confirmed identical (MD5) to upstream `references/`; font version (`7.000`) matches release tag.
