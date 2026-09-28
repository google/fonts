# Cousine: Source Metadata

**Model**: Claude Opus 5.5
**Date**: 2026-09-27

| Field | Value |
|-------|-------|
| Repository | https://www.github.com/googlefonts/cousine |
| Commit | `c0fbdb438443968c884a5c13f5f9bee916a7f89b` (tag `v1.241`) |
| Config | `sources/config.yaml` (upstream) |
| Status | complete |
| Confidence | HIGH |

## Initial state

- `METADATA.pb` had the source block that gftools-packager wrote in google/fonts
  commit ab75f7cf3e (PR #10604, "Cousine: Version 1.241; ttfautohint
  (v1.8.4.16-eb64) added", merged 2026-06-10): repository_url, commit
  `c0fbdb4`, the v1.241 `archive_url`, five `files` mappings and
  `branch: "main"`. It had no `config_yaml`.
- `ofl/cousine/` had no override `config.yaml` and no `upstream_info.md`. Both
  had existed in `apache/cousine/`. Commit 2dd93357f2 (PR #10478, merged
  2026-04-29) deleted them when it moved the family to `ofl/` at v1.240.

## Actions taken

- Verified the recorded commit `c0fbdb4`:
  - It is the target of upstream tag `v1.241` and was still the head of
    upstream `main` on 2026-09-27, so no upstream commit landed on `main`
    before the merge on 2026-06-10.
  - It is dated 2026-06-09 11:55 +0100, 8 minutes before the google/fonts
    commit.
  - The four shipped TTFs and `OFL.txt` are byte-identical to the files in the
    `v1.241` release archive (`cousine-v1.241.zip`).
  - The shipped TTFs match `fonts/ttf/*.ttf` at `c0fbdb4` in every table except
    `head` (`modified` and `checkSumAdjustment`). Their `head.modified`
    (10:59:59 to 11:00:02 UTC) and the zip entry times (11:01 UTC) are
    consistent with the upstream CI release job rebuilding the fonts at the
    tag.
  - `sources/` has not changed since `b0fe9f8` ("Bump version to 1.241"). The
    commits after it touched only the built fonts, CI, the Makefile and the
    requirements.
- Found `sources/config.yaml` at `c0fbdb4`. It was added in `e189758`
  (2026-04-27) and has not changed since. It lists the four `.glyphs` sources,
  with `buildVariable: false` and `removeOutlineOverlaps: false`.
- Set `config_yaml: "sources/config.yaml"` in `METADATA.pb`. No override
  `config.yaml` was created and no other field was changed.
- Build-tested the upstream config at `c0fbdb4`:
  - gftools-builder 3.0.0 (builder3 `e851b8b`, fontc 1.0.0) built all four
    TTFs. cmap (2282 codepoints), glyph order, advances, shaping, rendering,
    line metrics and GDEF all matched the shipped fonts. There were two
    differences:
    - The output is unhinted: builder3's recipe for single-master static
      sources has no ttfautohint step.
    - Bold and Bold Italic have `OS/2.usWeightClass` 400 where the shipped
      fonts have 700. This is a fontc gap: the `weightClass = Bold` of the
      single instance in these Glyphs 2 sources is not carried into OS/2. It
      is not a config error.
  - The Python gftools builder (gftools 0.9.100.dev6+g2db1fe32f.d20260315,
    fontmake 3.11.1, glyphsLib 6.12.7, ttfautohint-py 0.6.0) reproduced all
    four shipped TTFs in every table except `head` (`modified` and
    `checkSumAdjustment`).

## Final state

- `METADATA.pb` points at `googlefonts/cousine` at `c0fbdb4` with
  `config_yaml: "sources/config.yaml"`. That config reproduces the shipped
  v1.241 fonts with the Python builder, apart from the `head` timestamp.
- Open items for the fontc build: `usWeightClass` of Bold and Bold Italic
  (fontc), and hinting (builder3).

## Repository history

- 2020-07-05 to 2021-02-28: 10 commits by Marek Jeziorek, Denis Moyogo
  Jacquerye and CI, from `7f897db` to `134dfbb`. This was a development
  repository:
  - per-style Glyphs sources in `sources/Cousine-<Style>/` with GDEF, GPOS and
    GSUB text dumps and plists;
  - a variable build in `fonts/ttf/{hinted,unhinted}/variable_ttf/Cousine-VF.ttf`;
  - `LICENSE`, containing the SIL Open Font License 1.1 text;
  - no gftools-builder config.
- 2026-04-27: Simon Cozens moved the repository to the
  googlefonts-project-template layout in `e189758`, with
  `sources/Cousine-<Style>.glyphs`, `OFL.txt` (renamed from `LICENSE`) and
  `sources/config.yaml`. He then released v1.240 (`57b3425`, recorded by
  PR #10478) and v1.241 (`c0fbdb4`, PR #10604).
- Earlier source blocks in google/fonts recorded commit `7f897db` (in
  `apache/cousine/`, 2026-03-26) and `57b3425` (v1.240).
- The removed override `apache/cousine/config.yaml` listed
  `sources/Cousine-<Style>.glyphs`. Those paths did not exist at its recorded
  commit `7f897db`, where the sources were in per-style subdirectories.
- `librefonts/cousine` is a third-party mirror of TTX dumps with 14 commits,
  from 2014-07-16 (Mikhail Kashkin) to 2014-10-17 (hash3g). The 2026-03-03
  report below lists only the last of these commits.

## Earlier upstream_info.md content

Both versions were in `apache/cousine/upstream_info.md` and were deleted by
commit 2dd93357f2. They are reproduced below. Their headings were demoted three
levels, and one em dash was replaced by `--`.

### Version of 2026-03-26 (commit e243552ac)

#### Cousine -- Source Repository Investigation

**Model**: Claude Opus 4.6

##### Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/cousine |
| Commit | `7f897dbd87fbd14d2f8ec0306d5c1ed2317dfe47` |
| Confidence | High |

##### Source Types

The repository contains Glyphs sources:
- `sources/Cousine-Regular.glyphs`
- `sources/Cousine-Bold.glyphs`
- `sources/Cousine-Italic.glyphs`
- `sources/Cousine-BoldItalic.glyphs`

All four styles have individual Glyphs source files.

##### Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs sources could potentially be built with gftools-builder given an override config.

##### Investigation Notes

Cousine is one of the Chrome OS core fonts (metrically compatible with Courier New), hosted under the googlefonts organization. The binary in google/fonts was last updated on 2017-08-07 (v1.211 hotfix). The repository is the canonical upstream maintained by the Google Fonts team.

A source block was added to METADATA.pb pointing to this repository and commit.

##### Confidence: High

Official googlefonts organization repository.

### Version of 2026-03-03 (commit 7380f7ceb)

#### Investigation Report: Cousine

##### Summary

Cousine is a monospace sans-serif font designed by Steve Matteson at Monotype Imaging, part of the Chrome OS core fonts family (alongside Arimo and Tinos). It is metrically compatible with Courier New. The current binaries in google/fonts are Version 1.21, last updated via PR #769 in August 2017. There is a development repository at `googlefonts/cousine` (created July 2020 by Marek Jeziorek) containing .glyphs sources and a variable font build, but the currently-serving static binaries predate this repo. There is also a `librefonts/cousine` mirror containing TTX dumps and no buildable sources. No config.yaml exists in either repo.

##### Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Cousine |
| Designer           | Steve Matteson |
| License            | Apache 2.0 |
| Category           | MONOSPACE |
| Date Added         | 2010-11-18 |
| Repository URL     | https://github.com/googlefonts/cousine |
| Commit Hash        | Not determinable for current v1.21 binaries |
| Config YAML        | None (no config.yaml in repo) |
| Source Types        | .glyphs (in googlefonts/cousine, for future VF build) |
| Font Version        | 1.21 |
| Status             | missing_config |
| Confidence         | MEDIUM |

##### Investigation Details

###### Current State in google/fonts

- **Directory**: `apache/cousine/`
- **Files**: Cousine-Regular.ttf, Cousine-Italic.ttf, Cousine-Bold.ttf, Cousine-BoldItalic.ttf, DESCRIPTION.en_us.html, LICENSE.txt, METADATA.pb
- **No source block** in METADATA.pb
- **Font version**: Version 1.21 (from name table: "1.21;MONO;Cousine-Regular")
- **Copyright**: "Digitized data copyright (c) 2010-2012 Google Corporation."
- **Vendor**: Monotype Imaging Inc.

###### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| b8df781 | 2017-08-07 | Marc Foley | hotfix-cousine: v1.211 added (#769) |
| 49fbebd | 2017 | (batch) | chmod -x on all font files |
| 90abd17 | 2015-03-07 | Dave Crossland | Initial commit |

The last substantive font update was PR #769, merged 2017-08-07 by Marc Foley. The PR body was empty, providing no upstream reference or commit hash.

###### Upstream Repository: googlefonts/cousine

- **URL**: https://github.com/googlefonts/cousine
- **Created**: 2020-07-05 by Marek Jeziorek (marekj@google.com)
- **Default branch**: main
- **Description**: "Cousine sources, tests and development fonts"
- **Source files**: .glyphs format (sources/Cousine-Regular/Cousine-Regular.glyphs, etc.)
- **Built fonts**: Variable font only (fonts/ttf/hinted/variable_ttf/Cousine-VF.ttf)
- **No config.yaml** present in the repo
- **10 commits total**, last updated 2021-02-28

This repository was created in 2020 as a development repo for a variable font version of Cousine, using .glyphs sources. The variable font build has NOT been pushed to google/fonts yet -- the catalog still serves the older static v1.21 TTFs.

###### Cached Mirror: librefonts/cousine

- **Path**: upstream_repos/fontc_crater_cache/librefonts/cousine
- **URL**: https://github.com/librefonts/cousine
- **Content**: TTX dumps of the binary fonts, plus FontForge subset scripts in src/
- **Source type**: TTX (decompiled binary, not original design sources)
- **Single commit** by hash3g (2014-10-17): "update .travis.yml"
- **Versions file**: Lists Version 1.21 for all four styles

This is a librefonts automated mirror containing decompiled TTX files. It is not a proper upstream source repository and should not be used as the repository_url in METADATA.pb.

###### Origin of Current Binaries

The current v1.21 binaries were produced by Monotype Imaging (as indicated by the font name table). Cousine is one of the Chrome OS core fonts originally developed by Ascender Corporation (later acquired by Monotype). The fonts were delivered to Google as compiled binaries. The googlefonts/cousine repo was created later (2020) as a development workspace for a future variable font version.

The font version string says "Version 1.21" but the PR #769 title says "v1.211" -- this appears to be a minor discrepancy in the commit message (the actual name table says 1.21).

###### Config.yaml Assessment

Neither the googlefonts/cousine repo nor the librefonts mirror has a config.yaml file. The googlefonts/cousine repo has .glyphs sources that could potentially be built with gftools-builder, but:
1. The current binaries were not built from these sources
2. There are four separate .glyphs files (one per style), not a single source
3. No build configuration exists

##### Conclusion

The repository URL should be set to `https://github.com/googlefonts/cousine` as this is the official Google Fonts development repository. However, the current binaries predate this repo and were produced by Monotype. A specific onboarding commit hash cannot be determined for the v1.21 binaries. No config.yaml is available.

###### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/cousine"
}
```

**Note**: No commit hash or config_yaml can be specified because:
- The current v1.21 binaries were produced by Monotype before the GitHub repo existed
- The googlefonts/cousine repo contains newer development work (variable font) that has not been published to google/fonts yet
- No config.yaml exists in the repo

###### Status: missing_config
###### Confidence: MEDIUM

The repository URL is correct (official googlefonts org), but the relationship between the repo contents and the currently-serving binaries is indirect -- the repo represents future development, not the source of the current fonts.
