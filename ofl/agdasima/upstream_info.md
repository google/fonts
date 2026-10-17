# Agdasima

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: The DocRepair Project, Patric King
**METADATA.pb path**: `ofl/agdasima/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/docrepair-fonts/agdasima-fonts |
| Commit | `c971400d774dfd6d28e7a8e34aedc3b3dfdce6f9` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb source block, established during the gftools-packager onboarding. The copyright field in the font binary references the same URL: "The Agdasima Project Authors (https://github.com/docrepair-fonts/agdasima-fonts)." Multiple google/fonts commits confirm this URL, including PR #6249 and the final font update commit `92ba10a48`.

## How the Commit Hash Was Identified

The commit hash `c971400d` was set during the font onboarding and has remained unchanged:

1. **Font update** (google/fonts commit `92ba10a48`, 2023-06-14): The gftools-packager commit body states: "Agdasima Version 2.002 taken from the upstream repo https://github.com/docrepair-fonts/agdasima-fonts at commit c971400d774dfd6d28e7a8e34aedc3b3dfdce6f9."

2. **PR #6249**: The PR body initially referenced a different commit `ccbf4bfc6fc6c99bd6086d5fc7eff951f88b1bdf`, but the final squashed commit used `c971400d`. This is consistent with the PR branch being updated after the initial push.

3. **Batch port** (google/fonts commit `19cdcec59`, 2025-03-31): Only added `config_yaml: "sources/config.yaml"` -- did NOT change the commit hash, confirming the fontc_crater target also had the same commit.

The commit hash is well-corroborated: the google/fonts commit body, the METADATA.pb, and the fontc_crater data all agree on `c971400d`.

## How Config YAML Was Resolved

The `sources/config.yaml` path was added by the batch port commit `19cdcec59` (2025-03-31). The config file exists at the recorded commit in the upstream repo and specifies:
- Source: `Agdasima-Regular.designspace`
- Family name: Agdasima
- `buildOTF: false`, `buildVariable: false`, `buildWebfont: false`
- Output directory: `../fonts`

No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is HEAD of the shallow clone, matching the onboarding commit)
- Commit date: 2023-06-14 17:07:16 +0200
- Commit message: "New fonts"
- Source files at commit:
  - `sources/Agdasima-Regular.designspace`
  - `sources/config.yaml`
  - `sources/masters/Agdasima-Bold.ufo/` (with many .glif files)
  - `sources/masters/Agdasima-Regular.ufo/` (implied by designspace)
  - `.github/workflows/build.yaml`
  - `packager.yaml`

## Confidence

**High**: All three data points are strongly corroborated. The commit hash `c971400d` is confirmed by the gftools-packager commit message in google/fonts, the METADATA.pb, and the fontc_crater data. The commit date (2023-06-14 17:07:16) is within seconds of the google/fonts onboarding commit (2023-06-14 17:07:44), providing strong temporal correlation that this is the correct onboarding commit. The config.yaml and source files are verified to exist at this commit.

## Open Questions

None. This is a straightforward, well-documented onboarding with consistent references across all sources.
