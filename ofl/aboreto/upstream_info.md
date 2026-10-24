# Aboreto

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Dominik Jager
**METADATA.pb path**: `ofl/aboreto/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/domija/Aboreto |
| Commit | `6e64ee7e7ff1c53220d96b88a8d4bf2db9f76735` |
| Config YAML | override in google/fonts |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field: `https://github.com/domija/Aboreto`. This URL is also referenced in the font copyright string: "Copyright 2022 The Aboreto Project Authors (https://github.com/domija/Aboreto)". The URL was merged into METADATA.pb via commit `66f91f10f` ("Merge upstream.yaml into METADATA.pb").

## How the Commit Hash Was Identified

The commit hash `6e64ee7e7ff1c53220d96b88a8d4bf2db9f76735` was pre-existing in the METADATA.pb `source { commit }` field. This commit is part of a chain related to PR #4832 in google/fonts.

**Detailed commit chain analysis**:
- The last font-modifying commit in google/fonts is `4aa5ca44f692` from 2022-07-01, with message "[gftools-packager] Aboreto: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added (#4832)".
- The merge commit body of `4aa5ca44` states: "taken from the upstream repo https://github.com/domija/Aboreto at commit https://github.com/domija/Aboreto/commit/07795db7fb5cf9029f1bac1ae0b130bbae6c5feb".
- However, the PR #4832 body text references a different (earlier) commit: `1423a732a34d080e360e8771ae9aca3de47ced31`.
- In the upstream repo, the commit history shows: `1423a73` ("Merge pull request #3") -> `6e64ee7` ("V-metrics updated") -> `07795db` ("Merge pull request #4"). So `6e64ee7` is the actual content commit that was part of upstream PR #4, and `07795db` is its merge commit.
- The METADATA.pb references `6e64ee7`, which is the content commit within the merge. This is a reasonable and correct reference.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repo at commit `6e64ee7`. An override `config.yaml` exists in the google/fonts family directory at `ofl/aboreto/config.yaml`. Its contents:

```yaml
buildVariable: false
sources:
  - sources/Aboreto.glyphs
```

The upstream repo at this commit has a `.glyphs` source file at `sources/Aboreto.glyphs`. The override config correctly points to this file and specifies a static-only build.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-06-24 15:30:44 +0200
- Commit message: "V-metrics updated"
- Source files at commit: `sources/Aboreto.glyphs`, `old/sources/Aboreto-Regular.ufo` (legacy)

## Confidence

**High**: The repository URL is confirmed by both METADATA.pb and the font copyright string. The commit hash is pre-existing in METADATA.pb and is corroborated by the google/fonts PR #4832 merge commit body, which references the merge commit (`07795db`) that includes this content commit (`6e64ee7`). The override config.yaml correctly references the upstream source file.

## Open Questions

None. This family is fully documented with consistent evidence across METADATA.pb, google/fonts commit history, and the upstream repository.
