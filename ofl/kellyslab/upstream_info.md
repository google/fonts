# Investigation: Kelly Slab

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `kellyslab/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (4)

| File | Format | Notes |
|------|--------|-------|
| `KellySlab-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KellySlab-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KellySlab-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2011, Denis Masharov <denis.masharov@gmail.com>, with Reserved Font Names 'Kelly', 'Kelly Slab'."

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/kellyslab` containing similar source files. The git log shows commit `ed9a0d2` ("update .travis.yml") with no actual source changes beyond the initial librefonts import. The librefonts repo also contains a FontForge script (`menusubset-kelly.ff`). This librefonts repository is an archival mirror.

There is no publicly known upstream GitHub repository for Denis Masharov's Kelly Slab font.

## Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. No upstream GitHub repository is known for this family.
