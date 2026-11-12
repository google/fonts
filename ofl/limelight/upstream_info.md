# Limelight

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Limelight (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontForge import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/limelight.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Limelight-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/limelight at `31b7c7ff5548`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/limelight.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`31b7c7ff5548` is the equivalence commit: its build is functionally equivalent to the
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

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/limelight/src/Limelight-Regular-TTF.sfd,
  a FontForge import of the shipped font (quadratic outlines, its TrueType instructions;
  tools/probes/ttf_sfd_origin), not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Investigation Report: Limelight

**Model**: Claude Opus 4.6

### Source Repository

The original design sources for Limelight are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `limelight/src/`.

#### Source Files in googlefontdirectory-hg

- `Limelight-Regular.vfb` -- FontLab binary source (proprietary, not buildable with gftools-builder)
- `Limelight-Regular-OTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Limelight-Regular-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Limelight-Regular.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are in VFB and SFD legacy formats only. No `.glyphs`, `.ufo`, or `.designspace` files are present. These formats are not compatible with gftools-builder.

### Summary

Limelight is a display typeface designed by Nicole Fally with spacing and mastering by Eben Sorkin (Sorkin Type). It was added to Google Fonts on 2011-05-25 and has not been updated since the initial google/fonts repository commit on 2015-03-07.

### METADATA.pb Analysis

The current METADATA.pb at `ofl/limelight/METADATA.pb` contained no source block. Key fields:
- **Family name**: Limelight
- **Designer**: Nicole Fally, Sorkin Type
- **License**: OFL
- **Category**: DISPLAY
- **Date added**: 2011-05-25
- **Source block**: None

### Upstream Repository (librefonts archive)

**Repository**: [librefonts/limelight](https://github.com/librefonts/limelight)

The `librefonts` organization was created on 2013-10-20 by Google Fonts team members (davelab6, felipesanches, pathumego) to decompose the monolithic google/fonts repository into individual per-font source repositories. The Limelight repo was created on 2014-07-16 by Mikhail Kashkin (hash3g) with the commit message "Move limelight font files to separate repository."

The repository is not archived and not a fork. It has 12 commits total, all from 2014, primarily updating Travis CI configuration.

#### Commit History

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `f361773` | 2014-10-17 | hash3g | update .travis.yml |
| `36f4764` | 2014-10-06 | hash3g | Rename fontbakery |
| `288a162` | 2014-09-19 | hash3g | Update .travis.yml |
| `886773d` | 2014-09-15 | hash3g | Update .travis.yml |
| `d3ff1ff` | 2014-09-14 | hash3g | Installing ttfautohint from ppa |
| `0d56b89` | 2014-09-12 | hash3g | Added raw=True to VDMX and FFTM |
| `fdcaa8d` | 2014-09-11 | hash3g | update .travis.yml |
| `338c014` | 2014-08-22 | hash3g | Travis.yml update |
| `5599c12` | 2014-08-22 | hash3g | Travis.yml update |
| `50f7dc1` | 2014-08-21 | hash3g | Travis.yml update |
| `3569785` | 2014-08-19 | hash3g | Added .travis.yml |
| `3001376` | 2014-07-16 | Mikhail Kashkin | Move limelight font files to separate repository |

The HEAD commit (`f361773`) was used as the reference commit. Source files were unchanged after the initial commit (`3001376`); all subsequent commits only modified `.travis.yml` configuration.

### Font Binary History in google/fonts

The font binary `Limelight-Regular.ttf` (132,292 bytes, MD5: `665b887accf0b7deeeb087259fe67d59`) was included in the initial monolithic commit (`90abd17b4`) on 2015-03-07 and has never been updated since.

The FONTLOG indicated version 1.002, dated April 2012, with mastering by Eben Sorkin. The font's head table showed a creation date of April 7, 2012 and modification date of August 20, 2012.

### Verification

- **FONTLOG.txt**: Identical between google/fonts and librefonts/limelight.
- **OFL.txt**: Identical between google/fonts and librefonts/limelight.
- **Version**: Both indicated v1.002 (April 2012).
- The upstream repo contained no TTF binary -- only TTX decompositions and SFD/VFB sources.

### PR History in google/fonts

- **PR #6032** (merged 2023-03-16): "Limelight: Added designer (sorkin)" by emmamarichal -- added "Sorkin Type" to the designer field in METADATA.pb.
- **PR #6031** (merged 2023-06-07): Removed a useless line in Sorkin description.
- No PRs existed for source metadata or font binary updates.

### Build Configuration

An override config.yaml **cannot** be created because:
- The upstream sources are in SFD (FontForge) and VFB (FontLab) formats only.
- These formats are not supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources.
- No modern source files exist in any known repository.

### Conclusion

- **Repository URL**: `https://github.com/librefonts/limelight`
- **Commit**: `f361773b306c507e22a46d18d5e661a6dac84894`
- **Config**: None (SFD/VFB-only sources, not gftools-builder compatible)
- **Confidence**: HIGH
