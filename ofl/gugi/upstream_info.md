# Gugi

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Gugi as binaries only (google/fonts at commit `2eb0b48d5f76`). No
source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/gugi.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Gugi-Regular.ttf, the
  font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/gugi at `cb3b662a3137`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/gugi.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`cb3b662a3137` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/1020tj/Gugi at 7aa7f4c408a5b63e6f58a22c90eed13993f1cdae, the
  designers' repository: it holds the font as built (TTF), its license and a README; no
  source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/1020tj/Gugi"
      commit: "7aa7f4c408a5b63e6f58a22c90eed13993f1cdae"
    }

## Previous investigation

## Investigation Report: Gugi

### Summary

Gugi is a Korean display typeface designed by TAE System & Typefaces Co., added to Google Fonts on 2018-02-23 as part of the Korean families batch (PR #1459). The upstream repository at `https://github.com/1020tj/Gugi` is a minimal distribution repo containing only a compiled TTF binary, OFL.txt, and README.md -- no editable source files. The font binary was mastered by Aaron Bell. The repo has 6 commits, all from November 24, 2017, and the latest (`7aa7f4c`) adds the font file. No config.yaml is possible since there are no buildable sources.

### Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gugi                                                               |
| Designer          | TAE System & Typefaces Co.                                         |
| Date Added        | 2018-02-23                                                         |
| Repository URL    | https://github.com/1020tj/Gugi                                     |
| Commit Hash       | 7aa7f4c408a5b63e6f58a22c90eed13993f1cdae                           |
| Branch            | master                                                             |
| Config            | None (binary-only repo, no source files)                           |
| Source Format     | None (only compiled TTF)                                           |
| Status            | **no_config_possible**                                             |
| Confidence        | HIGH                                                               |

### Investigation Details

#### Upstream Repository

The upstream repo is `https://github.com/1020tj/Gugi` (HTTP 200, verified accessible). It is NOT cached locally in `fontc_crater_cache`.

The repo has exactly 6 commits, all from November 24, 2017:

| Hash    | Message                  |
|---------|--------------------------|
| 7aa7f4c | Add files via upload     |
| 4f9d58e | Create OFL.txt           |
| 9f98fbd | Create README.md         |
| 00ccc9f | Delete .gitattributes    |
| 147f479 | Delete README.md         |
| e7c6c28 | Initial commit           |

The repo contains only 3 files:
1. `구기R.ttf` -- The compiled font binary (Korean filename, ~1.06 MB)
2. `OFL.txt` -- Open Font License
3. `README.md` -- Readme file

There are NO editable source files (no .glyphs, .ufo, .designspace, .sfd, or .vfb files). This is a distribution-only repository.

#### Onboarding History

1. **Korean families batch** (16680f868, 2018-03-13, by Marc Foley, PR #1459): Gugi was added as part of a batch of Korean font families. The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com". The font binary `Gugi-Regular.ttf` (990,856 bytes) was added in this commit.

2. The font binary has never been updated since the initial onboarding, except for the temporary deploy commit cycle (76adaf1d2, 2021-11-01) which does not represent a font change.

#### Commit Hash Verification

The commit `7aa7f4c` (2017-11-24, "Add files via upload") is the latest commit in the repository and the one that added the TTF font file. This is the correct reference commit since it is the most recent commit and predates the google/fonts onboarding (2018-03-13). The font was likely downloaded from this repo by Marc Foley/Aaron Bell for the Korean families batch.

#### Source Block Status

A source block with `repository_url` and `commit` was added to Gugi's METADATA.pb in commit `9a14639f3c` (2026-02-25) on the `sources_info_2026-02-25` branch, but this has NOT been merged to main yet. The main branch METADATA.pb has no source block.

#### Build Configuration

No config.yaml is possible. The upstream repo contains only a compiled TTF binary with no editable source files. The font cannot be rebuilt using gftools-builder or fontc.

### Conclusion

**Status: no_config_possible**

The upstream repo is a binary distribution repository with no editable font sources. A config.yaml cannot be created. The source block should document the repository URL and commit hash for provenance tracking purposes only.

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/1020tj/Gugi"
  commit: "7aa7f4c408a5b63e6f58a22c90eed13993f1cdae"
}
```
