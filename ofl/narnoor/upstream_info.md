# Narnoor — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/silnrsi/font-narnoor
- **Branch**: `master`
- **License**: OFL
- **Designer/Maintainer**: SIL International
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/` (only `font-mingzat` found under the `silnrsi` owner directory)

## Source Files

The METADATA.pb `source` block references a GitHub release archive:

- **Archive URL**: https://github.com/silnrsi/font-narnoor/releases/download/v3.000/Narnoor-3.000.zip
- **Archive version**: v3.000
- **Files mapped from archive** (`Narnoor-3.000/` prefix):
  - `OFL.txt`
  - `Narnoor-Regular.ttf`
  - `Narnoor-Medium.ttf`
  - `Narnoor-SemiBold.ttf`
  - `Narnoor-Bold.ttf`
  - `Narnoor-ExtraBold.ttf`

The font family has 5 static weights (Regular 400, Medium 500, SemiBold 600, Bold 700, ExtraBold 800).

Primary script: Gunjala Gondi (`Gong`). Subsets: `gunjala-gondi`, `latin`, `latin-ext`, `math`, `symbols`.

## Build System

SIL International fonts typically use the `wscript`-based build system (Python WAF / smith) with UFO sources. Based on the pattern observed in the sibling SIL repo `font-mingzat`, the typical structure includes:
- `source/` directory with UFO sources and a `.designspace` file
- `wscript` build configuration (WAF/smith build system)
- `preflight` / `preflightg` scripts

Without a local clone of `font-narnoor`, the exact source format cannot be confirmed. However, SIL's standard smith/WAF toolchain with UFO sources is the most likely setup.

## config.yaml Status

- **Present in google/fonts**: No — no `config.yaml` found in `/mnt/shared/google/fonts/ofl/narnoor/`
- **METADATA.pb `config_yaml` field**: Not set
- Google Fonts is consuming pre-built binaries from the release archive. A `config.yaml` would be needed to enable building from source within the GF pipeline.

## Notes

- The font covers the Gunjala Gondi script, used for the Gondi language spoken in central India. This is a rare and recently-encoded script (Unicode 11.0, 2018).
- Complex copyright attribution: the font originates from CDAST, University of Hyderabad (2014–2017), with additions by SIL International (2015–2023), and Latin glyphs from Adobe Source (with Reserved Font Name 'Source').
- Stroke classification: `SANS_SERIF`.
- The `math` and `symbols` subsets are notable for a script-focused font — this likely reflects Unicode coverage of mathematical or general symbols in the Latin/symbols range.
- To fully enrich source metadata and determine if a `config.yaml` can be added, the upstream repo at https://github.com/silnrsi/font-narnoor would need to be cloned and inspected.
- The release archive structure (`Narnoor-3.000/`) follows the standard SIL distribution format.

## Commit Added (HIGH confidence)

Commit `53fa5d8f5c3afecd9c2247ef7c8b26a02208f267` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2023-11-02). This is the most reliable method.
