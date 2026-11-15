# Castoro Titling

**Date investigated**: 2026-09-27
**Status**: complete
**Model**: Claude Opus 5.5
**METADATA.pb path**: `ofl/castorotitling/METADATA.pb`

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/TiroTypeworks/Castoro |
| Commit | `4a1cb086e613f8a731229f78f4996982349e3f3b` |
| Config YAML | `googlefonts/sources/config-castoro-titling.yaml` (upstream) |
| Branch | `master` |
| Confidence | HIGH |

## Initial state

- Commit `3e6c5547a` (PR #10954, merged 2026-09-11) updated Castoro Titling to Version 3.000 from upstream commit `4a1cb086` and mapped the TTF from `googlefonts/fonts/ttf/CastoroTitling-Regular.ttf`.
- The source block had no `config_yaml`, and `ofl/castorotitling/` had no override `config.yaml`.
- The earlier investigation below described the v2.04 onboarding (commit `58a386a9`) and no longer matched the shipped font.

## Actions taken

- Verified the commit. The shipped TTF, OFL.txt and DESCRIPTION.en_us.html are byte-identical to the files at `4a1cb086`. The TTF was added at `googlefonts/fonts/ttf/` in `3b008989` (2026-08-27); `3b008989..4a1cb086` and the one later upstream commit (`85646cf1`, 2026-09-18) change only `googlefonts/requirements.txt`. The gftools-packager commit message and the PR #10954 body name the same commit.
- Located the upstream gftools-builder config `googlefonts/sources/config-castoro-titling.yaml` (source `CastoroTitling-Regular.ufo`, next to the config), which `googlefonts/sources/build.sh` runs. The top-level `source/` and `fonts/` directories hold Tiro's own v3.01 release (the files of tag `v3.01`), which Google Fonts does not ship.
- Build-tested the config at `4a1cb086`:
  - gftools-builder3 (fontc): built. Functional gate PASS on all seven checks (491 codepoints exact, 0 of 1640831 shaping runs differ, 0 of 408 advances differ; 261 glyphs store their outlines differently but draw the same ink). The build is unhinted where the release is ttfautohinted, and name ID 5 and `head.flags` differ.
  - Python gftools builder: identical to the shipped TTF in every table except `head` created/modified/checkSumAdjustment.
- Added `config_yaml: "googlefonts/sources/config-castoro-titling.yaml"` to the source block. No override config.yaml was needed.

## Final state

METADATA.pb records the repository, the verified commit and the upstream config. Built with the Python gftools builder, that config reproduces the shipped TTF apart from the `head` timestamps and checksum.

## Earlier investigation (2026-02-26, superseded)

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Tiro Typeworks, John Hudson
**METADATA.pb path**: `ofl/castorotitling/METADATA.pb`

### Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/TiroTypeworks/Castoro |
| Commit | `58a386a96e522b6d47c566175c7ee799d4c8d14f` |
| Config YAML | Missing (no override, no upstream config.yaml) |
| Branch | `master` |

### How the Repository URL Was Found

The repository URL `https://github.com/TiroTypeworks/Castoro` was set in the METADATA.pb `source { repository_url }` field. The gftools-packager commit `f5655f1b8` (2023-03-15, author: Viviana Monsalve) states: "Castoro Titling Version 2.04 taken from the upstream repo https://github.com/TiroTypeworks/Castoro at commit https://github.com/TiroTypeworks/Castoro/commit/58a386a96e522b6d47c566175c7ee799d4c8d14f."

Castoro Titling shares the same upstream repository as Castoro (the regular text family). Both families are produced from the same repo.

### How the Commit Hash Was Identified

The commit hash `58a386a96e522b6d47c566175c7ee799d4c8d14f` was specified in the gftools-packager commit message (`f5655f1b8`, date: 2023-03-15). This is the same commit used for the Castoro text family, which is expected since both are in the same repo.

Cross-verification: The upstream commit `58a386a9` has the message "v2.04 (update UFOs)", authored by tiroj on 2023-03-15. The gftools-packager commit says "Castoro Titling: Version 2.04 added", matching precisely. The METADATA.pb file mappings confirm: `source_file: "fonts/CastoroTitling/TTF/CastoroTitling-Regular.ttf"` maps to `dest_file: "CastoroTitling-Regular.ttf"`, and this font file exists at the recorded commit.

### How Config YAML Was Resolved

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

### Verification

- Commit exists in upstream repo: Yes
- Commit date: 2023-03-15
- Commit message: "v2.04 (update UFOs)"
- Commit author: tiroj (John Hudson)
- Source file at commit: `source/CastoroTitling-Regular.ufo`
- Override config.yaml in google/fonts: No
- Upstream config at commit: `castoro.yml` (combined, includes titling)
- Upstream config at HEAD: `castoro-titling.yml` (standalone for titling)
- Font was added to Google Fonts on 2023-03-15

### Confidence Level

**HIGH** for repository URL and commit hash -- both are confirmed by the gftools-packager commit message and cross-verified against the upstream repository.

**NEEDS ACTION** for config.yaml -- an override config.yaml needs to be created for Castoro Titling.

### Open Questions

- An override `config.yaml` is needed for the `ofl/castorotitling/` directory. A suitable config would reference `source/CastoroTitling-Regular.ufo` as the source. Example:
  ```yaml
  sources:
    - source/CastoroTitling-Regular.ufo
  ```
- The upstream repo has a `castoro-titling.yml` at HEAD that could serve as a reference, but it uses v3.01 sources. For the recorded v2.04 commit, the UFO file path should work.
- The upstream has progressed to v3.01 since the recorded commit. Same consideration as for Castoro text family applies here.
