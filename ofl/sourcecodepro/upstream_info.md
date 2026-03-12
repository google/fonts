# Source Code Pro — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/adobe-fonts/source-code-pro
- **Commit**: `803b7e23ec97ae58b6232ea76519a76d428ba268`
- **Status**: Commit hash was added to existing source block

## What Was Done
The upstream repository at https://github.com/adobe-fonts/source-code-pro was identified as the source for Source Code Pro. The latest commit on the default branch was retrieved via the GitHub API and added to the `source` block in METADATA.pb. Tagged releases were found (latest: `2.042R-u/1.062R-i/1.026R-vf`), but the head of the default branch was used as it represents the most current state of the repository.

## Build System
The Adobe fonts repository distributes pre-built font files across directories named `OTF/`, `TTF/`, `VF/`, `WOFF/`, and `WOFF2/` without a build script at the root level. A `package.json` file is present for CSS file management.

## Notes
Source Code Pro is Adobe's open-source monospaced typeface, released as variable fonts for the Google Fonts catalog. The font includes 2 variable font files (roman and italic), each covering a weight range of 200–900. The METADATA.pb source block previously lacked a commit hash, file mappings, and branch specification.
