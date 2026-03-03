# Afacad Flux

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: needs_correction
**Designer**: Kristian Möller, Dicotype
**METADATA.pb path**: `ofl/afacadflux/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Dicotype/Afacad |
| Commit | `b294b1f8610ff16a3846a255b1a6a2e6788a056e` (current in METADATA.pb; likely incorrect — see below) |
| Config YAML | `sources/config_flux.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/Dicotype/Afacad` was present in METADATA.pb from the initial onboarding. It is also referenced in the font copyright string: "Copyright 2023 The Afacad Project Authors (https://github.com/Dicotype/Afacad)". The upstream repo is cached at `Dicotype/Afacad` and is valid.

## How the Commit Hash Was Identified

Three different commit hashes appear in the history of this family, which is a concern:

1. **`a3d77cea32b6f29801c5c1771fbad276d817c97a`** — referenced in the PR #7851 body by Emma Marichal: "Taken from the upstream repo ... at commit a3d77ce..."
2. **`4655a472cef57467e1604ce80336ab87ea72facc`** — referenced in the google/fonts commit message (`ef30d6c39`) and in the original METADATA.pb at the time of onboarding
3. **`b294b1f8610ff16a3846a255b1a6a2e6788a056e`** — the current HEAD of the upstream repo's `main` branch, introduced into METADATA.pb by commit `19cdcec59` ("Batch 1/4 port info from fontc_crater targets list")

**Timeline analysis**:
- The google/fonts merge of PR #7851 occurred on **2024-07-05**
- Commit `b294b1f` in the upstream repo is dated **2024-10-03** (a README update), which is ~3 months AFTER the onboarding merge

**Conclusion on commit hash**: The current METADATA.pb commit hash `b294b1f` is **incorrect** — it points to a commit made after the font was already onboarded. This was introduced by the "Batch 1/4" update which imported fontc_crater target data (which uses the latest HEAD, not the original onboarding commit).

The original onboarding commit was `4655a47` (from the commit message / original METADATA.pb). The PR body referenced `a3d77ce`, which is a discrepancy typical of gftools-packager (the tool may have started with one commit and the final packaged result referenced another). Both `4655a47` and `a3d77ce` are inaccessible in the shallow clone but exist as objects in the pack file.

The binary font in google/fonts (sha256: `28aa3569...`) does NOT match the binary at `b294b1f` (sha256: `89b1d45d...`), confirming the current commit hash is wrong.

**Recommendation**: The commit hash should be reverted to `4655a472cef57467e1604ce80336ab87ea72facc` (the original onboarding value). Further investigation with a full (non-shallow) clone could determine whether `a3d77ce` or `4655a47` was the actual source commit, but `4655a47` was what the gftools-packager tool recorded in METADATA.pb.

## How Config YAML Was Resolved

The upstream repo contains two config files in the `sources/` directory:
- `sources/config.yaml` — for the Afacad (non-Flux) family, references `Afacad.glyphs` and `Afacad-Italic.glyphs`
- `sources/config_flux.yaml` — for Afacad Flux, references `AfacadFlux.glyphs`

The "Batch 1/4" update initially set `config_yaml` to `sources/config.yaml` (wrong — that's for the non-Flux family). This was corrected to `sources/config_flux.yaml` in commit `187711d44` ("sources info for Afacad Flux: Version 1.100", PR #7851 by Felipe Sanches).

The current value `sources/config_flux.yaml` is correct. The config builds from `AfacadFlux.glyphs` with axes `slnt` and `wght`, outputting to `fonts/Afacad_Flux/`, with TTF/OTF building disabled (pre-built binaries are used).

No override `config.yaml` exists in the google/fonts family directory.

## Conclusion

**Confidence: HIGH** for repository URL and config_yaml.
**Confidence: MEDIUM** for the commit hash correction.

The repository URL and config_yaml path are correct as currently set. However, the commit hash `b294b1f` is demonstrably wrong — it postdates the onboarding by 3 months and the binary files don't match. The commit should be corrected back to `4655a472cef57467e1604ce80336ab87ea72facc` (the original gftools-packager value). A full clone would be needed to definitively determine which of `4655a47` or `a3d77ce` was the true source commit, but `4655a47` was the value recorded by the packaging tool in the original METADATA.pb.
