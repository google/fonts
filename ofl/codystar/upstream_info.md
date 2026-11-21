# Codystar

**Model**: Claude Opus 5.5
**Date**: 2026-11-17

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Codystar (google/fonts at commit `2086013c4c53`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/codystar.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Codystar-{Light,Regular}.ttf, the fonts Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/codystar at `7bfc4fb2c00b`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts cc39c4c2c304 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF, hinting), 2 styles. Those
tools: https://github.com/felipesanches/gf-source-modernization at `c061ad8`.

`7bfc4fb2c00b` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/codystar at e32d050fbb01232b6a85423b121da89f21bba8b3
  (the repository google/fonts recorded): src/Codystar-Light-TTF.vfb and
  src/Codystar-Regular-TTF.vfb, a FontLab import of the shipped fonts (a -TTF .vfb,
  P13), not a source; the rest are the release's tables as TTX.

## Future work

Not part of what Google Fonts ships; for review in a font-update PR:
- commit `a269201` (after the equivalence commit): README: say what the earlier sources
  are, and list them

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/codystar"
      commit: "e32d050fbb01232b6a85423b121da89f21bba8b3"
    }

## Previous investigation

## Codystar - Investigation Report

### Source Data

| Field | Value |
|-------|-------|
| Family Name | Codystar |
| Designer | Neapolitan (Font Diner) |
| Repository URL | https://github.com/librefonts/codystar |
| Commit Hash | e32d050fbb01232b6a85423b121da89f21bba8b3 |
| Branch | master (default) |
| Config YAML | N/A (override config.yaml in google/fonts) |
| Override Config | Yes |
| Status | complete |

### How URL Was Found

The repository URL `https://github.com/librefonts/codystar` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") on January 14, 2024. The librefonts organization on GitHub hosts many font families that were originally contributed to Google Fonts.

### How Commit Was Determined

The commit `e32d050fbb01232b6a85423b121da89f21bba8b3` (dated July 16, 2014) is the initial commit in the repository with message "Move codystar font files to separate repository". This is the oldest and most foundational commit. Subsequent commits (9 more, up to October 2014) only add CI/Travis configuration and do not modify the font source files.

The commit was recorded in the METADATA.pb source block (commit `a76a3a1b3`, "sources info for Codystar", by Felipe Sanches on November 21, 2025). The original google/fonts commit referenced was `90abd17b4` (Initial commit).

### Config YAML Status

**Override config.yaml exists** in google/fonts at `ofl/codystar/config.yaml`:

```yaml
buildVariable: false
sources:
  - src/Codystar-Regular-TTF.vfb
  - src/Codystar-Light-TTF.vfb
```

The upstream repository only contains `.vfb` (FontLab binary) source files in `src/`:
- `src/Codystar-Regular-TTF.vfb`
- `src/Codystar-Light-TTF.vfb`

No `.ufo`, `.glyphs`, or `.designspace` files exist. The override config.yaml correctly references the VFB sources.

### Verification

- **Repository accessible**: Yes, https://github.com/librefonts/codystar is accessible
- **Commit exists**: Yes, `e32d050f` is present (it is the initial commit)
- **Source block on main**: Yes, the full source block (repository_url + commit) is on main
- **Override config exists**: Yes, at `ofl/codystar/config.yaml`
- **Config references correct files**: Yes, the VFB files referenced in config.yaml match the source files at the recorded commit

### Confidence Level

**High**. This is a straightforward case. The repository has minimal history (10 commits, all from 2014), the commit hash points to the initial commit which contains the actual font sources, and an override config.yaml is already in place.

### Open Questions

None. This family is complete.
