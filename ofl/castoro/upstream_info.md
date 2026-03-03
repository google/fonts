# Castoro

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Tiro Typeworks, John Hudson, Paul Hanslow, Kaja Slojewska
**METADATA.pb path**: `ofl/castoro/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/TiroTypeworks/Castoro |
| Commit | `58a386a96e522b6d47c566175c7ee799d4c8d14f` |
| Config YAML | Override in google/fonts family directory |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/TiroTypeworks/Castoro` was set in the METADATA.pb `source { repository_url }` field. The gftools-packager commit `aaaa055f9` (2023-03-15, author: Viviana Monsalve) states: "Castoro Version 2.04 taken from the upstream repo https://github.com/TiroTypeworks/Castoro at commit https://github.com/TiroTypeworks/Castoro/commit/58a386a96e522b6d47c566175c7ee799d4c8d14f." The copyright in the font files also references this URL.

## How the Commit Hash Was Identified

The commit hash `58a386a96e522b6d47c566175c7ee799d4c8d14f` was specified in the gftools-packager commit message (`aaaa055f9`, date: 2023-03-15).

Cross-verification: The upstream commit `58a386a9` in TiroTypeworks/Castoro has the message "v2.04 (update UFOs)", authored by tiroj (John Hudson) on 2023-03-15. The gftools-packager commit says "Version 2.04 added" -- the version numbers match. The commit date also matches the google/fonts onboarding date, suggesting the fonts were packaged and onboarded on the same day the upstream commit was made.

The METADATA.pb `source {}` block includes explicit file mappings (e.g., `source_file: "fonts/Castoro/TTF/Castoro-Regular.ttf"` to `dest_file: "Castoro-Regular.ttf"`), confirming that the binary TTF files were taken directly from the upstream's `fonts/` directory at this commit.

## How Config YAML Was Resolved

At the recorded commit (`58a386a9`), the upstream repo has a `castoro.yml` file (not named `config.yaml`). This file is a gftools-builder configuration that lists all three sources (Castoro-Regular.ufo, Castoro-Italic.ufo, CastoroTitling-Regular.ufo). However, it uses older gftools-builder conventions.

An override `config.yaml` was created in the google/fonts family directory (`ofl/castoro/config.yaml`) as part of the enrichment commit `5ddf312e6` (2026-02-20). The override references designspace files that exist at HEAD of the upstream repo (v3.01), not at the recorded commit:

```yaml
sources:
  - source/Castoro-Roman.designspace
  - source/Castoro-Italic.designspace
```

Note: At the recorded commit (`58a386a9`), the sources are UFO files (`source/Castoro-Regular.ufo`, `source/Castoro-Italic.ufo`), not designspace files. The designspace files only exist in the newer v3.x versions of the upstream repo. Since an override config exists in google/fonts, the `config_yaml` field is correctly omitted from METADATA.pb.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2023-03-15
- Commit message: "v2.04 (update UFOs)"
- Commit author: tiroj (John Hudson)
- Source files at commit: `source/Castoro-Regular.ufo`, `source/Castoro-Italic.ufo`, `source/CastoroTitling-Regular.ufo`
- Override config.yaml in google/fonts: Yes
- Upstream has progressed: Yes (to v3.01, with significant restructuring)
- Font was added to Google Fonts originally on 2020-11-03 (v1.x), updated to v2.04 on 2023-03-15

## Confidence Level

**HIGH** -- The commit hash is confirmed by the gftools-packager commit message. The version number and date match between google/fonts and the upstream commit. The file mappings in METADATA.pb further confirm the correct commit.

## Open Questions

- The override `config.yaml` references `source/Castoro-Roman.designspace` and `source/Castoro-Italic.designspace`, which are designspace files from the v3.x upstream, not from the recorded v2.04 commit. If the family were to be rebuilt from the recorded commit, the config would need to reference the UFO files instead. This discrepancy should be addressed if a rebuild from the recorded commit is ever needed.
- The upstream repo has progressed to v3.01, which represents a significant update (added weight axis). A separate review/update process would be needed to incorporate v3.x into Google Fonts.
