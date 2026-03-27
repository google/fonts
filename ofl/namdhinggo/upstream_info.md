# Namdhinggo — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/silnrsi/font-namdhinggo
- **Branch**: `master`
- **License**: OFL
- **Designer/Maintainer**: SIL International
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/` (only `font-mingzat` found under the `silnrsi` owner directory)

## Source Files

The METADATA.pb `source` block references a GitHub release archive:

- **Archive URL**: https://github.com/silnrsi/font-namdhinggo/releases/download/v3.001/Namdhinggo-3.001.zip
- **Archive version**: v3.001
- **Files mapped from archive** (`Namdhinggo-3.001/` prefix):
  - `OFL.txt`
  - `Namdhinggo-Regular.ttf`
  - `Namdhinggo-Medium.ttf`
  - `Namdhinggo-SemiBold.ttf`
  - `Namdhinggo-Bold.ttf`
  - `Namdhinggo-ExtraBold.ttf`

The font family has 5 static weights (Regular 400, Medium 500, SemiBold 600, Bold 700, ExtraBold 800).

Primary script: Limbu (`Limb`). Subsets: `latin`, `latin-ext`, `limbu`.

## Build System

SIL International fonts typically use the `wscript`-based build system (Python WAF) with UFO or Glyphs sources. Based on the pattern observed in the sibling SIL repo `font-mingzat` (also cached locally), the typical structure includes:
- `source/` directory with UFO sources and a `.designspace` file
- `wscript` build configuration
- `preflight` / `preflightg` scripts

Without local access to the `font-namdhinggo` repo, the exact source format cannot be confirmed. However, given SIL's standard toolchain, UFO sources with a WAF/smith build system is the most likely setup.

## config.yaml Status

- **Present in google/fonts**: No — no `config.yaml` found in `/mnt/shared/google/fonts/ofl/namdhinggo/`
- **METADATA.pb `config_yaml` field**: Not set
- Google Fonts is consuming pre-built binaries from the release archive. A `config.yaml` would be needed to enable building from source within the GF pipeline.

## Notes

- The font covers the Limbu script, which is used to write the Limbu language (spoken in Nepal, India, and Bhutan). This is a relatively rare script in the web font ecosystem.
- Copyright notice covers 2002–2022, indicating a long development history under SIL International.
- Reserved Font Names: "Namdhinggo" and "SIL".
- To fully enrich source metadata (e.g., add `config.yaml`, identify build toolchain, confirm source file format), the upstream repo at https://github.com/silnrsi/font-namdhinggo would need to be cloned and inspected.
- The release archive structure (`Namdhinggo-3.001/`) is the standard SIL distribution format.

## Commit Added (HIGH confidence)

Commit `2c6ac797b061941d1f46c980910982b1b1f240ab` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2023-07-06). This is the most reliable method.
