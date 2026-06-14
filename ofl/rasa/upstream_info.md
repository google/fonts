# Rasa — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/rosettatype/yrsa-rasa
- **Commit**: `36874c97c64a0d1853297afdfc0cfaf14a3c0f19`
- **Status**: Commit hash was added to existing source block

## What Was Done
The repository at https://github.com/rosettatype/yrsa-rasa was inspected. The repository contains both the Yrsa and Rasa families. Available tags were reviewed: the latest tagged release is `v2.005` (commit `ec1d6aa68525da0859a43048228aef2c5bff3b40`, dated 2021-11-18). However, the METADATA.pb references the `master` branch with no `archive_url` pointing to a specific release, and the repository has additional commits beyond v2.005 (latest HEAD commit dated 2023-06-14). The latest commit on `master` (`36874c97c64a0d1853297afdfc0cfaf14a3c0f19`) was verified via the GitHub API and added to the source block in METADATA.pb.

## Build System
The repository uses a UFO/designspace-based workflow. Source files are in `sources/` and include `Rasa-Its.designspace`, `Rasa-Ups.designspace`, and a `Rasa.stylespace`. A `production/` directory and `workflow.yaml` suggest an automated build pipeline using fontmake and related tools. A `requirements.txt` is present for Python dependencies.

## Notes
The Rasa family shares a repository with the Yrsa family (rosettatype/yrsa-rasa). The METADATA.pb source block references Rasa-specific file paths (`fonts/RasaVariable/RasaVF-Ups.ttf` and `fonts/RasaVariable/RasaVF-Its.ttf`). Both the upright and italic variable fonts are included in the source file mappings.
