# Oleo Script

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Oleo Script (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontForge import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/oleoscript.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from OleoScript-{Bold,Regular}.ttf, the fonts
  Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/oleoscript at `0fbf76846419`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 2 styles. Those tools,
including this family's plan `plans/oleoscript.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`0fbf76846419` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/oleoscript/src/OleoScript-Bold-TTF.sfd,
  src/OleoScript-Regular-TTF.sfd, a FontForge import of the shipped fonts (quadratic
  outlines, its TrueType instructions; tools/probes/ttf_sfd_origin), not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Oleo Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Summary

The original design sources for Oleo Script were found in the `googlefontdirectory-hg` monorepo. The sources are in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found.

### Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oleoscript/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

#### Source Files

| File | Format | Notes |
|------|--------|-------|
| `OleoScript-Regular-OTF.vfb` | FontLab VFB | Proprietary binary, not buildable with gftools |
| `OleoScript-Regular-TTF.sfd` | FontForge SFD | Not buildable with gftools-builder |
| `OleoScript-Bold-OTF.vfb` | FontLab VFB | Proprietary binary, not buildable with gftools |
| `OleoScript-Bold-TTF.sfd` | FontForge SFD | Not buildable with gftools-builder |
| `OleoScript-Regular.otf` | Compiled binary | Not a design source |
| `OleoScript-Bold.otf` | Compiled binary | Not a design source |

No UFO or Glyphs sources are available. The VFB files are the primary design sources, with SFD files serving as TrueType-hinting variants.

### Family Details

- **Designer**: soytutype fonts
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-03-29
- **Copyright**: "Copyright (c) 2012, Soytutype (contact@soytutype.com.ar|soytutype@gmail.com), with reserved fontname 'Oleo'"

### Investigation Details

#### GitHub Search

GitHub was searched for "OleoScript font" and "soytutype". No results were returned for either query. GitHub API search for "OleoScript" returned only four repositories: two librefonts mirrors (`librefonts/oleoscript`, `librefonts/oleoscriptswashcaps`) and two Google Fonts bower packaging repositories.

#### Soytutype Website

The Soytutype website (`www.soytutype.com.ar`) was unreachable (connection refused). No active web presence or GitHub profile was found for Soytutype.

#### Librefonts Mirror

The `librefonts/oleoscript` repository contains the same VFB and SFD source files as the googlefontdirectory-hg monorepo. This is a librefonts mirror, not a canonical designer-owned repository.

#### FONTLOG

The FONTLOG confirmed source files exist in VFB and SFD formats, with an initial release date of 27 March 2012.

### Conclusion

The original design sources for Oleo Script are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern (UFO/Glyphs) sources exist, and no canonical designer-owned repository was found.
