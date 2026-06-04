# Piazzolla — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Piazzolla was identified at https://github.com/huertatipografica/piazzolla, maintained by Huerta Tipográfica. The METADATA.pb file referenced commit `fbd775f98a0a27570de0eaf20206860021c68b6b` on the `google_prs` branch. No config_yaml was specified in the source block. A minisite is available at https://piazzolla.huertatipografica.com/.

## Font Description

Piazzolla is an expressive serif variable font designed by Juan Pablo del Peral at Huerta Tipográfica. The font is named after Astor Piazzolla, the Argentine tango composer. It features optical size (`opsz`, 8–30) and weight (`wght`, 100–900) variable axes, and is available in both upright and italic styles. The design is classified as both serif and display. It covers Latin, Cyrillic, Greek (including Extended), and Vietnamese scripts, giving it exceptionally broad multilingual support. The copyright dates to 2018.

## Designer

Juan Pablo del Peral is the lead designer, working at Huerta Tipográfica, an Argentine type foundry known for high-quality Latin and multilingual typefaces.

## Repository

- **URL**: https://github.com/huertatipografica/piazzolla
- **Commit**: `fbd775f98a0a27570de0eaf20206860021c68b6b`
- **Branch**: `google_prs`
- **License**: OFL
- **Minisite**: https://piazzolla.huertatipografica.com/

## Font Details

| Property | Value |
|----------|-------|
| Category | SERIF / DISPLAY |
| Stroke | SERIF |
| Style | Regular + Italic |
| Weight Axis | 100–900 |
| Optical Size Axis | 8–30 |
| Subsets | latin, latin-ext, cyrillic, cyrillic-ext, greek, greek-ext, vietnamese |
| Variable | Yes (opsz, wght) |

## File Mapping

The source block specified explicit file mappings: `fonts/variable/ttf/Piazzolla[opsz,wght].ttf`, `fonts/variable/ttf/Piazzolla-Italic[opsz,wght].ttf`, and `OFL.txt` were mapped from the upstream repository. The fonts are sourced from the `google_prs` branch rather than the default branch, suggesting a dedicated branch is maintained for Google Fonts deliverables.

## Notes

The use of a dedicated `google_prs` branch is notable — this is a pattern used by some foundries to maintain a stable, Google-ready version of their fonts separate from active development work.

## Confidence

**High** — The repository is referenced directly in both the METADATA.pb `repository_url` and the copyright notice. The commit and branch are explicitly specified.
