# Crimson Pro - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Crimson Pro |
| Designer | Jacques Le Bailly |
| Repository URL | https://github.com/Fonthausen/CrimsonPro |
| Commit | `24e8f7bf59ec45d77c67879ad80d97e5f94c787b` |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Status | complete |

## How URL Found

The repository URL `https://github.com/Fonthausen/CrimsonPro` is referenced in:
- The font copyright string: "Copyright 2018 The Crimson Pro Project Authors (https://github.com/Fonthausen/CrimsonPro)"
- The DESCRIPTION.en_us.html file
- PR #3632 by Aaron Bell mentions his fork at `https://github.com/aaronbell/CrimsonPro` but the canonical upstream is Fonthausen/CrimsonPro

The URL was first added to METADATA.pb source block in commit `cd5db6b6e` by Simon Cozens on 2023-12-14 ("Update upstreams").

## How Commit Determined

The commit hash `24e8f7bf59ec45d77c67879ad80d97e5f94c787b` was added in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list") by Felipe Sanches, ported from the fontc_crater targets.json file.

This commit is the HEAD of the Fonthausen/CrimsonPro repository, which is a merge commit from 2022-08-30: "Merge pull request #5 from rschiang/normalize-build". It introduces zero changes relative to the previous commit `f21e0a4` (Aaron Bell's merge from 2021-09-01), so the font sources at this commit are identical to those used for the last google/fonts update.

### Font update history in google/fonts:
1. `cd20fc29b` - crimsonpro: v1.000 added (#1779) - initial addition
2. `01204e1f0` - crimsonpro: v1.002 added
3. `5c70a7919` - CrimsonPro v1.003 (stat fix) (#3632) - by Aaron Bell, converted to UFR and rebuilt
4. `76adaf1d2` - deploy commit (re-added files, no content change)

The last meaningful font update was PR #3632 by Aaron Bell, who rebuilt the fonts after converting to UFR format. His work was merged into the upstream repo as commit `f21e0a4`, and the subsequent commit `24e8f7b` (normalize-build) introduced no source changes.

## Config YAML Status

The `sources/config.yaml` file exists in the upstream repo at the referenced commit. It is a valid gftools-builder configuration specifying:
- Sources: `CrimsonPro.glyphs`, `CrimsonPro-Italic.glyphs`
- Axis order: wght, ital
- Family name: "Crimson Pro"
- STAT table configuration

No override config.yaml exists in the google/fonts family directory.

## Verification

- **Repository URL**: Verified accessible, correct upstream for this font
- **Commit hash**: Exists in repo, is HEAD. Sources unchanged since the actual font build commit
- **Config YAML**: Present at `sources/config.yaml`, valid gftools-builder format
- **Upstream cache**: Present at `upstream_repos/fontc_crater_cache/Fonthausen/CrimsonPro/`

## Confidence Level

**HIGH** - All data verified. The commit hash points to HEAD which has identical source files to the commit used for the last font update.

## Open Questions

None.
