# Ovo

**Model**: Claude Opus 5.5
**Date**: 2026-11-20

Sources modernized 2026-11: https://github.com/googlefonts/ovo held only FontLab
(`.vfb`) and FontForge (`.sfd`) files, and the `.sfd` files are imports of the fonts
Google Fonts ships, so those fonts were converted to Glyphs (`.glyphs`) sources, which
build with gftools-builder and fontc. The repository, commit and config are in the
`source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Ovo with https://github.com/googlefonts/googlefontdirectory-hg at
`52f780bc9d19` recorded as its source. That repository and
https://github.com/googlefonts/ovo (at `a14af03d3960`) hold the same files:
`src/Ovo-Regular-TFF.sfd`, `src/Ovo-Regular.vfb`. The `.sfd` files are imports of the
shipped fonts, and the family could not be built with fontc.

## Actions taken

- The work was done on top of the history of https://github.com/googlefonts/ovo, in a
  pull request merged into its default branch.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Ovo-Regular.ttf, the
  font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/ovo at `c773c708edf5`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts cc39c4c2c304 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF, hinting), 1 style. Those tools,
including this family's plan `plans/ovo.json`:
https://github.com/felipesanches/gf-source-modernization at `2648f55`.

`c773c708edf5` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Ovo — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Summary

Ovo is a medium-contrast serif font designed by Nicole Fally, mastered by Eben Sorkin of SorkinType. The original design sources were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found, and the SorkinType GitHub organization does not contain an Ovo repository.

### Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ovo/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

#### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Ovo-Regular.vfb` | FontLab VFB | Original source, proprietary binary |
| `Ovo-Regular-TFF.sfd` | FontForge SFD | TrueType variant (note: filename has "TFF" typo) |
| `Ovo-Regular.otf` | Compiled binary | Not a design source |

The VFB file is the primary design source. No UFO or Glyphs sources are available.

### Family Details

- **Designer**: Nicole Fally (original design), Eben Sorkin (spacing and mastering)
- **License**: OFL
- **Google Fonts date added**: 2011-07-20
- **Copyright**: Sorkin Type Co (www.sorkintype.com)

Nicole Fally created the initial version (v1.000, July 2010) in FontLab VFB format. Eben Sorkin completed the mastering and TTF conversion (v1.002, July 2011). The FONTLOG credits Nicole Fally (nf@t-g-d.at, www.t-g-d.at) as the original designer.

### Investigation Details

#### Designer Profiles

- GitHub user search for "nicolefally": no account found
- GitHub repository search for "ovo font": no relevant font repository found
- SorkinType GitHub organization (https://github.com/SorkinType): reviewed all 70+ repositories — no Ovo repository exists

#### Librefonts Mirror

The `librefonts/ovo` repository (https://github.com/librefonts/ovo) contains the same VFB and SFD source files as the googlefontdirectory-hg monorepo. The FONTLOG confirms the original design was created in FontLab (VFB format).

### Conclusion

The original design sources for Ovo are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. Neither Nicole Fally nor Eben Sorkin maintain a public GitHub repository for this font.

### References

- librefonts mirror: https://github.com/librefonts/ovo
- SorkinType GitHub: https://github.com/SorkinType
- Google Fonts: https://fonts.google.com/specimen/Ovo
