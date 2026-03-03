# Abhaya Libre

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Mooniak
**METADATA.pb path**: `ofl/abhayalibre/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/mooniak/abhaya-libre-font |
| Commit | `f53da70786fe1dba6193bdbd45a2c4159e511079` |
| Config YAML | `sources/config.yaml` (upstream) + local override `config.yaml` in google/fonts |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/mooniak/abhaya-libre-font` was first added to METADATA.pb in commit `aec1b9f3e` (2023-12-20, "Add upstream repository URL"). The URL is consistent with the font's copyright notice, which lists "Mooniak (hello@mooniak.com)" as one of the copyright holders. The repo exists, is publicly accessible, and contains the source files for this font family.

## How the Commit Hash Was Identified

The commit hash has gone through three iterations in METADATA.pb:

1. **`edaabf89`** (from fontc_crater targets, set in Batch 1/4 commit `19cdcec59` on 2025-03-31): This was "Adding fontpackage.toml" dated 2025-01-10. It does have `sources/config.yaml` because it's a descendant of the commit that introduced it. However, it's far newer than when the fonts were built.

2. **`ade314aa`** (set in commit `04009b5bb` on 2025-03-31 by Felipe Sanches): This was "Adding description for Google Fonts" dated 2017-02-16. This is very close to when fonts were last updated in google/fonts via PR #665 (2017-02-17, "abhayalibre: v1.050 added"). This is the most historically accurate onboarding-era commit. However, `sources/config.yaml` does NOT exist at this commit (it was introduced in 2024).

3. **`f53da707`** (current, set in commit `5862ed413` on 2025-05-22 by Felipe Sanches): This is "Update to GF repo tempalte and CI" dated 2024-05-31. The commit message says "Updated commit hash to the one that contains sources/config.yaml". This is the first commit on main where `sources/config.yaml` exists, since it was created by renaming `sources/builder.yaml` to `sources/config.yaml` in that commit.

**Assessment**: The current commit `f53da707` was chosen pragmatically because it's the earliest commit where `sources/config.yaml` exists in the upstream repo. The historically accurate onboarding commit is `ade314aa` (2017-02-16), which is just one day before fonts were added to google/fonts via PR #665.

**Important note**: The fonts currently in google/fonts are static TTFs from 2017 (v1.050). The upstream repo has undergone significant development since then (v2-dev branch merged in 2024, plus contributions from Yanone in 2025). The current upstream sources would produce different fonts than what is in google/fonts.

## How Config YAML Was Resolved

**Upstream config** at commit `f53da707`: `sources/config.yaml` exists and references:
```yaml
sources:
  - AbhayaLibre.glyphs
outputDir: "../fonts"
buildStatic: false
buildVariable: true
```
This config builds a **variable** font (not static), which does not match what's in google/fonts (static TTFs).

**Local override** in `ofl/abhayalibre/config.yaml` (added in commit `04009b5bb`):
```yaml
sources:
  - sources/glyphs/Abhaya-Masters.glyphs
buildStatic: true
buildVariable: false
```
This override builds **static** fonts, matching what's in google/fonts. However, the source path `sources/glyphs/Abhaya-Masters.glyphs` references the file at its old location and old name. This file:
- Existed as `sources/glyphs/Abhaya-Masters.glyphs` up to commit `71089b83` (2017-10-22), when it was renamed to `sources/glyphs/AbhayaLibre.glyphs`
- Was later moved to `sources/AbhayaLibre.glyphs` in commit `e6973a96` (2021-05-26)
- At the currently referenced commit `f53da707`, the file is at `sources/AbhayaLibre.glyphs`

**Discrepancy**: The local override config references `sources/glyphs/Abhaya-Masters.glyphs`, but at the referenced commit `f53da707`, this path does not exist. The file is at `sources/AbhayaLibre.glyphs`. The override config would only work if pointed at a commit before `71089b83` (pre-October 2017).

The METADATA.pb currently sets `config_yaml: "sources/config.yaml"` pointing to the upstream config. Since a local override also exists, this creates potential confusion. Per project policy, when an override `config.yaml` exists in google/fonts, the `config_yaml` field can be omitted from METADATA.pb.

## Conclusion

The source block is technically complete but has internal inconsistencies:

1. **Repository URL**: Correct and verified.
2. **Commit hash**: `f53da707` was chosen because it's the earliest commit with `sources/config.yaml`, but it's from 2024 -- seven years after the fonts were built. The historically accurate commit is `ade314aa` (2017-02-16).
3. **Config situation is confused**: Both an upstream `config_yaml` reference AND a local override exist. The upstream config at `f53da707` builds a variable font (not matching google/fonts). The local override references a source path (`sources/glyphs/Abhaya-Masters.glyphs`) that doesn't exist at the referenced commit.

**Recommended corrections**:
- Change commit to `ade314aa678ceb44f892ed58169c6b270c775d02` (the actual onboarding-era commit)
- Remove `config_yaml` from METADATA.pb source block (since local override exists)
- Fix the local override config to reference `sources/glyphs/Abhaya-Masters.glyphs` (which exists at `ade314aa`) -- this path is actually correct for the onboarding-era commit
- These changes would make the data internally consistent: the commit hash matches the era when fonts were built, and the local override config references a source path that exists at that commit
