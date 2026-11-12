# Hi Melody

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Hi Melody as binaries only (google/fonts at commit `2eb0b48d5f76`).
No source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/himelody.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from HiMelody-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/himelody at `a322a95b1605`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/himelody.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`a322a95b1605` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/yoondesign/Yoonfont-HiMelody at
  4feb2315457c615527775b455d119e9f3b8c8863: the fonts as built (2 font files); no
  source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/yoondesign/Yoonfont-HiMelody"
      commit: "4feb2315457c615527775b455d119e9f3b8c8863"
    }

## Previous investigation

## Investigation Report: Hi Melody

### Summary

Hi Melody is a Korean handwriting font designed by YoonDesign Inc, added to Google Fonts on 2018-02-23 as part of a bulk Korean font onboarding (PR #1459) by Marc Foley. The upstream repository at `https://github.com/yoondesign/Yoonfont-HiMelody` contains only compiled binary fonts (.otf and .ttf) with no source files. The repo has a single meaningful commit (4feb231) from 2017-12-19. No config.yaml is possible since no buildable sources exist.

### Key Findings

| Field             | Value                                                                 |
|-------------------|-----------------------------------------------------------------------|
| Family Name       | Hi Melody                                                             |
| Designer          | YoonDesign Inc                                                        |
| Repository URL    | https://github.com/yoondesign/Yoonfont-HiMelody                      |
| Commit Hash       | 4feb2315457c615527775b455d119e9f3b8c8863                              |
| Config YAML       | N/A (no buildable sources)                                            |
| Status            | no_config_possible                                                    |
| Confidence        | HIGH                                                                  |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb has no source block in the upstream google/fonts main branch. A source block with `repository_url` and `commit` was added in a local commit (9a14639f3) as part of a batch of 602 families but may not yet be merged upstream.

Key METADATA.pb fields:
- Designer: YoonDesign Inc
- License: OFL
- Category: HANDWRITING
- Date added: 2018-02-23
- Primary script: Kore

#### Git History in google/fonts

The font was onboarded in commit `16680f868` (PR #1459, "korean families r01: added", 2018-03-13) by Marc Foley. This was a large batch commit adding ~25 Korean font families simultaneously. The PR body states: "Korean Font binaries have been mastered by Aaron Bell."

A subsequent commit `1ef157d39` ("Add back case corrected files", 2018-03-13) by Dave Crossland re-added the font file `HiMelody-Regular.ttf` with corrected filename casing (from `Himelody-Regular.ttf` to `HiMelody-Regular.ttf`). The font binary has not been modified since.

#### Upstream Repository Analysis

The upstream repo `yoondesign/Yoonfont-HiMelody` was verified via the GitHub API:
- Owner: yoondesign
- Default branch: master
- Last pushed: 2017-12-19
- Total files at HEAD: `Himelody.otf`, `Himelody.ttf`, `OFL_Yoondesign HiMelody.txt`, `README.md`, `Readme_Yoondesign_HiMelody.txt`

The repository contains **only compiled font binaries** (OTF and TTF). There are no source files (.glyphs, .ufo, .designspace, .sfd) whatsoever. The commit 4feb231 is the most recent commit and is dated 2017-12-19, which predates the google/fonts onboarding (2018-03-13).

The repo is NOT cached in the local upstream repos cache. Only two other yoondesign repos are cached (yoonfont-Gamjaflower and Yoonfont-KoreaDokdo).

#### Commit Verification

The commit `4feb2315457c615527775b455d119e9f3b8c8863` was verified on GitHub:
- Message: "Create README.md"
- Date: 2017-12-19
- This is the HEAD/latest commit of the repository

Since this is the only meaningful commit and the entire repo has only binaries, this is the correct reference commit. The font binary in google/fonts was likely provided directly by Aaron Bell who "mastered" the Korean fonts per the PR description, and the compiled binaries were placed in this upstream repo.

#### Source Files Assessment

No buildable source files exist anywhere in the repository at any commit:
- No .glyphs, .glyphx, .ufo, .designspace, or .sfd files
- No config.yaml or build.py
- Only compiled .otf and .ttf binaries

This is typical of several YoonDesign fonts where the company released only compiled binaries under OFL.

### Conclusion

**Status: no_config_possible**

Hi Melody's upstream repository contains only compiled font binaries with no source files. The repository URL and commit hash are verified and correct. No config.yaml can be created because there are no buildable sources. The source block should include `repository_url` and `commit` but cannot include `config_yaml`.
