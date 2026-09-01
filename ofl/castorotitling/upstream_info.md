# Castoro Titling

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Tiro Typeworks, John Hudson
**METADATA.pb path**: `ofl/castorotitling/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/TiroTypeworks/Castoro |
| Commit | `58a386a96e522b6d47c566175c7ee799d4c8d14f` |
| Config YAML | Missing (no override, no upstream config.yaml) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/TiroTypeworks/Castoro` was set in the METADATA.pb `source { repository_url }` field. The gftools-packager commit `f5655f1b8` (2023-03-15, author: Viviana Monsalve) states: "Castoro Titling Version 2.04 taken from the upstream repo https://github.com/TiroTypeworks/Castoro at commit https://github.com/TiroTypeworks/Castoro/commit/58a386a96e522b6d47c566175c7ee799d4c8d14f."

Castoro Titling shares the same upstream repository as Castoro (the regular text family). Both families are produced from the same repo.

## How the Commit Hash Was Identified

The commit hash `58a386a96e522b6d47c566175c7ee799d4c8d14f` was specified in the gftools-packager commit message (`f5655f1b8`, date: 2023-03-15). This is the same commit used for the Castoro text family, which is expected since both are in the same repo.

Cross-verification: The upstream commit `58a386a9` has the message "v2.04 (update UFOs)", authored by tiroj on 2023-03-15. The gftools-packager commit says "Castoro Titling: Version 2.04 added", matching precisely. The METADATA.pb file mappings confirm: `source_file: "fonts/CastoroTitling/TTF/CastoroTitling-Regular.ttf"` maps to `dest_file: "CastoroTitling-Regular.ttf"`, and this font file exists at the recorded commit.

## How Config YAML Was Resolved

**Config.yaml is missing.** Neither the upstream repository nor the google/fonts family directory has a `config.yaml` for Castoro Titling.

At the recorded commit (`58a386a9`), the upstream repo has a `castoro.yml` file that includes `CastoroTitling-Regular` as one of its builds (alongside Castoro Regular and Italic). However, this is a combined config for all Castoro families, not a standalone config for Titling.

At HEAD of the upstream repo, there is a `castoro-titling.yml` file with a standalone config for just Castoro Titling:

```yaml
names:
  5: Version 3.01

meta:
  slng: [Latn]
  dlng: [Latn]

fonts:
  CastoroTitling-Regular:
    source: source/CastoroTitling-Regular.ufo
```

An override `config.yaml` exists for the regular Castoro family (`ofl/castoro/config.yaml`), but no override was created for Castoro Titling (`ofl/castorotitling/config.yaml` does not exist).

The source for Castoro Titling at the recorded commit is a single UFO: `source/CastoroTitling-Regular.ufo`.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2023-03-15
- Commit message: "v2.04 (update UFOs)"
- Commit author: tiroj (John Hudson)
- Source file at commit: `source/CastoroTitling-Regular.ufo`
- Override config.yaml in google/fonts: No
- Upstream config at commit: `castoro.yml` (combined, includes titling)
- Upstream config at HEAD: `castoro-titling.yml` (standalone for titling)
- Font was added to Google Fonts on 2023-03-15

## Confidence Level

**HIGH** for repository URL and commit hash -- both are confirmed by the gftools-packager commit message and cross-verified against the upstream repository.

**NEEDS ACTION** for config.yaml -- an override config.yaml needs to be created for Castoro Titling.

## Open Questions

- An override `config.yaml` is needed for the `ofl/castorotitling/` directory. A suitable config would reference `source/CastoroTitling-Regular.ufo` as the source. Example:
  ```yaml
  sources:
    - source/CastoroTitling-Regular.ufo
  ```
- The upstream repo has a `castoro-titling.yml` at HEAD that could serve as a reference, but it uses v3.01 sources. For the recorded v2.04 commit, the UFO file path should work.
- The upstream has progressed to v3.01 since the recorded commit. Same consideration as for Castoro text family applies here.
