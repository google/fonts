# Xanh Mono — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/yellow-type-foundry/xanhmono
- **Commit**: `5c0ceb816ffc1e8f79be71c82a43201395f3eca5`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained only a repository_url with no files, branch, or commit fields. The latest commit hash was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/yellow-type-foundry/xanhmono/commits/{hash}`.

## Notes
- The source block has no explicit file mappings or branch specification, meaning it relies on default behavior.
- Repository is maintained by Yellow Type Foundry (Lâm Bảo, Duy Dao).
- Font includes both regular and italic styles; supports latin, latin-ext, and vietnamese subsets.
