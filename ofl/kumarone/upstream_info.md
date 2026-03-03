# Kumarone — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kumarone`
**Status**: complete (needs override config.yaml)

## Initial State

The METADATA.pb for Kumar One contained no `source { }` block. The file listed:
- **Designer**: Indian Type Foundry
- **License**: OFL
- **Category**: DISPLAY
- **Date added**: 2016-06-20
- **Primary script**: Gujarati (Gujr)

No `repository_url`, `commit`, or `config_yaml` fields were present.

The family directory in google/fonts contained:
- `KumarOne-Regular.ttf` (95,852 bytes)
- `METADATA.pb`
- `DESCRIPTION.en_us.html`
- `OFL.txt`

No override `config.yaml` existed in the google/fonts family directory.

## Investigation

### Upstream Repository Discovery

The DESCRIPTION.en_us.html file contained a direct link to the upstream repository:

> To contribute, see [github.com/itfoundry/kumar](https://github.com/itfoundry/kumar)

The repository at `https://github.com/itfoundry/kumar` was confirmed accessible and not archived. Default branch is `master`.

### Google Fonts Git History

The font binary was last modified (and initially added) in commit `06463af09`:

```
06463af09 hotfix-kumarone: v1.001 added (#973)
```

This was the onboarding commit, authored by Marc Foley on 2017-05-23. It added all four files in the family directory.

### PR #973

PR [#973](https://github.com/google/fonts/pull/973) titled "hotfix-kumarone: v1.001 added" was authored by Marc Foley (@m4rc1e) and merged on 2017-05-23. The PR body stated:

> This partially resolves https://github.com/google/fonts/issues/271 by adding a family already in the API back to this repo.

Issue #271 was about fonts available in the Google Fonts web interface but not yet in the git repository. The PR contained two commits:
1. `70810e8` — "hotfix-kumarone: v1.001 added" (by Marc Foley)
2. `79bb562` — "Update OFL.txt" (by Dave Crossland)

No upstream commit hash was referenced in the PR body or commit messages.

### Upstream Repository Analysis

The cached clone at `upstream_repos/fontc_crater_cache/itfoundry/kumar/` was clean and up-to-date with origin.

The repository contained only a single commit:

```
3192a79a79202eb715d83fd044e9234a6d0dde66  2016-04-12  Liang Hai  "Merge branch 'develop'"
```

#### Repository Structure

```
build.py              — hindkit-based build script
masters/
  Kumar One.glyphs    — Glyphs source (125,298 lines)
features/
  GSUB.fea
  GSUB_lookups.fea
products/
  KumarOne-Regular.otf
  KumarOne-Regular.ttf
  KumarOneOutline-Regular.otf
  KumarOneOutline-Regular.ttf
GlyphOrderAndAliasDB
OFL.txt
README.md
```

#### Source Structure

The `.glyphs` file contains **two masters**:
- **Outlined** (custom axis value 0) — used for Kumar One Outline
- **Filled** (custom axis value 1) — used for Kumar One

The `build.py` script uses `hindkit` to produce both Kumar One and Kumar One Outline from the same source file, selecting the appropriate master for each family. This is **not** a variable font — each master produces a separate static family.

No `config.yaml` existed in the upstream repository. The build system was `hindkit`, not `gftools-builder`.

#### Binary Comparison

The font in google/fonts (95,852 bytes) differed from the `products/KumarOne-Regular.ttf` in the upstream repo (92,076 bytes). SHA256 hashes did not match. This is expected — Marc Foley likely rebuilt the font with a different toolchain (possibly newer version) when preparing PR #973 in May 2017, while the upstream products were from the April 2016 build.

### Commit Identification

Since the upstream repository has only a single commit (`3192a79a` from 2016-04-12), this is necessarily the commit used for onboarding. The font version in `build.py` was `fontrevision = '1.001'`, matching the PR title "v1.001 added".

### Related Family

Kumar One Outline (`ofl/kumaroneoutline`) shares the same upstream repository and source file. It was added separately to google/fonts via PR [#9332](https://github.com/google/fonts/pull/9332) ("Missing in GH") by Rod Sheeter (@rsheeter) on 2025-04-10. A separate investigation report should be created for that family.

## Actions Taken

- Confirmed upstream repository URL: `https://github.com/itfoundry/kumar`
- Identified the single upstream commit: `3192a79a79202eb715d83fd044e9234a6d0dde66`
- Verified no config.yaml exists in upstream or as an override in google/fonts
- Verified the `.glyphs` source file is compatible with gftools-builder

## Final State

- **Repository URL**: `https://github.com/itfoundry/kumar`
- **Commit**: `3192a79a79202eb715d83fd044e9234a6d0dde66` (only commit in the repo, 2016-04-12)
- **Config**: No config.yaml in upstream; an override config.yaml should be created in google/fonts
- **Source file**: `masters/Kumar One.glyphs` (shared with Kumar One Outline; "Filled" master produces Kumar One)
- **Build system**: Originally `hindkit`; needs migration to gftools-builder via override config
- **Confidence**: HIGH — single commit in repo, version matches PR title

### Notes

- The `.glyphs` file produces two families from two masters (Filled/Outlined). The override `config.yaml` for Kumar One would need to select only the "Filled" master/instance. A separate config would be needed for Kumar One Outline.
- The upstream repository has had no activity since 2016. It is unlikely to be updated.

## Source Block

```
source {
  repository_url: "https://github.com/itfoundry/kumar"
  commit: "3192a79a79202eb715d83fd044e9234a6d0dde66"
}
```

Note: The `config_yaml` field is omitted. An override `config.yaml` should be created in the google/fonts family directory (`ofl/kumarone/config.yaml`). When the override is placed there, google-fonts-sources will auto-detect it and no `config_yaml` field is needed in METADATA.pb.
