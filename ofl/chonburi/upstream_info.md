# Chonburi - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Chonburi |
| Designer | Cadson Demak |
| Repository URL | https://github.com/cadsondemak/chonburi |
| Commit Hash | `1c6599a6ae44a2d30ff3ee44d015ffab2c0cb014` |
| Config YAML | Override in google/fonts (`ofl/chonburi/config.yaml`) |
| Status | Complete |
| Date Added | 2015-07-08 |

## How URL Found

The repository URL `https://github.com/cadsondemak/chonburi` was already recorded in the METADATA.pb source block. It was added as part of earlier source documentation efforts (commit `c8f729cbd` "Add more upstreams (c,d)").

## How Commit Determined

The commit `1c6599a` ("push final font and source files", dated 2015-07-03) was identified by correlating the upstream repository history with the google/fonts onboarding commit `f2bdc7d83` ("Adding Chonburi", dated 2015-07-06 by Dave Crossland). The upstream commit is 3 days before the google/fonts addition, and the commit message "push final font and source files" strongly indicates it was the preparation commit for onboarding.

This is the only commit in the upstream repo within the relevant time window (checked with `--after=2015-07-01 --before=2015-07-07`).

The commit hash was verified to exist in the upstream repository.

## Config YAML Status

- **No config.yaml in upstream**: The cadsondemak/chonburi repository does not contain a config.yaml file at any commit.
- **Override config.yaml exists**: An override `config.yaml` is present in `ofl/chonburi/config.yaml` in the google/fonts repository.

Override config.yaml contents:
```yaml
buildVariable: false
sources:
  - source/Chonburi-Regular.ufo
```

The source path `source/Chonburi-Regular.ufo` matches the file structure at the recorded commit, which contains the UFO source at that path.

## Verification

- Commit hash `1c6599a` verified to exist in upstream repo
- Source file `source/Chonburi-Regular.ufo` confirmed present at the recorded commit
- Timeline is consistent: upstream commit (2015-07-03) precedes google/fonts addition (2015-07-06)
- Override config.yaml correctly references the UFO source

## Confidence Level

**High** - The commit hash, repository URL, and override config.yaml are all consistent and verified.

## Open Questions

None.
