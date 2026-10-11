# Investigation Report: Fanwood Text

## Family Details
- **Family Name**: Fanwood Text
- **Designer**: Barry Schwartz
- **License**: OFL
- **Category**: Serif
- **Date Added**: 2011-08-31
- **Path in google/fonts**: `ofl/fanwoodtext/`

## Source Repository
- **Repository URL**: https://github.com/theleagueof/fanwood
- **Commit**: `cbaaed9704e7d37d3dcdbdf0b472e9efd0e39432`
- **Branch**: master
- **Status**: complete
- **Confidence**: HIGH

## Investigation Process

### METADATA.pb Analysis

The METADATA.pb already contains a source block with:
- `repository_url`: `https://github.com/theleagueof/fanwood`
- `commit`: `cbaaed9704e7d37d3dcdbdf0b472e9efd0e39432`

The source block was added in two stages:
1. Simon Cozens added the `repository_url` field on 2024-01-14 in commit `c8a4f8556` ("More upstreams (e,f)")
2. Felipe Sanches added the `commit` hash and override `config.yaml` on 2025-11-21 in commit `47ac77b7e` ("sources info for Fanwood Text")

### Binary File History

The binary font files (`FanwoodText-Regular.ttf` and `FanwoodText-Italic.ttf`) were added in the initial commit of google/fonts (`90abd17b4f97671435798b6147b698aa9087612f`, authored by Dave Crossland on 2015-03-07, "Initial commit"). The font files have never been updated since.

### Upstream Repository Analysis

The upstream repository at `https://github.com/theleagueof/fanwood` (The League of Moveable Type) contains a single commit:

- **Commit**: `cbaaed9704e7d37d3dcdbdf0b472e9efd0e39432`
- **Date**: 2011-05-25
- **Author**: micah rich
- **Message**: "Initial commit with readme and licenses"

Since there is only one commit in the entire repository, the commit hash is unambiguous and definitively correct.

The repository contains UFO sources for **two distinct font families**:
1. **Fanwood**: `source/Fanwood.ufo` (familyName: "Fanwood") + `source/Fanwood Italic.ufo` (familyName: "Fanwood")
2. **Fanwood Text**: `source/Fanwood Text.ufo` (familyName: "Fanwood Text") + `source/Fanwood Text Italic.ufo` (familyName: "Fanwood Text")

According to the readme, "Fanwood Text roman and italic are the same as Fanwood but slightly darker and reduced in contrast; I tailored it to increase readability on my Amazon Kindle 3 e-book reader." Only "Fanwood Text" is in the Google Fonts catalog; there is no separate "Fanwood" family in google/fonts.

The repository is clean (no local modifications) and on the master branch, up to date with origin.

### Config.yaml Analysis

There is no `config.yaml` in the upstream repository.

An override `config.yaml` exists in the google/fonts family directory (`ofl/fanwoodtext/config.yaml`), created by Felipe Sanches on 2025-11-21. Its contents:

```yaml
buildVariable: false
sources:
  - source/Fanwood.ufo
  - source/Fanwood Text.ufo
  - source/Fanwood Italic.ufo
  - source/Fanwood Text Italic.ufo
```

**Issue**: The config.yaml lists all 4 UFOs from the upstream repo, but this family directory is specifically for "Fanwood Text". The `source/Fanwood.ufo` and `source/Fanwood Italic.ufo` belong to a different family ("Fanwood") and should not be included. The config.yaml for this family should ideally only reference:
- `source/Fanwood Text.ufo`
- `source/Fanwood Text Italic.ufo`

Since the override config exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

### Historical Context

The original DESCRIPTION.en_us.html references two older source locations:
- Bitbucket: `https://bitbucket.org/sortsmill/sortsmill-fonts` (Barry Schwartz's Sorts Mill foundry)
- The League of Moveable Type: `https://www.theleagueofmoveabletype.com/fanwood`

The font was originally designed by Barry Schwartz as part of his Sorts Mill type foundry. It is a revival of Fairfield, the typeface first published in 1940 by Czech-American type designer Rudolph Ruzicka.

The copyright in the upstream license file uses the email `site-chieftain@crudfactory.com` with Reserved Font Name "Fanwood", while the google/fonts OFL.txt uses `chemoelectric@chemoelectric.org` without the Reserved Font Name clause.

## Summary

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/theleagueof/fanwood |
| Commit Hash | `cbaaed9704e7d37d3dcdbdf0b472e9efd0e39432` |
| Config | Override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |
| Note | Config.yaml includes all 4 UFOs but should only include the 2 Fanwood Text UFOs |

## Recommended Action

The override `config.yaml` should be corrected to only reference the Fanwood Text sources:

```yaml
buildVariable: false
sources:
  - source/Fanwood Text.ufo
  - source/Fanwood Text Italic.ufo
```

This is a minor issue since gftools-builder may handle the multi-family output correctly by filtering based on family name, but it would be cleaner to only reference the relevant sources.
