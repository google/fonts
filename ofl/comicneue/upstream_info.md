# Comic Neue - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Comic Neue |
| Designer | Craig Rozynski, Hrant Papazian |
| Repository URL | https://github.com/crozynski/comicneue |
| Commit | `c5ee07b5eebc4cc6347badfad56cb0c705a2e41e` |
| Branch | (not set in METADATA.pb) |
| Config YAML | (not set - override config in google/fonts) |
| Override Config | Yes (`ofl/comicneue/config.yaml`) |
| Date Added | 2020-03-12 |
| License | OFL |

## How URL Found

The repository URL `https://github.com/crozynski/comicneue` was first added to METADATA.pb by Simon Cozens in commit `cd5db6b6e` ("Update upstreams", December 2023). It is also referenced in the copyright string of all font files and was documented in the original onboarding PR #2389.

## How Commit Determined

The commit hash `c5ee07b5eebc4cc6347badfad56cb0c705a2e41e` was added to METADATA.pb by Felipe Sanches in commit `b538f1250` (November 2025), referencing PR #2389.

The onboarding PR #2389 (Font Bakery Dashboard, merged March 2020 by @vv-monsalve) explicitly records this commit in its metadata:

> **commit** c5ee07b5eebc4cc6347badfad56cb0c705a2e41e
> **commitDate** 2020-03-11T23:56:08.000Z
> **repository** https://github.com/crozynski/comicneue

This commit is a merge PR (#18 from vv-monsalve/master) that incorporated contributor file modifications and font file renaming/reorganization.

## Config YAML Status

The upstream repository does **not** have a `config.yaml` file. An override `config.yaml` was created in the google/fonts family directory (`ofl/comicneue/config.yaml`) by Felipe Sanches in commit `b538f1250` (November 2025). The override config contains:

```yaml
buildVariable: false
sources:
  - Sources/Glyphs/ComicNeue_Roman.glyphs
  - Sources/Glyphs/ComicNeue_Italics.glyphs
```

The source paths (`Sources/Glyphs/ComicNeue_Roman.glyphs` and `Sources/Glyphs/ComicNeue_Italics.glyphs`) were verified to exist at the referenced commit in the upstream repository.

Since the override config exists in the google/fonts directory, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block.

## Verification

- **Commit exists in upstream**: Yes - verified in the `master` branch
- **Branch**: Default branch is `master` (not explicitly set in METADATA.pb)
- **Override config references valid sources**: Yes - `Sources/Glyphs/ComicNeue_Roman.glyphs` and `Sources/Glyphs/ComicNeue_Italics.glyphs` both exist at commit `c5ee07b`
- **Font files**: 6 TTF files (Light, Regular, Bold in both Roman and Italic)
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/crozynski/comicneue/`
- **Additional commits exist after onboarding**: Yes - there are ~5 commits after `c5ee07b` on master (file reorganization, gitignore updates, cache clearing) but no source file changes appear relevant

## Confidence Level

**HIGH** - The commit hash is directly confirmed by the onboarding PR #2389 metadata. The repository URL is well-documented. The override config.yaml correctly points to existing source files.

## Open Questions

None. All source data is complete and verified.
