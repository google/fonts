# Meddon — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists. The current METADATA.pb contains only basic metadata:

```
name: "Meddon"
designer: "Vernon Adams"
license: "OFL"
category: "HANDWRITING"
date_added: "2011-02-02"
```

No `source { }` block is present.

## Repository Analysis

### librefonts/meddon (primary candidate)

- **URL**: https://github.com/librefonts/meddon
- **Status**: Active (not archived, not a fork)
- **Default branch**: master
- **Last push**: 2014-10-17
- **Single commit**: `0317f7b` (2014-10-17, by hash3g) — "update .travis.yml"

The repository contains:
- `src/Meddon.sfd` — FontForge source file (SFD format), Version 1.000
- TTX decomposition files (`.ttx`) — XML dump of the font binary tables
- `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`
- `.travis.yml` — legacy CI configuration using fontbakery-build.py

This repository was part of the `librefonts` organization's batch setup of Google Fonts upstream repos, created with TTX decompositions and FontForge sources. It was set up by hash3g as a standardized mirror.

### vernnobile/MeddonFont (original designer repo)

- **URL**: https://github.com/vernnobile/MeddonFont
- **Description**: "Repository for Meddon webfont"
- **Default branch**: master
- **Last push**: 2012-02-01
- **3 commits**: earliest from 2012-01-21 ("README"), latest from 2012-02-01 ("in progress")

The repository contains two directories:
- `Old/` — Meddon.sfd (458,060 bytes), Meddon.ttf (old version), OFL.txt
- `New/` — Meddon.sfd (458,295 bytes), Meddon.sfd~ (backup), Meddon.ttf (128,632 bytes), OFL.txt

The `vernnobile` GitHub account belongs to Vernon Adams (the font's designer), confirmed via GitHub profile (name: "vernon adams", blog: code.newtypography.co.uk).

The TTF in `New/` (128,632 bytes) matched the initial google/fonts binary size before the nbsp fix was applied.

## Onboarding History

The font was added to Google Fonts on **2011-02-02** according to `date_added` in METADATA.pb, predating the current google/fonts repository structure.

In the current google/fonts repository:

1. **`90abd17b`** (2015-03-07, Dave Crossland) — "Initial commit" — Bulk migration of all Google Fonts into the current repository. The Meddon.ttf was 128,632 bytes at this point.

2. **`d78eefe5`** (2015-03-19, Dave Crossland) — "Update Meddon to fix nbsp" — Updated the binary from 128,632 to 128,264 bytes. This was a targeted fix for the non-breaking space character.

3. **`bacec365`** (2015-08-05, Dave Crossland) — "Fix fsType for 54 font files" — Modified the binary (same size 128,264 bytes) to fix the fsType embedding bits.

No further binary modifications were made after 2015-08-05. Later commits only modified METADATA.pb (classifications, language support, etc.) and a promotional PR #8355 (2024-10-24, "Update families.csv with Meddon for Halloween") that did not touch the font binary.

## Build Configuration

**No config.yaml exists** in either upstream repository.

The font sources are exclusively in **SFD (FontForge) format**. There are no `.glyphs`, `.ufo`, or `.designspace` files in either repository. The SFD format is not compatible with gftools-builder, which requires one of those modern source formats.

The librefonts repo had a legacy `.travis.yml` CI setup using the old `fontbakery-build.py` tool, but this is not equivalent to a modern gftools-builder configuration.

## Findings

1. **No source block in METADATA.pb** — Needs to be added.

2. **SFD-only sources** — Both upstream repos contain only FontForge (.sfd) sources. These are not compatible with gftools-builder. An override config.yaml cannot be created because gftools-builder does not support SFD files.

3. **Two candidate repositories**: The `librefonts/meddon` repo is the more structured of the two (with TTX decomposition and CI), while `vernnobile/MeddonFont` is the original designer's repo. The librefonts repo is the conventional upstream for this family.

4. **Commit hash**: The librefonts repo has only one commit (`0317f7b`), which predates the google/fonts repo. The binary in google/fonts was not built from this repo — it was compiled separately (likely from the SFD using FontForge) and the librefonts repo was set up afterward as a mirror. The commit hash is therefore a reference point for the repo state, not a build provenance marker.

5. **Binary modifications in google/fonts**: The font binary was modified twice after the initial migration (nbsp fix and fsType fix), meaning the current binary in google/fonts does not match any binary in either upstream repo.

6. **Designer**: Vernon Adams (deceased, 2014). The font will not receive upstream updates from the original designer.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/meddon"
  commit: "0317f7b9df068bfbcdb958aa49887232c62d3541"
}
```

Notes on the recommended block:
- **repository_url** points to `librefonts/meddon` as the conventional upstream (structured with sources and CI)
- **commit** is the only commit in the repo (`0317f7b`), serving as a reference point
- **config_yaml is omitted** because the sources are SFD-only and no config.yaml can be created for gftools-builder
- **No override config.yaml** is possible because gftools-builder does not support SFD sources
- The status remains "incomplete" because the SFD-only nature of the sources means the font cannot be rebuilt with modern tooling without first converting the sources to a supported format
