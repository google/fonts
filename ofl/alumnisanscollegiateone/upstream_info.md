# Alumni Sans Collegiate One

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/alumnisanscollegiateone/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/alumni-sans-collegiate |
| Commit | `9dc96be1ead732fb1677c88632665e0bbf2e4ee2` |
| Config YAML | `sources/config.yml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source {}` block, set to `https://github.com/googlefonts/alumni-sans-collegiate`. This was confirmed by:

1. The google/fonts commit `0df02275b` (initial onboarding, PR #4489, April 2022) explicitly references the same upstream repo URL in its gftools-packager message.
2. The google/fonts commit `87033c631` (version 1.100 update, PR #4855, July 2022) also references the same repo URL.
3. The cached repo at `googlefonts/alumni-sans-collegiate` has its remote set to `https://github.com/googlefonts/alumni-sans-collegiate`.
4. The copyright string in METADATA.pb references the same GitHub URL.

## How the Commit Hash Was Identified

The commit hash `9dc96be1ead732fb1677c88632665e0bbf2e4ee2` was already recorded in the METADATA.pb source block. Verification:

1. **Commit exists in upstream repo**: Confirmed. The commit is authored by Viviana Monsalve on 2022-06-30 with message "sample image updated". This is the only commit in the repository -- it is the initial commit that added all files.
2. **Referenced in google/fonts**: The gftools-packager commit `87033c631` (PR #4855) explicitly states: "Alumni Sans Collegiate One Version 1.100 taken from the upstream repo ... at commit 9dc96be1ead732fb1677c88632665e0bbf2e4ee2".
3. **Binary file size match**: The TTF files at commit `9dc96be` in the upstream repo exactly match the files in google/fonts:
   - `AlumniSansCollegiateOne-Regular.ttf`: 163,484 bytes (both locations)
   - `AlumniSansCollegiateOne-Italic.ttf`: 173,756 bytes (both locations)
4. **Only commit in repo**: Since this is the sole commit in the upstream repository, there is no ambiguity about which commit was used.

## How Config YAML Was Resolved

The config file exists in the upstream repo at `sources/config.yml` and is referenced in METADATA.pb via `config_yaml: "sources/config.yml"`. The config was present at commit `9dc96be` (the only commit) and contains:

```yaml
sources:
  - AlumniSansCollegiate.glyphs
  - AlumniSansCollegiate-Italic.glyphs
familyName: "Alumni Sans Collegiate One"
buildVariable: false
autohintTTF: false
```

The source files referenced in the config (`AlumniSansCollegiate.glyphs` and `AlumniSansCollegiate-Italic.glyphs`) are present in the `sources/` directory. No override config.yaml exists in the google/fonts family directory.

**Note**: This config specifies `familyName: "Alumni Sans Collegiate One"`, which means it only builds the non-SC variant. The sibling family "Alumni Sans Collegiate One SC" shares the same upstream repository but would need a separate config to build the small caps variant (the SC fonts are likely produced from the same `.glyphs` sources using a different family name filter or separate build step).

## Sibling Family

This upstream repo also hosts **Alumni Sans Collegiate One SC**, which shares the same repository URL and commit hash. The SC variant was onboarded in a separate google/fonts commit (`9b0b4fda4`).

## Conclusion

This family is **fully documented** with high confidence. The repository URL, commit hash, branch, and config.yaml path are all correctly recorded in METADATA.pb. The commit hash is verified both by explicit reference in the gftools-packager commit message (PR #4855) and by exact binary file size matching. The upstream repo contains only a single commit, eliminating any ambiguity.

**Confidence: HIGH**
