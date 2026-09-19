# Viaoda Libre — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/bettergui/ViaodaLibre
- **Commit**: `a0d8da9d47c56c3ee53f9ca954b025734975a657`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained only a repository_url with no files, branch, or commit fields. The latest commit hash was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/bettergui/ViaodaLibre/commits/{hash}`.

## Notes
- The source block has no explicit file mappings or branch specification, meaning it relies on default behavior.
- Repository is maintained by Gydient / ViệtAnh Nguyễn.
- Font supports cyrillic, cyrillic-ext, latin, latin-ext, and vietnamese subsets.
