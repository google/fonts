# Bellefair - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bellefair |
| Repository URL | https://github.com/shinntype/bellefair |
| Commit Hash | 879a39cbf0b78b01a14f7f750927a075da4055f8 |
| Config YAML | null (override config.yaml in google/fonts) |
| Status | complete |
| Category | SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/shinntype/bellefair` is documented in the METADATA.pb `source {}` block and also referenced in the copyright string ("Copyright 2015 The Bellefair Project Authors (https://github.com/shinntype/bellefair)"). The URL was populated via the `f7455d788` commit ("Populate source.repository_url") in google/fonts.

## How the Commit Hash Was Determined

The commit hash `879a39cbf0b78b01a14f7f750927a075da4055f8` was added in commit `4c39ef86f` ("sources info for Bellefair: v1.003 (PR #1063)") by Felipe Sanches.

This commit is "Merge pull request #6 from m4rc1e/gf-mastering" in the upstream repo, dated 2017-06-21. The font was onboarded to google/fonts in PR #1063 ("bellefair: v1.003 added", by Marc Foley, merged 2017-06-26). The commit `879a39c` is the latest (HEAD) commit in the upstream repo, and it was a merge of Marc Foley's PR that prepared the font for Google Fonts mastering. The date sequence is correct: the upstream commit (2017-06-21) precedes the google/fonts onboarding commit (2017-06-26).

## Config YAML Status

**No config.yaml exists** in the upstream repository at the recorded commit. The repo structure at `879a39c` is:

```
.gitignore
AUTHORS.txt
CONTRIBUTING.md
CONTRIBUTORS.txt
OFL.txt
README.md
_glyphs/
documentation/
fonts/
sources/
  Bellefair-Regular.vfb
  Bellefair.glyphs
tests/
```

However, an **override config.yaml** exists in the google/fonts family directory at `google/fonts/ofl/bellefair/config.yaml`:

```yaml
buildVariable: false
sources:
  - sources/Bellefair.glyphs
```

This override was added in commit `4c39ef86f` alongside the commit hash. Since the override exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block.

## Verification

- Commit hash `879a39c` exists in the upstream repo and is the HEAD/latest commit
- The upstream repo contains `sources/Bellefair.glyphs` which is the source referenced in the override config.yaml
- PR #1063 in google/fonts added Bellefair v1.003, authored by Marc Foley
- The override config.yaml correctly points to `sources/Bellefair.glyphs`
- The METADATA.pb `source {}` block has repository_url and commit but no config_yaml (correct, since override exists)

## Confidence Level

**High** - The commit hash is the HEAD of the upstream repository, which is also a merge of Marc Foley's GF-mastering PR. Marc Foley is the same person who created the google/fonts PR #1063. The timeline is internally consistent.

## Open Questions

None. This family is fully documented and verified. The override config.yaml approach is appropriate since the upstream repo does not have its own config.yaml.
