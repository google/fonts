# Calligraffitti

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Calligraffitti as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/calligraffitti.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Calligraffitti-Regular.ttf, the font Google Fonts ships, with babelfont 58eedc8
  (felipesanches/babelfont-rs branch 2026-10-22: simoncozens/babelfont-rs main plus the
  TTF reader changes proposed to it): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/calligraffitti at `02b6fe053efa`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/calligraffitti.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`02b6fe053efa` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/librefonts/calligraffitti at
  983f7f33e1a63da6369e2f626ba9166ab7468fb9: the font as built, dumped to TTX, and its
  metadata; no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/calligraffitti"
      commit: "983f7f33e1a63da6369e2f626ba9166ab7468fb9"
    }

## Previous investigation

## Investigation Report: Calligraffitti

### Summary

Calligraffitti is a handwriting typeface designed by Open Window (Dathan Boardman). It was added to Google Fonts on 2011-01-06. The METADATA.pb has no source block. The only known upstream repository is `librefonts/calligraffitti`, which contains TTX-decomposed font data but no actual source files (no .vfb, .sfd, .glyphs, .ufo, or .designspace). The `src/` directory only contains metadata text files. There are no buildable sources anywhere in the repository. A config.yaml cannot be created.

### Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Calligraffitti                                     |
| Designer           | Open Window (Dathan Boardman)                      |
| License            | Apache 2.0                                         |
| Date Added         | 2011-01-06                                         |
| Repository URL     | https://github.com/librefonts/calligraffitti       |
| Commit Hash        | 983f7f33e1a63da6369e2f626ba9166ab7468fb9           |
| Config YAML        | None (no buildable sources)                        |
| Status             | no_config_possible                                 |
| Confidence         | MEDIUM                                             |

### Investigation Details

#### METADATA.pb Current State

The current METADATA.pb has no `source { }` block:

```
name: "Calligraffitti"
designer: "Open Window"
license: "APACHE2"
category: "HANDWRITING"
date_added: "2011-01-06"
```

#### Binary File History in google/fonts

The font binary has been modified exactly twice:

1. **Initial commit** (`90abd17b4`, 2015-03-07): Added `Calligraffitti-Regular.ttf`
2. **Hotfix PR #765** (`5ca10f1e0`, 2017-08-07): Updated `Calligraffitti-Regular.ttf`, updated METADATA.pb fields (full_name, copyright, subsets). Authored by Marc Foley. PR body was empty.

The hotfix renamed `full_name` from "Calligraffitti" to "Calligraffitti Regular", cleaned up the copyright string (removed email address), and dropped the `latin-ext` subset.

#### Upstream Repository: librefonts/calligraffitti

- **URL**: https://github.com/librefonts/calligraffitti
- **Cached at**: upstream_repos/fontc_crater_cache/librefonts/calligraffitti
- **Status**: Active (not archived)
- **Commits**: Single commit (`983f7f3`, 2014-10-17) - "update .travis.yml"

The repository contains:
- TTX-decomposed font tables (`.ttx` files) for Calligraffitti-Regular.ttf
- `LICENSE.txt`, `COPYRIGHT.txt`, `DESCRIPTION.en_us.html`
- `METADATA.json` (legacy format)
- `src/METADATA_comments.txt` - subsetting commands for the font
- `src/VERSIONS.txt` reports "Calligraffitti-Regular.ttf: Version 1.001"

#### Source File Analysis

The `src/` directory contains only:
- `METADATA_comments.txt` - Shell commands for font subsetting
- `VERSIONS.txt` - Version string

There are **no source files** of any kind in this repository:
- No `.vfb` (FontLab binary)
- No `.sfd` (FontForge)
- No `.glyphs` or `.glyphx` (Glyphs)
- No `.ufo` (Unified Font Object)
- No `.designspace`

The `librefonts` organization repos were automated TTX decompositions of early Google Fonts families, not development repositories. For Calligraffitti, the original source files were never included. The designer (Dathan Boardman / Open Window) does not appear to have a public GitHub repository with the original sources.

#### Commit Hash Determination

The repo has only one commit (`983f7f3`). This commit does not correspond to any specific onboarding action in google/fonts. The librefonts repo was created in 2014, while the font was onboarded in 2011, and the last binary update was in 2017 (PR #765). The hotfix binary was likely generated by Marc Foley using ttfautohint or similar post-processing, not built from this repo.

### Conclusion

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/calligraffitti"
}
```

#### Notes

- Status: **no_config_possible** - There are no source files of any kind in the repository. The repo only contains TTX decompositions and metadata files.
- The `librefonts/calligraffitti` repo is not a true development upstream -- it is an archival TTX decomposition created by the librefonts project. The original source files from Open Window / Dathan Boardman were never included.
- No commit hash is included in the source block because the repo's single commit does not correspond to any specific build or onboarding event in google/fonts.
- The font binary in google/fonts was last updated in PR #765 (August 2017) as a hotfix by Marc Foley. The exact source for that binary is unknown.
- Confidence is MEDIUM because while the repo URL is the only known repository for this family, it contains no buildable sources and the relationship to the google/fonts binary is indirect (TTX decomposition of the binary, not the other way around).
