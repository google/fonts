# Merienda — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/etunni/merienda
- **Default branch**: `master`
- **Pinned commit**: `15f2f36d29595fa3dd6cf068323ef44bc0713b56`
- **Commit date**: 2022-10-13
- **Commit message**: "Merge pull request #8 from emmamarichal/master — Interpolation issues"
- **Commit author**: Eduardo Rodríguez Tunni
- **Repo created**: 2013-12-30
- **Last updated**: 2024-05-22

## Source Files

- **Primary source**: `sources/Merienda.glyphs` (Glyphs format, ~1.3 MB)
- **Output fonts**:
  - `fonts/variable/Merienda[wght].ttf` — variable font (wght axis: 300–900)
  - `fonts/ttf/` — static TTFs: Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700), ExtraBold (800), Black (900)
  - `fonts/otf/` — static OTFs
  - `fonts/webfonts/` — web font formats
- **Documentation**: `documentation/` directory (contents not fully enumerated)
- **License**: `OFL.txt`
- **Author info**: `AUTHOR.txt`

## Build System

- **Build tool**: `gftools builder` (via `sources/config.yaml`)
- **Build file**: no `Makefile` found in repo root
- **CI**: no `.github/workflows/` directory found in the etunni/merienda repo
- **STAT table**: explicitly defined in `config.yaml` for `Merienda[wght].ttf` with named instances: Light (300), Regular (400, linkedValue: 700, flags: 2), Medium (500), SemiBold (600), Bold (700), ExtraBold (800), Black (900)

## config.yaml Status

- **Present**: yes — `sources/config.yaml`
- **Correctly referenced in METADATA.pb**: yes — `config_yaml: "sources/config.yaml"`
- **Key settings**:
  - `sources: [Merienda.glyphs]`
  - `axisOrder: [wght]`
  - `familyName: Merienda`
  - Full STAT table definition with 7 named weight instances
- **Note**: the config.yaml uses a non-standard indentation (4-space indent at top level) which may indicate it was originally nested inside a larger YAML document and extracted. It is syntactically valid.

## Notes

- Merienda is a Spanish word meaning "afternoon snack." The font was designed by Eduardo Rodríguez Tunni (edu@tipo.net.ar) as a slightly condensed, brush-influenced handwriting face suitable for headlines.
- Supports `latin`, `latin-ext`, and `vietnamese` subsets; wght axis covers 300–900.
- The pinned commit (`15f2f36d`) is the current HEAD of `master` as of the investigation date — no commits since 2022-10-13.
- PR #8 (merged at the pinned commit) was contributed by Emma Marichal and corrected interpolation issues on glyphs: s, €, ₲, ₺, ¥.
- The repo has no GitHub Actions CI configured; builds are done manually.
- No upstream cache found at `/mnt/shared/upstream_repos/fontc_crater_cache/etunni/merienda`.
- The `files` block in METADATA.pb maps only `OFL.txt` and `fonts/variable/Merienda[wght].ttf` — no DESCRIPTION or article files are mapped, which is consistent with the absence of a `DESCRIPTION.en_us.html` in the ofl/merienda working directory.
- The repo is independently maintained by the original designer (etunni organization), not under the googlefonts organization. Emma Marichal from the Google Fonts team contributed fixes via PRs.
- Confidence in metadata accuracy: **high** — config.yaml is present and correctly referenced; the pinned commit is HEAD; built variable font path matches METADATA.pb expectation; STAT table is well-defined.
