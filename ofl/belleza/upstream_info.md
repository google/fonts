# Belleza - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Belleza |
| Repository URL | https://github.com/etunni/belleza |
| Commit Hash | af3974fe84e2cfd236455a14d2c708264b692167 |
| Config YAML | null (override config.yaml in google/fonts) |
| Status | complete |
| Category | SANS_SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/etunni/belleza` is documented in the METADATA.pb `source {}` block and is also referenced in the copyright string ("Copyright 2012 The Belleza Project Authors (https://github.com/etunni/belleza)"). The URL was populated as part of the upstream metadata updates in google/fonts.

## How the Commit Hash Was Determined

The commit hash `af3974fe84e2cfd236455a14d2c708264b692167` was explicitly recorded in the gftools-packager commit in google/fonts (commit `8fecab113`, PR #4770):

> [gftools-packager] Belleza: Version 1.003; ttfautohint (v1.8.4.7-5d5b) added
> Belleza Version 1.003; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/etunni/belleza at commit https://github.com/etunni/belleza/commit/af3974fe84e2cfd236455a14d2c708264b692167.

The PR #4770 body also confirms: "Belleza Version 1.003; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/etunni/belleza at commit https://github.com/etunni/belleza/commit/af3974fe84e2cfd236455a14d2c708264b692167."

Cross-verification: The upstream commit `af3974f` is "Merge pull request #1 from emmamarichal/master", dated 2022-06-10. It is the HEAD/latest commit in the upstream repo. The google/fonts update was made on 2022-06-16 by Emma Marichal. This is consistent: Emma prepared the upstream PR and then submitted the google/fonts update.

## Config YAML Status

**No config.yaml exists** in the upstream repository. The repo structure at `af3974f` is:

```
AUTHOR.txt
CONTRIBUTORS.txt
OFL.txt
README.md
documentation/
fonts/
old/
requirements.txt
sources/
  Belleza.glyphs
```

An **override config.yaml** exists in the google/fonts family directory at `google/fonts/ofl/belleza/config.yaml`:

```yaml
buildVariable: false
sources:
  - sources/Belleza.glyphs
```

This override was originally auto-generated (commit `3b645f8db`, "Adding 119 automatically generated config.yaml files") and later updated (commit `072f204fd`, "sources info for Belleza: Version 1.003 (PR #4770)") to add the `buildVariable: false` flag. Since the override exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block.

## Verification

- Commit hash `af3974f` exists in the upstream repo and is the HEAD/latest commit
- The upstream repo contains `sources/Belleza.glyphs` which is the source referenced in the override config.yaml
- PR #4770 in google/fonts explicitly references this commit hash (both in commit message and PR body)
- The override config.yaml correctly points to `sources/Belleza.glyphs`
- The METADATA.pb has a `files {}` mapping that references `fonts/ttf/Belleza-Regular.ttf` and `OFL.txt`
- The METADATA.pb `source {}` block has repository_url and commit but no config_yaml (correct, since override exists)

## Confidence Level

**High** - The gftools-packager commit and PR #4770 both explicitly reference this exact commit hash. The upstream commit is the HEAD commit, and the timeline (upstream merge 2022-06-10, google/fonts update 2022-06-16) is internally consistent. Both were handled by Emma Marichal.

## Open Questions

None. This family is fully documented and verified.
