# Cormorant Garamond

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Christian Thalmann
**METADATA.pb path**: `ofl/cormorantgaramond/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/CatharsisFonts/Cormorant |
| Commit | `6d210fd3550b7358ca62d6ba3e354ec1ec940813` |
| Config YAML | `sources/config-garamond.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/CatharsisFonts/Cormorant` was already present in the METADATA.pb `source { repository_url }` field. It is confirmed by multiple sources:
- The copyright string in the font files: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
- The gftools-packager commit `6a386aadc` (PR #4890, Version 4.000) explicitly references this URL
- The Version 4.001 commit `93473babe` (PR #8593) by Simon Cozens also references this URL

The Cormorant project is a single upstream repo that produces multiple sub-families: Cormorant, Cormorant Garamond, Cormorant Infant, Cormorant SC, Cormorant Unicase, and Cormorant Upright. All six families in google/fonts share this same upstream repository.

## How the Commit Hash Was Identified

The commit hash `6d210fd3550b7358ca62d6ba3e354ec1ec940813` is directly stated in the google/fonts commit `93473babe` (PR #8593, "Cormorant Garamond: Version 4.001 added") by Simon Cozens (2024-11-26):

> "Taken from the upstream repo https://github.com/CatharsisFonts/Cormorant at commit https://github.com/CatharsisFonts/Cormorant/commit/6d210fd3550b7358ca62d6ba3e354ec1ec940813."

This upstream commit (`6d210fd3`, 2024-11-26) is "Merge pull request #75 from simoncozens/vf-and-gf" -- a merge that added gftools-builder configs, generated Glyphs sources, and pre-built variable fonts for all Cormorant sub-families. Simon Cozens was both the author of the upstream PR and the person who submitted the fonts to google/fonts, so the commit reference is reliable.

The google/fonts commit used the pre-built VFs directly from `fonts/variable/` in the upstream repo (as indicated by the `files {}` block in METADATA.pb), rather than building from sources. After the initial onboarding, the fonts were rebuilt three times by Simon Cozens with babelfont updates:
- `06b080045` (2024-11-26): Rebuild with babelfont 3.1.1
- `72ecfc335` (2024-12-06): Rebuild with babelfont 3.1.2
- `5fcfd99f2` (2025-01-09): Rebuild with babelfont 3.1.2

These rebuilds changed the binary files (from 1,176,628 to 1,195,560 bytes for the Roman VF) but did not alter the METADATA.pb source block.

### Prior Version History

Before the variable font upgrade (Version 4.001), the family had the following history in google/fonts:
1. **v3.301** (2017-01-18): Initial onboarding by Marc Foley (PR #580) -- static fonts
2. **v3.302** (PR #593): Update
3. **v3.303** (PR #636): Update
4. **v4.000** (2022-07-05): gftools-packager update by Marc Foley (PR #4890) at upstream commit `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` -- still static fonts
5. **v4.001** (2024-11-26, merged 2025-01-10): Variable font upgrade by Simon Cozens (PR #8593) at upstream commit `6d210fd3` -- converted to variable fonts

## How Config YAML Was Resolved

The config file `sources/config-garamond.yaml` exists in the upstream repository at the referenced commit `6d210fd3`. It was created as part of PR #75 (simoncozens/vf-and-gf branch) which added gftools-builder configurations for all Cormorant sub-families.

The config file references generated Glyphs sources:
- `sources/generated/CormorantGaramond.glyphs`
- `sources/generated/CormorantGaramond-Italic.glyphs`

Key configuration details:
- `familyName: Cormorant Garamond`
- `axisOrder: [wght, ital]`
- `buildStatic: False`
- `buildWebfont: True`
- Includes STAT table definitions for both Roman and Italic VFs
- Weight axis range: 300 (Light) to 700 (Bold)

No override `config.yaml` exists in the google/fonts family directory (`ofl/cormorantgaramond/`). The `config_yaml` field in METADATA.pb was added by commit `a20b1875` (2025-04-02) by Felipe Sanches, which added source info for all Cormorant sub-families.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-11-26 10:25:37 +0100
- Commit message: "Merge pull request #75 from simoncozens/vf-and-gf"
- Source files at commit: `sources/generated/CormorantGaramond.glyphs`, `sources/generated/CormorantGaramond-Italic.glyphs`, `sources/config-garamond.yaml`
- Binary VFs at commit: `fonts/variable/CormorantGaramond[wght].ttf`, `fonts/variable/CormorantGaramond-Italic[wght].ttf`
- Upstream has 3 newer commits since referenced commit (preparing for release 4.002, fixing ydotbelow/kcaron, fixing Upright udieresiscaron)

## Confidence

**HIGH**: The source block is fully populated and well-evidenced. The repository URL is confirmed by copyright strings, multiple google/fonts commits, and PRs. The commit hash was explicitly stated by Simon Cozens, who both authored the upstream PR #75 and submitted the fonts to google/fonts via PR #8593. The config YAML path points to a valid gftools-builder configuration file at the referenced commit. The only caveat is that the current binary files in google/fonts differ from those at the referenced commit due to post-onboarding babelfont rebuilds, but this is a known and documented discrepancy -- the source block correctly references the original onboarding commit.

## Open Questions

None. The source metadata is complete and well-documented.
