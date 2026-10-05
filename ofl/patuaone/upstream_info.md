# Patua One

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Patua One built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/patuaone` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/patuaone.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/patuaone at `d380c3be2b3d`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`d380c3be2b3d` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Where the shipped
binaries differ from the source, the difference is reproduced by a documented commit
before the conversion, never silently corrected. Any improvement is a later commit that
needs its own QA, and is left as future work for an onboarder to review in a font-update
PR.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Patua One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/patuaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files

- **.vfb** (FontLab, proprietary): PatuaOne-Regular-OTF.vfb
- **.sfd** (FontForge): PatuaOne-Regular-TTF.sfd
- **Compiled binary** (not a design source): PatuaOne-Regular.otf
- **Metadata**: METADATA_comments.txt

The design sources are VFB (FontLab, proprietary) and SFD (FontForge) format files. Neither format is buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

### Investigation

The METADATA.pb listed the designer as LatinoType with copyright held by LatinoType Limitada (info@latinotype.com), dated 2011.

The DESCRIPTION.en_us.html described Patua One as a slab serif text type designed for use in small sizes with low contrast and strong serifs. No upstream repository link was present.

No FONTLOG.txt file was found in the google/fonts ofl/patuaone/ directory.

Web searches were conducted for a LatinoType GitHub organization, for "latinotype/patua" or related repository names, and for any public upstream source for Patua One. No results were found. LatinoType does not appear to maintain a public GitHub presence for their font sources.

### Conclusion

No canonical upstream repository was found beyond the legacy googlefontdirectory-hg archive. LatinoType does not appear to maintain a public GitHub repository for Patua One. Sources exist as VFB/SFD files, which are not buildable with gftools-builder. No METADATA.pb changes were made.
