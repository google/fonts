# Do Hyeon

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Do Hyeon as binaries only (google/fonts at commit `2eb0b48d5f76`).
No source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/dohyeon.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from DoHyeon-Regular.ttf,
  the font Google Fonts ships, with babelfont 58eedc8 (felipesanches/babelfont-rs branch
  2026-10-22: simoncozens/babelfont-rs main plus the TTF reader changes proposed to it):
  its TTF reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/dohyeon at `8607d13340cc`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/dohyeon.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`8607d13340cc` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/baemin/Dohyeon at 1d32c9fa97c9f3d349587b45fe1851ebebd89cae: the
  fonts as built (2 font files); no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/baemin/Dohyeon"
      commit: "1d32c9fa97c9f3d349587b45fe1851ebebd89cae"
    }

## Previous investigation

## Do Hyeon

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Woowahan Brothers
**METADATA.pb path**: `ofl/dohyeon/METADATA.pb`

### Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/baemin/Dohyeon |
| Commit | `1d32c9fa97c9f3d349587b45fe1851ebebd89cae` |
| Config YAML | N/A (no buildable source files) |
| Branch | N/A |

### How the Repository URL Was Found

The repository URL `https://github.com/baemin/Dohyeon` was identified from the METADATA.pb `source { }` block, which was added by batch commit `9a14639f3` on the `sources_info_2026-02-25` branch. The repo belongs to "baemin" (Woowahan Brothers / Baedal Minjok, a Korean food delivery company that sponsors font development).

The repository is publicly accessible and contains pre-compiled font binaries but no font source files.

### How the Commit Hash Was Identified

The commit hash `1d32c9fa97c9f3d349587b45fe1851ebebd89cae` is the HEAD (latest) commit in the baemin/Dohyeon repository. This commit (2020-07-30) is "Update README.md" and is a README-only change.

The repository has only 7 commits:
1. `6e7faae` - Create README.md
2. `cd87ab5` - Create OFL.txt
3. `a372ab8` - Add files via upload (2018-02-07) -- **this is when the font files were uploaded**
4. `d4f32f3` - Update README.md
5. `430b1af` - Update README.md
6. `f876725` - Update README.md
7. `1d32c9f` - Update README.md (2020-07-30) -- **HEAD, recorded in tracking**

The font files were uploaded in commit `a372ab8` (Feb 2018), and the Do Hyeon font was added to google/fonts in PR #1459 (March 2018). Since no specific upstream commit was referenced during onboarding, the HEAD commit was used as the tracking reference. The actual font-relevant commit is `a372ab8`.

### Build Configuration

**No buildable source files exist** in the upstream repository. The repo only contains:
- `FONT/DOHYEON.otf` - Pre-compiled OpenType font
- `FONT/DOHYEON.ttf` - Pre-compiled TrueType font
- `OFL.txt` - License file
- `README.md` - Description

There are no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` source files. The fonts were compiled externally (Korean font binaries were mastered by Aaron Bell, as noted in PR #1459).

There is no `config.yaml` in the upstream repo, and no override `config.yaml` in the google/fonts family directory.

### Google Fonts History

- **2018-03-13**: Do Hyeon added to google/fonts as part of "korean families r01" batch (commit `16680f868`, PR #1459, by Marc Foley). PR notes that "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com".
- **2024-01-19**: Font binary hotfixed by Yanone (commit `c6f978399`) to fix space and nbspace characters. This was a binary-level hotfix, not from upstream sources.

### Issues Found

1. **Commit hash is not font-relevant**: The tracked commit `1d32c9f` is just a README update. The actual font upload commit is `a372ab8`. However, since HEAD is the standard convention for repos where the exact onboarding commit cannot be determined, this is acceptable.
2. **No buildable sources**: The upstream repo only contains pre-compiled binaries. A config.yaml cannot be created since there are no source files to build from. Status correctly remains `missing_config`.
3. **Source block not on main**: The source block with repository_url and commit was added on branch `sources_info_2026-02-25`, not yet merged to main. The current METADATA.pb on main has no source block.
