# Dokdo

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Dokdo as binaries only (google/fonts at commit `2eb0b48d5f76`). No
source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/dokdo.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Dokdo-Regular.ttf, the
  font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/dokdo at `47a91e8d460e`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/dokdo.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`47a91e8d460e` is the equivalence commit: its build is functionally equivalent to the
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

- None known: google/fonts has no source block for this family; the fonts were added as
  built in google/fonts#1459 (2018, "korean families r01"), and FONTRIX publishes no
  source repository.

## Previous investigation

## Dokdo

### Summary

Dokdo is a Korean and Latin display font designed by FONTRIX. No upstream source repository has been identified on GitHub or elsewhere.

### Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | Dokdo |
| **Designer** | FONTRIX |
| **License** | OFL |
| **Date Added** | 2018-02-23 |
| **Repository URL** | None found |
| **Commit Hash** | N/A |
| **Config YAML** | N/A |
| **Status** | no_upstream_repo |

### Investigation Details

#### Onboarding History

Dokdo was added to Google Fonts in PR #1459 ("korean families r01: added") by Marc Foley on 2018-03-13 (commit `16680f868`). The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com". This was a batch addition of Korean fonts.

The font binary has not been updated since onboarding.

#### Upstream Repository Search

- No GitHub repository found for "Dokdo font" or "FONTRIX"
- FONTRIX appears to be a Korean foundry that contributed the font under OFL
- The copyright states "Copyright (c) 2005-2017 FONTRIX. All Rights Reserved."
- No upstream repo is cached in fontc_crater_cache
- Dokdo is the only family in the Google Fonts catalog attributed to FONTRIX

#### Source Availability

No source files (`.glyphs`, `.ufo`, `.designspace`, `.sfd`) are publicly available. Only the compiled TTF binary exists in google/fonts.

### Conclusion

Dokdo has no known upstream repository. The font was provided as a compiled binary by FONTRIX for the Korean fonts batch addition. Without an upstream repo, no config.yaml can be set up and the font cannot be rebuilt from sources via gftools-builder.
