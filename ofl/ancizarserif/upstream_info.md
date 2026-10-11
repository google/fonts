# Ancizar Serif

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Universidad Nacional de Colombia (UNAL), César Puertas, Viviana Monsalve, Julián Moncada
**METADATA.pb path**: `ofl/ancizarserif/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/UNAL-OMD/UNAL-Ancizar |
| Commit | `063bdd3121fef76289b035226acdc1b4e885f31a` |
| Config YAML | `sources/config-serif.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/UNAL-OMD/UNAL-Ancizar` is already recorded in the METADATA.pb `source {}` block. It is also referenced in the onboarding commit message (`599dc5827` in google/fonts), which states: "Taken from the upstream repo https://github.com/UNAL-OMD/UNAL-Ancizar". The copyright string in METADATA.pb also points to this same URL. The cached clone at `UNAL-OMD/UNAL-Ancizar` has `origin` set to this URL. The repository is valid and accessible.

## How the Commit Hash Was Identified

The commit `063bdd3121fef76289b035226acdc1b4e885f31a` is already recorded in the METADATA.pb `source {}` block. It was explicitly referenced in the google/fonts onboarding commit (`599dc5827`, authored by Yanone on 2025-04-16), which states it was taken at this exact commit.

**Binary verification**: SHA-256 hashes of both `AncizarSerif[wght].ttf` and `AncizarSerif-Italic[wght].ttf` in google/fonts match exactly with the files at this commit in the upstream repo:
- `AncizarSerif[wght].ttf`: `fcc35d7fe2780846344d7187515d483bb69f3d9bcc49c4833a219e4d9109db98`
- `AncizarSerif-Italic[wght].ttf`: `b30f075790e14795508a42dda7b8f6269509e15a13a4c653b3665662bdfbf45c`

The commit message in the upstream repo is "New Serif binaries" (2025-04-16), authored by Yanone. This is the same author and same date as the google/fonts onboarding commit, confirming the font engineer (Yanone) built the binaries upstream and immediately onboarded them to google/fonts.

One subsequent commit exists in the upstream repo (`c4303cb`, "Added RFN", 2025-04-24), which modifies the Serif binary files (sizes changed slightly). This commit was made after the google/fonts merge (PR #9355 merged 2025-04-17) and was not included in the onboarding.

## How Config YAML Was Resolved

The config file `sources/config-serif.yaml` exists at the referenced commit and is already recorded in METADATA.pb. Its contents:

```yaml
sources:
  - AncizarSerif.glyphs
  - AncizarSerif-Italic.glyphs
buildVariable: true
buildStatic: true
buildTTF: false
buildOTF: false
buildWebfont: false
buildSmallCap: false
```

The source files (`AncizarSerif.glyphs`, `AncizarSerif-Italic.glyphs`) are confirmed to exist under `sources/` at the referenced commit. No local override config.yaml exists in the google/fonts family directory.

Note: The upstream repo also contains `sources/config-sans.yaml` for the sibling family Ancizar Sans.

## Sibling Family Note

This upstream repo (`UNAL-OMD/UNAL-Ancizar`) serves both **Ancizar Serif** and **Ancizar Sans**. They share the same repo but use different config files (`config-serif.yaml` vs `config-sans.yaml`) and may reference different commits in their respective METADATA.pb files.

## Onboarding Timeline

| Date | Event |
|------|-------|
| 2025-04-16 | Yanone committed "New Serif binaries" to upstream (`063bdd3`) |
| 2025-04-16 | Yanone created onboarding commit in google/fonts (`599dc58`) via gftools-packager |
| 2025-04-17 | Emma Marichal merged PR #9355 into google/fonts |
| 2025-04-24 | Upstream commit `c4303cb` ("Added RFN") -- after onboarding, not included |
| 2025-05-22 | Source block added to METADATA.pb in google/fonts (`e258478`, PR #9355) |

## Conclusion

The source metadata for Ancizar Serif is **complete and correct**. All fields in the METADATA.pb `source {}` block are verified:

- **Repository URL**: Valid, accessible, confirmed by onboarding commit message and copyright string.
- **Commit hash**: Verified via binary SHA-256 hash comparison -- files match exactly.
- **Config YAML**: `sources/config-serif.yaml` exists at the referenced commit with valid gftools-builder configuration referencing `.glyphs` sources.
- **Branch**: `main` (confirmed; the commit is on the main branch).

No corrections needed. Status: **complete**.
