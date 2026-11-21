# Abril Fatface

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Abril Fatface built from FontForge `.sfd` sources in
https://github.com/librefonts/abrilfatface at commit
`5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f`. There was no source that builds with fontc.
The shipped binary carries FontForge's `FFTM` table, so FontForge generated it. The
directory also holds FontLab `.vfb` files; the `.sfd` is taken as the master because
FontForge generated the shipped fonts and the build from the `.sfd` is functionally
equivalent to them.

## Actions taken

- The work was done on top of the upstream history, in
  https://github.com/googlefonts/abrilfatface.
- Each change to the `.sfd` before conversion is its own commit: Name
  AbrilFatface-Regular as the release does.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last change to the font.

## Final state

The source is https://github.com/googlefonts/abrilfatface at `9d1486e10152`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/abrilfatface.json`:
https://github.com/felipesanches/gf-source-modernization at `488fa72`.

`9d1486e10152` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Where the shipped
binaries differ from the source, the difference is reproduced by a documented commit
before the conversion, never silently corrected. Any improvement is a later commit that
needs its own QA, and is left as future work for an onboarder to review in a font-update
PR.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/abrilfatface"
      commit: "5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f"
    }

## Previous investigation

## Abril Fatface

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: TypeTogether
**METADATA.pb path**: `ofl/abrilfatface/METADATA.pb`

### Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/abrilfatface |
| Commit | `5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f` |
| Config YAML | -- |
| Branch | `master` |

### How the Repository URL Was Found

The repository URL `https://github.com/librefonts/abrilfatface` was identified from the upstream repo cache at `upstream_repos/fontc_crater_cache/librefonts/abrilfatface`. There is no `source { }` block in METADATA.pb at all. The `librefonts` organization on GitHub hosts TTX-decomposed mirrors of many early Google Fonts families, created by Dave Crossland.

Note: TypeTogether (the credited designer) does not appear to have a public GitHub repository for Abril Fatface. The `librefonts/abrilfatface` repo is a legacy TTX mirror, not the original design source.

### How the Commit Hash Was Identified

The upstream repo has only a single commit: `5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f` (dated 2014-10-17, message: "update .travis.yml"). This is the HEAD and only commit of the repository. The commit hash was selected as it represents the complete state of this single-commit repo.

The last font-modifying commit in google/fonts is `90abd17b4f97` from 2015-03-07, with message "Initial commit" (part of the initial google/fonts repository setup). The font was added to Google Fonts on 2011-08-31 according to METADATA.pb, predating this repository's creation.

### How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in the google/fonts family directory (`ofl/abrilfatface/`).

The upstream repo contains only legacy source formats:
- `src/AbrilFatface-Regular-TTF.sfd` (FontForge SFD format)
- `src/AbrilFatface-Regular.vfb` (FontLab VFB format)
- Various `.ttx` decomposed table files
- OTF-related TTX source files

These source formats are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. A config.yaml cannot be meaningfully created without converting the sources to a modern format first.

### Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:27:35 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/AbrilFatface-Regular-TTF.sfd`, `src/AbrilFatface-Regular.vfb`, various `.ttx` files

### Confidence

**Medium**: The repository URL is confirmed and the commit is verified in the upstream repo. However, `librefonts/abrilfatface` is a legacy TTX mirror, not a true design source repository. TypeTogether (the credited designer) may have the original design sources in a different format or location. The font binary in google/fonts predates the librefonts repo (2011 vs 2014). The relationship between this repo and the original font production is indirect -- the repo was created as an archival/reproducibility effort, not as the original design source.

### Open Questions

- Does TypeTogether maintain an original source repository for Abril Fatface with `.glyphs` or `.ufo` sources?
- Since the source formats (SFD/VFB) are not gftools-builder compatible, is there a plan to convert the sources to a modern format?
- Should METADATA.pb be updated to include a `source { }` block pointing to this repo, even though it cannot be built with gftools-builder?
- The font has been in Google Fonts since 2011 and has not been updated since the initial commit. Is an update planned?
