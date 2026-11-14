# Dekko - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Dekko |
| Designer | Sorkin Type |
| Repository URL | https://github.com/EbenSorkin/Dekko |
| Commit Hash | `4887c14997f1158a2a122d4351343e8745a8d504` |
| Branch | (not specified in METADATA.pb) |
| Config YAML | `sources/config.yaml` (in upstream) |
| Status | complete |
| Date Added | 2015-01-28 |

## How URL Found

The repository URL `https://github.com/EbenSorkin/Dekko` was added in commit `c8f729cbd` by Simon Cozens (Jan 14 2024, "Add more upstreams (c,d)"). This is the canonical upstream repository maintained by Eben Sorkin / Sorkin Type.

## How Commit Determined

The commit `4887c14997f1158a2a122d4351343e8745a8d504` was set in commit `19cdcec59` ("Batch 1/4 port info from fontc_crater targets list" by Felipe Sanches, Mar 31 2025). This commit is the HEAD of the upstream repository, representing a merge of PR #12 from SorkinType/dependabot (Bump fonttools from 4.33.3 to 4.43.0).

### Font Binary History

The font binary in google/fonts was last modified in commit `b0235e00e` by Dave Crossland (May 11 2015, "Updating Dekko"). The current font in google/fonts was NOT rebuilt from the current upstream source using gftools-builder. The METADATA.pb source block references HEAD (`4887c14`) with the `config_yaml` pointing to `sources/config.yaml`, which is set up for future rebuilds.

Note: The font binary in google/fonts predates the current upstream repo structure. The upstream was later restructured to have a proper `sources/` directory with `config.yaml` and `.glyphs` source.

## Config YAML Status

- **config.yaml exists in upstream**: `sources/config.yaml` with content:
  ```yaml
  sources:
    - Dekko.glyphs
  familyName: Dekko
  buildVariable: False
  ```
- The `config_yaml` field in METADATA.pb is correctly set to `sources/config.yaml`
- No override config.yaml in google/fonts
- Source file `sources/Dekko.glyphs` exists in the upstream repo

## Verification

- Repository URL is valid and accessible: https://github.com/EbenSorkin/Dekko
- Commit `4887c14` exists in the upstream repo and is HEAD
- The upstream repo is a shallow clone, cached at `upstream_repos/fontc_crater_cache/EbenSorkin/Dekko/`
- The `sources/config.yaml` file exists in the upstream repo at commit `4887c14`
- The source block in METADATA.pb does NOT have `files` mappings or `branch` field, indicating it references the upstream for future rebuilds rather than documenting the original binary source

## Confidence Level

**HIGH** for URL and config_yaml. The upstream is the correct canonical repository with proper gftools-builder configuration.

**MEDIUM** for commit hash. The commit `4887c14` is HEAD and was set for fontc_crater targets. The actual font binary in google/fonts was built from an earlier state of the upstream. However, for the purpose of gftools-builder compatibility, referencing HEAD is appropriate since the font would be rebuilt from the latest sources.

## Open Questions

- The font in google/fonts (last updated 2015) has not been rebuilt from the current upstream sources. A rebuild would update the font to the latest version with potential improvements.
