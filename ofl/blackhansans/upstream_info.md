# Black Han Sans

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Black Han Sans as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/blackhansans.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  BlackHanSans-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/blackhansans at `41b7d933d1c5`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/blackhansans.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`41b7d933d1c5` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/zesstype/Black-Han-Sans at
  8809d5944fbf6aa2cd99158cb7ab55629058348a: the fonts as built (2 font files); no
  source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/zesstype/Black-Han-Sans"
      commit: "8809d5944fbf6aa2cd99158cb7ab55629058348a"
    }

## Previous investigation

## Investigation Report: Black Han Sans

### Source Data

| Field | Value |
|-------|-------|
| Family Name | Black Han Sans |
| Designer | Zess Type |
| License | OFL |
| Date Added | 2018-02-23 |
| Repository URL | https://github.com/zesstype/Black-Han-Sans |
| Commit | `8809d5944fbf6aa2cd99158cb7ab55629058348a` |
| Branch | None |
| Config YAML | None |
| Status | missing_config |

### How URL Found

The repository URL was added to METADATA.pb by Emma Marichal (commit `9bb786b0e`, 2024-11-28) with the message "adds family.source.repository_url entry". The URL also appears in the copyright string: "Copyright 2015 The Black Han Sans Project Authors (https://github.com/zesstype/Black-Han-Sans)".

### How Commit Determined

The commit hash `8809d5944fbf6aa2cd99158cb7ab55629058348a` was added as part of a batch operation (commit `9a14639f3`, 2026-02-25). This is the HEAD commit of the upstream repository's master branch, representing the latest state of the repo.

#### Cross-verification

The commit was verified in the upstream repo at `upstream_repos/fontc_crater_cache/zesstype/Black-Han-Sans/`. It corresponds to "Update README.md" (dated 2020-09-03).

However, this is a **binary-only** repository. At the recorded commit, the repo contains only:
- `BlackHanSans.ttf` - the font binary
- `OFL.txt` - the license
- `README.md` - readme
- A Korean-named OTF file (the same font in OTF format)

There are no source files (no `.glyphs`, `.ufo`, `.designspace`, `.sfd` files) anywhere in the repo's history.

#### Relationship to google/fonts binary

The font in google/fonts has been modified multiple times after the initial Korean batch import:
1. **2018-03-13**: Initial add as part of Korean families batch (PR #1459, by Marc Foley)
2. **2024-11-25**: "Black Han Sans: 1.001" - hotfix by Aaron to correct a cmap encoding bug
3. **2024-11-27**: Two additional hotfixes by Aaron (adding BA87 glyph, updating copyright)
4. **2024-11-28**: Final copyright hotfix by Emma Marichal

The font binary currently in google/fonts is NOT from the upstream repo - it was hotfixed directly by Aaron Bell and Emma Marichal. The upstream repo was last updated in 2020 and has not been synced with these hotfixes.

### Config YAML Status

No `config.yaml` exists in the upstream repository at any commit. The repo contains only pre-built binaries with no source files. Therefore, no config.yaml can be created for this family.

There is also no override `config.yaml` in the google/fonts family directory.

### Verification

- **Upstream repo accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/zesstype/Black-Han-Sans/`
- **Commit exists in repo**: Yes - `8809d59 Update README.md` (HEAD of master, dated 2020-09-03)
- **Font file at commit**: Yes - `BlackHanSans.ttf` exists
- **Source files at commit**: No - repository contains only pre-built binaries
- **Config YAML**: Not applicable - no source files to build from

### Confidence Level

**MEDIUM** - The commit hash is the HEAD of the upstream repo, which is the best available reference. However, the font binary in google/fonts has diverged significantly from the upstream version due to multiple hotfixes applied directly in google/fonts. The upstream repo is effectively a binary distribution point, not a true source repository.

### Open Questions

1. Where are the actual source files for Black Han Sans? The upstream repo only contains compiled binaries.
2. Should the commit hash reference the original import state, or is HEAD the correct choice given the binary-only nature of the repo?
3. The hotfixed binary in google/fonts was created by Aaron Bell directly - are there source files in Saja Type Works' private workspace?

### Notes

- Black Han Sans was part of the same Korean fonts batch as Black And White Picture (PR #1459, March 2018).
- The upstream repo (zesstype/Black-Han-Sans) is a very simple repo with only 19 commits total, all simple file uploads and README edits.
- The font was hotfixed in google/fonts in November 2024 to fix cmap encoding issues and copyright strings. These changes are not reflected in the upstream repo.
- The status is correctly `missing_config` because no buildable source files exist in the upstream repo. This cannot be resolved without obtaining source files from the designer (Zess Type).
- The `source {}` block in METADATA.pb currently only contains `repository_url` and `commit` (added by our batch update), with no `config_yaml` field, which is correct.
