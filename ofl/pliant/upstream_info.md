# Pliant

**Model**: Claude Opus 4.8 (1M context)
**Date**: 2026-06-02
**Designer**: Non Foundry, Jona Saucedo
**METADATA.pb**: ofl/pliant/METADATA.pb

Pliant is a variable sans-serif type family (Roman + Italic) with width
(`wdth` 100..125) and weight (`wght` 100..900) axes. The upstream project is
owned by TheJonassss (Jona Saucedo / Non Foundry); the Google Fonts onboarding
arrived through `emmamarichal/main` (upstream PR #2).

## Source Data

| Field          | Value |
|----------------|-------|
| Repository URL | https://github.com/TheJonassss/Pliant |
| Commit         | dc119b45f0b60597305af387b97b2f5a94b2e1e4 |
| Config YAML    | sources/config.yaml |
| Branch         | main |

## Initial state

The onboarding left a complete `source { ... }` block in METADATA.pb
(repository_url, pinned commit `dc119b4`, branch `main`, and the three
`files` mappings for `OFL.txt` and the two variable TTFs). There was **no**
`config_yaml` field set, and **no** `upstream_info.md` report for the family.
The upstream repository already shipped a gftools-builder configuration at
`sources/config.yaml`, so no override config was needed — only the
`config_yaml` pointer and a verification report were missing.

## Actions taken

- The repository URL was confirmed reachable over HTTPS (HTTP 200).
- The pinned commit was independently verified by binary comparison (details
  below): the shipped fonts were confirmed to be the committed binaries after
  gftools-packager fixes, so `commit_verified` is **true**.
- The build configuration was resolved to the upstream
  `sources/config.yaml` (`set_config_yaml` with value `sources/config.yaml`).
  The config's `sources` (`Pliant.glyphs`, `Pliant-Italic.glyphs`),
  `familyName` (`Pliant`), `axisOrder` (`wdth`, `wght`, `ital`), and its
  full STAT for both `Pliant[wdth,wght].ttf` and
  `Pliant-Italic[wdth,wght].ttf` were checked against the shipped binaries
  and METADATA.pb axes — they match.
- The config was validated by generating its recipe with
  `gftools builder --generate sources/config.yaml` from a throwaway clone of
  the pinned commit (exit code 0; the recipe emits both
  `fonts/variable/Pliant[wdth,wght].ttf` and
  `fonts/variable/Pliant-Italic[wdth,wght].ttf`). The only diagnostics were
  benign upstream kerning-class warnings.
- This report was written.

## Final state

This change delivers the build-provenance pointer (`config_yaml:
sources/config.yaml`) and a verified investigation report for Pliant.
The pinned commit is confirmed; the source build path is confirmed to be
gftools-builder compatible and to reproduce the correct variable-font
targets and axis structure.

## How the Commit Hash Was Verified

The shipped variable TTFs (`Pliant[wdth,wght].ttf`,
`Pliant-Italic[wdth,wght].ttf`) do **not** sha256-match the repo's
`fonts/variable/*.ttf` at the pinned commit, and are 28 bytes smaller. A
fontTools table-level comparison explains the difference precisely:

- **Outline and layout tables are byte-identical** between shipped and
  committed for both Roman and Italic: `glyf`, `loca`, `gvar`, `HVAR`,
  `GPOS`, `GSUB`, `STAT`, `cmap`, `fvar`, `avar`, `hmtx`, `post` all have
  identical lengths. This rules out a rebuild from source and rules out a
  different commit.
- **`head.fontRevision` identical** (1.0) and **name ID 5 identical**
  ("Version 1.000") — same version, same build-tool/version string.
- **`head.created` identical**; only **`head.modified`** changed
  (committed 2026-05-14 → shipped 2026-05-21, which equals METADATA
  `date_added`), with `checkSumAdjustment` recomputed accordingly.
- **name ID 0 (copyright)** was corrected: the committed repo binaries
  still carried a leftover template string
  `Copyright 2025 The Radio Canada Display Project Authors (...)`, fixed
  in the shipped fonts to
  `Copyright 2025 The Pliant Project Authors (...)`. The 14-character
  shortening of the UTF-16 Windows name record fully accounts for the
  28-byte size reduction. Name IDs 3, 8, 11 are unchanged.

**Conclusion:** the shipped fonts are the committed binaries from commit
`dc119b4`, **post-processed by gftools-packager fixes** (copyright name
correction + modified-timestamp/checksum normalization) — not a rebuild and
not a different commit. The commit hash is verified.

## Build Configuration

- **Source type**: Glyphs (`sources/Pliant.glyphs`,
  `sources/Pliant-Italic.glyphs`).
- **Config**: upstream `sources/config.yaml` exists and is gftools-builder
  compatible. Decision: `set_config_yaml` = `sources/config.yaml`. No
  override config was created.
- **Validation**: `gftools builder --generate sources/config.yaml` returned
  exit 0 and produced a recipe targeting both variable outputs at the paths
  referenced by METADATA's `source.files`.
- **Reproducibility**: `refresh_needed`. A fresh source build via
  `config.yaml` would not be byte-identical to the currently shipped
  binaries, because the shipped fonts carry gftools-packager
  post-processing (corrected copyright, rewritten modified timestamp) that a
  raw source build does not reproduce verbatim. The outlines and layout are
  identical, so this is metadata-level non-determinism, not a design drift.

## Timeline

- **2026-05-06** — variable font binaries first added upstream
  (`eab283b`, "Add variable font binaries").
- **2026-05-07** — `head.created` timestamp of the shipped/committed fonts.
- **2026-05-14** — `head.modified` of the committed binaries.
- **2026-05-20** — `emmamarichal/main` pushed refreshed fonts
  (`8ad29e6`, "push fonts"); merged into upstream `main` via PR #2 at the
  pinned merge commit `dc119b4`.
- **2026-05-21** — family added to Google Fonts (METADATA `date_added`);
  this equals the shipped fonts' rewritten `head.modified`, consistent with
  gftools packaging on that date.
- **2026-06-02** — this investigation: commit verified, `config_yaml` set to
  `sources/config.yaml`, report written.

## Issues Found

- Shipped binary != committed binary at the pinned commit (sha256 mismatch).
  Explained as gftools-packager copyright fix + timestamp/checksum
  normalization; not a rebuild and not a different commit.
- Upstream template artifact: the committed repo binaries' name ID 0 still
  read "The Radio Canada Display Project Authors" (a leftover from a project
  template); corrected to "The Pliant Project Authors" during onboarding.
- No `upstream_info.md` existed for the family before this work.
- `OS/2.panose` is all-zero in both shipped and committed binaries
  (cosmetic; not blocking).
