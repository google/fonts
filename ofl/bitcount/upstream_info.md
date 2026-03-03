# Bitcount

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Petr van Blokland
**METADATA.pb path**: `ofl/bitcount/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `653fc48a72cf3b6a293f6fc207a770f537921889` |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was set in the METADATA.pb from the very first onboarding commit `50712b8cc` (2025-01-17), authored by Yanone. The commit message explicitly states: "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount". The URL also matches the copyright string in the font files. The font was added as part of issue #5468 ("Add Bitcount"), filed by Dave Crossland.

## How the Commit Hash Was Identified

The original onboarding commit `50712b8cc` in google/fonts referenced upstream commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a` (2025-01-13, "Update fixAnchors.py"). This was the commit used for all 12 initial Bitcount variant PRs created by Yanone on 2025-01-17.

The current METADATA.pb records commit `653fc48a72cf3b6a293f6fc207a770f537921889` (2025-01-31, "Add some first JS animations to show the working of the color layers"). This change was introduced by commit `19cdcec59` in google/fonts ([Batch 1/4] port info from fontc_crater targets list, 2025-03-31), authored by Felipe Sanches. This batch commit ported data from fontc_crater's target.json file and also added the `config_yaml` field.

The `653fc48a7` commit is 2 commits ahead of `af0818eae` in the upstream repo. The font binary files did **not** change between these two commits -- the intervening commits (`67d4d91b7` and `653fc48a7`) only modified JavaScript demo/sample files in the `docs/` directory. The `sources/config.yaml` file is also unchanged between both commits.

While the original onboarding commit was `af0818eae`, the `653fc48a7` hash recorded in fontc_crater targets (and subsequently ported to METADATA.pb) still points to identical source files and font binaries, so it is functionally equivalent.

## How Config YAML Was Resolved

The upstream `sources/config.yaml` exists at both the original (`af0818eae`) and current (`653fc48a7`) commit hashes. However, its content is minimal: `familyName: Bitcount` only. It does not specify a `sources:` list or a designspace file. Despite this, it is referenced in METADATA.pb as `config_yaml: "sources/config.yaml"`.

Bitcount does **not** have a local override config.yaml in `ofl/bitcount/` -- it relies solely on the upstream config.yaml. The font binary in google/fonts was taken directly from `fonts/ttf/variable/Bitcount[CRSV,ELSH,ELXP,slnt,wght].ttf` in the upstream repo (not built from source via gftools-builder).

## Verification

- Commit `653fc48a7` exists in upstream repo: Yes
- Commit date: 2025-01-31 23:50:48 +0100
- Commit message: "Add some first JS animations to show the working of the color layers. Run Test-003 on Chrome"
- Font binary unchanged since original onboarding commit `af0818eae`: Yes
- Source files unchanged: Yes
- config.yaml content: `familyName: Bitcount`

## Confidence

**High**: The repository URL is well-established, confirmed by the onboarding PR (#8958, merged 2025-01-21), issue #5468, copyright strings, and commit messages. The commit hash `653fc48a7` differs from the original onboarding commit `af0818eae`, but the font binaries and source files are identical between both commits. The discrepancy arose from fontc_crater target.json using a slightly newer commit, which was then ported to METADATA.pb.

## Open Questions

1. The upstream `sources/config.yaml` only contains `familyName: Bitcount` with no `sources:` list. The font binary was taken directly from the upstream repo's `fonts/ttf/variable/` directory rather than built from sources. This means fontc_crater cannot rebuild this font from source using this config. A more complete config.yaml with source references would be needed for fontc_crater builds.
