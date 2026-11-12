# Carlito

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Carlito from https://github.com/googlefonts/carlito at commit
`3a810cab78eb`, which holds the fonts as built and no source, so it could not be built
with fontc.

## Actions taken

- The work was done on top of that repository's history, in a pull request merged into
  its default branch, so its fonts are the ones converted.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from
  fonts/ttf/Carlito-{Bold,BoldItalic,Italic,Regular}.ttf, the fonts Google Fonts ships,
  with babelfont d7f67ca (simoncozens/babelfont-rs): its TTF reader, no filters.
  sources/config.yaml: productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/carlito at `a8d610ee6e4a`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools,
including this family's plan `plans/carlito.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`a8d610ee6e4a` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the releases', its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Previous source block

The source block this replaces (the same repository, before this work), preserved for
provenance:

    source {
      repository_url: "https://github.com/googlefonts/carlito"
      commit: "3a810cab78ebd6e2e4eed42af9e8453c4f9b850a"
      files {
        source_file: "OFL.txt"
        dest_file: "OFL.txt"
      }
      files {
        source_file: "fonts/ttf/Carlito-Regular.ttf"
        dest_file: "Carlito-Regular.ttf"
      }
      files {
        source_file: "fonts/ttf/Carlito-Bold.ttf"
        dest_file: "Carlito-Bold.ttf"
      }
      files {
        source_file: "fonts/ttf/Carlito-BoldItalic.ttf"
        dest_file: "Carlito-BoldItalic.ttf"
      }
      files {
        source_file: "fonts/ttf/Carlito-Italic.ttf"
        dest_file: "Carlito-Italic.ttf"
      }
      branch: "main"
    }

## Previous investigation

## Investigation: Carlito

### Source Data

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

### How URL Found

The repository URL `https://github.com/googlefonts/carlito` is recorded in the METADATA.pb source block, which was added by gftools-packager during the initial onboarding in PR #6005. The copyright strings in the font files themselves also reference this URL. The repo is part of the `googlefonts` organization.

### How Commit Determined

The commit hash `3a810cab78ebd6e2e4eed42af9e8453c4f9b850a` was set by gftools-packager during onboarding. The commit message for `07ace6aba` in google/fonts explicitly states:

> "Carlito Version 1.104 taken from the upstream repo https://github.com/googlefonts/carlito at commit https://github.com/googlefonts/carlito/commit/3a810cab78ebd6e2e4eed42af9e8453c4f9b850a."

PR #6005, authored by RosaWagner, confirms this. The commit is the HEAD (and only commit) of the upstream repository's `main` branch, which is a merge of PR #5 from RosaWagner/main.

### Verification

- **Commit exists in upstream repo**: Yes. The commit `3a810ca` is the HEAD and sole commit in the repository.
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/googlefonts/carlito/`.
- **Files match METADATA.pb**: The source block lists `fonts/ttf/Carlito-Regular.ttf`, `fonts/ttf/Carlito-Bold.ttf`, `fonts/ttf/Carlito-BoldItalic.ttf`, `fonts/ttf/Carlito-Italic.ttf`, and `OFL.txt`, all of which exist in the repo.

### Config YAML Status

**No config.yaml exists, and none can be created.** The upstream repository contains only pre-compiled TTF binary files under `fonts/ttf/`. There are no buildable source files (.glyphs, .ufo, .designspace, .sfd) anywhere in the repository. The repo's README notes that Carlito is derived from Lato (also by Lukasz Dziedzic) and is metric-compatible with Calibri, but the actual design sources are not included.

The history of this font's inclusion is documented in google/fonts issue #1441 ("Add Carlito and Caladea"), which shows a long process before the fonts were finally onboarded.

Since there are no buildable sources, a config.yaml is not applicable for this family.

### Confidence Level

**HIGH** -- The repository URL and commit hash are explicitly confirmed by the gftools-packager commit message in google/fonts (PR #6005). The commit is the only commit in the upstream repo, so there is no ambiguity.

### Open Questions

- The font sources (likely Glyphs or FontLab files) are not publicly available. The upstream repo is a binary-only distribution repository. If the original design sources were ever to be published, a config.yaml could be created at that point.
- The status should remain `missing_config` as there are genuinely no buildable sources.
