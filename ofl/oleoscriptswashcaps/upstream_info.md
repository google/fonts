# Oleo Script Swash Caps

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Oleo Script Swash Caps (google/fonts at commit `2fe1e8c6b137`). Its
only published source is a FontForge import of the shipped fonts, not a design source
(listed under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the
binary files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/oleoscriptswashcaps.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from OleoScriptSwashCaps-{Bold,Regular}.ttf,
  the fonts Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs
  branch 2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it
  (#117, typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/oleoscriptswashcaps at `74fc46cc9011`.
Builds with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 2 styles. Those tools,
including this family's plan `plans/oleoscriptswashcaps.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`74fc46cc9011` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6:
  ofl/oleoscriptswashcaps/src/OleoScriptSwashCaps-Bold-TTF.sfd,
  src/OleoScriptSwashCaps-Regular-TTF.sfd, a FontForge import of the shipped fonts
  (quadratic outlines, its TrueType instructions; tools/probes/ttf_sfd_origin), not a
  source: Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Oleo Script Swash Caps — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oleoscriptswashcaps/src/`

#### Source Files in googlefontdirectory-hg

- `OleoScriptSwashCaps-Regular-OTF.vfb` — FontLab source for Regular weight (proprietary format, not buildable with gftools)
- `OleoScriptSwashCaps-Bold-OTF.vfb` — FontLab source for Bold weight (proprietary format, not buildable with gftools)
- `OleoScriptSwashCaps-Regular-TTF.sfd` — FontForge SFD for Regular (converted from VFB, not buildable with gftools-builder)
- `OleoScriptSwashCaps-Bold-TTF.sfd` — FontForge SFD for Bold (converted from VFB, not buildable with gftools-builder)
- `OleoScriptSwashCaps-Regular.otf` — compiled OTF binary (not a design source)
- `OleoScriptSwashCaps-Bold.otf` — compiled OTF binary (not a design source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The primary design sources are the `.vfb` files (FontLab proprietary format). The `.sfd` files are TTF-flavored conversions. Neither format is buildable with gftools-builder.

### Family Details

- **Designer**: soytutype fonts
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-11-12
- **Copyright**: "Copyright (c) 2012, Soytutype (contact@soytutype.com.ar|soytutype@gmail.com), with reserved fontname 'Oleo'"

### Search Results

- GitHub was searched for "OleoScript", "soytutype", and related terms — no designer-owned repositories found
- GitHub API search for "OleoScript" returned only four repositories, all mirrors or packaging repos
- The Soytutype website (`www.soytutype.com.ar`) was unreachable (connection refused)
- No active GitHub profile was found for Soytutype
- No cached clone found in `/mnt/shared/upstream_repos/fontc_crater_cache/`

### Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/oleoscriptswashcaps — contains the same VFB and SFD files as googlefontdirectory-hg. This is a mirror, not a canonical designer-owned repository.

### Relationship to Oleo Script

Oleo Script Swash Caps is explicitly described as a "sister family" to Oleo Script, both produced by Soytutype in 2012. The FONTLOG for this family references the same source file structure as Oleo Script.

### Notes

- No canonical upstream repository with Glyphs or UFO sources exists for Oleo Script Swash Caps.
- The original sources were in FontLab VFB format, preserved in googlefontdirectory-hg.
- The googlefontdirectory-hg monorepo is the only known location of the original source files (aside from the librefonts mirror).
- Confidence in source identification: **High** — the VFB files in googlefontdirectory-hg are the original design sources. However, the proprietary format limits usefulness for rebuilding.
