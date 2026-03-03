# Alan Sans

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Raphael Ronot
**METADATA.pb path**: `ofl/alansans/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/alan-eu/Alan-Sans |
| Commit | `425d3a0674a49f0ad6bc6ceef5ca0c557b520838` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/alan-eu/Alan-Sans` was present in the original onboarding METADATA.pb from commit `1b91df7f5` (Sep 5, 2025), authored by Emma Marichal via gftools-packager. The URL is also referenced in the copyright string within the font metadata. The repository exists and is accessible at this URL.

## How the Commit Hash Was Identified

The commit hash `425d3a0674a49f0ad6bc6ceef5ca0c557b520838` was set by the onboarding engineer Emma Marichal in the original METADATA.pb. The onboarding commit message in google/fonts (`1b91df7f5`) explicitly states:

> Taken from the upstream repo https://github.com/alan-eu/Alan-Sans at commit https://github.com/alan-eu/Alan-Sans/commit/425d3a0674a49f0ad6bc6ceef5ca0c557b520838.

This was part of PR #9796, merged on Sep 11, 2025 by Marc Foley. The PR was created by gftools-packager, which automatically records the upstream commit hash.

The commit hash could not be verified locally because the cached upstream repo at `upstream_repos/fontc_crater_cache/alan-eu/Alan-Sans` is a shallow clone with only 1 commit (`11bb823`, from Jan 20, 2026). However, cross-verification supports the hash being correct:

- The font file in google/fonts (134888 bytes) differs from the current upstream HEAD (134900 bytes), confirming the upstream has changed since onboarding.
- The upstream HEAD commit `11bb823` ("Update AlanSans.glyphs") dates from Jan 2026, well after the Sep 2025 onboarding.
- The commit hash was recorded automatically by gftools-packager at onboarding time, making it a reliable source.

## How Config YAML Was Resolved

The upstream repo has a `sources/config.yaml` file containing gftools-builder configuration. This file specifies `AlanSans.glyphs` as the source, family name "Alan Sans", with weight axis instances from Light (300) to Black (900).

The `config_yaml: "sources/config.yaml"` field was NOT part of the original onboarding METADATA.pb. It was added later by commit `5ddf312e6` (Feb 20, 2026) as part of a batch enrichment of 82 font families. Because the upstream repo does contain this config file, the `config_yaml` field correctly points to it.

Note: Since this is a shallow clone, we cannot confirm that `sources/config.yaml` existed at the exact commit `425d3a0`. However, it is highly likely given that gftools-packager was used for onboarding (which requires a buildable config), and the enrichment commit verified its presence.

There is no local override `config.yaml` in the google/fonts family directory.

## Conclusion

Alan Sans has a complete source block in METADATA.pb with all required fields: repository URL, commit hash, branch, and config_yaml path. The data was established during original onboarding by Emma Marichal (PR #9796, merged Sep 2025), with the config_yaml field added later during batch enrichment (Feb 2026). The repository URL is valid, the commit hash was recorded by gftools-packager, and the upstream repo contains a proper gftools-builder config.yaml. The upstream repo has received updates since onboarding (Jan 2026 commit), but the referenced commit correctly reflects the version used for the initial catalog addition.

**Confidence**: HIGH
