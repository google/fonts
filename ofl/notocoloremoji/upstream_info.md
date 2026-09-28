# Noto Color Emoji - Source Metadata Investigation
**Model**: Claude Opus 5.5
**Date**: 2026-09-28

## Initial state
- METADATA.pb had a source block with an empty `repository_url`, an `archive_url` pointing at the `main` branch zip of googlefonts/noto-emoji, the mapping `noto-emoji-main/fonts/Noto-COLRv1.ttf` -> `NotoColorEmoji-Regular.ttf`, `branch: "main"`, and no `commit` or `config_yaml`. The block came from the upstream.yaml of the first upload (335064e83, 2022-07-27) and was merged into METADATA.pb by 66f91f10f (2024-04-03).
- The shipped binary was last replaced by PR #10891 (205859f68, 2026-09-03, name ID 5 `Version 3.055;GOOG;noto-emoji:20260821:86225d3d8316a1b42d84758bcf57a1968fcb724e`) and PR #10950 (142c8963e, 2026-09-09, `Version 2.055;GOOG;noto-emoji:20260909:d95d1b76f2c62771c34acbbcd7269145e8398e10`). #10950 changed only the head and name tables. Neither PR had a description or named an upstream commit.

## Actions taken
- The repo archive mirror of googlefonts/noto-emoji was synced (main 8998f5dd6 -> e20cbc2bb). Its refs, including `refs/pull/*`, matched `git ls-remote` of the GitHub repository.
- The name ID 5 string was traced. It is maintained by hand in `NotoColorEmoji.tmpl.ttx.tmpl`, and `colrv1_postproc.py` copies the CBDT font's name table into the COLRv1 font. For every published version, the recorded hash is the parent of the commit that bumped the version. No version of the template in any public ref contains 2.055 or 3.055.
- The recorded hashes were resolved. 86225d3d (v3.055), d95d1b76 (v2.055), fc4ca365 (public v2.057), e92753bf (v2.051) and 30d0ecb3 (v2.045) are in no ref, and github.com returns 404 for 86225d3d and d95d1b76. The hashes of v2.041 (69db1642, on main) and of v2.042, v2.047 and v2.048 (7f49a00d, 6c211821 and c7a259fc, only on branch `sf`) exist.
- All 62 blob/path pairs of `fonts/Noto-COLRv1*.ttf` and `2D/fonts/Noto-COLRv1*.ttf` in every ref were read, and none is v2.055 or v3.055. The public Emoji 18 build is v2.057 (`2D/fonts/Noto-COLRv1.ttf`, added by 1ffdd21 and merged to main on 2026-09-17; release tag v2026-09-24-unicode18_0, "2D - v2.057").
- The onboarding pipeline was confirmed on earlier releases:
  - Shipped v2.042 (cc4c9099f) was byte-identical to upstream `fonts/Noto-COLRv1.ttf` at f06dfe7cf.
  - Shipped v2.041, v2.047 and v2.048 kept glyf, loca, CPAL and name identical to the public builds and added an SVG table with nanoemoji's maximum_color, as google/fonts 45be8f593 ("Ran maximum_color") did for v2.042.
  - Shipped v2.048 matched upstream v2.048 in all 3905 emoji sequences.
- Shipped v2.055 was compared with public v2.057 emoji by emoji (flattened COLRv1 paint per cmap codepoint and GSUB ligature). Both have 1508 codepoints and 4072 sequences, and 18 sequences differ in layers, fills or outline structure:
  - U+1FAC4 pregnant person and its 5 skin tones use teal #00BDA3/#06927F where v2.057 uses orange #F06E00/#DA4C00.
  - U+1F463 footprints and U+1F43E paw prints are grey #616266 instead of blue #176BC6.
  - U+1F3C2 snowboarder, in 5 variants, has 23-24 layers instead of 45.
  - U+1F4AB, U+1F4F4, U+1F600, U+1F635 U+200D U+1F4AB and U+1F6DC also differ.
- The public SVGs were checked. `2D/svg/` at main (added by 9411589) carries the v2.057 colours, and no version of these SVGs in any ref carries the shipped colours. A nanoemoji 0.15.9 build of 12 of the SVGs reproduced v2.057, not v2.055.
- The build path was checked. Upstream compiles the SVGs with nanoemoji from `colrv1/*.toml` and post-processes them with `colrv1_postproc.py`, which needs the CBDT font built by `make`. No .glyphs, .ufo or .designspace sources exist, so no upstream or override config.yaml was written. At main, the TOML files and `colrv1_postproc.py` still use the old `../svg/` and `fonts/` paths.
- `repository_url` was set to https://github.com/googlefonts/noto-emoji.

## Final state
- METADATA.pb records `repository_url: "https://github.com/googlefonts/noto-emoji"`. No `commit` or `config_yaml` was recorded, for three reasons: the shipped build commit d95d1b76 (2026-09-09) is not public, no public commit contains the shipped binary or its sources, and the family has no gftools-builder sources. The shipped binary is nanoemoji's maximum_color output applied to an unpublished COLRv1 build.
- `archive_url`, `branch` and the file mapping were left unchanged. The mapping has not resolved since 2026-09-17, when 1ffdd21 moved `fonts/` to `2D/fonts/`. googlefonts/noto-emoji PR #571 proposed restoring the old paths and was closed unmerged on 2026-09-25.

## Previous investigation (2026-03-12)
**Model**: Claude Opus 4.6

### Source Repository
- **URL**: https://github.com/googlefonts/noto-emoji (archive_url only; repository_url is empty)
- **Commit**: `N/A`
- **Status**: Source block present (archive_url only, no repository_url or commit)

### What Was Done
The existing source metadata was reviewed. The source block contained an archive_url pointing to the noto-emoji GitHub repository's main branch zip, but no repository_url or commit hash was recorded.

### Notes
- **Designer**: Google
- **Script**: Emoji (color)
- **Category**: SANS_SERIF (symbols)
- Part of the Google Noto Emoji project at github.com/googlefonts/noto-emoji. Provides COLRv1 color emoji coverage.
