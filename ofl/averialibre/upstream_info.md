# Averia Libre

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: missing_config
- **Designer**: Dan Sayers

## Source Data

| Field           | Value                                              |
|-----------------|----------------------------------------------------|
| repository_url  | https://github.com/librefonts/averialibre           |
| commit          | 091de18a939349eeae407b64f045296a771f6882            |
| config_yaml     | none (TTX-only sources)                             |

## How URL Found

The METADATA.pb in google/fonts has no source block and no `repository_url`. The cached upstream repo at `fontc_crater_cache/librefonts/averialibre` has its git remote set to `https://github.com/librefonts/averialibre`. This is a `librefonts` organization repo, part of a large collection of Google Fonts family mirrors that were created around 2014. The repo contains the same TTX-decomposed source files and metadata files (FONTLOG.txt, OFL.txt, DESCRIPTION.en_us.html) that correspond to this font family.

## How Commit Identified

The upstream repo has only a single commit:

- `091de18` (2014-10-17) by hash3g: "update .travis.yml" -- this is the initial (and only) commit, which added all TTX source files, the Travis CI configuration, and metadata files.

There is no other commit to choose from. The repo's `src/VERSIONS.txt` records all fonts at Version 1.001, while the fonts currently in google/fonts are v1.002 (updated via PR #837 in August 2017 by Marc Foley). This means the upstream repo predates the last font update in google/fonts and was never updated to reflect the v1.002 hotfix.

### google/fonts commit history for `ofl/averialibre/`:

1. `90abd17` (2015-03-07) -- Initial commit of the google/fonts repo (bulk import)
2. `fc10731` (2017-08-07) -- "hotfix-averialibre: v1.002 added" (PR #837 by Marc Foley). Updated all 6 TTF files with minor size changes and updated DESCRIPTION.en_us.html and METADATA.pb.
3. `76adaf1` (2021-11-01) -- deploy commit that temporarily removed and re-added files (infrastructure change)
4. Several metadata-only commits (METADATA.pb format changes, language support updates)

The v1.002 hotfix (PR #837) is the last substantive update to the font binaries. The PR body was empty, providing no upstream reference. Since the upstream repo was never updated past v1.001, the v1.002 binaries were likely produced by Marc Foley directly from the TTX sources with modifications, or from a separate pipeline not reflected in the upstream repo.

## How Config Resolved

The upstream repo contains **no gftools-builder compatible sources**. The only "source" files are TTX (FontTools XML) decompositions of the TTF font tables:

- 6 master `.ttx` files (one per style: Regular, Bold, Italic, BoldItalic, Light, LightItalic)
- Each master `.ttx` references multiple table-specific `.ttx` files (e.g., `_g_l_y_f.ttx`, `_c_m_a_p.ttx`, `_k_e_r_n.ttx`, etc.)

There are **no** `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files anywhere in the repo. The `.travis.yml` shows a `fontbakery-build.py` pipeline from 2014, which is a legacy build system, not gftools-builder.

The font was created by Dan Sayers using an algorithmic averaging process (averaging all 725 OFL fonts from Google Fonts as of November 2011). There are no traditional editable design sources -- the font outlines were generated programmatically. The TTX files are the closest thing to "source" that exists.

**An override config.yaml cannot be created** because gftools-builder requires `.glyphs`, `.ufo`, or `.designspace` sources. TTX files are not a supported input format for gftools-builder.

## Conclusion

Averia Libre has a known upstream repository at `https://github.com/librefonts/averialibre` with a single commit (`091de18`). However, the repo only contains TTX-decomposed font data from v1.001, while google/fonts serves v1.002 (updated in 2017). The font was created algorithmically by averaging other fonts, so no traditional design sources exist. No config.yaml can be created because the sources are TTX-only, which is not compatible with gftools-builder. Status is `missing_config` with the note that this is inherent to the font's nature -- there are no editable design sources to build from.
