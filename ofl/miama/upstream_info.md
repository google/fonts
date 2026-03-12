# Miama — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

The most complete upstream repository found is the librefonts mirror on GitHub:

- **URL**: https://github.com/librefonts/miama
- **Type**: Non-fork repository (not marked as fork on GitHub)
- **Last commit**: `c1383daa982130014964e87cb5394eb6f4d7a2cc` (2014-10-17, "update .travis.yml")

The designer, Linus Romer (`linus.romer@gmx.ch`), does not appear to maintain a dedicated GitHub repository for Miama. His GitHub account (`linusromer`) contains tooling repositories (curvatura, mf2outline, etc.) but no Miama font repo.

The authoritative distribution source is **CTAN**: https://ctan.org/pkg/miama — the latest CTAN release is version 1.2 (January 15, 2025). CTAN provides a zip archive at `https://mirrors.ctan.org/fonts/miama.zip`. The CTAN package does not provide a public version-control URL.

## Source Files

In the `librefonts/miama` repository, source files are under `src/`:

- `src/Miama.sfd` — FontForge source file (main master, 655 KB)
- `src/Miama-Regular-TTF.sfd` — FontForge source file (TTF-specific export)
- `src/Miama.otf.*.ttx` — ttx table dumps of the OTF build
- `src/Miama.ttf.*.ttx` — ttx table dumps of the TTF build
- `src/VERSIONS.txt` — notes version as `Miama-Regular.ttf: 0.32`

The `.sfd` files (FontForge native format) are the canonical source. The repo also contains a `menusubset-miama.ff` FontForge script at the root.

CTAN provides the same font (version 1.2 as of 2025-01-15), but CTAN does not expose the `.sfd` source via a public repository.

## Build System

The `librefonts/miama` repo uses a legacy `fontbakery-build.py` CI pipeline via `.travis.yml`, driven by FontForge + ttfautohint. This build system is obsolete (Travis CI is no longer free; fontbakery-cli as used here is a very old version).

No modern build system (e.g., gftools builder, fontmake) is present in any known upstream source.

## config.yaml Status

No `config.yaml` exists in `/mnt/shared/google/fonts/ofl/miama/`. None exists in the upstream repositories found.

## Notes

- The `librefonts/miama` repo is a legacy mirror from around 2014 and has not been updated since. It predates the current Google Fonts workflow.
- The most current version (1.2, released 2025-01-15) is available on CTAN, but without a public VCS URL. Linus Romer should be contacted at `linus.romer@gmx.ch` to obtain the current source files or a repository URL.
- The CTAN release date of 2025-01-15 strongly implies ongoing maintenance; the designer is actively updating the font even if the source is not publicly hosted on GitHub.
- The font was drawn using FontForge; `.sfd` is the native source format.
- The `librefonts` organization on GitHub appears to be an old Google Fonts mirror project; all its repos were last updated in 2014 and are likely outdated relative to current font versions.
- A config.yaml would need to be authored from scratch for any future Google Fonts rebuild.
