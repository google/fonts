# Ruda — Upstream Source Investigation

**Designer**: Mariela Monsalve, Angelina Sanchez
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at `m4rc1e/Ruda-new` containing a Glyphs source file. The METADATA.pb was updated with the source block.

## Investigation

The METADATA.pb copyright line referenced `https://github.com/marmonsalve/Ruda-new` as the upstream source, but that repository does not exist on GitHub.

The repository `m4rc1e/Ruda-new` was found to be a non-fork repository containing a Glyphs source file (`Ruda_new.glyphs`) and a README. Examination of the commit history confirmed that the designer marmonsalve (Mariela Monsalve) committed directly to this repository, making it the canonical upstream despite being hosted under a different GitHub user's namespace.

## Repository Details

| Field | Value |
|-------|-------|
| Repository | https://github.com/m4rc1e/Ruda-new |
| Source format | Glyphs (`Ruda_new.glyphs`) |
| Latest commit | `a63532e04ffb0f46b635cf9e000966155958e19d` |
| Commit date | 2018-05-04 |
| Commit author | marmonsalve |
| Is fork | No |

## Changes Made

Added `source` block to `ofl/ruda/METADATA.pb`:

```
source {
  repository_url: "https://github.com/m4rc1e/Ruda-new"
  commit: "a63532e04ffb0f46b635cf9e000966155958e19d"
}
```
