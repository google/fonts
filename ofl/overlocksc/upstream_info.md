# Overlock SC

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Overlock SC built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/overlocksc` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/overlocksc.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/overlocksc at `ce67d0418281`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`ce67d0418281` is the equivalence commit: its build is functionally equivalent to the
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

## Overlock SC — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Summary

Overlock SC is the small-caps companion family to Overlock, designed by Dario Manuel Muhafara of TIPO digital typefoundry (Buenos Aires, Argentina). The original design sources were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned repository was found.

### Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `overlocksc/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

#### Source Files

| File | Format | Notes |
|------|--------|-------|
| `OverlockSC-Regular.vfb` | FontLab VFB | Original source, proprietary binary |
| `OverlockSC-Regular-OTF.vfb` | FontLab VFB | OTF variant |
| `OverlockSC-Regular-TTF.sfd` | FontForge SFD | TrueType hinting variant |
| `OverlockSC-Regular.otf` | Compiled binary | Not a design source |

The primary design sources are VFB files. The SFD file is a FontForge variant for TrueType output. No UFO or Glyphs sources are available.

### Family Details

- **Designer**: Dario Manuel Muhafara (TIPO digital typefoundry)
- **License**: OFL
- **Google Fonts date added**: 2011-12-19
- **Related family**: Overlock (shares upstream source and designer)

### Investigation Details

Overlock SC shares its upstream with Overlock. No GitHub account for Dario Manuel Muhafara was found. The TIPO foundry website (tipo.net.ar) does not link to any source repositories.

The `librefonts/overlock` repository (https://github.com/librefonts/overlock) is a librefonts organization mirror containing VFB and SFD sources for both Overlock and Overlock SC. It is not the designer's own repository.

### Conclusion

The original design sources for Overlock SC are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

### References

- librefonts mirror (shared with Overlock): https://github.com/librefonts/overlock
- TIPO foundry: https://www.tipo.net.ar
- Google Fonts: https://fonts.google.com/specimen/Overlock+SC
