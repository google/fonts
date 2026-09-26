# Chokokutai - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Chokokutai |
| Repository URL | https://github.com/go108go/Chokokutai |
| Commit Hash | `55016eef4cfaf7d9001eeaa64ad5a0a0f20a67c7` |
| Branch | `master` |
| Config YAML | N/A (override in google/fonts) |
| Override Config | Yes (`ofl/chokokutai/config.yaml`) |
| Designer | Font Zone 108 |
| License | OFL |
| Date Added | 2020-12-14 |

## How URL Found

The repository URL `https://github.com/go108go/Chokokutai` was set in the upstream.yaml file when the family was onboarded via PR #2874 (commit `9c80bcb86`), and later migrated to the METADATA.pb source block. Both the onboarding commit message and the PR body confirm this URL.

## How Commit Determined

The commit hash `55016eef4cfaf7d9001eeaa64ad5a0a0f20a67c7` is explicitly stated in the merge commit message of google/fonts PR #2874 (commit `9c80bcb86`):

> "Chokokutai Version 1.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/go108go/Chokokutai.git at commit https://github.com/go108go/Chokokutai/commit/55016eef4cfaf7d9001eeaa64ad5a0a0f20a67c7."

Note: The original PR body mentioned an earlier commit `fee1e58664551731f5546bf33637f76fe5fe0851`, but the final merged commit uses `55016ee`. Checking the upstream repo, `55016ee` ("Fixing copyright string") is one commit ahead of `fee1e58` ("Update DESCRIPTION.en_us.html"), indicating a last-minute fix was included before the merge.

The commit was verified to exist in the local upstream clone on the `master` branch.

## Config YAML Status

The upstream repository does NOT have a `config.yaml` file. Instead, an override `config.yaml` exists in the google/fonts family directory at `ofl/chokokutai/config.yaml`. This override is a minimal configuration:

```yaml
buildVariable: false
sources:
  - sources/Chokokutai.glyphs
```

Since the override exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects the local override).

## Verification

- Repository URL is valid and accessible
- Commit `55016ee` exists in the upstream repo on the `master` branch
- The commit is by Aaron Bell (2020-12-08), with message "Fixing copyright string"
- The override `config.yaml` exists at `ofl/chokokutai/config.yaml` in google/fonts
- The METADATA.pb source block correctly has no `config_yaml` field (override is used)
- Font binary `fonts/ttf/Chokokutai-Regular.ttf` exists at the referenced commit

## Confidence Level

**HIGH** - All data is fully verified. The commit hash is confirmed by the google/fonts merge commit message and verified in the upstream repo. The override config.yaml is properly set up.

## Open Questions

None. The data is complete and verified.
