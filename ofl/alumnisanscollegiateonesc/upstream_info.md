# Alumni Sans Collegiate One SC

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: missing_config
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/alumnisanscollegiateonesc/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/alumni-sans-collegiate |
| Commit | `9dc96be1ead732fb1677c88632665e0bbf2e4ee2` |
| Config YAML | `sources/config.yml` (set in METADATA.pb, but see notes below) |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/alumni-sans-collegiate` is already recorded in the METADATA.pb `source {}` block. It was confirmed by the onboarding commit in google/fonts (`9b0b4fda4`, 2024-05-27) and PR #7769, both of which explicitly reference this upstream repository. The repo is cached at `googlefonts/alumni-sans-collegiate` and is accessible.

## How the Commit Hash Was Identified

The commit hash `9dc96be1ead732fb1677c88632665e0bbf2e4ee2` was explicitly stated in:

1. The google/fonts onboarding commit message (`9b0b4fda4`): "Taken from the upstream repo https://github.com/googlefonts/alumni-sans-collegiate at commit https://github.com/googlefonts/alumni-sans-collegiate/commit/9dc96be1ead732fb1677c88632665e0bbf2e4ee2."
2. PR #7769 body, authored by Simon Cozens (`simoncozens`), merged 2024-05-30.
3. The METADATA.pb `source {}` block.

The upstream repository has only a single commit (`9dc96be`, dated 2022-06-30), which is also HEAD. This means there is no ambiguity about the commit -- it is the only one in the repository, and it was correctly referenced during onboarding.

## How Config YAML Was Resolved

The METADATA.pb `source {}` block sets `config_yaml: "sources/config.yml"`. This file exists at the referenced commit and contains:

```yaml
sources:
  - AlumniSansCollegiate.glyphs
  - AlumniSansCollegiate-Italic.glyphs
familyName: "Alumni Sans Collegiate One"
buildVariable: false
autohintTTF: false
```

**Critical issue**: This config builds the **non-SC** family "Alumni Sans Collegiate One", not the SC variant. The `familyName` is set to "Alumni Sans Collegiate One", and building with this config produces `AlumniSansCollegiateOne-Regular.ttf` and `AlumniSansCollegiateOne-Italic.ttf` -- the non-SC fonts.

The SC variant ("Alumni Sans Collegiate One SC") is derived from the same Glyphs sources, which contain extensive `.sc` (small caps) glyphs and OpenType `smcp`/`c2sc` features. However, the SC fonts were not pre-built in the upstream repository. At commit `9dc96be`, the only TTF files present are the non-SC variants under `fonts/ttf/`.

The METADATA.pb `source.files` mapping references `fonts/ttf/AlumniSansCollegiateOneSC-Regular.ttf` and `fonts/ttf/AlumniSansCollegiateOneSC-Italic.ttf`, but these files **do not exist** at the referenced commit in the upstream repo. The SC fonts were produced during the onboarding process (likely by gftools-packager with a custom build configuration), not pulled directly from the upstream repo.

There is no override `config.yaml` in the google/fonts family directory (`ofl/alumnisanscollegiateonesc/`).

### What would be needed

To rebuild the SC variant from sources, a separate config.yaml would be needed that:
- References the same Glyphs sources (`AlumniSansCollegiate.glyphs` and `AlumniSansCollegiate-Italic.glyphs`)
- Sets `familyName: "Alumni Sans Collegiate One SC"` or uses appropriate small-caps extraction settings
- Configures the build to produce only the small-caps subset of glyphs

## Additional Notes

- **Sibling family**: This repo also hosts "Alumni Sans Collegiate One" (non-SC), which lives at `ofl/alumnisanscollegiateone/`. The non-SC family was onboarded earlier (2022-04-09) via PR #4855, while the SC variant was added later (2024-05-27) via PR #7769.
- **Same commit**: Both families reference the same upstream commit `9dc96be`, which is the only commit in the repository.
- **Source file mapping issue**: The `source.files` entries for the SC TTFs point to paths that don't exist in the upstream repo. The fonts were generated during onboarding, not extracted from pre-built files.
- **Designer**: Robert Leuschke (Robert E. Leuschke), with contributions from Viviana Monsalve who made the single upstream commit.
- The `config_yaml` field in METADATA.pb points to a config that builds the wrong family (non-SC). This needs correction -- either an override config.yaml for the SC build, or the `config_yaml` field should be removed/corrected.

## Conclusion

**Confidence: HIGH** for repository URL and commit hash. The upstream repo URL and commit are well-documented and unambiguous (single-commit repo, explicitly referenced in onboarding).

**Status: missing_config** -- The `config_yaml` field in METADATA.pb (`sources/config.yml`) points to a config that builds the non-SC family "Alumni Sans Collegiate One", not the SC variant. An override `config.yaml` specific to the SC build would need to be created in the google/fonts family directory to properly rebuild this family from sources. The `source.files` TTF paths also don't exist in the upstream repo at the referenced commit.
