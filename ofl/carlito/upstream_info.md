# Investigation: Carlito

## Source Data

| Field | Value |
|---|---|
| Family Name | Carlito |
| Designer | Lukasz Dziedzic |
| License | OFL |
| Date Added | 2023-03-10 |
| Repository URL | https://github.com/googlefonts/carlito |
| Commit Hash | `3a810cab78ebd6e2e4eed42af9e8453c4f9b850a` |
| Branch | main |
| Config YAML | None |
| Override Config | No |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/googlefonts/carlito` is recorded in the METADATA.pb source block, which was added by gftools-packager during the initial onboarding in PR #6005. The copyright strings in the font files themselves also reference this URL. The repo is part of the `googlefonts` organization.

## How Commit Determined

The commit hash `3a810cab78ebd6e2e4eed42af9e8453c4f9b850a` was set by gftools-packager during onboarding. The commit message for `07ace6aba` in google/fonts explicitly states:

> "Carlito Version 1.104 taken from the upstream repo https://github.com/googlefonts/carlito at commit https://github.com/googlefonts/carlito/commit/3a810cab78ebd6e2e4eed42af9e8453c4f9b850a."

PR #6005, authored by RosaWagner, confirms this. The commit is the HEAD (and only commit) of the upstream repository's `main` branch, which is a merge of PR #5 from RosaWagner/main.

## Verification

- **Commit exists in upstream repo**: Yes. The commit `3a810ca` is the HEAD and sole commit in the repository.
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/googlefonts/carlito/`.
- **Files match METADATA.pb**: The source block lists `fonts/ttf/Carlito-Regular.ttf`, `fonts/ttf/Carlito-Bold.ttf`, `fonts/ttf/Carlito-BoldItalic.ttf`, `fonts/ttf/Carlito-Italic.ttf`, and `OFL.txt`, all of which exist in the repo.

## Config YAML Status

**No config.yaml exists, and none can be created.** The upstream repository contains only pre-compiled TTF binary files under `fonts/ttf/`. There are no buildable source files (.glyphs, .ufo, .designspace, .sfd) anywhere in the repository. The repo's README notes that Carlito is derived from Lato (also by Lukasz Dziedzic) and is metric-compatible with Calibri, but the actual design sources are not included.

The history of this font's inclusion is documented in google/fonts issue #1441 ("Add Carlito and Caladea"), which shows a long process before the fonts were finally onboarded.

Since there are no buildable sources, a config.yaml is not applicable for this family.

## Confidence Level

**HIGH** -- The repository URL and commit hash are explicitly confirmed by the gftools-packager commit message in google/fonts (PR #6005). The commit is the only commit in the upstream repo, so there is no ambiguity.

## Open Questions

- The font sources (likely Glyphs or FontLab files) are not publicly available. The upstream repo is a binary-only distribution repository. If the original design sources were ever to be published, a config.yaml could be created at that point.
- The status should remain `missing_config` as there are genuinely no buildable sources.
