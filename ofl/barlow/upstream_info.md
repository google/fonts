# Barlow

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Jeremy Tribby
**METADATA.pb path**: `ofl/barlow/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/jpt/barlow |
| Commit | `b4726ddf91525818e85e5fce111c285b9273d764` (v1.408 tag) |
| **Config YAML** | Override in google/fonts |
| Branch | N/A (not set in METADATA.pb) |

## How the Repository URL Was Found
The repository URL is documented in the METADATA.pb `source {}` block (added by Simon Cozens in commit 5f2b22f48, 2023-12-14, "Update upstreams"). It is also referenced in the copyright string of the font files.

## How the Commit Hash Was Identified
The METADATA.pb does not include a commit hash. The tracking file has `b4726ddf91525818e85e5fce111c285b9273d764`, which corresponds to the `v1.408` tag in the upstream repo.

Evidence:
- The last TTF update in google/fonts was in commit 89f5431f (2018-12-05, "barlow family updated to v1.408 (#1330) - major fixes")
- PR #1330 was submitted by Jeremy Tribby himself (login: jpt), with body: "This is a few versions ahead now, fixes a number of issues"
- The `v1.408` tag in the upstream repo points to commit `b4726ddf` (2018-11-06, "Fixes #34 and #37")
- The tag date (2018-11-06) predates the google/fonts merge (2018-12-05), which is consistent

## How Config YAML Was Resolved
No `config.yaml` exists anywhere in the upstream repo -- not at the v1.408 commit, not at HEAD. The font was built by the designer using their own build process (likely Glyphs.app export). The repo has `sources/Barlow.glyphs` as the source file.

No override `config.yaml` exists in the google/fonts family directory.

This is a pre-gftools-builder era font that was onboarded with pre-compiled binaries from the upstream repo.

## Verification
- Commit exists in upstream repo: Yes (as tag v1.408)
- Commit date: 2018-11-06 19:54:05 -0800
- Commit message: "Fixes #34 and #37"
- Source files at commit: `sources/Barlow.glyphs`
- Pre-built fonts at commit: `fonts/ttf/`, `fonts/otf/`, `fonts/woff/`, `fonts/woff2/`, `fonts/eot/`, `fonts/gx/`
- TTFs last updated in google/fonts: 2018-12-05 (commit 89f5431f, PR #1330 by jpt)
- No override config.yaml in google/fonts family directory

## Confidence
**High**: The repository URL and commit hash are strongly supported by the tag structure, PR history, and timeline. The missing_config status is accurate -- the upstream repo has never had a config.yaml.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Barlow.glyphs
familyName: Barlow
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions
- Barlow has `.glyphs` sources and could potentially be made buildable with gftools-builder by adding a `config.yaml`. However, this is a complex family with 18 styles (9 weights x 2 italics) and the build configuration would need careful testing.
- The upstream repo has additional commits after v1.408 (up to HEAD at dc2940e2). The latest version appears to be v1.422 (tag exists). The fonts in google/fonts are still at v1.408.
- Note that the Barlow family also includes Barlow Condensed and Barlow Semi Condensed, which are separate families in google/fonts but share the same upstream repo.
