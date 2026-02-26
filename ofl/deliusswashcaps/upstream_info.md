# Delius Swash Caps - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Delius Swash Caps |
| Designer | Natalia Raices |
| License | OFL |
| Repository URL | https://github.com/librefonts/deliusswashcaps |
| Commit Hash | a18d931eb4b66533df5df07d91e0851938a96121 |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |
| Date Added | 2011-08-03 |

## How URL Found

The repository URL `https://github.com/librefonts/deliusswashcaps` was identified through the librefonts GitHub organization. Like the other Delius variants (Delius, Delius Unicase), each variant has its own separate repository under the librefonts organization. A source block was prepared in commit `9a14639f3` (on PR branch `sources_info_2026-02-25`, not yet merged to main).

## How Commit Determined

The commit `a18d931eb4b66533df5df07d91e0851938a96121` is the HEAD of the master branch in the upstream repo (the only visible commit in the shallow clone: "update .travis.yml"). This is a legacy font added to the Google Fonts catalog on 2011-08-03 and present since the initial google/fonts commit (2015-03-07).

The TTF file in google/fonts was last modified in the deploy commit `76adaf1d2` (2021-11-01). Before that, it was in the initial commit.

The upstream repo contains:
- `src/DeliusSwashCaps-Regular-TTF.sfd` (FontForge source)
- `src/DeliusSwashCaps-Regular.vfb` (FontLab source)
- TTX decompositions of the font tables
- No modern build sources (.glyphs, .ufo, .designspace)

## Config YAML Status

- No `config.yaml` exists in the upstream repository
- No override `config.yaml` exists in google/fonts at `ofl/deliusswashcaps/`
- The upstream repo only contains SFD (FontForge) and VFB (FontLab) source formats
- These formats are not compatible with gftools-builder
- A config.yaml cannot be created without converting the sources to a modern format first

## Verification

- Repository URL is valid and accessible
- Upstream repo cloned at `upstream_repos/fontc_crater_cache/librefonts/deliusswashcaps/` (shallow clone)
- Commit `a18d931` verified as HEAD of master
- No modern source files found (.glyphs, .ufo, .designspace)
- METADATA.pb in google/fonts main branch currently has no source block (a PR branch adds one)

## Confidence Level

**High** for repository URL. **Medium** for commit hash (HEAD of shallow clone). **N/A** for config_yaml (legacy source format only).

## Open Questions

- Same situation as Delius and Delius Unicase: sources would need conversion to modern format for gftools-builder compatibility.
- The copyright string references Reserved Font Names: "Delius", "Delius Unicase", "Delius Swash Caps" - all three variants share the same designer (Natalia Raices) and were created as a family.
- The source block for METADATA.pb has been prepared on branch `sources_info_2026-02-25` but is not yet merged.
