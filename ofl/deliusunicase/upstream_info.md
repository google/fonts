# Delius Unicase - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Delius Unicase |
| Designer | Natalia Raices |
| License | OFL |
| Repository URL | https://github.com/librefonts/deliusunicase |
| Commit Hash | cf094caecc96589701f341db1994fd10642e3c88 |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |
| Date Added | 2011-10-12 |

## How URL Found

The repository URL `https://github.com/librefonts/deliusunicase` was identified through the librefonts GitHub organization. This is the third variant in the Delius family (alongside Delius and Delius Swash Caps), each hosted in its own repository. A source block was prepared in commit `9a14639f3` (on PR branch `sources_info_2026-02-25`, not yet merged to main).

## How Commit Determined

The commit `cf094caecc96589701f341db1994fd10642e3c88` is the HEAD of the master branch in the upstream repo (the only visible commit in the shallow clone: "update .travis.yml"). This is a legacy font added to the Google Fonts catalog on 2011-10-12.

Unlike the other Delius variants which have only one weight, Delius Unicase has two weights:
- DeliusUnicase-Regular.ttf (400)
- DeliusUnicase-Bold.ttf (700)

The TTF files in google/fonts were last modified in the deploy commit `76adaf1d2` (2021-11-01). Before that, they were in the initial commit.

The upstream repo contains:
- `src/DeliusUnicase-Regular-TTF.sfd` and `src/DeliusUnicase-Bold-TTF.sfd` (FontForge sources)
- `src/DeliusUnicase-Regular.vfb` and `src/DeliusUnicase-Bold.vfb` (FontLab sources)
- TTX decompositions of the font tables for both weights
- No modern build sources (.glyphs, .ufo, .designspace)

## Config YAML Status

- No `config.yaml` exists in the upstream repository
- No override `config.yaml` exists in google/fonts at `ofl/deliusunicase/`
- The upstream repo only contains SFD (FontForge) and VFB (FontLab) source formats
- These formats are not compatible with gftools-builder
- A config.yaml cannot be created without converting the sources to a modern format first

## Verification

- Repository URL is valid and accessible
- Upstream repo cloned at `upstream_repos/fontc_crater_cache/librefonts/deliusunicase/` (shallow clone)
- Commit `cf094ca` verified as HEAD of master
- No modern source files found (.glyphs, .ufo, .designspace)
- Source files for both Regular and Bold weights are present in `src/` directory
- METADATA.pb in google/fonts main branch currently has no source block (a PR branch adds one)

## Confidence Level

**High** for repository URL. **Medium** for commit hash (HEAD of shallow clone). **N/A** for config_yaml (legacy source format only).

## Open Questions

- Same situation as Delius and Delius Swash Caps: sources would need conversion to modern format for gftools-builder compatibility.
- This is the only Delius variant with multiple weights (Regular + Bold), so source conversion would be more involved.
- The source block for METADATA.pb has been prepared on branch `sources_info_2026-02-25` but is not yet merged.
- The copyright string references Reserved Font Names: "Delius", "Delius Unicase", "Delius Swash Caps".
