# Ruwudu — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/silnrsi/font-ruwudu
- **Commit**: `b5aa4e64386fa7fe286634b10b7c874a42b9d1cf`
- **Status**: Commit hash was added to existing source block

## What Was Done
The repository at https://github.com/silnrsi/font-ruwudu was inspected. The METADATA.pb already contained an `archive_url` pointing to the `v3.000` release (`https://github.com/silnrsi/font-ruwudu/releases/download/v3.000/Ruwudu-3.000.zip`). The tag `v3.000` was resolved via the GitHub API to commit SHA `b5aa4e64386fa7fe286634b10b7c874a42b9d1cf`. This commit was verified and added to the source block in METADATA.pb to match the pinned release.

## Build System
The repository uses a designspace-based build system (`source/Ruwudu.designspace`) with UFO masters in `source/masters/`. The build tooling is waf-based (`wscript` file present in root), which is SIL International's preferred build system for font projects. Additional tooling scripts are present in `tools/` and preflight scripts (`preflight`, `preflightff`, `preflightfl`, `preflightg`) for quality checks. A `makedocs` script handles documentation generation.

## Notes
Ruwudu is a Hausa-script (Arabic-based) font developed by SIL International. The `primary_script` is set to `Arab` in METADATA.pb. The font includes four weights: Regular, Medium, SemiBold, and Bold. The commit pinned here corresponds to the `v3.000` release, which is the release referenced by the existing `archive_url` in METADATA.pb.
